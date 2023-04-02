from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
def main(request):
    return HttpResponse('Главная страница')

def get_post(request):
    return render(request, 'blog/list_detail.html')
def get_posts(request, name_post):
    data = {
        'post':name_post
    }
    return  render(request, 'blog/detail_by_name.html', context=data)
def get_info_about_num(request, num: int):
    data = {
        'number' : num
    }
    return render(request, 'blog/detail_by_number.html', context=data)

def index_html(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)