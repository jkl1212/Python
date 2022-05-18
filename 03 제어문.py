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

# # 제어문 
# - 코드의 흐름을 제어하는 구문

# # 조건문(분기문)

#입력받은 값이 0이면 0입니다를 출력하기
num = int(input('정수: '))
if num == 0:
    print('0 입니다')
    print('zero')
print('종료')

# 입력받은 값이 0이면 "0입니다" 출력하고 0이 아니면 '0이 아닙니다' 출력한다
# if else 문: 조건이 True일 때 할일과 False 할일 두가지로 분기하는 경우
num = int(input('정수: '))
if num == 0:
    print('0 입니다')
else:
    print('0 이 아닙니다')
    print(f'입력한 숫자는 {num}입니다')
print('종료')

# +
# 입력받은 값이 0이면 '0입니다.'를 출력하고
# 양수이면 '양수입니다'를 출력
# 음수이면 '음수입니다'를 출력 한다. 
# if elif 문: 조건이 여러개일 경우 사용
# elif: else if
num = int(input('정수: '))
if num == 0:
    print('0 입니다.')
elif num > 0:
    print('양수입니다')
    print(f'입력한 숫자는 {num}입니다')
# elif num < 0:
else:  #위 조건이 모두 False이면(나머지 조건들) else문을 실행
    print('음수입니다')

print('종료')

# +
# num이 0이상이면 "양수입니다."를 출력하고 100 이상이면 "100보다 큽니다."를 출력
num = 20
if num >= 0:
    print('양수')
    
if num >= 100:
    print('100이상')
# -

if num >= 0:
    print('양수')
    if num >= 100:
        print('100이상')

# ## 반복문
# ### While 문
# - 조건이 True 인 동안 구문을 반복한다

limit = int(input('반복 횟수: '))
count = 0 #현재 몇 번째 반복인지를 저장할 변수
while limit > count : #조건 반복 횟수가 limit보다 적을 때 까지
    count = count + 1
    print(f'{count}.hi')
    print('='*10)

# ## for in 문
# - iterable(자료구조들, 문자열 등)이 가지고 있는 값을 순환조회 할 때 사용

lst = [10, 20, 5, 6, 9, 23, 44, 70, 113,100]
lst

for i in range (len(lst)):
    print(f'{i+1}.',lst[i])

for n in lst:
    print(n)
    print('='*5)

# +
for v in (10,20,30,40):
    print(v, end=',') #end=>v를 출력후 엔터대신에 출력할 값

print(' end')
# -

for c in {1,2,2,2,3,4,4,4}:
    print(c, end = '\t')

for v in dict(name='홍길동', age=20, address='서울'): #dictionary -> key가 조회된다
    print(v)

for v in "안녕하세요.abcde~":
    print(v)

list("abcdefg")

tuple("abcdefg")

set("abcdefgazaasdfasaa")

d = dict(name='홍길동', age=20, address='서울')
d

for key in d:
    print(d[key])

for v in d.values():
    print(v)

# ## continue, break
# - continue: 다음 반복을 실행해라
# - break: 반복을 멈춰라

# lst값들 중에 2의 배수만 출력
for v in lst:
    if v % 2 == 0:
        print(v)

lst

for v in lst:
    if v % 2 != 0: #2의 배수가 아니면(조건)
        continue  # 나머지 반복구문 실행하지 말고 다음 반복 실행해라
    print(v)

# +
for v in lst:
    print(v)
    if v >= 100: # break할 조건
        break #더이상 반복하지 않고 반복문을 끝낸다
    
print('end')
# -

# ## for in문 관련 함수
# - range()
#     - 특정값만큼 증감하는 연속된 숫자를 제공하는 iterable을 생성

# nums = [1, 2, 3, 4, 5, 6, 7, 8, ...,, 100]
# range(시작숫자, 끝숫자, 증감치)
range(10, 100, 10) # 10 ~ 100-1 까지 10씩 증가하는 연속된 값을 제공
                   # 생성된 값이 필요할 때 제공한다

for i in range(10, 100, 10):
    print(i)

l = list(range(10,100,10))
l

tuple(range(10,100,10)), set(range(10,100,10))

# 시작값이 종료보다 크고 증감치가 음수이면 내림차순으로 제공
list(range(100,10,-5))  #100 ~ 10-(-1) 

# 증감치를 생략 - 1
list(range(1,10)) # 1 ~ 9 1씩증가

# 시작값 생략 (증감치도 같이 생략해야함.) - 0부터 시작
list(range(10)) # 0 ~ 9

# 종료값은 생략할 수 없다.
list(range(36))

# # range() 전달하는 값이
# - 1개: 종료값
# - 2개: 시작값, 종료값
# - 3개: 시작값, 종료값, 증감치

# - enumerate()
#     - 튜플로 (반복 횟수, 값)을 묶어서 반환

list1 = [10,5,7,8,10,2]
for i in enumerate(list1):
    print(i)

for i in enumerate(list1,start = 1): #시작값을 정해줄 수 있다
    print(i)

for i in enumerate(list1,start = 1): 
    print(i, f'번호 : {i[0]}, 값 {i[1]}')

#enumerate() 반환값을 튜플 대입을 이용해서 받는다
for idx, value in enumerate(list1 , start = 1):
    print(f'{idx}. {value}')

# - zip (자료구조1, 자료구조2,...)
# - 여러 개의 자료구조 객체를 받아 같은 index값끼리 튜플로 묶어 반환한다

names = ['gigi', 'cici', 'soso']
ages = [24,43,12]
address = ['NY','HK','LA']

for i in zip(names,ages,address):
    print(i)

for name, age, addr in zip(names, ages,address):
    print(name, age, addr)

emails = ['g@a.com','c@a.com','s@a.com','k@a.com']
for name, age, addr, email in zip(names, ages,address,emails):
    print(name, age, addr, email)

# # 컴프리핸션

l1 = [1,2,2,2,3,4,5]
#l1의 원소들을 5배 한 값을 넣은 리스트 생성
new_list = []
for i in l1:
    new_list.append(i*5)
new_list

new_list2 = [i*5 for i in l1]
new_list2

new_set ={i*5 for i in l1}
new_set

new_dic = {key : value for key, value in enumerate(l1,start =100)}
new_dic

ne1_dic = {'key' + str(value):value for value in l1}
ne1_dic

# +
s = ['a','b','c','abc']

s2 =[]
for v in s:
    s2.append(v.upper())
s2 , s
# -

s4 = {v.upper()for v in s}
s4

s5 = {v:v.upper()for v in s}
s5

s = ['a','b','c','abc', 'wer', 'dse','gt']
s6=[]
for i in s:
    if len(i)==1:
        s6.append(i.upper())
s6

s7 = [i.upper() for i in s if len(i)==1]
s7




