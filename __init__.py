from flask import Flask, render_template
from nba_api.stats.endpoints import scoreboard, playbyplay
import json

# Today's Score Board
games = scoreboard.Scoreboard()
plays = playbyplay.PlayByPlay("0022300735", 1, 1)

# json
x = games.get_json()

# dictionary
y = games.get_dict()

# print("checking: ", json.dumps(y, indent=4))
print(type(y))
with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(y, indent=4))

with open("plays.json", "w") as outfile:
    outfile.write(json.dumps(plays.get_dict(), indent=4))

app = Flask(__name__)

@app.route('/')
def route_default():
    print(games)
    return render_template('main.html', team_set=y["resultSets"][1]["rowSet"], game_set=y["resultSets"][0]["rowSet"])

@app.route('/players')
def route_halftime():
    return render_template('players.html')

@app.route('/one_on_one')
def route_one_on_one():
   return render_template('one_on_one.html')

@app.route('/stat_leaders')
def route_stat_leaders():
   return render_template('stat_leaders.html')

@app.route('/evolution_of_the_game')
def route_evolution_of_the_game():
   return render_template('evolution_of_the_game.html')

@app.route('/strategies')
def route_strategies():
   return render_template('strategies.html')

@app.route('/coaches')
def route_coaches():
   return render_template('coaches.html')

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