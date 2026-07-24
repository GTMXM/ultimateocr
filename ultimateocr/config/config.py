
from pathlib import Path
import yaml


class Config:

    def __init__(self, config_path):

        self.path = Path(config_path)

        with open(self.path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        return self.data[item]

    def get(self, key, default=None):
        return self.data.get(key, default)
