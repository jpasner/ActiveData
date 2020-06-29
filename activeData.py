from flask import Flask, render_template

#Create Flask object 'app' with special variable __name__
app = Flask(__name__)

# Define routes and html for desired pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

# __name__ == __main__ when the script is executed directly as opposed to being imported
if __name__ == '__main__':
    app.run(debug=True)
