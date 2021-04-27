from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)
#/home/mugdha/Projects/Library_Management_System/config.py
app.config.from_pyfile('/home/mugdha/Projects/Library_Management_System/config.py')

# Initializing MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Register Form Class
class RegisterForm(Form):
    customerName = StringField("customer Name", [validators.Length(min=1, max=100)])
    customerUsername = StringField('Username- customer ID number', [validators.Length(min=1, max=25)])
    email = StringField('Email', [validators.Length(min=1, max=50)])
    mobile = StringField("Mobile Number", [validators.Length(min=12, max=12)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')

#User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
        form = RegisterForm(request.form)
        if request.method == 'POST' and form.validate():
            customerName = form.customerName.data
            email = form.email.data
            mobile = form.mobile.data
            customerUsername = form.customerUsername.data
            password = sha256_crypt.encrypt(str(form.password.data))

            # Creating the cursor
            cur = mysql.connection.cursor()

            # Executing Query
            cur.execute("INSERT INTO customers(customerName, email, mobile, customerUsername, password) VALUES(%s, %s, %s, %s, %s)", (customerName, email, mobile, customerUsername, password))


            # Commit to database
            mysql.connection.commit()

            # Close connection
            cur.close()

            flash("You are now registered.", 'success')

            return redirect(url_for('login'))

        return render_template('register.html', form= form )

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        #Get form fields
        customerUsername = request.form['customerUsername']
        password_candidate = request.form['password']

        # Create Cursor
        cur = mysql.connection.cursor()

        # Get user by Username
        result = cur.execute("SELECT * FROM customers WHERE customerUsername = %s", [customerUsername])

        if result > 0:

            # Get the stored hash
            data = cur.fetchone()
            password = data['password']


            # Comparing the Passwords
            if sha256_crypt.verify(password_candidate, password):

                # Password matched
                session['logged_in'] = True
                session['customerUsername'] = customerUsername
                # session['aadharNo'] = data['aadharNo']

                flash('You have successfully logged in', 'success')
                return redirect(url_for('bookslist'))

            else:
                error = 'Invalid login.'
                return render_template('login.html', error = error)

            #Close connection
            cur.close()

        else:
            error = 'Username not found.'
            return render_template('login.html', error = error)

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash('Unauthorized, please Login.', 'danger')
            return redirect(url_for('login'))
    return wrap

# Creating the Books list
@app.route('/bookslist')
# @is_logged_in
def bookslist():

    # Create Cursor
    cur = mysql.connection.cursor()

    # Execute
    result = cur.execute("SELECT bookName, count(bookName) AS count FROM books GROUP BY bookName")

    books = cur.fetchall()

    if result > 0:
        return render_template('bookslist.html', books = books)
    else:
        msg = 'No books found'
        return render_template('bookslist.html', msg= msg)

    # Close connection
    cur.close()

# Personal Details
@app.route('/customer_detail')
@is_logged_in
def customer_detail():

    # Create Cursor
    cur = mysql.connection.cursor()

    # Execute
    result = cur.execute("SELECT * FROM transactions WHERE customerUsername = %s", (session['customerUsername'], )) 

    transactions = cur.fetchall()
    cur.execute("select due from transactions where customerUsername like %s",(session['customerUsername'], ))
    due=cur.fetchone()
    print due
    if result > 0:
        return render_template('customer_detail.html', transactions = transactions,due=due)
    else:
        msg = 'No recorded transactions'
        return render_template('customer_detail.html', msg= msg)

    # Close connection
    cur.close()

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You have logged out.', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(host = '0.0.0.0', port = 5001, debug=True)
