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

# # 튜플
# # list와 다르게 내용 변경이나 추가가 불가능함. 대신 속도가 빠름. const 같은 느낌
# menu = ("돈까스", "치즈까스")   # ()와 "", ','로 구분
# # menu.add("생선까스") # 튜플은 추가/삭제/변경을 지원하지 않음
# print(menu[0])
# print(menu[1])

# # 활용
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
# # 위 아래 출력값은 같음.
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)


# # 집합(set)
# # 중복 안됨, 순서 없음
# my_set = {1, 2, 3, 3, 3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합(java를 할 수 있거나 python을 할 수 있는 개발자)
# print(java|python)
# print(java.union(python))

# # 차집합(java는 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java-python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)


# # 자료구조의 변경(형변환)
# # 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# '''
# Quiz 4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))
# '''
# from random import *
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(lst)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : " + str(lst[0]))
# lst.remove(lst[0])  # 뽑은 수 제외
# print("커피 당첨자 : " + str(sample(lst, 3)))
# print("-- 축하합니다 --")

# from random import *
# users = range(1, 21) # 1부터 20까지 숫자를 생성. 자료형은 range
# users = list(users) # 자료형을 range에서 list로 변환
# shuffle(users)  # 섞기
# winners = sample(users, 4)  # 4명 추출. 4명 중에서 1명은 치킨, 3명은 커피
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("치킨 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")


# # if
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지" : # elif : else if
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요없어요.")
    
# temp = int(input("기온은 어때요? ")) # input은 항상 문자열로 받기 때문에 int형으로 형변환 필요   
# if 30<=temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else :
#     print("너무 추워요. 나가지 마세요")
    
# # for
# for waiting_no in range(1, 6) :    # 1, 2, 3, 4, 5 // range(시작점, ~미만)
#     print("대기번호 : {0}".format(waiting_no))
    
# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
    
# # while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기처분되었습니다. ")
        
# customer = "아이언맨"
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
#     index += 1
#     # 무한 루프. Ctrl + c를 통해 중단
    
# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")


# # continue와 break
# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11) : # 1, 2, 3, 4, 5, 6, 7, 8, 9, 
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))
   
    
# # 한 줄 for
# # 출석번호가 1, 2, 3, 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# # 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

'''
불필요한 코드를 최소화한 파이썬이라 한 줄에 for문을 적용하는 것이 가능한 것 같다. 
단순 반복 작업에 있어서는 코드를 작성하는 시간을 꽤 단축시킬 수 있을 것 같다. 
'''


# '''
# Quiz 5) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분
# '''
# # 1차 시도
# from random import *
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if time >= 5 & time <= 15:
#         select = 'O'    
#         cnt += 1
#     else:
#         select = ' '
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(select, i, time))

# print("총 탑승 승객 : {0}분".format(cnt))
'''
모든 손님이 O표시가 되었다. if문이 통과가 자유롭게 되는 것 같았다. 
'''

# # 2차 시도
# from random import *
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if time <= 15:
#         select = 'O'    
#         cnt += 1
#     else:
#         select = ' '
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(select, i, time))

# print("총 탑승 승객 : {0}분".format(cnt))

'''
앞의 조건을 지우니 제대로 동작했다. & 연산자를 잘못 사용한 것 같다. 
+) & 대신 and를 사용해야한다고 한다.
(& 연산자의 경우 집합에서 교집합을 나타낼 때 사용할 수 있는 연산자이다.)
'''

# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51): # 1 ~ 50 이라는 수(승객)
#     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님(매칭 성공), 탑승 승객 수 증가 처리
#         print("[O] {0}번째 손님 (소요시간 {1}분)".format(i, time))
#         cnt += 1
#     else: # 매칭 실패한 경우
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(cnt))
'''
오 저렇게 한 번에 사용하는 거구나. 나와 달랐던 점은 난 string형을 통해 매칭이 된 것 안된 것 같이 이용했다는 것이다. 
그 외에 차이점은 if의 조건문 차이 정도?
'''

