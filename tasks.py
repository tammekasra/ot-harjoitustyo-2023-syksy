from invoke import task
from subprocess import call
from sys import platform


@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))


@task
def test(ctx):
    ctx.run("poetry run pytest src")


@task
def coverage_report_poetry(ctx):
    ctx.run("poetry run coverage run --branch -m pytest src")
    ctx.run("poetry run coverage report -m")
    ctx.run("poetry run coverage html")


@task
def format(c):
    c.run("autopep8 --in-place --recursive src")