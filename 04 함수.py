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



#함수 정의
#정의된 함수는 메모리에 로딩되어야 한다
def s_hello():
    print('hello')
    print('hi')


#호출 시에는 함수명([argument])
s_hello()


#매개변수가 있는 함수
def hello(name):
    hi = f'{name}님 반가워요'
    print(hi)


hello('anan')


def hello2(name, age):
    hi = f'{age}세 {name}님 반가워요'
    return(hi)


hi1 = hello2('anan',34)
print(hi1)


def print_info3(name, age, address=None, email = None):
    print(f' 이름: {name}, 나이: {age}, 주소: {address}, 이메일: {email}')


print_info3('cc',55)


# ## 가변 인자

def sum_funtion(num_list):
    sum_v = 0
    for i in num_list:
        sum_v += i
    return sum_v



list2 = [1,3,5,7,9,11]
s = sum_funtion(list2)
print(s)


#*변수명 => tuple로 반환
def sum_f1(*num_list): 
    print(type(num_list),num_list)


r1 = sum_f1(2,3,4,4,5)


# **변수명 => dictionary로 반환
def print_info(**info):
    print(type(info),info)
    return_v=''
    for key, value in info.items():
        return_v = f'{return_v}, {key}:{value}'
    return return_v



print(print_info(이름 ='길동', 주소='서울',이메일='ㄹㅇㄴ'))


#
# # 함수는 일급시민객체
# - 함수를 변수에 할당, 함수를 (다른)함수를 호출할 때 argument로 전달, 함수가 리턴값으로 함수를 반환할 수 있다
# - 함수도 값으로 처리할 수 있다

def my_fn(name= None):
    print(str(name)+'님 안녕하세요')
    return 'dd'


i = my_fn()# 함수 호출 i에 대입되는 값 = 함수가 반환하는 값

my_fn #함수 자체(함수 객체)

j = my_fn 
j()

# +
r1 = my_fn('gildong')
r2 = my_fn()
print('='*10)

print(r1,r2)
# -

your_fn = my_fn

your_fn('sunsin')
test_fn = your_fn
test_fn()


def cal(num1, num2):
    a = num1 + num2
    b = num1 - num2
    c = num1 * num2
    print(a,b,c)


def ca(func):
    num1, num2 = 6 ,4
    result = func(num1,num2)
    print(result)


def plus(n1,n2):
    return n1 +n2


ca(plus)


# ## lambda 표현식
# - 함수를 단일구문으로 작성하는 방법
# - 다시 사용할 필요 없이 함수 호출할 때 넘겨줄 함수를 만들 때 사용된다

def plus(n1,n2):
    return n1 +n2


# lambda [매개변수] : 리턴값 처리 구문
x = lambda n1,n2 : n1 + n2
x(4,5)

v = lambda n1 : n1**2
v(9)

v(3), v(4), v(8)

ca(lambda n1, n2: n1+n2)


def m10(x):
    return x*10


list(map(m10 , l2))

l2 = [10, 20, 30]

list(map(lambda x:x*10, l2))


# ## docstring
# - 함수 구현시 함수에 대한 설명을 문자열로 정의하는 것 
# - 선언부와 구현부 사이에 여러줄 문자열(''' ''')을 이용해서 작성
# - 보통 작성하는 내용
#     - 함수 설명
#     - 매개변수에 대한 설명
#     - 리턴값에 대한 설명
#     - 발생 error에 대한 설명

def print_i(name, age):
    '''
    정보 출력과 나이 10배 출력
    [paramater]
        dfs
    [return_value]
        fdf
    [Exception]
        dfs
    '''
    print(f'이름: {name}, 나이: {age}')
    return age *10

# +
# print_i?
# -


