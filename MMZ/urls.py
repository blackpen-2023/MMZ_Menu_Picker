from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='mmz_home'),
    path('mmz_ask_1/', views.page2, name='mmz_ask_1'),  # URL 패턴 설정


    path('how_set/', views.how_set, name='how_set'),  # 버튼 클릭 시 호출될 뷰
    path('mmz_ask_1_1/', views.mmz_ask_1_1, name='mmz_ask_1_1'),

    path('mood_set/', views.mood_set, name='mood_set'),  # 버튼 클릭 시 호출될 뷰
    path('mmz_ask_1_2/', views.mmz_ask_1_2, name='mmz_ask_1_2'),

    path('who_set/', views.who_set, name='who_set'),  # 버튼 클릭 시 호출될 뷰
    path('mmz_ask_2/', views.mmz_ask_2, name='mmz_ask_2'),

    path('price_set/', views.price_set, name='price_set'),  # 버튼 클릭 시 호출될 뷰
    path('mmz_ask_3/', views.mmz_ask_3, name='mmz_ask_3'),

    path('kind_set/', views.kind_set, name='kind_set'),  # 버튼 클릭 시 호출될 뷰
    path('mmz_ask_3_1/', views.mmz_ask_3_1, name='mmz_ask_3_1'),

    path('country_set/', views.country_set, name='country_set'),  # 버튼 클릭 시 호출될 뷰
    path('mmz_ask_4/', views.mmz_ask_4, name='mmz_ask_4'),

    path('spicy_set/', views.spicy_set, name='spicy_set'),  # 버튼 클릭 시 호출될 뷰
    path('mmz_ask_5/', views.mmz_ask_5, name='mmz_ask_5'),

    path('condition_set/', views.condition_set, name='condition_set'),  # 버튼 클릭 시 호출될 뷰
    path('mmz_ask_6/', views.mmz_ask_6, name='mmz_ask_6'),

    path('weather_set/', views.weather_set, name='weather_set'),  # 버튼 클릭 시 호출될 뷰
    path('mmz_ask_7/', views.mmz_ask_7, name='mmz_ask_7'),

    path('etc_set/', views.etc_set, name='etc_set'),  # 버튼 클릭 시 호출될 뷰

    path('mmz_loading/', views.mmz_loading, name='mmz_loading'),
    path('mmz_ai/', views.mmz_ai, name='mmz_ai'),  # AJAX 요청을 처리할 URL
    path('result/', views.result, name='result'),


    path('error/', views.error, name='error'),



]