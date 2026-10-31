from pathlib import Path

# Project directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset location
DATA_PATH = PROJECT_ROOT /"data"/"raw"/"creditcard.csv"

# Output directories
OUTPUT_DIR = PROJECT_ROOT / "outputs"
REPORT_DIR = PROJECT_ROOT / "reports"

# Reproducibility settings
RANDOM_STATE = 42

# Model evaluation settings (for later use)
TEST_SIZE = 0.20
TARGET_COLUMN = "Class"