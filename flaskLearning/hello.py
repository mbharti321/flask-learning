from flask import Flask, redirect, url_for
app = Flask(__name__)

# using route decorator for url routing
@app.route('/')
def hello_world():
   return '<h1>Hello World</h1>'
# using route decorator for url routing

@app.route('/hello')
def hello_world1():
   return '<h1>Hello World1</h1>'

# using add_url_rule for route mapping
def addURLRule():
   return "using add_url_rule for route mapping"
app.add_url_rule('/hello2', 'addURLRule', addURLRule)

# build a URL dynamically or using path variable
@app.route('/hello/<name>')
def helloPathvriable(name):
   return 'Build a URL dynamically or using path variable by "%s"' %name


# using path variable int and float
@app.route('/integer/<int:id>')
def show_blog(id):
   return 'Blog Number %d' %id

# usingurl_for for redireactions
@app.route("/admin")
def admin():
   return 'Admin Page'
@app.route('/guest/<guest>')
def guest(guest):
   return 'Guest Page %s' %guest

@app.route('/user/<username>')
def helloUser(username):
   if username == 'admin':
      return redirect(url_for('admin'))
   else:
      return redirect(url_for("guest", guest = username))


if __name__ == '__main__':
#    app.run()
   app.run(debug=True)