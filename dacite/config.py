from enum import Enum
from dataclasses import dataclass
from typing import List
from aws_lambda_powertools.utilities.typing import TypedDict

class Environment(str, Enum):
    DEV = "dev"
    TEST = "test"
    PROD = "prod"

class Region(str, Enum):
    AP_SOUTHEAST_2 = "ap-southeast-2"
    US_WEST_1 = "us-west-1"

@dataclass
class AppConfig:
    name: str
    environment: Environment
    regions: List[Region]

@dataclass
class Config:
    app: AppConfig
