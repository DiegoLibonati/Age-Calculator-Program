# Age Calculator Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Use `python -m src.app` to execute program

## Description

I made a program in Python using Tkinter as user interface that allows the user to visualize how old he/she is depending on the year, month and day we pass it.

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
No 3rd libraries used.
```

#### Requirements.test.txt

```
pytest
```

## Portfolio Link

[https://www.diegolibonati.com.ar/#/project/Age-Calculator-Program](https://www.diegolibonati.com.ar/#/project/Age-Calculator-Program)

## Video

https://user-images.githubusercontent.com/99032604/198900699-c37c81e7-17e7-4ce9-9211-9b8af5f73177.mp4

## Testing

1. Join to the correct path of the clone
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute: `pip install -r requirements.txt`
5. Execute: `pip install -r requirements.test.txt`
6. Execute: `pytest --log-cli-level=INFO`

## Documentation

Whenever the `Calculate age` button is touched and the inputs are complete this function will be executed: `_get_current_age()`. This function will collect all the information that we pass it by the inputs and depending on the date that we pass it will make the pertinent calculations to know how old is the person with that information entered:

```
def _get_current_age(self) -> None:
    name = self.name.get()

    try:
        year = int(self.year.get())
        month = int(self.month.get())
        day = int(self.day.get())
    except ValueError:
        self.final_label["text"] = ERROR_NON_NUMERIC
        return

    if not name or not year or not month or not day:
        self.final_label["text"] = ERROR_MISSING_VALUES
        return
    elif year > datetime.now().year:
        self.final_label["text"] = ERROR_FUTURE_DATE
        return
    elif not (1 <= month <= 12):
        self.final_label["text"] = ERROR_MONTH_RANGE
        return
    elif not self.is_valid_date(year, month, day):
        self.final_label["text"] = ERROR_INVALID_DATE
        return
    
    self._calculate_age(name=name, day=day, month=month, year=year)

def _calculate_age(self, name: str, year: int, month: int, day: int) -> None:
    current_date = datetime.now()
    relative_age = current_date.year - year if month < current_date.month or month == current_date.month and day <= current_date.day else current_date.year - year - 1
    self.final_label["text"] = f"Hi {name}, your age is {relative_age}."
```
