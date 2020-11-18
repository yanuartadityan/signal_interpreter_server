# routes.py
from flask import Flask, request
from signal_interpreter_server.src_server.json_parser import SignalParser


signal_interpreter_app = Flask(__name__)

@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    # get data
    data = request.get_json()

    # create a parser, and use it to get signal value
    ps = signal_interpreter_app.config.get('signal_db')
    signal_name = ps.get_signal_by_id(data["signal"])

    return {
        "title": signal_name
    }