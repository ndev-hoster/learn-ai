from pathlib import Path
import sys
import torch

# Auto-detect project root (works from anywhere in project)
def _find_project_root():
    """Find project root by looking for utils/ directory."""
    current = Path(__file__).resolve()
    
    # If running from utils/paths.py, go up one level
    if current.parent.name == 'utils':
        return current.parent.parent
    
    # Otherwise search upwards for utils/ directory
    for parent in current.parents:
        if (parent / 'utils').exists():
            return parent
    
    # Fallback: assume current directory
    return Path.cwd()

# Project root
PROJECT_ROOT = _find_project_root()

# Add project root to Python path (so imports work from notebooks)
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Directory paths
DATA_DIR = PROJECT_ROOT / 'data'
MODELS_DIR = PROJECT_ROOT / 'models'
OUTPUTS_DIR = PROJECT_ROOT / 'outputs'
LOGS_DIR = PROJECT_ROOT / 'logs'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'

# Create directories if they don't exist
for directory in [DATA_DIR, MODELS_DIR, OUTPUTS_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Device configuration
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
CUDA_AVAILABLE = torch.cuda.is_available()

# Helper functions
def data_path(filename: str) -> Path:
    """Get path to file in data directory."""
    return DATA_DIR / filename

def model_path(filename: str) -> Path:
    """Get path to file in models directory."""
    return MODELS_DIR / filename

def output_path(filename: str) -> Path:
    """Get path to file in outputs directory."""
    return OUTPUTS_DIR / filename

def log_path(filename: str) -> Path:
    """Get path to file in logs directory."""
    return LOGS_DIR / filename
