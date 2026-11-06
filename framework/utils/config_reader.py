"""Configuration reader utility."""
import os
import yaml


def get_config():
    """
    Configuration reader function
    Returns the content of the config.yaml file as a dictionary
    """
    config_path = os.path.join(
        os.path.dirname(__file__),
        "../../config/config.yaml",
    )
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
    
