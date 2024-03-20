# 멤버쉽 연산자
# a in c : 컬렉션 c에 요소에 a 가 표함되어 있으면 true
#          그렇지 않으면 false

a = [1,2,3]

x = 3 in a
y = 10 in a
z = 10 not in a

print('x : {}'.format(x))
print('y : {}'.format(y))
print('z : {}'.format(z))
