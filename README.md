## Bugsquash practice

This exercise uses Werkzeug 3.1.9, pinned to upstream commit
`6604c3b8784ecc7cf5ac0b7412d916989b4c7d45`. It is based on the Pallets
Werkzeug project and retains its source, tests, documentation, examples, and
BSD-3-Clause license. See [`UPSTREAM.md`](UPSTREAM.md) for provenance and the
included and omitted upstream materials. The original upstream README follows
this exercise introduction.

Three seeded regressions are described in [`problems/`](problems/). Start with
the symptom reports and reproductions, then investigate the public behavior
through the library and its tests. The focused exercise tests are in
`tests/test_bugsquash.py`.

### Setup

Use Python 3.11 and create a virtual environment:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, use `python3.11 -m venv .venv` and activate with
`source .venv/bin/activate`.

Run the original suite and focused exercise tests with:

```text
python -m pytest -q
python -m pytest tests/test_bugsquash.py -q
```

The exercise tests are expected to fail until the three reported behaviors are
corrected. Upstream tests remain intact.

The upstream baseline on Python 3.11.9 is 979 passed and 2 skipped, with one
existing `ResourceWarning` from the malformed multipart end-of-file test. The
exercise adds 10 deterministic test cases. After all three behaviors are
corrected, the full suite passes with 989 passed and 2 skipped, retaining that
same warning. With the seeds present, the full suite reports 5 expected
failures, 984 passed, and 2 skipped: four exercise cases and the existing
upstream routing assertion for the same slash-policy regression. The same
single warning is present.

---

<div align="center"><img src="https://raw.githubusercontent.com/pallets/werkzeug/refs/heads/stable/docs/_static/werkzeug-name.svg" alt="" height="150"></div>

# Werkzeug

*werkzeug* German noun: "tool". Etymology: *werk* ("work"), *zeug* ("stuff")

Werkzeug is a comprehensive [WSGI][] web application library. It began as
a simple collection of various utilities for WSGI applications and has
become one of the most advanced WSGI utility libraries.

It includes:

-   An interactive debugger that allows inspecting stack traces and
    source code in the browser with an interactive interpreter for any
    frame in the stack.
-   A full-featured request object with objects to interact with
    headers, query args, form data, files, and cookies.
-   A response object that can wrap other WSGI applications and handle
    streaming data.
-   A routing system for matching URLs to endpoints and generating URLs
    for endpoints, with an extensible system for capturing variables
    from URLs.
-   HTTP utilities to handle entity tags, cache control, dates, user
    agents, cookies, files, and more.
-   A threaded WSGI server for use while developing applications
    locally.
-   A test client for simulating HTTP requests during testing without
    requiring running a server.

Werkzeug doesn't enforce any dependencies. It is up to the developer to
choose a template engine, database adapter, and even how to handle
requests. It can be used to build all sorts of end user applications
such as blogs, wikis, or bulletin boards.

[Flask][] wraps Werkzeug, using it to handle the details of WSGI while
providing more structure and patterns for defining powerful
applications.

[WSGI]: https://wsgi.readthedocs.io/en/latest/
[Flask]: https://www.palletsprojects.com/p/flask/


## A Simple Example

```python
# save this as app.py
from werkzeug.wrappers import Request, Response


@Request.application
def application(request: Request) -> Response:
    return Response("Hello, World!")


if __name__ == "__main__":
    from werkzeug.serving import run_simple

    run_simple("127.0.0.1", 5000, application)
```

```
$ python -m app
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


## Donate

The Pallets organization develops and supports Werkzeug and other
popular packages. In order to grow the community of contributors and
users, and allow the maintainers to devote more time to the projects,
[please donate today][].

[please donate today]: https://palletsprojects.com/donate

## Contributing

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/
