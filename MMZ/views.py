from django.shortcuts import render, redirect
from MMZ.MMZ_AI import *
from django.http import JsonResponse
import logging
import random

def home(request):
    return render(request, 'mmz_home.html')
def page2(request):
    return render(request, 'mmz_ask_1.html')

def how_set(request):
    how_value = request.GET.get('how_value')
    if how_value:
        request.session['how'] = how_value
        if how_value == '1':
            request.session['how'] = '1'
            return redirect('mmz_ask_1_2')
        else:
            return redirect('mmz_ask_1_1')

def who_set(request):
    who_value = request.GET.get('who_value')
    if who_value:
        request.session['who'] = who_value
    return redirect('mmz_ask_1_2')

def mood_set(request):
    mood_value = request.GET.get('mood_value')
    if mood_value:
        request.session['mood'] = mood_value
    return redirect('mmz_ask_2')

def price_set(request):
    price_value = request.GET.get('price_value')
    if price_value:
        request.session['price'] = price_value
    return redirect('mmz_ask_3')

def kind_set(request):
    kind_value = request.GET.get('kind_value')
    if kind_value:
        request.session['kind'] = kind_value
    return redirect('mmz_ask_3_1')

def country_set(request):
    country_value = request.GET.get('country_value')
    if country_value:
        request.session['country'] = country_value
    return redirect('mmz_ask_4')

def spicy_set(request):
    spicy_value = request.GET.get('spicy_value')
    if spicy_value:
        request.session['spicy'] = spicy_value
    return redirect('mmz_ask_5')

def condition_set(request):
    condition_value = request.GET.get('condition_value')
    if condition_value:
        request.session['condition'] = condition_value
    return redirect('mmz_ask_6')

def weather_set(request):
    weather_value = request.GET.get('weather_value')
    if weather_value:
        request.session['weather'] = weather_value
    return redirect('mmz_ask_7')

def etc_set(request):
    etc_value = request.GET.get('etc_value')
    if etc_value:
        request.session['etc'] = etc_value
    return redirect('mmz_loading')

def mmz_loading(request):
    return render(request, 'mmz_loading.html')

# views.py
from django.http import JsonResponse

def mmz_ai(request):
    # 세션에서 데이터 가져오기
    how = request.session.get('how', 0)
    if how == '1':
        who = '혼자서'
    else:
        who = request.session.get('who', 0)

    mood = request.session.get('mood', 0)
    price = request.session.get('price', '없음')
    kind = request.session.get('kind', 0)
    country = request.session.get('country', 0)
    spicy = request.session.get('spicy', 0)
    condition = request.session.get('condition', 0)
    weather = request.session.get('weather', 0)
    etc = request.session.get('etc', 0)

    # 메뉴 리스트 생성
    menu_list = send_data(make_senddata(how, who, price, mood, kind, country, spicy, condition, weather, etc))

    menu_rec = menu_list[random.randint(0, 4)]

    # 메뉴 리스트가 문자열인 경우 따옴표 제거 및 리스트로 변환
    if isinstance(menu_list, str):
        menu_list = menu_list.replace("'", "").replace('"', '').split(' ')

    # 리스트에 메뉴가 5개 미만일 경우를 대비해 기본값을 설정

    menu_1 = menu_list[0] if len(menu_list) > 0 else '오류'
    if menu_1.find("'"):
        menu_1 = menu_1.replace("'", "")
    menu_2 = menu_list[1] if len(menu_list) > 1 else '오류'
    menu_3 = menu_list[2] if len(menu_list) > 2 else '오류'
    menu_4 = menu_list[3] if len(menu_list) > 3 else '오류'
    menu_5 = menu_list[4] if len(menu_list) > 4 else '오류'
    if menu_5.find("'"):
        menu_5 = menu_5.replace("'", "")

    # 각 메뉴를 세션에 저장
    request.session['menu_rec'] = menu_rec
    request.session['menu_1'] = menu_1
    request.session['menu_2'] = menu_2
    request.session['menu_3'] = menu_3
    request.session['menu_4'] = menu_4
    request.session['menu_5'] = menu_5

    # JSON 응답 반환 (리디렉션할 URL 포함)
    return JsonResponse({'message': '메뉴 리스트 생성 완료', 'redirect_url': '/result/'})

def result(request):
    # 세션에서 각 메뉴 변수 가져오기
    menu_rec = request.session.get('menu_rec', '메뉴 없음')
    menu_1 = request.session.get('menu_1', '메뉴 없음')
    menu_2 = request.session.get('menu_2', '메뉴 없음')
    menu_3 = request.session.get('menu_3', '메뉴 없음')
    menu_4 = request.session.get('menu_4', '메뉴 없음')
    menu_5 = request.session.get('menu_5', '메뉴 없음')

    return render(request, 'mmz_result.html', {
        'menu_rec':menu_rec,
        'menu_1': menu_1,
        'menu_2': menu_2,
        'menu_3': menu_3,
        'menu_4': menu_4,
        'menu_5': menu_5,
    })

def mmz_ask_1_1(request):
    return render(request, 'mmz_ask_1_1.html')

def mmz_ask_1_2(request):
    return render(request, 'mmz_ask_1_2.html')

def mmz_ask_2(request):
    return render(request, 'mmz_ask_2.html')

def mmz_ask_3(request):
    return render(request, 'mmz_ask_3.html')

def mmz_ask_3_1(request):
    return render(request, 'mmz_ask_3_1.html')

def mmz_ask_4(request):
    return render(request, 'mmz_ask_4.html')

def mmz_ask_5(request):
    return render(request, 'mmz_ask_5.html')

def mmz_ask_6(request):
    return render(request, 'mmz_ask_6.html')

def mmz_ask_7(request):
    return render(request, 'mmz_ask_7.html')

def error(request):
    return render(request, 'mmz_error.html')
