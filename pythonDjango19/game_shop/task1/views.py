from django.shortcuts import render
from .forms import ContactForm
from .models import *
from django.core.paginator import Paginator


def platform_func(request):
    title = 'Главная страница'
    text = 'Главная страница'

    context = {
        'title': title,
        'text': text
    }
    return render(request, 'first_task/platform.html', context)


def games_func(request):
    title = 'Игры'
    text = 'Игры'
    games = Game.objects.all()
    paginator = Paginator(games, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'title': title,
        'text': text,
        'page_object': page_object,
    }
    return render(request, 'first_task/games.html', context)


def cart_func(request):
    title = 'Корзина'
    text = 'Корзина'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'first_task/cart.html', context)


def entrance(request):
    return render(request, 'first_task/entrance.html')


def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    info = dict()
    context = {
        'error': info,
        'buyers': buyers,
    }

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            print(f'username: {username}')
            print(f'password: {password}')
            print(f'repeat_password: {repeat_password}')
            print(f'age: {age}')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'first_task/registration_page.html', context)

            for buyer in buyers:
                if username == buyer.name:
                    info['error'] = 'Пользователь уже существует'
                    return render(request, 'first_task/registration_page.html', context)
            else:
                Buyer.objects.create(name=username, balance=100, age=age)
                return render(request, 'first_task/entr_shop.html', {'username': username})

    else:
        form = ContactForm()
        return render(request, 'first_task/registration_page.html', {'form': form})


def entrance_by_django(request):
    buyers = Buyer.objects.all()
    info = dict()
    context = {
        'error': info,
        'buyers': buyers,
    }

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            print(f'username: {username}')
            print(f'password: {password}')
            print(f'repeat_password: {repeat_password}')
            print(f'age: {age}')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'first_task/entrance_page.html', context)

            for buyer in buyers:
                if username == buyer.name:
                    return render(request, 'first_task/entr_shop.html', {'username': username})
            else:
                info['error'] = 'Пользователь не найден. Зарегистрируйтесь!'
                return render(request, 'first_task/entrance_page.html', context)

    else:
        form = ContactForm()
        return render(request, 'first_task/entrance_page.html', {'form': form})


def news(request):
    news_ = News.objects.all().order_by('-date')
    paginator = Paginator(news_, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'first_task/news.html', {'page_object': page_object})
