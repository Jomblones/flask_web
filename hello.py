from flask import Flask, render_template

#   Create Flask Instance
app = Flask(__name__)


#  Create route decorator
#@app.route("/")
#def index():
#    return "<h1>Hello World!</h1>"


#   render_template to render html
@app.route("/")
def index():
    first_name = "Farhan"
    stuff = "This is bold Text"
    favourite_pizza = ["Pepperoni","Chese","Mushrooms",41]
    
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favourite_pizza=favourite_pizza)


#   localhost:5000/user/name
@app.route("/user/<name>")
def user(name):
    return render_template("user.html",user_name=name)

#   Custom Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500



#       Jinja Documentation  
#   Jinja DjangoHTML filter
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags