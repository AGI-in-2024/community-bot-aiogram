from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class CurrentEnvType(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env",
        extra="ignore"
    )


class BotSettings(CurrentEnvType):
    bot_token: SecretStr

    @property
    def token(self) -> str:
        return self.bot_token.get_secret_value()


class PostgresSettings(CurrentEnvType):
    postgres_dsn: PostgresDsn

    @property
    def dsn(self):
        return self.postgres_dsn.unicode_string()


class Settings(CurrentEnvType):
    @property
    def bot(self) -> BotSettings:
        return BotSettings()

    @property
    def postgres(self) -> PostgresSettings:
        return PostgresSettings()


@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    return Settings()
