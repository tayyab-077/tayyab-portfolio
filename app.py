from flask import Flask,request,render_template # type: ignore


application = Flask(__name__, static_folder='my_static', static_url_path='/assets')


app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('home.html') 

if __name__ == "__main__":
    app.run(port=8000)
