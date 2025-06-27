from enum import Enum
from dataclasses import dataclass
from typing import List
import yaml

class Environment(Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"

class Region(Enum):
    AP_SOUTHEAST_2 = "ap-southeast-2"
    US_WEST_1 = "us-west-1"


@dataclass
class AppConfig:
    name: str
    environment: Environment

@dataclass
class Config:
    app: AppConfig
