from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!! I'am Seydan."

@app.route("/second")
def second():
    return "This is the second page"

@app.route("/third")
def third():
    return "This is the third page`"

@app.route('/third/subthird')
def third1():
    return "This is the subpage of third page"

@app.route("/fourth/<string:id>")
def fourth(id):
    return f"Id of this page is {id}"

if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)