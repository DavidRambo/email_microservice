import pydantic
import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    """Settings for the default mail server and sender.

    pydantic-settings will retrieve their values from the environment, including
    a dotenv file specified with model_config, in a case-insensitive manner.
    """

    model_config = pydantic_settings.SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    mail_server: str
    mail_port: int
    sender_addr: str = pydantic.Field(alias="sender")
    sender_password: str = pydantic.Field(alias="password")

    origins: list[str] = [
        "http://localhost:5173",
        "http://localhost:8000",
        "http://localhost",
    ]


settings = Settings()
