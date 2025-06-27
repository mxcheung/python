def parse_enum(enum_class, value):
    try:
        return enum_class(value)
    except ValueError:
        raise ValueError(f"Invalid value '{value}' for enum {enum_class.__name__}")

def from_dict(data_class, data):
    from dataclasses import fields, is_dataclass
    kwargs = {}

    for field in fields(data_class):
        value = data.get(field.name)
        field_type = field.type

        if isinstance(value, dict) and is_dataclass(field_type):
            kwargs[field.name] = from_dict(field_type, value)
        elif isinstance(field_type, type) and issubclass(field_type, Enum):
            kwargs[field.name] = parse_enum(field_type, value)
        else:
            kwargs[field.name] = value

    return data_class(**kwargs)


# Load the YAML file
with open("config.yaml") as f:
    raw = yaml.safe_load(f)

config = from_dict(Config, raw)


print(config.app.name)              # my-ecs-app
print(config.app.environment)       # Environment.DEV
print(config.app.environment.value) # dev
