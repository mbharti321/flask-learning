# Flask learning project for api creation

### **Notes:**

- Web Server Gateway Interface (WSGI): a universal interface between the web server and the web applications.
- **Werkzeug:** It is a WSGI toolkit, which implements requests, response objects, and other utility functions.
- **Jinja2:** Jinja2 is a popular templating engine for Python.
- `app.route(rule, options)`
- `app.run(host, port, debug, options)`
  
- **code snippet**
  ```python
  from flask import Flask
  app = Flask(__name__)

  @app.route('/')
  def hello_world():
     return 'Hello World.'

  if __name__ == '__main__':
     # app.run()
  	 app.run(debug=True)
  ```
  - Run Flask app: `flask run`
  ---

  ```python
  # build a URL dynamically or using path variable
  @app.route('/hello/<name>')
  def helloPathvriable(name):
     return 'Build a URL dynamically or using path variable by "%s"' %name
  ```
  ```python
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
  ```
  
- Fetching data from UI from
  - `user = request.form['nm']` : if method is post
      ```python
         @app.route('/login', methods=['POST', 'GET'])
         def login():
            if request.method == 'POST':
               user = request.form['nm']
               return redirect(url_for('success', name=user))
            else:
               user = request.args.get('nm')
               return redirect(url_for('success', name=user))
      ```
  - `User = request.args.get(‘nm’)`: if the method is GET
      ```python
      @app.route('/add')
      def add():
         a = int(request.form.get('a'))
         b = int(request.form.get('b'))

         return str(a+b)
      ```

- **`__name__`**:** is **a built-in variable that evaluates the name of the current module**
- **web templating system:**  refers to designing an HTML script in which the variable data can be inserted dynamically
  - for Flask its **jinja2.**
- To render HTML pages: `render_template(‘hello.html’)`

### The **jinja2** template engine uses the following delimiters for escaping from HTML.

- **{% ... %}:** for Statements
- **{{ ... }}:** for Expressions to print to the template output
- **{# ... #}:** for Comments not included in the template output
- **# ... ##:** for Line Statements

### Use static files in HTML pages

- Create a `static` folder under `templates` folder> put all static files here
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='main.css') }}" />
  <script
    type="text/javascript"
    src="{{ url_for('static', filename = 'login.js') }}"
  ></script>
  ```

---

- Reference: [Tutoial point flask](https://www.tutorialspoint.com/flask/index.htm)
