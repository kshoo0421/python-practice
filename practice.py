# # 자료형
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))


# # 문자형
# print('풍선')
# print('나비')
# print("ㅋㅋㅋㅋㅋㅋㅋ")
# print('ㅋ'*9)


# # 참 / 거짓
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not(5>10))


# # 변수
# # 애완동물을 소개해주세요~
# animal = "고양이"
# name = "해피"
# age = 5
# hobby = "낮잠"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "이에요")
# #print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# # 단 , 사용 시 빈칸이 들어감
# print(name + "는 어른일까요? " + str(is_adult))


# # 주석
# # 주석은 이렇게나
# '''
# 이렇게
# 사용합니다.
# '''
# # 범위 선택 후
# # Ctrl + / 시
# # 주석 선택 및 해제
# # 대신 #만 사용

# '''
# Quiz 1) 변수를 이용하여 다음 문장을 출력하시오

# 변수명
#  : station

# 변수값
#  : "사당", "신도림", "인천공항" 순서대로 입력
 
#  출력 문장
#  : XX행 열차가 들어오고 있습니다.
# '''
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")

# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")

# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")


# # 연산자
# print(1+1)  # 2
# print(3-2)  # 1
# print(5*2)  # 10
# print(6/3)  # 2

# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(10%3) # 1
# print(5//3) # 1
# print(10//3) # 3

# print(10>3) # True
# print(4>=7) # False
# print(10<3) # False
# print(5<=5) # True

# print(3==3) # True
# print(4==2) # False
# print(3+4==7)   # False

# print(1!=3) # True
# print(not (1!=3)) # False

# print((3>0) and (3<5)) # True
# print((3>0) & (3<5))    # True

# print((3>0) or (3<5)) # True
# print((3>0) | (3<5))    # True

# print(5>4>3)    # True
# print(5>4>7)    # False


# # 간단한 수식
# print(2+3*4) # 14
# print((2+3)*4) # 20
# number = 2+3*4  # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2 # 18
# print(number)   
# number -= 2 # 16
# print(number)   
# number *= 2 # 32
# print(number)   
# number /= 2 # 16
# print(number)   
# number %= 5 # 1
# print(number)   

# # 숫자 처리 함수
# print(abs(-5)) # 5
# print(pow(4, 2))    # 제곱  4^2 = 4*4 = 16
# print(max(5, 12))   # 최대  12
# print(min(5, 12))   # 최소  5
# print(round(3.14))  # 반올림    3
# print(round(4.99))  # 반올림    5

# from math import *  # 수학 라이브러리 이용
# print(floor(4.99))  # 내림  4
# print(ceil(3.14))   # 올림  4
# print(sqrt(16))   # 제곱근 4

# from random import *
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0 ~ 9범위의 정수 임의의 값 생성
# print(int(random()*10)+1) # 1 ~ 10범위의 정수 임의의 값 생성

# print(int(random() * 45 +1)) # 1~45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 이상 46 미만의 임의의 값 생성
# print(randint(1, 45))   # 1~45 이하의 임의의 값 생성

# '''
# Quiz 2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매원 1~3일은 스터디 준비를 해야하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
# '''

# from random import *
# print("오프라인 스터디 모임 날짜는 매월", randrange(4, 28), "일로 선정되었습니다.")

# # 문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = '''
# 나는 소년이고,
# 파이썬은 쉬워요
# '''
# print(sentence3)


# # 슬라이싱
# jumin = "990123-1234567"    # 주민등록번호 예시

# print("성별 : " + jumin[7]) # 주민이라는 문자열 중에서 7번째(0부터 시작) 글자 가져오기
# print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (0~1)
# print("월 : " + jumin[2:4]) # 2부터 4 직전까지 (2~3)
# print("일 : " + jumin[4:6]) # 4부터 6 직전까지 (4~5)

# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 (0~5)
# print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤부터 7부터 끝까지


