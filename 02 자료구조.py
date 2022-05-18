# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

name = 'abc' # tap 사용시 선택 가능

# +
# 명령모드 m- 마크다운 y- 코드작성 셀
# 대제목 
## 중제목 
### 소제목
# -

# # 마크다운
# - 셀변환: 
#     - m : markdown cell 
#     - y : code cell
#     1. hi
#     1. bye
#     
#     _hi_
#     
#     *hi*
#     **hi**
#     ***hi***

# # list
# - 순서가 있는 자료구조
#     - index 로 관리한다
# - 생성
#     - list1 = [값,값,값,...]

l1 = [1, 2, 3, 4]
l2 = ['q', 1, 'sdf', True, None, 10.2, ]
print(l1[3])
print(l2[2])

# +
# 없는 인덱스 조회하면 indexError 에러가 발생한다
# -

len(l1)

l1[1:]

l2[0:2]=[]

l2

# **리스트를 포함한 자료구조도 값이다**
# - 리스트에 다른 자료구조들을 원소로 추가할 수 있다

l3 = [[1,2], [3,4], [5,6]]
print(l3[0],l3[1],l3[2])
l4 = l3[0]
print(l4[0])
l3[2][0]

l4 = [[[1,2],[3,4],[5,6]]
      ,[[10,20,],[30,40],[50,60]]
     ]
l4[0][1][1]

l4[1][2][1]

a, b ,c = [1, 2, 3,] #변수의 개수 원소의 개수가 동일해야 한다
print(a,b,c)

#정렬 원본 리스트는 변경하지 않는다.
sorted(l1)
sorted(l1, reverse=True)

#index로 삭제
del l1[3]

l1

#값으로 삭제 같은 값이 여러개가 있을 시 제일 앞에 있는 것만 삭제됨
l1.remove(1)
l1

num = [1, 2, 3]
num_Tuple = tuple(num)
num_Tuple

# # 튜플 대입

name, age, adress = ('ad', 34, 'NY')
print(name, age, adress)

name, age, adress = 'ad2', 32, 'NY2'
print(name, age, adress)

# # indexing slicing
# - 조회만 가능하고 원소를 변경할 수 없다

t1 = 100, 4, 7, 32, 32, 5
t1[0],t1[4],t1[5]

t1[::4]

t1[::-1]

sorted(t1)
#단 정렬한 튜플은 다른 리스트에 저장해야 한다 튜플의 값의 위치는 바뀌지 않는다

sorted(t1,reverse=True)

# # 딕셔너리
# - 데이터를 Key - value 쌍으로 모아서 관리하는 자료구조

#생성
p1 = {'name' : 'pipi', 'age' : 30, 'address' : 'NY' }

#값 조회
print(p1['name'])

#값 변경
p1['name'] = 'cici' #있는 키 값을 대입하면 변경
p1

#값 추가
p1['tel'] = '00700' #없는 키 값을 대입하면 추가 
p1

#dictionary.get('key') : 조회
print(p1.get('age'))


# +
#없는 키 값을 조회하면 None / 다른 반환값을 설정할 수 있다
print(p1.get('email'))

v = p1.get('email','없음')
print(v)
# -

# # 주요 메소드

p1.pop('name')

p1

del p1['tel']
p1

# # set(집합)
#
# - 중복을 허용하지 않는 자료구조

s1 = {1, 1, 1, 2, 2, 3, 3, 3, 'a', 'a', 'a', True, False, True, False}
s1
#1 == true / 0 == false

1 in s1

10 in s1

s1 = {1,2,3}
s2 = {3,4,5}
s1|s2

s1 & s2

s1 - s2

s2 - s1

# # 메소드
#

#추가 
s2.add(6)
print(s2)

s2.add(6)
print(s2) #중복되면 추가 안 됨

s2.update([1,2,3,3,30,50])
print(s2)

v = s2.pop()
print(v)
s2

# # 자료구조 변환 함수
#
# - list(자료구조) 자료구조를 list로 변환
# - tuple(자료구조)  자료구조를 tuple로 변환
# - set(자료구조) 자료구조를 set로 변환
# - dictionary로 변환하는 것은 불가능하다

t = 1, 2, 2, 10, 5, 9
l = list(t)
l, type(l)

s = set(t)
s, type(s)

t1 = tuple([1,3,10,9,11]) #list -> tuple
t1

d = {1 :'name', 2: 'age', 3: 'address'}
set(d)

list(d)

tuple(d)

# dict(key=value,key=value) dictionary를 쉽게 만들도록 도와주는 함수
d1 = dict(name = 1,age = 20 , address = 'NY')
d1


