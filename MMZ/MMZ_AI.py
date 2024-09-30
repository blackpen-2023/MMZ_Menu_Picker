from openai import OpenAI
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('MMZ')

client = OpenAI(api_key="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")

def gpt_on(ask_text):
    # 새로운 API 호출 방식
    response = client.chat.completions.create(model="gpt-3.5-turbo",  # 사용할 모델
    messages=[
        {"role": "system", "content": "관련된 메뉴 5개를 추천해줘. '스테이크 파스타 떡볶이 마라탕 김밥' 처럼 꼭 한줄로 출력해. 다른말없이 메뉴를 단어와 공백으로만 대답해. 출력값을 받아다 리스트로 변환할건데 따옴표나 큰 따옴표 쓰지마. 마지막으로 '김치 볶음밥' 처럼 띄어쓰기가 있는 단어는 '김치볶음밥' 처럼 띄어쓰기를 제거해줘."},
        {"role": "user", "content": ask_text + "주재료를 꼭 고려해"}
    ],
    max_tokens=50)
    return response.choices[0].message.content.strip()


def get_data(data):
    while True:
        try:
            logger.info("서버로 전송됨.")
            get = gpt_on(data)
            get = re.sub(r'[^가-힣\s]', '', get)
            logger.info(get)
            if len(get.split(' ')) == 5:
                li = get.split(' ')
                break
            elif len(get.split(', ')) == 5:
                li = get.split(', ')
                break
            else:
                logging.error("데이터 편집오류. 재실행")
                continue
        except Exception as e:
            logging.critical(f"오류 발생 : {e}")
            break
    return li

def make_senddata(how, who, price, mood, kind, country, spicy, condition, weather, etc):
    data = f"{how}명 {who} 먹기좋고, {price}원 이하로 {mood}분위기에 {kind}이며 {country}이고 {spicy}인 먹기좋은 메뉴를 추천해줘. {condition}기분이고 날씨는 {weather}이야. 꼭 고려해서 {etc}메뉴를 추천해줘."
    if price == '상관없음':
        data = data.replace("상관없음원 이하로", "")
    if kind == '상관없음':
        data = data.replace("상관없음이며", "")
    if country == '상관없음':
        data = data.replace("상관없음이고", "")
    if spicy == '상관없음':
        data = data.replace("상관없음인", "")
    if condition == '상관없음':
        data = data.replace("상관없음기분이고", "")
    if weather == '상관없음':
        data = data.replace("날씨는 상관없음이야.", "")
    if etc == '상관없음':
        data = data.replace("상관없음", "")
    data = data.replace("'", "")
    data = data.replace('"', "")
    logger.info(data)
    return data

def send_data(data):
    data = get_data(data)
    return data