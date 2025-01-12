# Project 25: Quizzler

## Author
- **Name**: Pranjal Sarnaik  
- **Date Created**: 06 Jan 2025  
- **Last Modified**: [Provide modification dates as applicable]

---

## Description:
The **Quizzler** project is a quiz game application built using **Object-Oriented Programming (OOP)** and **Tkinter** for the graphical user interface (GUI). The app fetches a set of ten questions from the Open Trivia Database (API) and allows users to answer them through an interactive interface.  

- **Gameplay Features**:  
  1. Questions and answers are dynamically fetched from an API.  
  2. The extracted question text is displayed on a canvas, along with two buttons ("True" and "False").  
  3. Players choose between the two answers:
      - A correct answer makes the canvas green, and the score increases by one.
      - An incorrect answer makes the canvas red, and the score remains unchanged.  
  4. When all questions are answered:
      - Buttons are disabled.
      - A completion message displays the final score.  

---

## How to Use:
1. Launch the application (see installation and running instructions below).  
2. Answer each question by clicking **True** or **False**.  
3. Observe feedback (green/red canvas) and track your score on the top bar.  
4. Complete the quiz to view your final score and finish the game.

---

## Level
- **Level**: Intermediate  
- **Skills**:  
  - API Integration  
  - Object-Oriented Programming  
  - GUI Design with Tkinter  
- **Domain**: Game Development  

---

## Features
1. Dynamically fetches quiz questions and answers using an API.  
2. Provides real-time feedback for correct/incorrect answers.  
3. Displays updated scores as players progress.  
4. Disables gameplay and displays a completion message once the quiz ends.  
5. Organized codebase with three main classes:  
   - `Question`: Manages question objects.  
   - `QuizBrain`: Handles quiz logic, including question progression and answer validation.  
   - `QuizUI`: Manages the GUI, including buttons, canvas, and feedback.  

---

## Installation

1. **Clone this repository**:  
   ```bash
   git clone https://github.com/pranjalco/quizzler.git
   ```

2. **Navigate to the project directory**:  
   ```bash
   cd quizzler
   ```

3. **Install required dependencies** (if applicable). Example:  
   ```bash
   pip install requests
   ```

---

## Running the Program

1. **Ensure Python 3.9 or later** is installed on your system.  
2. Run the program using any of the following methods:  
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.  
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:  
     ```bash
     python app.py
     ```  
   - **By Double-Clicking**: Double-click `app.py` to run it directly, provided Python is set up to execute `.py` files.  
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.  

---

## File Structure

```plaintext
quizzler-intermediate/
│
├── experiments/        # Contains temporary files or practice code.
├── images/             # Contains all required images for the project.
├── screenshots/        # Contains screenshots of the program in action.
├── data.py             # Fetches questions and processes data from the API.
├── main.py             # Main entry point for running the application.
├── quiz_brain.py       # Implements QuizBrain class (quiz logic).
├── ui.py               # Implements QuizUI class (Tkinter GUI).
└── README.md           # Project documentation.
```

---

**Created by Pranjal Sarnaik**  
*© 2025. All rights reserved.*
