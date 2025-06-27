import yaml
from dacite import from_dict, Config as DaciteConfig
from pathlib import Path

def load_config(path: str = "values.yaml") -> Config:
    with open(path, "r") as f:
        raw = yaml.safe_load(f)
    return from_dict(data_class=Config, data=raw, config=DaciteConfig(cast=[Environment]))
