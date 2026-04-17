# learn-ai

A repository for personal learning in artificial intelligence.

## Organization

The project notebooks are organized by chapters within the `notebooks/` directory.

## Setup Instructions

### 1. Install Miniconda
Execute the following commands to install Miniconda:
```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ~/Miniconda3-latest-Linux-x86_64.sh
```

### 2. Create and Activate Environment
You can create the environment using either `requirements.txt` or `environment.yml`.

**Option A: Using Conda `environment.yml` (Recommended)**
```bash
conda env create -f environment.yml
conda activate learn-ai
```

**Option B: Using Conda and pip `requirements.txt`**
```bash
conda create -n learn-ai python=3.10
conda activate learn-ai
pip install -r requirements.txt
```

### 3. Install Project in Editable Mode
To ensure the `utils` directory can be imported from anywhere within the project, install the project in editable mode:
```bash
pip install -e .
```

### 4. Register Jupyter Kernel
To use the environment within Jupyter notebooks, register it as a kernel:
```bash
python -m ipykernel install --user --name learn-ai --display-name "Python (learn-ai)"
```

## Utilities Summary

The `utils/` directory contains centralized logic to maintain consistency across notebooks:

*   `__init__.py`: Provides easy access to key paths and device configuration (CPU/CUDA).
*   `imports.py`: Consolidates common imports for data manipulation, visualization, and machine learning.
*   `paths.py`: Automatically detects the project root and manages directory structures for data, models, and logs.
