# Problem 02: Per-route slash policy

A routing map is configured to normalize repeated slashes by default. One route
opts out of that behavior. Requests to its exact path work, but a path with a
repeated slash is redirected instead of being treated as missing.

Reproduce it with a routing map and adapter:

```text
python problems/problem02_repro.py
```

```python
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
```

Expected: the exact route matches, while the doubled-slash path raises
`NotFound` because that route opted out of slash merging.

Observed output:

```text
exact: no_merging
doubled: 308 http://example.org/no/merging
```

Focused test command:

```text
python -m pytest tests/test_bugsquash.py -k problem02 -q
```