# # 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())   # 문자열을 소문자로 출력하는 함수
# print(python.upper())   # 문자열을 대문자로 출력하는 함수
# print(python[0].isupper())    # 첫 번째 문자([0])가 대문자인지 확인하는 함수, boolean으로 출력
# print(len(python))  # 문자열의 길이를 계산해주는 함수
# print(python.replace("Python", "Java")) # 문자열 내의 특정 문자를 바꿔서 출력해주는 함수(1회성)

# index = python.index("n")   # python이라는 변수에서 n이라는 글자가 몇 번째 위치에 있는지 알려주는 함수
# print(index)    
# index = python.index("n", index+1)  # index 뒤에서 또 n을 찾는 함수
# print(index)

# print(python.find("n")) # 해당 글자를 찾아서 위치를 알려줌(0부터 시작)
# print(python.find("Java"))  # 없는 글자를 찾는 경우 결과값이 -1을 반환(오류 발생 X)
# # print(python.index("Java"))  # 없는 글자를 index할 경우 오류가 발생

# print(python.count("n"))    # python에서 n이 몇 번 등장하는지 찾아주는 함수


# # 문자열 포맷
# print("a" + "b")
# print("a", "b")
# # 위와 같은 방식으로 출력을 해왔음. 

# # 방법 1 : %의 사용
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 는 %c로 시작해요." % "A")
# # %s : 모든 자료형 사용 가능
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# # 방법 2 : 중괄호 사용과 .format() 사용
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간")) # 괄호를 통해 여러개 사용 가능
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간")) # 숫자가 없는 경우와 동일
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간")) # 순서 변경 가능. format의 순서에 따라감

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간")) # 숫자 대신 변수로 사용도 가능
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20)) # 숫자 대신 변수로 사용도 가능

# # 방법 4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")   # f 사용 필요


# # 탈출문자(\ 사용)
# # \n \" \' \\사용 가능
# print("백문이 불여일견\n백견이 불여일타")
# print("저는 '슈'입니다.")   # 따움표의 종류를 다르게 해서 표시 가능
# print('저는 "슈"입니다.')   # 마찬가지
# print("저는 \"슈\"입니다.") # c언어와 동일
# print("C:\\Users\\kshoo0421\\Desktop\\공부\\코딩\\기초 파이썬") # \\ 사용
# # \r 커서를 맨 앞으로 이동
# print("Red Apple\rPine")    # PineApple 출력. 처음으로 돌아가 대신 출력하는 방법
# # \b : 백스페이스(한 글자 삭제)
# print("Redd\bApple")
# # \t : 탭
# print("Red\tApple") # 탭 한 번 누른 것과 동일

# '''
# Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver 
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                 (nav)               (5)             (1)         (!)
# 예) 생성된 비밀번호 : nav51!
# '''
# url= 'http://naver.com'
# domain = url[7:url.index('.')] #http://는 고정이므로 7부터 시작. . 이후 제외이므로 .까지
# print("생성된 비밀번호 : {}{}{}!".format(domain[0:3], len(domain), domain.count("e")))

# # 모범답안
# my_str = url.replace("http://", "")    # 규칙1
# my_str = my_str[:my_str.index(".")] # 규칙2
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" 
# print("{0}의 비밀번호는 {1}입니다." .format(url, password))


# # 리스트[] 
# # 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인하기
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# num_list = [5, 2, 4, 3, 1]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)


# # 사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5]) # 잘못된 숫자를 넣으면 오류 발생(뒤에 실행 안됨)
# print(cabinet.get(5)) # get 사용 시 없어도 실행 가능(none 출력)
# print(cabinet.get(5, "사용가능")) # 없으면 none대신 뒤에 있는 문자열 출력

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"   # 기존 값이 있는 곳에 넣으면 해당 값을 대체
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key들만 출력
# print(cabinet.keys())

# # value들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# 튜플
# 사전과 다르게 내용 변경이나 추가가 불가능함. const 같은 느낌
