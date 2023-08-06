# codeclimate-mypy

`mypy-to-codeclimate` is a converter from [mypy](https://github.com/python/mypy) to codeclimate report for gitlab ci.

### Run

`mypy --show-error-end --show-absolute-path`

`python mypy-to-codeclimate in_file.txt out_file.txt`

when running mypy-to-codeclimate.py all the paths in the codeclimate report are relative to the current working directory, so run this on the root of the project. \
Otherwise gitlab won't parse the paths very well.

### Also supports
- The `--show-column-numbers --show-error-end` are supported
- Fingerprint (like [this mr](https://gitlab.com/ErezAmihud/pyright-to-gitlab-ci/-/merge_requests/2))

# Note
There are more options like this, like https://pypi.org/project/mypy-gitlab-code-quality/ but it doesn't support basic things like end line, and specific columns.