# # 함수 - 전달값과 반환값
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
    
# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많다면
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance
    
# def withdraw_night(balance, money):
#     commission = 100 #수수료 100원
#     return commission, balance - money - commission
   
# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))    
'''
함수는 def 를 통해 정의한다. 어차피 파이썬에서 자료형을 자동으로 인식하기 때문에 함수인지 아닌지만 표시해주면 된다.
오히려 함수에 있어서는 일관성이 있다고 볼 수도 있다.
'''

# # 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업.
# def profile(name, age = 17, main_lang = "파이썬"):  # 기본값(입력값이 없으면)으로 age 17, main_lang "파이썬"
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#           .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")
'''
\ 후 엔터를 치면 같은 줄에 작성을 하는 것으로 친다. 가독성을 위해 이런 기능을 넣은 것으로 생각된다.
기본값은 입력값이 없을 경우 기본으로 넣는 값을 의미한다. sparse matrix와 같은 구조에서 사용하면 좋을 것 같다.
'''

# # 키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
    
# profile(name="유재석", main_lang="파이썬", age = 20)
# profile(main_lang="자바", age = 25 ,name="김태호")
'''
키워드 = 값 으로 넣어주면 변수(키워드)의 순서가 달라진다고 하더라도 값을 잘 넣을 수 있다.
여러 변수 중 특정 변수에 값을 넣어야 할 때 사용할 것 같다.
'''


# # 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5) 

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "")    # 빈칸으로 처리. 매번 빈칸으로 처리하기 귀찮
# # 이럴 때 쓰는 것이 가변인자

# def profile(name, age, *language):  # * 사용
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
        
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")

'''
한 변수에 0개부터 여러 종류를 넣을 수 있을 때 사용하는 것이 가변인자라고 한다. 
c에서는 *가 포인터 역할로 쓰였지만, 여기서는 파이썬에서는 마치 집합처럼 사용되는 것 같다. 
'''


# # 지역변수와 전역변수
# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

'''
c나 c#에서는 전역변수의 경우 지역변수와 이름이 겹칠 경우 지역변수를 우선으로 사용하고, 아닐 경우 전역변수로 취급하는데
여기서는 외부에 있는 전역 변수를 global을 통해 한 번 더 사용한다고 선언한다.
나름의 장점은 있을 것으로 보이나, 파이썬에서 전역변수를 사용하기는 다소 귀찮을 것으로 생각된다.
'''


# '''
# Quiz 6) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.
# '''

# # 1차 시도
# gender = 'x'
# while(gender != 'm' and gender != 'f') : # 성별이 남자이거나 여자라면 탈출
#     gender = input("성별을 입력하세요 (m / f) : ")
# height = input("키를 입력하세요(m 단위) : ")

# if (gender == 'm'):
#     print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(float(height)*100, float(height)*float(height)*22))
# else :
#     print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(float(height)*100, float(height)*float(height)*21))
    
'''
소숫점을 잘 모르겠다. 이건 모르는 거라서 더 시도를 하기 보다는 정답을 보는 것이 나을 것 같다. 
'''


# def std_weight(height, gender): # 키 m단위(실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21
    
# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height/100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

'''
우선 함수를 만들었다. 소수점 둘째자리까지 표시하는 방법은 round()를 이용하면 된다. 
'''


# # 표준 입출력
# print("Python", "Java", sep=", ", end="?") # sep은 두 단어 사이를 ,로 이어줌. end 는 맨 뒤에 글자(기존 줄바꿈)를 바꿔줌(=줄바꿈도 안됨)
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)    # 표준 출력
# print("Python", "Java", file=sys.stderr)    # 에러 처리 가능

# # 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}  # 배열을 :를 통해 연결하고, 각 자료형이 다르므로 
# for subject, score in scores.items():   # 이 코드에서 바로 변수들로 받을 수 있는 것 같다. 
#                                         # items()를 쓴 이유는 이 변수들을 받으려는 목적 같다. 
#     print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")    # ljust : 8칸 공간확보 후 왼쪽으로 정렬, rjust : 반대

