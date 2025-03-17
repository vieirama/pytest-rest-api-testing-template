# pytest-rest-api-testing-template

Template for testing framework using Pytest.

## Installation

### Create virtual environment

```commandline
python -m venv venv
.\venv\Scripts\activate.bat
```

### Activate virtual environment and install requirements

```commandline
.\venv\Scripts\Activate.ps1 
```

```commandline
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

## Local execution

```commandline
pytest --env=dev
```

## Container execution

```commandline
podman build -t pytest-testing:latest .
podman run pytest-testing
```
