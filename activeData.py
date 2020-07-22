from flask import flask, render_template
import pymongo
from bson.json_util import dumps #pymongo utilities

mongoConnection = mymongo.Connection("localhost",27017) # Connect to pymongo server
myDB = mongoConnection["Norton4NID_Database"] #specify database
collection = myDB.Div5_Voter_Roll_Jake_Prioritization #specify collection

#Create Flask object 'app' with special variable __name__
app = Flask(__name__)

# Define routes and html for desired pages
@app.route('/')
def home():
    return render_template('home.html')

# Every webpage needs an about page!
@app.route('/about/')
def about():
    return render_template('about.html')

# This exmple returns a data object of your choice
@app.route('/data/')
def data():
    string = "string!"
    return string

@app.route('/query/')
def data():
    string = "string!"
    return json_object

# __name__ == __main__ when the script is executed directly as opposed to being imported
if __name__ == '__main__':
    app.run(debug=True)
