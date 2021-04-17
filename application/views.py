from django.shortcuts import render

def main_page(request):
    data ={
        'CV':[
            {
             'name':'Ожанов Азамат',
             'pics':'image\\aza.jpg',
             'age':'Возраст 29',
             'about':'Свободно владею английским и русским языками. Изучаю программирование с целью повышения квалификации и изменения направления в работе.',
             'exp':['Специалист по ИТ, 2013 - 2014','Специалист по программному обеспечению, 2014 - 2019','Инженер по Специальному оборудованию, 2019-наст.время'
             ],
             'edu':['2007-2010 гг. - Среднее образование','2010-2013 гг. - Высшее образование'],
             'skills':['Pyhton','Delphi'],
             'contacts':[
                {
                'img':'image\contacts\instagram.png',
                'link':'https:\\www.instagram.com/azamatozhanov/'
                },
                {
                'img':'image\contacts\\facebook.png',
                'link':'https://www.facebook.com/ozhanov.azamat/'
                },
                {
                'img':'image\contacts\\email.png',
                'link':'mailto:1911aza@gmail.com'
                },
              ]
            }
        ]
    }
    return render(request,'main.html',data)

def gallery(request):
    data = {
        'gallery':[
            {
             'img':'image\gallery\\banana.jpg',
             'description':'Банан'   
            },
            {
             'img':'image\gallery\\watermelon.jpg',
             'description':'Арбуз'
            },
            {
             'img':'image\gallery\\apple.jpg',
             'description':'Яблоко'
            },
            {
             'img':'image\gallery\\lemon.jpg',
             'description':'Лимон'
            },
        ]
        
    }

    return render(request,'gallery.html',data)

def favorites(request):
    data = {
        'favorites':[
            {
            'name':'1.GOOGLE',
            'link':'https://www.google.com'
            },
            {
            'name':'2.YANDEX',
            'link':'https://www.yandex.com'
            },
            {
            'name':'3.Vkontakte',
            'link':'https://www.vk.com'
            },
            {
            'name':'4.Facebook',
            'link':'https://www.facebook.com'
            },
            {
            'name':'5.MAIL RU',
            'link':'https://www.mail.ru'
            },

        ]
    }
    return render(request, 'favorites.html',data)

def navigation(request):
    data = {
        'pic':['/image/navi.jpg'],
        'links':[
            {
                'txt':'Мое резюме',
                'link':'/'
            },
            {
                'txt':'Галлерея',
                'link':'/gallery/'
            },
            {
                'txt':'Мои любимые сайты',
                'link':'/favorites/'
            }
        ]
    }
    return render(request,'navigation.html',data)
# Create your views here.
