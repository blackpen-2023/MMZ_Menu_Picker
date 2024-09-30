from MMZ_AI import *

#몇명이서
how = 0
#누구와
who = ''
#어디서
where = ''
#분위기
mood = ''
#가격
price = 0
#음식종류
kind = '상관없음'
#한중일양식
country = '상관없음'
#맵기
spicy = ''
#기타
etc = '없음'
#특이사항
etc_2 = '없음'

test_data = "가족관계, 총 5명이 집에서 무난하게 50000원 미만으로 먹을 수 있는 밥종류 음식 중에서 한식으로 순한맛 메뉴를 추천해줘."

#li = send_data(test_data)
li = send_data(make_senddata(how, who, where, mood, price, kind, country, spicy, etc, etc_2))
print(li)
