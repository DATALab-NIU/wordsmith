from starlette.config import Config as StarConfig

config = StarConfig(".env")


class AppConfig:
    def __init__(self) -> "AppConfig":
        self.APP_NAME = "Knowledge Graph API"
        self.APP_VERSION = "0.1.0"
        self.IS_DEBUG = False

    def __str__(self) -> str:
        return(
            "Config["
            f"APP_NAME={self.APP_NAME},"
            f"APP_VERSION={self.APP_VERSION}"
            f"IS_DEBUG={self.IS_DEBUG}"
        )


Config = AppConfig()
