from dataclasses import dataclass
from enum import Enum
from typing import Optional
from dacite import from_dict, Config as DaciteConfig

class Environment(str, Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"

@dataclass
class AppConfig:
    name: str
    environment: Environment
    cluster: str
    container: str
    desired_count: int

@dataclass
class ValuesConfig:
    app: AppConfig
