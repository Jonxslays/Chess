import nox
import toml


def get_dependencies() -> dict[str, str]:
    with open("pyproject.toml") as f:
        data = toml.loads(f.read())["tool"]["poetry"]["dev-dependencies"]

    return dict((k, f"{k}{v}") for k, v in data.items())


DEPS = get_dependencies()


@nox.session(reuse_venv=True)
def formatting(session: nox.Session) -> None:
    session.install("-U", DEPS["len8"], DEPS["isort"], DEPS["black"])
    session.run("len8")
    session.run("isort", ".", "-cq", "--profile", "black")
    session.run("black", ".", "--check")


@nox.session(reuse_venv=True)
def types(session: nox.Session) -> None:
    session.install("-U", DEPS["mypy"], DEPS["pyright"])
    session.run("mypy", "chess")
    session.run("pyright")
