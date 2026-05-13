# Age Snap

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Age Snap** is a desktop application built with Python and Tkinter that calculates a person's exact age in years based on their date of birth. The user provides four inputs: their name, and the year, month, and day they were born. Upon clicking the calculate button, the app validates all fields — ensuring they are filled in, that the values are numeric, that the date is a real calendar date, and that the birth year is not in the future. If any validation fails, a descriptive error dialog is shown to the user. Once all inputs are valid, the app computes the current age by comparing the birth date against today's date, correctly accounting for whether the birthday has already occurred in the current year or not. The result is displayed directly in the interface as a personalized message showing the person's name and their calculated age.

The application is structured with a clean separation of concerns: a config layer that supports `development`, `production`, and `testing` environments via a `.env` file; a UI layer composed of reusable Tkinter widgets (`LabeledEntry`, `MainView`, `InterfaceApp`); a utils layer with pure functions for validation and age calculation; a dialog error system based on a `BaseDialogError` hierarchy for consistent and user-friendly error handling; and a constants module that centralizes all user-facing strings. The app can also be packaged into a standalone executable using PyInstaller.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

All dependencies are declared in `pyproject.toml`. The `requirements*.txt` files are thin wrappers that delegate to the package extras.

#### Runtime (`pip install -e .`)

```
python-dotenv>=1.0
```

#### Dev (`pip install -e .[dev]`)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Test (`pip install -e .[test]`)

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Build (`pip install -e .[build]`)

```
pyinstaller==6.16.0
```

## Getting Started

Follow these steps to set up the project locally for development.

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e .[dev,test]`
6. Copy the development env template: `cp .env.example.dev .env` (Windows: `copy .env.example.dev .env`)
7. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Env Keys

The application is configured through environment variables loaded from the `.env` file you created in the previous step.

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.

```
ENVIRONMENT=development
```

## Testing

With the project installed and the env file in place, you can run the test suite.

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e .[test]`
6. Execute: `pytest --log-cli-level=INFO`

## Security Audit

Before shipping, check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -e .[dev]`
4. Execute: `pip-audit`

## Build

Once tests pass and the audit is clean, you can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

> **IMPORTANT — production `.env` is separate from your dev `.env`.**
> `app.spec` bundles the project-root `.env` file into the executable. Before
> building, you MUST replace your development `.env` with a production one
> (typically by copying `.env.example.prod` to `.env` just before the build).
> Never commit a real production `.env` (or real secrets) to the repository.
> After building, restore your development `.env`.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -e .[build]`
4. Prepare a production `.env`: `copy .env.example.prod .env` (edit it if needed; do NOT commit)
5. Create the executable: `pyinstaller app.spec`
6. Restore your development `.env`: `copy .env.example.dev .env`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -e .[build]`
4. Prepare a production `.env`: `cp .env.example.prod .env` (edit it if needed; do NOT commit)
5. Create the executable: `pyinstaller app.spec`
6. Restore your development `.env`: `cp .env.example.dev .env`

Alternatively, you can run the helper script: `./build.sh`

## Known Issues

None at the moment.

## Portfolio Link

[https://www.diegolibonati.com.ar/#/project/age-snap](https://www.diegolibonati.com.ar/#/project/age-snap)
