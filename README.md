# model_template

A reusable Python project template. Copy this repo and replace the placeholder components with your own logic.

## Structure

```
model_template/
├── main.py                  # Entry point. Define config and call model.run()
├── model.py                 # Model class. run() orchestrates all components
├── model_components/
│   ├── loader.py            # Loads input data
│   ├── processor.py         # Processes loaded data
│   └── outputter.py         # Writes results to output
├── data/
│   ├── input/               # Place raw input files here
│   └── output/              # Results are written here
└── secrets/
    └── .env.example         # Template for API keys / credentials (never commit real values)
```

## How it works

1. `main.py` defines a `config` dict (paths, parameters) and calls `Model(config).run()`.
2. `Model.run()` in `model.py` calls each component in order: Loader → Processor → Outputter.
3. All logic lives in `model_components/`. Add or rename components there as needed.

## Usage

```bash
python main.py
```

## Adding a new component

1. Create `model_components/mycomponent.py` with a class and a `run()` method.
2. Import and instantiate it in `model.py`.
3. Call `self.mycomponent.run(...)` inside `Model.run()`.

## Secrets

Copy `secrets/.env.example` to `secrets/.env` and fill in real values.  
The `.gitignore` inside `secrets/` prevents `.env` files from being committed.
