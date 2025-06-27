import yaml
from jinja2 import Environment, FileSystemLoader

# 1. Load values.yaml
with open("values.yaml") as f:
    values = yaml.safe_load(f)

# 2. Load and render Jinja2 template
env = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("template.yaml")
rendered = template.render(values)

# 3. Optionally save or print output
with open("output.yaml", "w") as f:
    f.write(rendered)

print(rendered)
