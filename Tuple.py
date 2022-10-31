# 빈 튜플 선언
t1 =()

# 튜플 () / {}set / [] 리스트 / {,} 딕셔너리 

# 생성 수정 추가 삭제 불가
t2 =(1,2,3,4)
print(t2)

# set = 집합
# 인덱스가 존재하지 않음 = 순서가 없이 한곳에 모아둔것임
s1 = set([1,3,5])
s2 = set([2,4,6])

print(s1)

# .add() = 값 1개 추가

# .update() = 값 여러개 추가

# .remove() = 해당 값 제거, 해당 값 없을 시 오류 발생함
# s1.remove(3)

# .discard() 
# s1.remove(3)
# remove 와 차이점. 존재하지 않는 값을 삭제 시에도 오류 발생하지 않음

# 집합끼리 합 가능
print(s1 | s2)
print(s1.union(s2))

# 교집합
print(s1&s2)
print(s1.intersection(s2))

# 차집합
print(s1-s2)
print(s1.difference(s2))

# 대칭차집합
print(s1^s2)

# sum() = 리스트나 튜플에 사용하며 숫자로 이루어진 자료형에 한해 총 합을 구해준다
arr = [1,2,3,4,5]
print(sum(arr))

# min() = 최솟값 구하는 함수
print(min(arr))

# max() = 최대값 구하는 함수
print(max(arr))

# pow(a,b) 거듭제곱 
print(pow(6,3))

#사용자 제작 함수
def test():
  print("사용자 제작 함수 실행")
test()

# 디폴트 매개변수 -> 매개변수 옆에 ='' 으로 디폴트 값 정할 시 매개변수 미지정한 경우 해당 값을 출력해줌
def test2(t1='oo',t2='im si gap'):
  print("hello",t1,t2)
test2()