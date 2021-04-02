# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models.aggregates import Count
from random import randint
from Main.models import Quote, Tag, Author
from Main.forms import FormCreateQuote

######################################################################################################################


def index(request):
    """
    Отображение главноей страницы сайта со случайной цитатой
    :param request: WSGIResponse
    :return: HttpResponse
    """
    quote_count = Quote.objects.all().aggregate(count=Count('id'))['count']
    random_index = randint(0, quote_count - 1)
    quote = Quote.objects.all()[random_index]
    context = {
        'title': 'Главная',
        'quote': quote,
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
        'quotes_active': True,
        'quotes': Quote.objects.all(),
    }
    return render(request=request, template_name='quote_list.html', context=context)


######################################################################################################################


def tag_list(request):
    """
    Отображение списка тематик
    :param request: WSGIResponse
    :return: HttpResponse
    """
    context = {
        'title': 'Тематики',
        'tags_active': True,
        'tags': Tag.objects.all(),
    }
    return render(request=request, template_name='tag_list.html', context=context)


######################################################################################################################


def author_list(request):
    """
    Отображение списка авторов
    :param request: WSGIResponse
    :return: HttpResponse
    """
    context = {
        'title': 'Авторы',
        'authors_active': True,
        'authors': Author.objects.all(),
    }
    return render(request=request, template_name='author_list.html', context=context)


######################################################################################################################


def tag_show(request, tag_id: int):
    """
    Отображает цитаты в выбранной тематике
    :param request: WSGIResponse
    :param tag_id: int
    :return: HttpResponse
    """
    tag = get_object_or_404(Tag, id=tag_id)
    context = {
        'title': tag.title,
        'breadcrumbs': (
            ('tag_list', 'Тематики',),
        ),
        'tags_active': True,
        'tag': tag,
        'quotes': Quote.objects.filter(QuoteTag__tag=tag),
    }
    return render(request=request, template_name='tag_show.html', context=context)


######################################################################################################################


def author_show(request, author_id: int):
    """
    Отображает цитаты выбранного автора
    :param request: WSGIResponse
    :param author_id: int
    :return: HttpResponse
    """
    author = get_object_or_404(Author, id=author_id)
    context = {
        'title': author.name,
        'breadcrumbs': (
            ('author_list', 'Авторы',),
        ),
        'authors_active': True,
        'author': author,
        'quotes': Quote.objects.filter(author=author),
    }
    return render(request=request, template_name='author_show.html', context=context)


######################################################################################################################


def quote_create(request):
    if request.GET:
        author = request.GET.get('author', '')
        authors = list(Author.objects.values('id', 'name').filter(name__icontains=author.title()))
        return JsonResponse({'authors': authors, })

    context = {
        'title': 'Добавление цитаты',
        'form_create_quote': FormCreateQuote()
    }

    return render(request=request, template_name='quote_create.html', context=context, )


######################################################################################################################
