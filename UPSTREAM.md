# Upstream provenance

- Project: Pallets Jinja, release 3.1.6.
- Source: `https://github.com/pallets/jinja`, commit `15206881c006c79667fe5154fe80c01c65410679`.
- License: BSD 3-Clause. The upstream `LICENSE.txt` and copyright notices are retained.
- The source was exported from the pinned Git commit. Upstream source, tests, docs, examples, artwork, changelog, and project metadata are retained. `.github/` workflows and `.devcontainer/` were omitted from this exercise repository.
- The root README adds exercise setup and report links, then retains the upstream README content. `problems/` contains task-facing reports; `tests/test_bugsquash.py` contains deterministic behavior checks.

## Setup

Use the Python 3.11 setup and shell activation steps in the root README, then install the editable project with the pinned upstream test dependencies and run the suite as documented there.

`requirements-bugsquash.txt` installs this checkout in editable mode and includes the upstream `requirements/tests.txt` pins. The Jinja runtime dependency `MarkupSafe>=2.0` is resolved through the project metadata.
