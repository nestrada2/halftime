from flask import Flask, render_template
from nba_api.stats.endpoints import scoreboard

# Today's Score Board
games = scoreboard.Scoreboard()

# json
x = games.get_json()

# dictionary
y = games.get_dict()

print("checking: ", y.get("Golden State"))
print(type(y))

app = Flask(__name__)

@app.route('/')
def route_default():
    print(games)
    return render_template('main.html')

@app.route('/halftime')
def route_halftime():
    return "halftime stats"

@app.route('/oneonone')
def route_one_on_one():
   return 'compare eras'

if __name__ == '__main__':
    app.run(debug=True)


'''
-------------------- Footnotes --------------------
    (1) render_template is a function that allows us to grab an HTML file and render that as our 
    web page.

    (2) It is very import that you name a folder templates that store your HTML files and that it 
    is sitting beside or in the same directory as your Python script that is running the website.

    
-------------------- References --------------------
display an image in flask - https://stackoverflow.com/questions/53758128/display-image-on-html-page-using-flask
'''