from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     return "<h1>Hello, Flask!</h1>"

# @app.route('/new')
# def new_message():
#     return "<h1>This is the new page accessed by /new</h1>"

# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This page is about {username}!!</h1>'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/base')
def base_page():
    items = [
        {'id': 1, 'name' : 'Madhu'},
        {'id' : 2, 'name' : 'John'},
        {'id' : 3, 'name' : 'Seth'}
    ]
    # return render_template('base.html', item_name='Flask!')
    return render_template('base.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)
