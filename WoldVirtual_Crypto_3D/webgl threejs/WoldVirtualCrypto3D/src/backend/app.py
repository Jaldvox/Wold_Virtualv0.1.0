from flask import Flask, jsonify
from src.backend.state.MetaverseState import MetaverseState
from src.backend.state.UserState import UserState
from src.backend.state.SceneState import SceneState
from src.backend.state.BlockchainState import BlockchainState

app = Flask(__name__)

# Initialize states
metaverse_state = MetaverseState()
user_state = UserState()
scene_state = SceneState()
blockchain_state = BlockchainState()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Metaverse Crypto 3D API!"})

@app.route('/api/state', methods=['GET'])
def get_state():
    return jsonify({
        "metaverse": metaverse_state.get_state(),
        "user": user_state.get_state(),
        "scene": scene_state.get_state(),
        "blockchain": blockchain_state.get_state()
    })

# Additional routes can be defined here

if __name__ == '__main__':
    app.run(debug=True, port=8000)