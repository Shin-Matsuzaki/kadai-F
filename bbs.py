"""
要件
・Usernameに投稿者名を入力，Messageに投稿内容を入力
・「送信」ボタンで投稿される
・水平線区切りで投稿が表示　Username未記入で「名無しさん」になる
・投稿された内容が保存される
"""

from flask import Flask, render_template, request

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
