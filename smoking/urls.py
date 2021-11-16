from django.urls import path
from . import views

app_name = 'smoking'

urlpatterns=[

    path('boroughlist/', views.boroughlist, name='borough_list'),
    path('', views.smokingmap, name='smoking_map'),
    path('location/', views.location, name='location'),
    path('cp_cd/', views.cp_cd, name='cp_cd'),

    path('graph/', views.graph, name='graph'),
    path('graph_age/', views.graph_age, name='graph_age'),
    path('graph_cigaretteprice/', views.graph_cigaretteprice, name='graph_cigaretteprice'),

    path('direction/', views.direction, name='direction'),
    path('gangnam_map/', views.gangnam_map, name='gangnam_map'),
    path('gangdong_map/', views.gangdong_map, name='gangdong_map'),
    path('gangbuk_map/', views.gangbuk_map, name='gangbuk_map'),
    path('gangseo_map/', views.gangseo_map, name='gangseo_map'),
    path('gwanak_map/', views.gwanak_map, name='gwanak_map'),
    path('gwangjin_map/', views.gwangjin_map, name='gwangjin_map'),
    path('guro_map/', views.guro_map, name='guro_map'),
    path('geumcheon_map/', views.geumcheon_map, name='geumcheon_map'),
    path('nowon_map/', views.nowon_map, name='nowon_map'),
    path('dobong_map/', views.dobong_map, name='dobong_map'),
    path('dongdaemun_map/', views.dongdaemun_map, name='dongdaemun_map'),
    path('dongjak_map/', views.dongjak_map, name='dongjak_map'),
    path('mapo_map/', views.mapo_map, name='mapo_map'),
    path('seodaemun_map/', views.seodaemun_map, name='seodaemun_map'),
    path('seocho_map/', views.seocho_map, name='seocho_map'),
    path('seongdong_map/', views.seongdong_map, name='seongdong_map'),
    path('seongbuk_map/', views.seongbuk_map, name='seongbuk_map'),
    path('songpa_map/', views.songpa_map, name='songpa_map'),
    path('yangcheon_map/', views.yangcheon_map, name='yangcheon_map'),
    path('yeongdeungpo_map/', views.yeongdeungpo_map, name='yeongdeungpo_map'),
    path('yongsan_map/', views.yongsan_map, name='yongsan_map'),
    path('eunpyeong_map/', views.eunpyeong_map, name='eunpyeong_map'),
    path('jongro_map/', views.jongro_map, name='jongro_map'),
    path('jung_map/', views.jung_map, name='jung_map'),
    path('jungrang_map/', views.jungrang_map, name='jungrang_map'),
    path('area/', views.area, name='area'),

    path('fullopen/', views.fullopen, name='fullopen'),
    path('fullclose/', views.fullclose, name='fullclose'),
    path('littleopen/', views.littleopen, name='littleopen'),
    path('etc/', views.etc, name='etc'),

    path('chart', views.ChartView.as_view(), name="chart"),

]