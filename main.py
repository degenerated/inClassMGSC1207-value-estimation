from flask import Flask, render_template, request, redirect, url_for, abort
from datetime import datetime  # Import the datetime module

app = Flask(__name__)

# Store submitted data with timestamp
user_data = []

# Password for secure-clear

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a_number = request.form['a_number']
        name = request.form['name']
        question_one = request.form['question_one']
        question_two = request.form['question_two']

        # Validate A number and Answer
        if a_number.lower().startswith('a') and question_one.isdigit() and question_two.isdigit():
            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            user_data.append({
                'a_number': a_number,
                'name': name,
                'question_one': int(question_one),
                'question_two': int(question_two),
                'timestamp': timestamp  # Include the timestamp in user_data
            })

            return redirect(url_for('index'))
        else:
            return "Invalid input. A number must start with 'A' or 'a', and Both Answer must be a number."

    return render_template('index.html', users=user_data)

@app.route('/summary')
def summary():
    # question_ones = [user['question_one'] for user in user_data]
    question_results = [{'question_one': user['question_one'], 'question_two': user['question_two']} for user in user_data]
    return render_template('summary.html', question_results=question_results)

@app.route('/secure-summary')
def secure_summary():
    secure_data = [{'name': user['name'], 'a_number': user['a_number'], 'question_one': user['question_one'], 'question_two': user['question_two'], 'timestamp': user['timestamp']} for user in user_data]
    return render_template('secure_summary.html', secure_data=secure_data)

@app.route('/secure-clear')
def secure_clear():

        # Check if the provided password is correct
            # Clear user_data
            user_data.clear()
            return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
