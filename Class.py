class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1+num2
        return self.result
    def sub(self, num1, num2):
        self.result = num1-num2
        return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

print(cal1.add(3,4))

print(cal2.add(3,7))

print(cal3.sub(10,1))

#모듈이란
#미리 만들어 놓은 파이썬(.py) 파일을 뜻한다. 즉 함수와 변수,클래스 등을 미리 파이썬 파일 하나에 만들어 놓고 다른 곳에서 가져다 쓰기 위한 것 이다.

#모듈 불러오기
#import 형식으로 불러온다.
#import를 할 때, 작업하려는 파일과 임포트 할 파이썬 파일이 같은 경로에 있으면 문제가 없지만
#다른 경로에 있다면 따로 함수를 호출해서 경로를 추가해줘야한다.

#ex)
#모듈 전체 불러오기
#hello.py 
#import mod1

#특정 함수만 불러오기
#hello2.py
#from mod1 import add
#print(add(3,4))