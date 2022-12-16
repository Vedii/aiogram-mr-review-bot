from pydantic import BaseSettings, SecretStr, Field, BaseModel


class CommonConfig(BaseSettings):
    token: SecretStr = Field(..., env="token")
    log_cfg_path: str = Field("./configs/logging.json", env="log_cfg_path")

    class Config:
        case_sentive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'


class DbConfig(BaseSettings):
    driver: str = Field(..., env="driver")
    user: str = Field(..., env="user")
    password: SecretStr = Field(..., env="password")
    host: str = Field(..., env="host")
    port: int = Field(..., env="port")
    sid: str = Field('review', env="sid")

    dsn: str = Field(None, env="dsn")

    echo_db_queries: bool = Field(False, env="echo_db_queries")
    echo_db_pool: bool = Field(False, env="echo_db_cp")

    class Config:
        case_sentive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'


class ConfigProvider(BaseModel):
    db: DbConfig = DbConfig()
    common: CommonConfig = CommonConfig()
