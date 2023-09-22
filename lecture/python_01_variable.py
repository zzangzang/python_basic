# 주석(comment) : 단순 메모, 개발 실행 x

# 출력함수 (print)
# - ()안의 값을 출력
# 변수 값 확인 용도 또는 메세지 출력 용도
print("=" * 200)
print("Hello python")

# 문자열 타입(string type)
# - python; ' ', "" -> string
# - c, java: ' '(char), ""(string)

#참고: Escape Code
# -문법: \(역슬러쉬) + @
# - 문자열 내의 일부 문자의 의미를 달리하여 특정한 효과주기
# - 예) \n: 한줄 개행, \t: 탭(8칸 공백)
print("=" * 200)
print("hello \npython")
print("hello \tpython")

# 자료형(type)
# - 파이썬의 모든 자료형은 객체(object)
# - c, java언어 문자형(char): 'A', 'E' 키보드 제어!
#  1)문자열(string): "hello", "hi"
#  2)정수형(int): 3, 0, -1
#  3)실수형(float): 3.14, 8.8, -2.2
#  4)논리형(boolean): true, false

# 예) 다양한 종류의 자료형을 사용하는 이유?
# - java에서 정수형: byte, shor, int, long
# - python 정수형: int
# 만들어진지 오래된 언어는 다양한 종류의 자료형을 사용!
# 이유는? 자원(메모리)를 효율적으로 사용하기 위해서!
#  예) 자료형은 담을 수 있는 크기의 범위가 지정되어 있음
#       예를 들어서 int는(-10000~10000)까지 담을 수 있다고 가정
#       그런데 우리 회사에서 특정 값이 0~9만 사용!
#       int를 사용하게 되면 메모리 낭비, 이런 경우 크기의 범위가 더
#       작은 자료형을 사용하면 좋음(short)

# python은 동적 타이핑 언어 -> python 실행 될 때 type을 지정!
# - type() 함수: ()안의 값의 type을 확인할 때 사용
print("=" * 200)
print(type("ABC"))
print(type(123))

# 형변환(type casting)
# - type casting을 사용하면 값을 원하는 자료형으로 변환 가능
# 1) int(): 정수형으로 변환
# 2) float(): 실수형으로 변환
# 1) str(): 문자열형으로 변환


print("=" * 200)
# type casting 실습
int_a = 3
float_b = 3.14
str_c = "9.2"
# 1) 문자열 정수형("9") -> 정수형(9)
print(int(str_int_c))
# 2) 문자열 정수형 ("9")-> 실수형 (9.0)
print(float(str_int_c))
# 3) 문자열 실수형 ("9.2")-> 정수형(error)
#print(imt(str_int_c))
# 4) 문자열 실수형 ("9,2")-> 실수형(9.2)
print(float(str_float_d))
# 5) 정수형(3) -> 실수형(3.0)
print(float(int_a))
# 6) 정수형 (3)-> 문자열("3")
print(str(int_a))
# 7) 실수형(3.14) -> 정수형(3)
print(int(float_b))
# 8) 실수형(3.14) -> 문자열("3.14")
print(str(float_b))
# * float("hello"), int("hello") 형 변환 불가!

print("=" * 200)
# None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값을 갖지 않게 변수만 생성하고 싶을 때 사용
# - 기타 언어의 Null과 같은 의미로 사용!
# - 예) student_name
student_name = None # 적극 권장 X (절대 사용 금지)
student_name = "" #적극 권장 O
#이유? "Null pointer exception" error 개발자 공포의 대상!

# 기본자료형(primetive type): 변수에 값이 저장
# - int num = 4;
# 객체자료형(reference type): 변수에 값의 "주소"가 저장
# - string name = "10";
# * java: 기본, 객체 모두 사용
# * python: 객체만 사용

# c언어 변수 생성 -> int b; (변수 생성, 값X)
# python 변수 생성 -> b (변수 호출)

# 변수 (variable)
# - 변수: "하나의 값"을 저장할 수 있는 메모리 공간
print("=" * 200)
num = 4
num = 10
print(num) # 출력: 10

# -변수 생성 및 초기화
# num = 5 # 문법
# 대입연산자(=) : 우측의 값을 좌측에 저장
# 동등연산자(==): equal

# name 변수 생성
# "Jang jeong min" 값을 name 변수에 담기

# name(변수명), =(대입연산자), "Jang jeong min" (값)
name = "Jang jeong min"


# 명명규칙 (Naming Rule)
# * 변수, 함수, 클래스 등의 사용자 정의 이름을 붙일 때 사용!
# * 명확하고 알아보기 쉽게 찾기 !

#   1. 영문 대소문자, 숫자, 특수문자(_)만 사용
#   2. 숫자로 시작할 수 없음
#       abc1(o), 1abc(x)
#   3. 영어 대소문자 구별
#       abc Abc ABc abC 모두 다른 변수
#   4. 예약어 사용 불가
#       예약어: python에서 미리 선정하여 사용중인 키워드
#              Ex) print, For, while, if, elese, class, try, except, True, False, and,
#                  return, import, def, break, continue, del, ...
# Naming Method **** 중요! (시험에 나온다)
#   - 변수, 함수, 클래스 등의 사용자 정의 이름에 사용하는 기법
#   - 프로그래밍 언어별로 사용하는 Naming Method가 다름!

#   1. snake_case: 소문자만 사용, 합성어는 (_) 사용
#       ex) student_name
#   2. camelCase: 첫글자 소문자, 합성어 첫글자 대문자
#       ex) studentName
#   3. PascalCase: 첫글자 대문자, 합성어 첫글자 대문자
#       ex) StudentName

#                       변수                  함수              클래스
#Java,C               camelCase            camelcase()         PascalCase
#Python               snake_case           snake_case()        PascalCase


# 동적 출력 !
student_num = 20233177
student_name = "jang jeong min"

# 출력 예 : 조선대학교 20233076, Jang jeong min 입니다.
print("조선대학교 20233076, Jang jeong min 입니다.")    # 하드 코딩 지양!

# 1. format()함수 - Old
print("조선대학교 {}, {} 입니다.".format(student_num, student_name))

# 2. f-string - New
print(f"조선대학교 {student_num}, {student_name} 입니다.")

# 간단한 사칙 연산
#   + : 더하기
#   - : 빼기
#   / : 나누기
#  // : 나누기 ( 몫 )
#   % : 나머지
#  ** or ^ : 제곱
#
#  5/2 : 나누기        2.5
# 5//2 : 나누기(몫)     2
#  5%2 : 나누기 (나머지) 1




