from django.shortcuts import render
from django.utils import timezone
# Create your views here.

def about(request):
    context = {
        'title': "О нас",
        'description': "Мы группа 18-1B ",
        'students': ['Митаева Кызжибек', 'Нурпаяз кызы Арууке', 'Анвардинов Билолдин', 'Анапияев Залкар'],
        'image' : 'https://th.bing.com/th/id/OIP.GaoHDSRd4FTZWa0LcF5_aAHaFW?rs=1&pid=ImgDetMain'
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'title': "Контакты",
        'numder': "0597912425 ",
        'info': "Это мои контактные данные, если что звоните, а снизу моя инста!",
        'link': "https://www.instagram.com/flovr_z?igsh=MWQ1YnVlcnJmYXZiMQ=="
   }
    return render(request, 'contact.html', context)

def news(request):
    context = {
        'title': "Новости",
        'news': ['Кыргызыстан взял бронзу в Париже по вольной борьбе','Туркия взяла серебро в Париже по стрельбе','К сожеленгию Акжол махмудов проиграл на стадии 1/4 финала, по вольной борьбе'],
    }
    return render(request, 'news.html', context)

def time(request):
    current_time = timezone.now()
    context = {
        'title': "Текущее время",
        'description': "Время захода",
        'time': current_time.strftime('%Y-%m-%d %H:%M:%S') 
    }
    return render(request, 'time.html', context)



