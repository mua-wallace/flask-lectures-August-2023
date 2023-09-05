from flask import Flask, render_template

from friends import Friend

app = Flask(__name__)


@app.route('/')
def home():
    friends_list = Friend.get_all_friends()
    # print(friends_list)
    return render_template('index.html', friends = friends_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8000)