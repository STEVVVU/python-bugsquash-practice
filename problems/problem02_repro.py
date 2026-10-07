from werkzeug.exceptions import NotFound
from werkzeug.routing import Map, RequestRedirect, Rule


url_map = Map(
    [
        Rule("/no/merging", endpoint="no_merging", merge_slashes=False),
        Rule("/yes/merging", endpoint="yes_merging"),
    ]
)
adapter = url_map.bind("example.org", "/")

print(f"exact: {adapter.match('/no/merging')[0]}")

try:
    adapter.match("/no//merging")
except NotFound:
    print("doubled: 404 Not Found")
except RequestRedirect as error:
    print(f"doubled: {error.code} {error.new_url}")
