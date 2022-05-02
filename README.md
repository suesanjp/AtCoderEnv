# Install

```bash
# Creating virtual environments
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install --upgrade pip

# Install dependencies
$ pip install online-judge-tools black flake8 isort
$ npm install -g atcoder-cli

# Login
$ oj login https://atcoder.jp/
$ acc login

# Set oj path
$ acc config oj-path /Users/username/Dev/AtCoder/.venv/bin/oj

# Set a template
$ mv py `acc config-dir`
$ acc config default-template py

# Set all tasks to download
$ acc config default-task-choice all
```

# How to use

```bash
$ source .venv/bin/activate
```

If you solve "abc101" "a"
```bash
# download tasks
acc new abc101
cd abc101/a
```
Write the answer to main.py
```bash
# test
oj t -c "pypy main.py" -d ./tests/
```
If the answer is correct the result is "AC"

```bash
# Submit answer as "pypy"
acc s main.py -- --guess-python-interpreter pypy
```

# Reference

https://github.com/online-judge-tools/oj

http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/
