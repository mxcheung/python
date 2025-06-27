import yaml
from dacite import from_dict, Config as DaciteConfig
from pathlib import Path

def load_config() -> Config:
    config_path = Path(__file__).parent / "config.yaml"
    with open(config_path) as f:
        raw = yaml.safe_load(f)
    return from_dict(
        data_class=Config, 
        data=raw,
        config=DaciteConfig(cast=[Environment, Region])
    )
