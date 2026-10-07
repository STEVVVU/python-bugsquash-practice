# Problem 01: Multipart part limits

An upload endpoint limits the number of multipart parts to control the cost of
processing unusually complex requests. A request with more parts than the
configured maximum is accepted in some cases.

Reproduce it with the public request API:

```text
python problems/problem01_repro.py
```

```python
from io import BytesIO

from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.wrappers import Request


request = Request.from_values(
    method="POST",
    data={"field": "value", "upload": (BytesIO(b"payload"), "file.txt")},
)
request.max_form_parts = 1

try:
    fields = request.form
except RequestEntityTooLarge:
    print("rejected: 413 Request Entity Too Large")
else:
    print(f"accepted: fields={list(fields)}, files={list(request.files)}")
```

Expected: the request is rejected with `413 Request Entity Too Large` because
it contains two parts and the configured maximum is one.

Observed output:

```text
accepted: fields=['field'], files=['upload']
```

Focused test command:

```text
python -m pytest tests/test_bugsquash.py -k problem01 -q
```
