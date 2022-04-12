from invoke import task


@task
def start(ctx):
    ctx.run("cd src && flask run", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)


@task
def initialize_database(ctx):
    ctx.run("python3 src/initialize_database.py", pty=True)


@task
def robot(ctx):
    ctx.run("dotenv -f .env.test run bash run_robot_tests.sh", pty=True)
