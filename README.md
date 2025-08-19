# AI-astrologer
to predict your astrology behavior using AI 
# AI Astrologer

A simple web app built with Flask that generates astrology reports based on user birth details (name, date/time/place of birth) and allows one free-text question.

---

##  Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Setup & Installation](#setup--installation)  
- [Usage](#usage)  
- [Dependencies](#dependencies)  
- [Authors & License](#authors--license)

---

## Overview

The **AI Astrologer** app has two components:

1. **Backend** (`backend.py`): Calculates Sun sign and generates a brief astrology report based on birth details.
2. **Frontend** (`ui.html` and `app.py`): Provides a user interface via Flask for input and displays a friendly, formatted result plus a Q&A section.

---

## Features

- Collects user inputs: Name, Date of Birth, Time of Birth (optional), Place (optional).
- Calculates Sun sign using Western zodiac date ranges.
- Provides a user-friendly summary (Sun sign, element, age, personality).
- Accepts a free-text question (e.g., about career or relationships) and generates a simple “astrology-aware” response.

---

## Setup & Installation

### Prerequisites

- **Python 3.9+**
- **Git** (if you're cloning from a repository)

## Installation & Setup

1. **Clone or download** the project folder to your local machine.

2. Open **PowerShell or Command Prompt**, then navigate to the project directory.

3. **Create a virtual environment**:
   ```powershell
   py -3 -m venv .venv

4.  **Create and activate a virtual environment** (recommended):
    ```bash
    # Create the environment
    python -m venv .venv

    # Activate it (Windows)
    .venv\Scripts\activate
    ```
    *You should now see `(.venv)` before your command prompt — this confirms you’re in the virtual environment.*

5.  **Install the required dependencies**:
    ```bash
    pip install Flask python-dateutil
    ```

6.  **(Optional) Save the dependencies to a requirements file**:
    ```bash
    pip freeze > requirements.txt
    ```

## Usage

1.  **Start the Flask development server**:
    ```bash
    python app.py
    ```

2.  Open your web browser and go to `http://localhost:5000`.

3.  Fill in your name and date of birth (time and place are optional). Click **"Get Astrology Report"**.

4.  You'll see a friendly summary (e.g., *“Your Sun sign is Leo – confident, expressive, generous…”*). You can also ask a specific question (about career, love, health, etc.) and get a thoughtful AI-generated response.

## Dependencies

This project relies on the following Python packages:
*   **[Flask](https://flask.palletsprojects.com/)**: A lightweight WSGI web application framework.
*   **[python-dateutil](https://pypi.org/project/python-dateutil/)**: Provides powerful extensions for parsing and manipulating dates and times.

## Authors & License
**Created by:** sourav mondal


Copyright (c) 2024 sourav mondal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
