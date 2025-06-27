config = load_config()

print(config.app.name)                # my-ecs-app
print(config.app.environment.value)   # dev
for region in config.app.regions:
    print(region.value)               # ap-southeast-2, us-west-1
