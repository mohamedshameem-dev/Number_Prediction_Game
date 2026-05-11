# Number Prediction Game

## Overview

The **Number Prediction Game** is a simple Python GUI application built using **Python Tkinter**.

This application guides users through a series of mathematical steps and predicts the original number selected by the user based on the final calculated value entered.

The project demonstrates:

- Python GUI development
- Tkinter basics
- Input validation
- Event-driven programming
- Step-by-step UI interaction
- Business logic implementation

---

## Features

- Interactive desktop UI
- Step-by-step instructions display
- Input validation
- Supports 2 digit final values
- Predicts original selected number
- Error handling for invalid inputs
- Lightweight Python project for beginners

---

## Technologies Used

| Technology | Purpose        |
|------------|----------------|
| Python     | Core programming |
| Tkinter    | GUI framework  |

---

## Project Structure
NumberPredictionGame/
│
├── number_prediction.py
├── README.md
└── requirements.txt

---

## How the Logic Works

The application follows these steps:

1. User chooses a number
2. Multiply by 5
3. Add 5
4. Multiply by 2
5. Add 2
6. Enter final value

The system then:

- Takes all digits **except the last digit**
- Subtracts 1
- Predicts the original selected number

---

## Example

**User Selection:** `4`

**User Calculations:**
4 × 5 = 20
20 + 5 = 25
25 × 2 = 50
50 + 2 = 52

**Final Input:** `52`

**Application Output:**
Selected Number is: 4

---

## Installation

### Step 1 — Install Python

Download Python from the [Python Official Website](https://www.python.org/downloads/)

### Step 2 — Run the Application

Open terminal or command prompt:

```bash
python number_prediction.py
```

---

## Input Validation

**Accepted inputs:**
- Integer values only
- 2 digit numbers

**Blocked inputs:**
- Text inputs
- Special characters
- Decimal values
- Floating-point numbers

---

## UI Features

The UI includes:

- Start button
- Dynamic instruction display
- Text input field
- Predict button
- Result display section

---

## Future Enhancements

Possible improvements:

- [ ] Dark mode UI
- [ ] 2 to 5 digits support
