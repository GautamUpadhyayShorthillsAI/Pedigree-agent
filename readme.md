# Pedigree Agent Setup Guide

Follow the steps below to set up and run the project:

## 1. Clone the repository
```bash
git clone https://github.com/GautamUpadhyayShorthillsAI/Pedigree-agent
```

## 2. Navigate into the project directory
```bash
cd Pedigree-agent
```

## 3. Create a virtual environment
```bash
python -m venv .venv
```

## 4. Activate the virtual environment
```bash
source .venv/bin/activate
```

## 5. Install dependencies
```bash
pip install google-adk
```

## 6. Run the application
```bash
adk web
```

## Notes
- Make sure you have Python installed on your system before running these commands
- On Windows, use `.venv\Scripts\activate` instead of `source .venv/bin/activate` to activate the virtual environment
- If you encounter any issues with the installation, ensure you have the latest version of pip: `pip install --upgrade pip`