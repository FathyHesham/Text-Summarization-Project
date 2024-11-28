import os
from pathlib import Path

# Building Structure
structure_file = [
    "main.py",
    "config.yaml",
    "application/__init__.py",
    "application/streamlit_app.py",
    "model/__init__.py",
    "model/summarizer_model.py",
    "model/summarizer_experiment.ipynb",
    "model/preprocessing.py",
    "cutom_logging/__init__.py",
    "cutom_logging/custom_logger.py",
    "utils/__init__.py",
    "utils/config_loader.py"
]

for filepath in map(Path, structure_file):
    if filepath.parent:
        filepath.parent.mkdir(parents = True, exist_ok = True)
        print(f"Ensured directory exists: {filepath.parent}")
    if filepath.exists():
        filepath.touch()
        print(f"Created file: {filepath}")
    else:
        print(f"File already exists: {filepath}")