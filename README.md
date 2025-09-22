# Age Calculator Program

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.app` to execute program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

I made a program in Python using Tkinter as user interface that allows the user to visualize how old he/she is depending on the year, month and day we pass it.

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
pre-commit==4.3.0
```

#### Requirements.test.txt

```
pytest==8.4.2
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[https://www.diegolibonati.com.ar/#/project/Age-Calculator-Program](https://www.diegolibonati.com.ar/#/project/Age-Calculator-Program)

## Video

https://user-images.githubusercontent.com/99032604/198900699-c37c81e7-17e7-4ce9-9211-9b8af5f73177.mp4

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Join to the correct path of the clone
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller --onefile --windowed src/app.py`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Join to the correct path of the clone
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller --onefile --windowed src/app.py`

Alternatively, you can run the helper script: `./build.sh`

## Known Issues
