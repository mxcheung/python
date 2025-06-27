from dataclasses import dataclass
from enum import Enum
from typing import Optional

class Environment(str, Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"

@dataclass
class AppConfig:
    name: str
    repo_name: str
    branch: str
    environment: Environment
    cluster_name: str
    service_name: str
    container_name: str
    region: str
    account_id: str

@dataclass
class Config:
    app: AppConfig
