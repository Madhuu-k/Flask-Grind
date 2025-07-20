from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page(): 
    return render_template('practice1.html')

@app.route('/marksheet')
def marks_page():
    items = [{'id' : '1210', 'name' : 'Shree Ram', 'marks' : 100},
             {'id' : '1211', 'name' : 'Shree Ram', 'marks' : 90},
             {'id' : '1212', 'name' : 'Shree Ram', 'marks' : 70},
             {'id' : '1213', 'name' : 'Shree Ram', 'marks' : 99},
             {'id' : '1214', 'name' : 'Shree Ram', 'marks' : 80}]
    return render_template('practice1.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)
