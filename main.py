from model import Model

config = {
    "input_path": "data/input/sample.csv",
    "output_path": "data/output/result.json",
}

if __name__ == "__main__":
    model = Model(config)
    model.run()
