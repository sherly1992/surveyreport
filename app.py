from flask import Flask,render_template
app = Flask(__name__)


@app.route('/index')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/bar')
def bar():
    return render_template("bar-stack.html")

@app.route('/bar2')
def bar2():
    return render_template("bar-y-category-stack.html")

@app.route('/single.html')
def single():
    return render_template("single.html")

@app.route('/shu')
def shu():
    return render_template("jxbgs.html")
if __name__ == '__main__':
    app.run()
