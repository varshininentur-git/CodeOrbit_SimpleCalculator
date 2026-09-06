from flask import Flask, render_template, request


# Create the Flask application.
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    """Show the calculator and process submitted calculations."""
    result = None
    error = None
    first_number = ""
    operator = "+"
    second_number = ""

    # Process the form only after the user clicks Calculate.
    if request.method == "POST":
        first_number = request.form.get("first_number", "")
        operator = request.form.get("operator", "")
        second_number = request.form.get("second_number", "")

        # Convert both inputs to numbers and show a friendly message if that fails.
        try:
            first_value = float(first_number)
            second_value = float(second_number)
        except ValueError:
            error = "Error: Please enter valid numbers."
        else:
            # Perform the selected operation.
            if operator == "+":
                result = first_value + second_value
            elif operator == "-":
                result = first_value - second_value
            elif operator == "*":
                result = first_value * second_value
            elif operator == "/":
                if second_value == 0:
                    error = "Error: Cannot divide by zero."
                else:
                    result = first_value / second_value
            else:
                error = "Error: Invalid operator."

    # Send the values, result, and error message to the HTML template.
    return render_template(
        "index.html",
        first_number=first_number,
        operator=operator,
        second_number=second_number,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    # Start the development server when this file is run directly.
    app.run(debug=True)