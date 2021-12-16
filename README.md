# Chess

Python version 3.10 or greater is required to play.

##### Note
> This is a gui application, and as such will not run inside WSL.
> (Get a real operating system, stop faking it.)

## Warning

This game is not fully developed, the README will be updated when it is
in a playable state.

## How to play

Using pip:

```bash
git clone "https://github.com/Jonxslays/Chess.git" && cd Chess
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m chess
```

Using poetry:

```bash
git clone "https://github.com/Jonxslays/Chess.git" && cd Chess
poetry install --no-dev
poetry run python -m chess
```

## License

Jonxslays/Chess is licensed under the [MIT license](https://github.com/Jonxslays/Chess/blob/master/LICENSE).