# # 은행 대기순번표
# # 001, 002, 003, ..., 
# for num in range(1, 21):
#     print("대기번호 : " + str(num.zfill(3))) # zfill(number) : number만큼의 공간을 확보하고 나머지를 0으로 채움

# answer = input("아무 값이나 입력하세요 : ") # 사용자 입력을 받을 때는 항상 문자열로 입력을 받음
# answer = 10
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")
'''
sep과 end를 잘 사용하면 print를 자유롭게 사용할 수 있을 것 같다. 
sys를 들여와서 표준 출력과 에러 처리가 가능하다. 에러 처리는 디버깅할 때 유용할 것 같다.
배열에서 :를 통해 여러 자료형을 묶어서 저장하고, .items()를 통해 한 번에 가져오는 것이 가능한 것 같다.
이를 잘 쓸지는 모르겠지만 한 번 짚고 넘어가는 것이 나을 것 같다.

공간확보 및 정렬은 c언어에서 %d 사이에 점을 찍고 숫자들을 배열해가며 정리했었는데 
이렇게 함수화(ljust, rjust)시키는 것이 오히려 더 직관적인 것 같다. 

사용자 입력을 받을 때에는 항상 문자열로 인식이 되는데, 이에 맞는 형변환이 제 때 이루어져야할 것 같다.
'''


# # 다양한 출력포맷
# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500))
# # 3자리마다 콤마를 찍어주기(thousand 단위라 기본 지원)
# print("{0:,}".format(1000000000000))
# # 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(1000000000000))
# print("{0:+,}".format(-1000000000000))
# # 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
# print("{0:^<+30,}".format(1000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수까지만 표시(소수점 3째 자리에서 반올림)
# print("{0:2f}".format(5/3))
'''
규칙은 나중에 다시 정리할 필요는 있을 것 같다. 
개념적인 문제라기보다는 사용법의 문제라 찾아보면서 하는 것이 더 도움될 것 같다. 
'''


# # 파일입출력
# score_file = open("score.txt", "w", encoding="utf8")    # "w"는 덮어쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()  # 파일을 열었으면 닫아주기

# score_file = open("score.txt", "a", encoding="utf8")    # "a"는 이어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")    # 줄바꿈도 넣어줘야함.

# score_file = open("score.txt", "r", encoding= "utf8") # "r"은 읽어오겠다. 
# print(score_file.read())    # 한 번에 읽기
# score_file.close()

# score_file = open("score.txt", "r", encoding= "utf8")  
# print(score_file.readline(), end="")    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:    # 읽어올 내용이 없으면 탈출
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  # 모든 내용을 가져와서 list 형태로 저장
# for line in lines:
#     print(line, end="")
    
# score_file.close()
'''
특정 파일을 여는 것은 다른 언어에서는 해본 적이 없는 것 같아 조금 낯설다. 
각 기능들의 개념을 이해하기는 어렵지 않으나 코드를 쓸 때 바로바로 나올지는 잘 모르겠다. 
'''



# # pickle
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()
'''
피클 : 프로그램에서 사용하고 있는 데이터를 파일로 저장해주는 것
항상 파일을 실행하면 데이터가 초기화되었는데,
데이터 저장과 불러오기의 기초적인 부분인 것 같다. 
'''


# # with
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
    
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# '''
# Quiz 7) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
# '''

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding = "utf8") as report_file:
#         report_file.write("- {0}주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")


# # 클래스
# # 마린 : 공격 유닛, 군인, 총을 쓸 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 쑤 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
#         name, location, damage))
    
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank_damage)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린")
# marine3 = Unit("마린", 40)


# # 멤버 변수
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# # 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
    
    
# # 메소드
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # 공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# # 상속 / 다중 상속
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
   
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
        
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)
        
# # 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


# # 메소드 오버라이딩
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
   
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))
        
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
        
