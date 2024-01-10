from flask import Flask,jsonify, request

app = Flask(__name__)

numbers = [
    {
        'id': 1,
        'name': u'Rahul',
        'contact': u'9356235477', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Sofia',
        'contact': u'9624352666', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-no", methods=["POST"])
def add_number():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    number = {
        'id': numbers[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    numbers.append(number)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })

@app.route("/get-no")
def get_number():
    return jsonify({
        "data" : numbers
    }) 
if __name__=='__main__':
    app.run(debug=True)