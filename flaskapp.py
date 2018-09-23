from flask import Flask, render_template
from gamelogic import Game
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('game_page.html')
    # return app.send_static_file('game_page.html') 

@app.route('/start_game/<user><comp>')
def start_game(user,comp):
    g = Game(user, comp)
    return g

@app.route('/update_board/<game><val><int:index>')
def update_board(val, index):
    status = g.update_board(val,index)
    return status



if __name__ == "__main__":
    app.run()