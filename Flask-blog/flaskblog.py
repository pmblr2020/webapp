from flask import Flask, escape, request, render_template, url_for,flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='d4c4ec2c345fde0ae32a86fdd32c28b72c7bd0f79ad7db1ca96b20a02c124141'

posts=[
    {
        'author':'InteliServe',
        'title':'Triage model',
        'content':'More at here'
    },
    {
        'author': 'InteliServe',
        'title': 'Triage cleanup',
        'content': 'More at here'
    },
    {
        'author': 'InteliServe',
        'title': 'Ingestion start',
        'content': 'More at here'
    },

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register',methods=['GET', 'POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account crated for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login' ,methods=['GET', 'POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =='password':
            flash('You have been LogIn', 'success')
            return redirect(url_for('home'))
        else:
            flash('LogIn unsuccessful, Please check your Username and Password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
    app.run(debug=True)