from aws_cdk import App, Environment
from my_stack import PipelineToEcsStack
from config_loader import load_config  # your config loading function

cfg = load_config("values.yaml")

app = App()
PipelineToEcsStack(
    app,
    "PipelineToEcsStack",
    config=cfg,
    env=Environment(account=cfg.app.account_id, region=cfg.app.region),
)
app.synth()