# # 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공주 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move.fly("9시")


# # pass
# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(self, name, hp, 0)
#         # pass
        
# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
    
# def game_over():
#     pass
# game_start()
# game_over()
       
       
# # super
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")
        
# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")      
        
# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__()
        
# # 드랍쉽
# dropship = FlyableUnit()

            
# # 스타크래프트 오류 있음. 하면서 잡아낼 것
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
        
#         def move(self, location):
#             print("[지상 유닛 이동]")
#             print("{0} : {1} 방향으로 이동합니다. [ 속도 {2}]"\
#                 .format(self.name, location, self.speed))
                
#         def damaged(self, damage):
#             print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#             self.hp -= damage
#             print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#             if self.hp <= 0:
#                 print("{0} : 파괴되었습니다.".format(self.name))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
        
#     # 스팀팩 : 일정 시간동안 이동 및 공격속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다. ")
        
# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
#     seize_developed = False # 시즈모드 개발여부
    
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
        
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         # 현재 시즈모드일 때 -> 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False
            
# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")      
        
# class FlyableAttackUnit(Unit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
        
#     def move(self, location):
#         print("[공중 유닛 이동")
#         self.fly(self.name, location) 
        
# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__("레이스", 80, 20, 1, 5)
#         self.clocked = False # 클로킹 모드 (해제 상태)
        
#     def clocking(self):
#         if self.clocked == True: # 클로킹 모드 -> 모드 해제
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else: # 클로킹 모드 해제 -> 모드 설정
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True 
        
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
    
# def game_over():
#     print("Player : gg")    # good game
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")
    
# # 실제 게임 진행
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리(생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")
    
# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()
        
# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")
    
# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21))    # 공격은 랜덤으로 받음 (5 ~ 20)
    
# # 게임 종료
# game_over()


# '''
# Quiz 8) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass
    
#     # 매물 정보 표시
#     def show_detail(self):
#         pass
# '''
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
        
#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type\
#             , self.price, self.completion_year)

# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2010년")
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다".format(len(houses)))
# for house in houses:
#     house.show_detail()


# # 예외 처리
# try:
#     print("나누기 전용 계산깅입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(num[0] / nums[1]))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하엿습니다.")
#     print(err)    


# # 사용자 정의 예외처리, finally
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.") 
#     print(err)
# finally: 
#     print("계산기를 이용해주셔서 감사합니다.")


# '''
# Quiz 9) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
#         출력 메시지 : "잘못된 값을 입력하였습니다.
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."
# [코드]
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
# while(True):
#     print("[남은 치킨 : {0}]".format(chicken))
#     order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#     if order > chicken: # 남은 치킨보다 주문량이 많을 때
#         print("재료가 부족합니다.")
#     else:
#         print("[대기번호 {0}] {1}마리 주문이 완료되었습니다." \
#             .format(waiting, order))
#         waiting += 1
#         chicken -= order
# '''
# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError

#         else:
#             print("[대기번호 {0}] {1}마리 주문이 완료되었습니다." \
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order
        
#             if chicken == 0:
#                 raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break    
        
        
# 모듈
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때 가격
# theater_module.price_soldier(5) # 5명의 군인이서 영화 보러 갔을 때 가격

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning, price_soldier
# price(5)
# price_morning(6)
# price_soldier(7)

# from theater_module import price_soldier as price
# price(5)


# # 패키지
# import travel.thailand
# # import travel.thailand.ThailandPackage
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.ThailandPackage()
# trip_to.detail()

# # from random import *
# from travel import *
# from travel import thailand
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random

# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


# # pip install
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# 내장 함수
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))


# 외장 함수
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))


# '''
# Quiz 10) 프로젝트 내에 나마느이 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : nadocoding@gmail.com
# '''
# def sign():
#     print("이 프로그램은 나도코딩에 의해 만들어졌습니다.")
#     print("유튜브 : http://youtube.com")
#     print("이메일 : nadocoding@gmail.com")