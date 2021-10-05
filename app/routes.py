#from app import app
#@app.route('/')
#@app.route('/index')
#def index():
   # return 'Hello World'
from flask import render_template
from app import app
print('Hello world')
@app.route('/')
@app.route('/index')
def index():
    user={'username':'DIMA'}
    posts = [
        {
            'author':{'username':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'username':'Susan'},
            "body":"The Avengers movie was so cool!"
        },
        {
            'author':{'username':'Василиий'},
            'body':'Привет!!'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)


