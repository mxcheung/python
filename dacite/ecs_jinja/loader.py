import yaml

def load_values(filepath="values.yaml") -> ValuesConfig:
    with open(filepath, "r") as f:
        raw = yaml.safe_load(f)
    return from_dict(data_class=ValuesConfig, data=raw, config=DaciteConfig(cast=[Environment]))
