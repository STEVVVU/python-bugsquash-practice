from jinja2 import DictLoader
from jinja2 import Environment
from jinja2 import pass_context
from jinja2 import pass_eval_context


def test_inherited_override_can_read_scoped_loop_values():
    env = Environment(
        loader=DictLoader(
            {
                "base.html": (
                    "{% for item in items %}{% block card scoped %}"
                    "base{% endblock %}{% endfor %}"
                ),
                "child.html": (
                    "{% extends 'base.html' %}{% block card %}"
                    "{{ loop.index }}={{ item }};{% endblock %}"
                ),
            }
        )
    )

    assert env.get_template("child.html").render(items=["a", "b"]) == "1=a;2=b;"


def test_ordinary_loop_can_read_loop_index():
    env = Environment()
    template = env.from_string(
        "{% for item in items %}{{ loop.index }}={{ item }};{% endfor %}"
    )

    assert template.render(items=["a", "b"]) == "1=a;2=b;"


def test_scoped_block_inside_loop_can_read_loop_index():
    env = Environment()
    template = env.from_string(
        "{% for item in items %}{% block card scoped %}"
        "{{ loop.index }}={{ item }};{% endblock %}{% endfor %}"
    )

    assert template.render(items=["a", "b"]) == "1=a;2=b;"


def test_nested_autoescape_state_returns_to_each_enclosing_scope():
    @pass_eval_context
    def autoescape_state(eval_ctx, value):
        return str(eval_ctx.autoescape)

    env = Environment(autoescape=False)
    env.filters["autoescape_state"] = autoescape_state
    template = env.from_string(
        "{% autoescape true %}{{ value|autoescape_state }}|"
        "{% autoescape false %}{{ value|autoescape_state }}"
        "{% endautoescape %}|{{ value|autoescape_state }}"
        "{% endautoescape %}|{{ value|autoescape_state }}"
    )

    assert template.render(value="x") == "True|False|True|False"


def test_context_callable_sees_loop_assignment_without_leaking_it():
    @pass_context
    def current_value(context):
        return context.get("value", "missing")

    env = Environment(autoescape=False)
    env.globals["current_value"] = current_value
    template = env.from_string(
        "{% set value='outer' %}{{ current_value() }}|"
        "{% for item in ['x'] %}{% set value='inner' %}"
        "{{ current_value() }}{% endfor %}|{{ current_value() }}"
    )

    assert template.render() == "outer|inner|outer"


def test_context_callable_without_loop_sees_outer_value():
    @pass_context
    def current_value(context):
        return context.get("value", "missing")

    env = Environment(autoescape=False)
    env.globals["current_value"] = current_value
    template = env.from_string(
        "{% set value='outer' %}{{ current_value() }}"
    )

    assert template.render() == "outer"
