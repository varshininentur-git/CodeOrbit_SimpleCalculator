# 🧮 Simple Calculator

A beginner-friendly web-based **Simple Calculator** built using Python, Flask, HTML, and CSS. The application performs basic arithmetic operations and handles invalid user inputs safely.

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 🚫 Division-by-zero handling
* ⚠️ Invalid input handling
* 🎨 Clean and responsive user interface
* 🌐 Web-based calculator
* 🐍 Python and Flask backend
* 📝 HTML and CSS frontend

## 🛠️ Technologies Used

| Technology | Purpose           |
| ---------- | ----------------- |
| Python     | Application logic |
| Flask      | Web framework     |
| HTML5      | Webpage structure |
| CSS3       | Styling           |

## 📁 Project Structure

```text
CodeOrbit-Task1/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ How It Works

1. Enter the first number.
2. Select an arithmetic operation.
3. Enter the second number.
4. Click the **Calculate** button.
5. The Flask backend processes the input.
6. Python performs the selected calculation.
7. The result is displayed on the webpage.

## 🚨 Error Handling

The application handles invalid inputs using Python's `try/except`.

### Invalid Number

If the user enters an invalid value:

```text
Error: Please enter a valid number.
```

### Division by Zero

If the user tries to divide by zero:

```text
Error: Cannot divide by zero.
```

The application handles these errors without crashing.

## 💻 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Go into the project folder:

```bash
cd CodeOrbit-Task1
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application:

```bash
python3 app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## 🧪 Example

```text
First Number: 10
Operation: +
Second Number: 5

Result: 10 + 5 = 15
```

Another example:

```text
First Number: 20
Operation: /
Second Number: 4

Result: 20 / 4 = 5
```

## 🎯 Learning Objectives

This project demonstrates:

* Python programming
* Flask web development
* HTML forms
* CSS styling
* Handling user input
* Functions
* Arithmetic operations
* Exception handling using `try/except`
* Connecting a Python backend with an HTML frontend

## 🚀 Future Improvements

Some possible improvements include:

* Add calculation history
* Add scientific calculator operations
* Add dark mode
* Add keyboard support
* Add JavaScript for a more interactive interface
* Improve the mobile interface
