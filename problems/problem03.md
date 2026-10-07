# Problem 03: Conditional byte ranges

A response supports byte ranges and has an entity tag. A client sends a range
request with an `If-Range` validator that matches that tag. The server returns
the complete response instead of the requested byte range.

Reproduce it with a response and request environment:

```text
python problems/problem03_repro.py
```

```python
from werkzeug.test import create_environ
from werkzeug.wrappers import Response


environ = create_environ(
    headers={"Range": "bytes=0-3", "If-Range": '"current"'}
)
response = Response("abcdefgh")
response.set_etag("current")
response.make_conditional(environ, accept_ranges=True, complete_length=8)

print(
    response.status_code,
    response.headers.get("Content-Range"),
    response.get_data(),
)
```

Expected: status `206`, content range `bytes 0-3/8`, and body `b'abcd'`.

Observed output:

```text
200 None b'abcdefgh'
```

Focused test command:

```text
python -m pytest tests/test_bugsquash.py -k problem03 -q
```
