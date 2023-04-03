from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

def type_sign(request):
    li_elements= ''
    for type in zodiac_element:
        li_elements += f"<li><a href='{type}'>{type.title()}</a></li>"
    return HttpResponse(f'<ol>{li_elements}</ol>')
def type(request, type_name):
    li_elements = ""
    for sign in zodiac_element[type_name]:
        redirect_path = reverse("horoscope-name", args=(sign,))
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    response = f'''
      <ol> {li_elements} </ol>
      '''
    return HttpResponse(response)
def index(request):
    zodiacs = list(signs)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context )


def get_horoscope_by_sign(request, sign_of_zodiac: str):
    default = 'Нет такого знака зодиака: {}'.format(sign_of_zodiac)
    value = signs.get(sign_of_zodiac, default)
    return HttpResponse(value)


def get_horoscope_by_num(request, sign_of_zodiac: int):
    zodiacs = list(signs)
    if sign_of_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер {sign_of_zodiac}")
    name_zodiac = zodiacs[sign_of_zodiac]
    redirect_url = reverse("horoscope-name", args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)
# Create your views here.
