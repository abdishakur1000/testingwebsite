from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/services')
def services():
  return render_template('services.html')


@app.route('/products')
def products():
  return render_template('products.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    # Handle form submission
    username = request.form['username']
    password = request.form['password']
    # Do something with the form data (e.g. store in database)
    return redirect(url_for('index'))
  else:
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    # Handle form submission
    username = request.form['username']
    password = request.form['password']
    # Do something with the form data (e.g. check if valid credentials)
    if valid_credentials:
      return redirect(url_for('index'))
    else:
      return render_template('login.html', error='Invalid credentials')
  else:
    return render_template('login.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
