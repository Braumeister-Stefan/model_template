from model_components import Loader, Processor, Outputter


class Model:
    def __init__(self, config):
        self.config = config
        self.loader = Loader(config)
        self.processor = Processor(config)
        self.outputter = Outputter(config)

    def run(self):
        data = self.loader.run()
        result = self.processor.run(data)
        self.outputter.run(result)
