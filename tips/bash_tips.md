 - Use `set -euxo pipefail` instead of `set -ex` or `/bin/bash -ex` so that:
    - `-u` ensures you don't use any unset variables
    - `-o pipefail` ensures that if a command in a pipe fails, the overall command
      still exits with an error.
