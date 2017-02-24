from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@socketio.on('knob_turn')
def on_knob_turn(data):
    emit('knob_turn', data, broadcast=True)
