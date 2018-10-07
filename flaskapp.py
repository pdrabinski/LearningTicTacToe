from flask import Flask, render_template, g, request
from gamelogic import Game
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('game_page.html')
    # return app.send_static_file('game_page.html') 

@app.route('/start_game', methods=['POST'])
def start_game():
    user = request.args.get('user')
    comp = request.args.get('comp')
    game = Game(user,comp)
    g.game = game
    return "true"

# @app.route('/start_game_2/')
# def start_game():
#     game = Game('x', 'o')
#     g.game = game
#     return "true"

@app.route('/update_board/')
def update_board(val, index):
    game = g.game
    status = game.update_board(val,index)
    return status

if __name__ == "__main__":
    app.run()