#!/usr/bin/env uv run --script
#  このスクリプトはちょっと特殊です。以下の方法で起動してみてください(PEP723)
# uv run --script 03/bottle_example.py
# PEP723: https://peps.python.org/pep-0723/
# /// script
# dependencies = [
#     "bottle",
# ]
# ///
from bottle import route, run

# / (ルートURL) へのアクセスを hello 関数に結びつける
@route('/')
def hello():
    return "<h1>Hello World!</h1>"

# /user/<name> へのアクセスを greet 関数に結びつける
@route('/user/<name>')
def greet(name):
    return f"<h1>こんにちは, {name}さん!</h1>"

run(host='localhost', port=18080)
