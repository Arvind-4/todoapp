import pathlib

CURRENT_DIR = pathlib.Path(__file__).resolve(strict=True).parent

ENV_FILE = CURRENT_DIR / ".env"


def read_env(env_file: pathlib.Path = ENV_FILE) -> None:
    import dotenv

    dotenv.read_dotenv(str(env_file))


