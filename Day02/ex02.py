# 컬랙션
# : '모음집'
# 여러 값을 하나의 이름으로 묶어서 관리하는 자료형

# 컬렉션 종류
# 1. 리스트
# 2. 튜플
# 3. 세트
# 4. 딕셔너리

# 리스트
# : 서로 다른 자료형의 값을 지정할 수 있는 컬렉션

# 1i = [값1, 값2, ...]
li = [100, 12.34, 'hello']
print('1i : ', li)

#리스트 인덱싱
print('1i[0] : ', li[0])
print('1i[1] : ', li[1])
print('1i[2] : ', li[2])

# 리스트 슬라이싱
li2 = ['월', '화', '수', '목', '금', '토', '일']
print('li2[0:5] : ', li2[0:5])    #평일
print('li2[5:7] : ', li2[5:7])    #주말

print('li2[:5] : ', li2[:5])      #평일
print('li2[5:] : ', li2[5:])      #주말

# 요소 추가 및 삭제
# - 요소 추가함수  : append(), insert()
# - 요소 삭제함수  : pop()

# append()        : 마지막에 요소 추가
print('### append( ###)')

li3 = [1,2,3,4,5]
print(li3)

li3.append(6)
print(li3)

li3.append(7)
print(li3)

# insert(index, 추가할 요소) : 특정 index 에 요소 추가
print('### index() ###')
li4 = [1,3,5,7,9]
print(li4)

li4.insert(1, 2)
print(li4)

li4.insert(3, 4)
print(li4)

li4.insert(5, 6)
print(li4)

li4.insert(7, 8)
print(li4)


# pop(index) : 특정 index 를 지정하여 삭재
# index 를 생략하면 마지막 요소를 삭제
print('### pop() ###')
print(li4)

li4.pop()
li4.pop()
li4.pop()
li4.pop()
print(li4)

li4.pop(2)
print(li4)
