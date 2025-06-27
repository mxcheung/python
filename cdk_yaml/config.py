from enum import Enum
from dataclasses import dataclass
from typing import List
import yaml

class Environment(Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"
    
@dataclass
class AppConfig:
    name: str
    environment: Environment

@dataclass
class Config:
    app: AppConfig
