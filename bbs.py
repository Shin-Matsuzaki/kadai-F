"""
要件
・Usernameに投稿者名を入力，Messageに投稿内容を入力
・「送信」ボタンで投稿される
・水平線区切りで投稿が表示　Username未記入で「名無しさん」になる
・投稿された内容が保存される
"""
import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/bbs', methods=["GET", "POST"])
def index():
    post_list = []
    if request.method == 'GET':
        return render_template('bbs.html')
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        if username == '':
            username = '名無しさん'

        with open('post.csv', 'a') as f:
            f.write(f'{username}, {message}\n')
        with open('post.csv', 'r') as f:
            line = f.readline()[:-1]
            while line:
                row = line.split(',')
                post_list.append(row)
                line = f.readline()[:-1]
        return render_template('bbs.html', post_data=post_list)


def main():
    # 1行目にタグ付けして管理しようかと頑張った痕跡
    # if not os.path.isfile("post.csv"):
    #     with open("post.csv", "w") as f:
    #         writer = csv.writer(f)
    #         writer.writerow(['username', 'message'])

    app.run(debug=True, port=8888)


if __name__ == '__main__':
    main()
