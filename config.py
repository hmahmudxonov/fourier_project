# fourier_project/config.py
from pathlib import Path

# dynamically finds the root directory (fourier_project\)
BASE_DIR = Path(__file__).resolve().parent

# defines data\ and output\ directory locations
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

# creates output\ dir
OUTPUT_DIR.mkdir(exist_ok=True)

# creates the directories in output\
def get_assignment_output_dir(problem_name):
    path = OUTPUT_DIR / problem_name
    path.mkdir(parents=True, exist_ok=True)
    return path