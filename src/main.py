from flask import Flask, request, render_template
import sqlite3
import hashlib

app = Flask(__name__)
DATABASE = 'Database/SystemDiagnoses.db'  # Update with the correct path to your database


@app.route('/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # Collect form data
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        dob = request.form['dob']
        email = request.form['email']
        # Hash the password before storing
        password_hash = hashlib.sha256(request.form['password'].encode()).hexdigest()
        gender = request.form['gender']

        # Connect to the SQLite database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert the new user into the 'users' table
        cursor.execute(
            'INSERT INTO users (FirstName, Surname, Email, Gender, DateOfBirth, Password) VALUES (?, ?, ?, ?, ?, ?)',
            (first_name, last_name, email, gender, dob, password_hash))
        conn.commit()  # Commit changes
        cursor.close()  # Close the cursor
        conn.close()  # Close the connection

        return render_template('homePage.html')
    else:
        # Render the registration form template
        return render_template('registration.html')  # Ensure 'registration.html' is in the 'templates' directory


if __name__ == '__main__':
    app.run(debug=True)
