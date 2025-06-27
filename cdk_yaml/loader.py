def from_dict(data_class, data):
    """Recursively convert a dictionary to a dataclass"""
    from dataclasses import fields, is_dataclass

    if not is_dataclass(data_class):
        return data

    kwargs = {}
    for f in fields(data_class):
        value = data.get(f.name)
        if value is not None:
            if isinstance(f.type, type) and issubclass(f.type, list):
                kwargs[f.name] = value
            else:
                kwargs[f.name] = from_dict(f.type, value)
    return data_class(**kwargs)

# Load the YAML file
with open("config.yaml") as f:
    raw = yaml.safe_load(f)

config = from_dict(Config, raw)

print(config.app.name)            # my-ecs-app
print(config.app.environments)   # ['dev', 'test', 'prod']
