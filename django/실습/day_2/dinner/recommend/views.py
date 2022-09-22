from django.shortcuts import render
import random
# Create your views here.
def index(request):
    menus = ['삽겹살','김치찌개','피자','치킨','초밥']

    menu = random.choice(menus)
    imgs = ['http://image.newsis.com/2020/06/17/NISI20200617_0000546793_web.jpg',
            'https://i.ytimg.com/vi/PH_-nGRatgo/maxresdefault.jpg',
            'https://cdn.dominos.co.kr/admin/upload/goods/20200311_x8StB1t3.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/2/20/Korean_fried_chicken_3_banban.jpg',
            'https://mp-seoul-image-production-s3.mangoplate.com/1869758_1610938867363653.jpg',
    ]
    for i in range(len(menus)):
        if menu == menus[i]:
            img = imgs[i]
    context = {
        'menu': menu,
        'img' : img,
    }


    return render(request, 'index.html',context)