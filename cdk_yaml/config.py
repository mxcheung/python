from dataclasses import dataclass
from typing import List
import yaml

@dataclass
class AppConfig:
    name: str
    environments: List[str]

@dataclass
class Config:
    app: AppConfig
