# 빈 딕셔너리 생성, 중괄호로 생성한다.
# 키(인덱스)를 사용자가 임의로 만들어 호출 가능하다
# 홍길동 이라는 키(인덱스)의 값은 010-1234-1234가 된다.

dic = {}
dic["홍길동"]="010-1234-1234"
print(dic)
print(dic['홍길동']) #키로 해당 값만 출력

# get() 키 유무 확인, 없는 키값은 None 출력, 있는 키면 해당 키의 값 출력

# del() 키 삭제기능
# del dic["홍길동"] 시 홍길동 이라는 키값이 삭제됨