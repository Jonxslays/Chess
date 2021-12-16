import nox


@nox.session(reuse_venv=True)
def formatting(session: nox.Session) -> None:
    session.run("poetry", "-q", "shell", external=True)
    session.run("poetry", "install", external=True)
    session.run("len8")
    session.run("isort", ".")
    session.run("black", ".", "--check")


@nox.session(reuse_venv=True)
def types(session: nox.Session) -> None:
    session.run("poetry", "-q", "shell", external=True)
    session.run("poetry", "install", external=True)
    session.run("mypy", ".")
    session.run("pyright")
