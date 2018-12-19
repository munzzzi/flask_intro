from flask import Flask, render_template
app = Flask(__name__)
import random

@app.route("/")
def hello():
    return '''<h1>오잉<h/1>'''
    
    
@app.route("/html_tag")
def html_tag():
    return '''
    <h1>첫번째<h/1>
    <h2>두번째<h/2>
    '''
    
    
@app.route("/html_file")    
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html",people=name)
    
@app.route("/cube/<int:num>")
def cube(num): 
    return render_template("cube.html",number=num)
    
    
@app.route('/lunch')
def lunch():
    menu=["삼겹살","샤브샤브","치킨","국밥"]
    pick = random.choice(menu)
    return render_template("lunch.html",pick=pick)
    
    
@app.route('/lotto')
def lotto():
    numbers= range(1,46)
    pick=random.sample(numbers,6)
    sort_pick = sorted(pick)
    return render_template("lotto.html", sort_pick=sort_pick )
    
@app.route('/naver')
def naver():
    return render_template("naver.html")
    
    
@app.route('/google')
def google():
    return render_template("google.html") 
    
    
@app.route('/wiki')
def wiki():
    return render_template("wiki.html")  
