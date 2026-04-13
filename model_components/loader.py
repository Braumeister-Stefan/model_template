class Loader:
    def __init__(self, config):
        self.config = config
        self.data = None

    def run(self):
        path = self.config.get("input_path", "data/input/sample.csv")
        self.data = {"source": path, "records": []}
        return self.data
