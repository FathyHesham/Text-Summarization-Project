# import libraries
from pathlib import Path # import the class path from the pathlib medule for working file paths

# Building the structure
structure_file = [
    "main.py",
    "config.yaml",
    "application/__init__.py",
    "application/streamlit_app.py",
    "model/__init__.py",
    "model/summarizer_model.py",
    "model/summarizer_experiment.ipynb",
    "model/load_chunk_document.py",
    "model/preprocessing.py",
    "model/generated_summaries.py",
    "custom_logging/__init__.py",
    "custom_logging/custom_logger.py",
    "utils/__init__.py",
    "utils/config_loader.py"
]


# Loop through each file path in the structure
for filepath in map(Path, structure_file):
    # Check if the file has a parent directory
    if filepath.parent:
        # Ensure the parent directory exists, create if it doesn't
        filepath.parent.mkdir(parents = True, exist_ok = True)
        print(f"Ensured directory exists: {filepath.parent}")
    # Check if the file does not exist
    if not filepath.exists():
        # Create the file
        filepath.touch()
        print(f"Created file: {filepath}")
    else:
        # Notify that the file already exists
        print(f"File already exists: {filepath}")