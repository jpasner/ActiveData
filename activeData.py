from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap

#Create Flask object 'app' with special variable __name__
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Norton4NID_Database"
mongo = PyMongo(app)
collection = mongo.db.Div5_Voter_Roll_Jake_Prioritization

#mongoConnection = pymongo.MongoClient("localhost",27017) # Connect to pymongo server
#myDB = mongoConnection["Norton4NID_Database"] #specify database
#collection = myDB.Div5_Voter_Roll_Jake_Prioritization #specify collection

# Define routes and html for desired pages
@app.route('/')
def home():
    string = "hello"
    return render_template('home.html')

# Every webpage needs an about page!
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/query/')
def query():
    # Define MongoDB queries of interest
    query = {}

    # The MongoDB "find" method returns a cursor object which points to the documents which satisfy your "query"
    query_cursor = collection.find(query, {"_id":0}).limit(10)

    output_list = list(query_cursor)

    print(output_list)

    return render_template('query.html',output_list=output_list) #pass output_list to query.html

# __name__ == __main__ when the script is executed directly as opposed to being imported
if __name__ == '__main__':
    app.run(debug=True)
