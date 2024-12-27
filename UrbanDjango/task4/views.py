from django.shortcuts import render


def platform_func(request):
    title = 'Главная страница'
    text = 'Главная страница'

    context = {
        'title': title,
        'text': text
    }
    return render(request, 'fourth_task/platform.html', context)


def games_func(request):
    title = 'Игры'
    text = 'Игры'
    games = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']}

    context = {
        'title': title,
        'text': text,
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)


def cart_func(request):
    title = 'Корзина'
    text = 'Корзина'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'fourth_task/cart.html', context)


def entrance(request):
    return render(request, 'fourth_task/entrance.html')
