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

#단축키
#SHIFT+ENTER = 실행
#CONTEROL+ENTER = 실행 후 실행한 cell에 머무른다
1+2

#변수
name = "홍길동" #NAME이라는 변수에 '홍길동'이라는 값을 대입

print(name)

age = 25

print(age)

age = 50

print(age)

age = age - 20

print(age)

# +
#데이터 타입
#숫자형
# -

f1 = .5 #0은 생략해도 됨
f2 = 324.3
print(f1,f2)

type(f1),type(10), type(5.5)


#지수 표기법
f3 = 5e5
print(f3)

f4 = 3e-3
print(f4)

# +
#연산자
# -

print(2**5) #제곱

print(2*5)#곱하기

print(233/2) #나누기
print(234//2) #몫
print(233//2)
print(233%2) #나머지

num =1001 #해당 num이 어떤 숫자에 대한 배수인지 확인할 때 나머지를 활용함
if num%5==0:
    print("true")
else:
    print("false")

'a'>'b'

3>5

print(bool(" "),bool('abc'),(bool('')))

#비교연산자
print(10==5)

print(ord('a'),ord('b'))

#특수문자 < 숫자 < 영문 < 한글 
print(ord('#'),ord('0'),ord('A'),ord('a'),ord('ㄱ'))

num = 30 
#num이 5~20 사이의 숫자인지 알아보기 위함
result = (num>5)|(num<20)
print(result)
print(not result)

#조건 연산자
num =10
var = '양수' if num >=0 else'음수'
#var = '값' 조건 '값'
#조건이 T이면 앞의 값 F이면 뒤의 값 반환
print(var)

print('C:\tdhjs\nhkhk\.dfsf')
#escape 문자의 \를 무시 r-string
print(r'C:\tdhjs\nhkhk\.dfsf')

print('a\\b\\c')
print("I'm a boy")

print('abc"def')
print("abc\"def")

var = 'dfsfadsgasfsdgfdgs'
len(var)

print('aac',end = '-')
print ('fgd')

#indexing
s ="안녕하세요 반가워요"
print(s)

print(s[2])
print(s[6])
print(s[-3])
print(s[-7])

s.index('가')

s[2:10],s[2:10:2],s[::-1]

s[8:], s[:8], s[7:1],s[7:1:-1]

name1, age1 = 'bibi', '21',
name2, age2 = 'cici', '22'

info1 = "name: "+name1+"\nage: "+str(age1)
print(info1)

info_layout = "name: {} \nage:{}"
info2 = info_layout.format(name2,age2)
print("name:{}\nage:{}".format(name1,age1))
print(info1)
print(info2)

print("name: {name}\nage: {age}".format(name=name1,
                                        age=age1))
#{}안에는 숫자를 이용해도 된다

s3 = "sdfafadfafadfsa"
s3.replace('fadf','조')

len(s3)
s3.count('a')
s3.count('b')

s3.index('a') #없는 문자열을 찾으면 에러가 난다
s3.find('t')#없는 문자열을 찾으면 -1 반환

s = input("num: ")

s

int(True) # 1
int(False) # 0


