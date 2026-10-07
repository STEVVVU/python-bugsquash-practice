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
