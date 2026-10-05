# Upstream source

This practice repository is based on Pallets Click 8.5.0, pinned at commit
`8b19813f2bfca99f1018a587a8cf54fc959f2e5d` from
<https://github.com/pallets/click>. The upstream source, tests, documentation,
examples, `LICENSE.txt`, and copyright notices are retained. Click is distributed
under the BSD 3-Clause License; see `LICENSE.txt`.

The exercise repository omits the upstream `.git` history and `.github`
directory. Omitting `.github` excludes publishing and automation workflows from
the practice package; it does not alter Click source behavior.

The upstream `.devcontainer` files are retained with their setup aligned to the
exercise instructions: the image is pinned to Python 3.11 and its on-create
command installs Click and the pinned test dependency from `requirements-dev.txt`.
The upstream on-create command referenced `requirements/dev.txt`, which is not
part of this repository, and installed pre-commit hooks that are not required by
the practice setup.
