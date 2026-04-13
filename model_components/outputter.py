import os
import json


class Outputter:
    def __init__(self, config):
        self.config = config

    def run(self, result):
        path = self.config.get("output_path", "data/output/result.json")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(result, f, indent=2)
