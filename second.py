arr = [1,2,3,"hello",True]
arr2 =[]
arr3 = list()
num=1

print(arr[3]) #앞에서부터 네번째인 hello 출력됨
print(arr[-3]) #뒤에서부터 1,2,3번째인 3이 출력됨

##while 하단에 else 사용 시 while조건 부합하지 않는경우 else문의 내용 실행함
while num ==2 :
  print("d") 
  print(1)
else:
  print(3)

#append() 요소의  추가
arr.append("777")
print(arr)

#len() 배열의 길이를 나타내는 함수
print(len(arr))

arr22 = [[1,2,3,4],[5,6,7,8]] #2차원 배열
print(arr22[0][1])

# sort() 오름차순으로 정렬을 해주는 함수
# arr.sort()

# reverse() 현재 리스트 뒤집기
# arr.reverse()

# remove(x) 요소 x 없애기
# arr.remove(777)

# count(x) 요소 x의 개수
# arr.count(777)

# insert(인덱스,값) 특정 위치에 요소를 삽입
# arr.insert(3,-20) 4번째 인덱스에 -20을 추가함

# index(x) 요소 x의 위치
# arr.index(-777)


