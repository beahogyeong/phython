# 파이썬 제어문
# 조건문
# if
#   if 조건식:
#   (들여쓰기) 조건식의 결과가 참일 떄 실행문

# * 들여쓰기
# 1. 공백이나 탭을 통해서 들여쓰기를 수행
# 2. 공백의 개수는 무관
# 3. 탭은 1개만 사용해야한다.
# 4. 같은 영역 들여쓰기를 통일해야한다.

age = input("당신은 몇 살입니까?")
age = int(age)

if age >=20:
        print('성인 입니다')
        print('나이 : {}'. format(age))
else:
        print('청소년입니다.')
        print('나이 : {}'.format(age))
