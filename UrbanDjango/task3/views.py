from django.shortcuts import render


# Create your views here.
def platform_func(request):
    title = 'Главная страница'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/platform.html', context)


def games_func(request):
    title = 'Игры'
    text = 'Игры'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/games.html', context)


def cart_func(request):
    title = 'Корзина'
    text = 'Корзина'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/cart.html', context)


def entrance(request):
    return render(request, 'third_task/entrance.html')
