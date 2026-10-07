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
