#모듈 임포트
from flask import Flask

#웹앱 객체를 만듭니다.
app = Flask(__name__)

#웹브라우저에서 /를 경로로 지정합니다. localhost의 첫 페이지
@app.route('/')
def hello_world():      #함수이름을 정합니다.
   return 'Hello Flask~!!' #해당 텍스트를 html페이지로 만듭니다.

if __name__ == '__main__':  #파이썬 메인의 위치를 지정합니다.
   app.run()  #웹앱을 실행합니다.