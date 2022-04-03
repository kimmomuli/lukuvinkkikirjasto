from invoke import task


@task
def start(ctx):
    ctx.run("cd src && flask run")


@task
def test(ctx):
    ctx.run("pytest src")


@task
def lint(ctx):
    ctx.run("pylint src")
