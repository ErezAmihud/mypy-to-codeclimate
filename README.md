# codeclimate-mypy

`mypy-to-codeclimate` is a converter from [mypy](https://github.com/python/mypy) to codeclimate report for gitlab ci.

### Run

`mypy --show-error-end --show-absolute-path`

`python mypy-to-codeclimate in_file.txt out_file.txt`


### Also supports
- The `--show-column-numbers --show-error-end` are supported
- Fingerprint (like [this mr](https://gitlab.com/ErezAmihud/pyright-to-gitlab-ci/-/merge_requests/2))

