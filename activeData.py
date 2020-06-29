from flask import Flask

#Create Flask object 'app' with special variable __name__
app = Flask(__name__)

# Define a function which runs when the user navigates to home '/' or localhost:5000 if run privately
@app.route('/')
def home():
    return 'Hello World!'

# __name__ == __main__ when the script is executed directly as opposed to being imported
if __name__ == '__main__':
    app.run(debug=True)
