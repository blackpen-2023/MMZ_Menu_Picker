from openai import OpenAI

client = OpenAI(api_key="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")

def gpt_on(ask_text):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[
                                                  {"role": "system", "content": "관련된 메뉴 5개를 추천해줘. '스테이크 파스타 떡볶이 마라탕 김밥' 처럼 꼭 한줄로 출력해. 다른말없이 메뉴를 단어와 공백으로만 대답해. 출력값을 받아다 리스트로 변환할건데 따옴표나 큰 따옴표 쓰지마."},
                                                  {"role": "user", "content": ask_text}
                                              ],
                                              max_tokens=50)
    return response.choices[0].message.content.strip()


def get_data(data):
    while True:
        try:
            print('서버로 전송됨.')
            get = gpt_on(data)
            print(get)
            if len(get.split(' ')) == 5:
                li = get.split(' ')
                break
            elif len(get.split(', ')) == 5:
                li = get.split(', ')
                break
            else:
                print('오류확인. 재실행')
                continue
        except:
            print('서버 전송오류. 연결상태 확인필요')
            break
    return li

def make_senddata(who, how, where, mood, price, kind, country, spicy, etc, etc_2):
    data = f"{who}관계, 총 {how}명이 {where}에서 {mood} {price}원 미만으로 먹을 수 있는 {kind}종류 음식 중에서 {country}으로 {spicy} 메뉴를 추천해줘. 그리고 {etc}와 {etc_2}를 고려해줘."
    if kind == '상관없음':
        data = data.replace(" 상관없음종류 ", "")
    if country == '상관없음':
        data = data.replace(" 상관없음으로 ", "")
    if etc == '없음':
        data = data.replace("그리고 없음와 ", "")
    if etc_2 == '없음':
        data = data.replace("없음를 고려해줘.", "")
    return data

def send_data(data):
    li = get_data(data)
    return li