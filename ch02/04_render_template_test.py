from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def startPage():
    return '시작페이지 입니다. http://IP주소/hello/name으로 실행해주세요.'

@app.route('/hello/')
@app.route('/hello/<name>')
#render_template함수는 templates폴더의 파일로 포워딩 시켜줍니다.

def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)