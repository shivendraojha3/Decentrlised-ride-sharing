from flask import Flask, request

app = Flask(__name__)

# Route for login
@app.route('/login', methods=['POST'])
def login():
    # Handle login logic here
    return 'Login route'

# Route for signup
@app.route('/signup', methods=['POST'])
def signup():
    # Handle signup logic here
    return 'Signup route'

# Route to store consumer data
@app.route('/consumer', methods=['POST'])
def store_consumer_data():
    data = request.form  # Access form data
    # Process and store consumer data logic here
    return 'Consumer data stored successfully'

# Route to store driver data
@app.route('/driver', methods=['POST'])
def store_driver_data():
    data = request.form  # Access form data
    # Process and store driver data logic here
    return 'Driver data stored successfully'

if __name__ == '__main__':
    app.run(debug=True)

