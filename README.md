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
- [Project Structure](#project-structure)  
- [Troubleshooting](#troubleshooting)  
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

### Steps (Windows-focused)

1. **Clone or download** the project folder to your local machine.

2. Open **PowerShell or Command Prompt**, then navigate to the project directory.

3. **Create a virtual environment**:
   ```powershell
   py -3 -m venv .venv
