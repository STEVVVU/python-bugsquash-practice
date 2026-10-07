from io import BytesIO

import pytest

from werkzeug.exceptions import NotFound
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.routing import Map
from werkzeug.routing import RequestRedirect
from werkzeug.routing import Rule
from werkzeug.test import create_environ
from werkzeug.wrappers import Request
from werkzeug.wrappers import Response


def _multipart_request(data):
    return Request.from_values(
        method="POST", data=data, content_type="multipart/form-data"
    )


def test_problem01_exact_part_limit_accepts_one_part():
    request = _multipart_request({"field": "value"})
    request.max_form_parts = 1

    assert request.form["field"] == "value"
    assert not request.files


def test_problem01_exact_part_limit_accepts_one_file():
    request = _multipart_request(
        {"upload": (BytesIO(b"payload"), "file.txt")}
    )
    request.max_form_parts = 1

    assert request.files["upload"].read() == b"payload"
    request.close()


@pytest.mark.parametrize(
    ("data", "max_parts"),
    [
        (
            {"field": "value", "upload": (BytesIO(b"payload"), "file.txt")},
            1,
        ),
        (
            {
                "first": "one",
                "second": "two",
                "upload": (BytesIO(b"payload"), "file.txt"),
            },
            2,
        ),
    ],
)
def test_problem01_part_limit_counts_file_parts(data, max_parts):
    request = _multipart_request(data)
    request.max_form_parts = max_parts

    with request:
        with pytest.raises(RequestEntityTooLarge):
            request.form


def test_problem02_merge_enabled_route_redirects_to_normalized_path():
    url_map = Map([Rule("/yes/merging", endpoint="merged")])
    adapter = url_map.bind("example.org", "/")

    with pytest.raises(RequestRedirect) as error:
        adapter.match("/yes//merging")

    assert error.value.new_url.endswith("/yes/merging")


def test_problem02_merge_disabled_route_does_not_redirect():
    url_map = Map(
        [Rule("/no/merging", endpoint="no_merging", merge_slashes=False)]
    )
    adapter = url_map.bind("example.org", "/")

    assert adapter.match("/no/merging")[0] == "no_merging"
    with pytest.raises(NotFound):
        adapter.match("/no//merging")


@pytest.mark.parametrize(
    ("headers", "status", "content_range", "body"),
    [
        (
            {"Range": "bytes=0-3", "If-Range": '"current"'},
            206,
            "bytes 0-3/8",
            b"abcd",
        ),
        (
            {"Range": "bytes=0-3", "If-Range": '"stale"'},
            200,
            None,
            b"abcdefgh",
        ),
        ({"Range": "bytes=0-3"}, 206, "bytes 0-3/8", b"abcd"),
        ({"If-Range": '"current"'}, 200, None, b"abcdefgh"),
    ],
)
def test_problem03_range_depends_on_if_range_validator(
    headers, status, content_range, body
):
    environ = create_environ(headers=headers)
    response = Response("abcdefgh")
    response.set_etag("current")

    response.make_conditional(environ, accept_ranges=True, complete_length=8)

    assert response.status_code == status
    assert response.headers.get("Content-Range") == content_range
    assert response.get_data() == body
