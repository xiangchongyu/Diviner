from django.shortcuts import render

# Create your views here.

# 定义函数去显示相应的页面
# render 它是专门负责显示一个网页的


def Index(request):
    return render(request, 'index.html', locals())

def Anime(request):
    return render(request, 'anime.html', locals())

def jz_gl(request):
    return render(request, 'parental_supervision.html', locals())

def jf_cl(request):
    return render(request, 'dispute_resolution.html', locals())
