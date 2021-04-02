from django.shortcuts import render
from Main.models import Quote, QuoteTag
from django.db.models.aggregates import Count
from random import randint

######################################################################################################################


def index(request):
    """
    Отображение главноей страницы сайта
    :param request: WSGIResponse
    :return: HttpResponse
    """
    quote_count = Quote.objects.all().aggregate(count=Count('id'))['count']
    random_index = randint(0, quote_count - 1)
    quote = Quote.objects.all()[random_index]
    context = {
        'title': 'Главная',
        'quotes': True,
        'quote': quote,
        'tags': QuoteTag.objects.filter(quote=quote),
    }
    return render(request=request, template_name='index.html', context=context)


######################################################################################################################


def quote_list(request):
    """
    Отображение списка цитат
    :param request: WSGIResponse
    :return: HttpResponse
    """
    context = {
        'title': 'Цитаты',
        'quotes': True,
    }
    return render(request=request, template_name='quote_list.html', context=context)


######################################################################################################################


def subject_list(request):
    """
    Отображение списка тематик
    :param request: WSGIResponse
    :return: HttpResponse
    """
    context = {
        'title': 'Тематики',
        'subjects': True,
    }
    return render(request=request, template_name='subject_list.html', context=context)


######################################################################################################################


def author_list(request):
    """
    Отображение списка авторов
    :param request: WSGIResponse
    :return: HttpResponse
    """
    context = {
        'title': 'Авторы',
        'authors': True,
    }
    return render(request=request, template_name='author_list.html', context=context)


######################################################################################################################
