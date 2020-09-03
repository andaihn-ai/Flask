from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def startPage():
    return '시작페이지 입니다. '

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile : ' + username

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('get_profile', username='flask'))
    
    app.run(host='0.0.0.0', port='80', debug=True)

#with는 try/catch 구문 대신 사용할 수 있는 예외처리를 위한 키워드 입니다.

#test_request_context()함수는 with와 함께 사용하여 임시 사용과같은
#테스트 용도로 사용할 수 있습니다.

#url_for는 @app.route아래에 있는 함수를 직접호출할 수 있습니다.