from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def loginScreen():
    return render_template('login.html')


@app.route('/success/<name>')
def success(name):
    # return 'welcome %s' % name
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('success.html', name=name, dict=dict)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))



@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run(debug=True)
