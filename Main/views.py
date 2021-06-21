# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models.aggregates import Count
from django.utils.html import strip_tags as st
from random import randint
from Main.models import Quote, Tag, Author, QuoteTag
from Main.forms import FormAuthor, FormQuote


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
        'keywords': 'цитатник, цитаты',
        'description': 'Цитатник различных цитат. Случайная цитата',
        'quote': quote,
    }
    return render(request=request, template_name='index.html', context=context)


######################################################################################################################


def show_list_quote(request):
    """
    Отображение списка цитат
    :param request: WSGIResponse
    :return: HttpResponse
    """
    context = {
        'title': 'Цитаты',
        'keywords': 'цитатник, цитаты',
        'description': 'Цитатник различных цитат. Список цитат',
        'quotes_active': True,
        'quotes': Quote.objects.all(),
    }
    return render(request=request, template_name='quote/list.html', context=context)


######################################################################################################################


def show_list_tag(request):
    """
    Отображение списка тематик
    :param request: WSGIResponse
    :return: HttpResponse
    """
    context = {
        'title': 'Тематики',
        'keywords': 'цитатник, цитаты',
        'description': 'Цитатник различных цитат. Список тематик цитат',
        'tags_active': True,
        'list_tag': Tag.objects.all(),
    }
    return render(request=request, template_name='tag/list.html', context=context)


######################################################################################################################


def show_list_author(request):
    """
    Отображение списка авторов
    :param request: WSGIResponse
    :return: HttpResponse
    """
    context = {
        'title': 'Авторы',
        'keywords': 'цитатник, цитаты',
        'description': 'Цитатник различных цитат. Список авторов цитат',
        'authors_active': True,
        'list_author': Author.objects.all(),
    }
    return render(request=request, template_name='author/list.html', context=context)


######################################################################################################################


def show_tag(request, tag_id: int):
    """
    Отображение списка цитат в выбранной тематике
    :param request: WSGIResponse
    :param tag_id: int
    :return: HttpResponse
    """
    tag = get_object_or_404(Tag, id=tag_id)
    context = {
        'title': tag.title,
        'keywords': 'цитатник, цитаты, {0}'.format(tag),
        'description': 'Цитатник различных цитат. Список цитат тематики {0}'.format(tag),
        'breadcrumbs': (
            ('show_list_tag', 'Тематики',),
        ),
        'tags_active': True,
        'tag': tag,
        'list_quote': Quote.objects.filter(QuoteTag__tag=tag),
    }
    return render(request=request, template_name='tag/show.html', context=context)


######################################################################################################################


def show_author(request, author_id: int):
    """
    Отображение списка цитат выбранного автора
    :param request: WSGIResponse
    :param author_id: int
    :return: HttpResponse
    """
    author = get_object_or_404(Author, id=author_id)
    context = {
        'title': author.name,
        'keywords': 'цитатник, цитаты, {0}'.format(author),
        'description': 'Цитатник различных цитат. Список цитат автора {0}'.format(author),
        'breadcrumbs': (
            ('show_list_author', 'Авторы',),
        ),
        'authors_active': True,
        'author': author,
        'list_quote': Quote.objects.filter(author=author),
    }
    return render(request=request, template_name='author/show.html', context=context)


######################################################################################################################


def show_quote(request, quote_id: int):
    """
    Отображение выбранной цитаты
    :param request:
    :param quote_id:
    :return:
    """
    quote = get_object_or_404(Quote, id=quote_id)
    context = {
        'title': quote,
        'keywords': 'цитатник, цитаты, {0}'.format(quote.author),
        'description': 'Цитатник различных цитат. Цитата автора {0}'.format(quote.author),
        'breadcrumbs': (
            ('show_list_quote', 'Цитаты',),
        ),
        'quotes_active': True,
        'quote': quote,
    }
    return render(request=request, template_name='quote/show.html', context=context)


######################################################################################################################


def search_quote(request):
    """
    Поиск по введеному запросу цитат, поиск среди автора, текста и тематики цитаты
    :param request:
    :return:
    """
    search_query = ''
    list_search_quote = []
    if request.POST:
        search_query = request.POST.get('search', '')
        if search_query:
            list_search_id_quote = list(
                set(
                    list(Quote.objects.filter(author__name__icontains=search_query).values_list('id', flat=True)) +
                    list(Quote.objects.filter(quote__icontains=search_query).values_list('id', flat=True)) +
                    list(QuoteTag.objects.filter(tag__title__icontains=search_query).values_list('quote', flat=True))
                )
            )
            list_search_quote = Quote.objects.filter(id__in=list_search_id_quote)
            count_search_quote = len(list_search_quote)
            if count_search_quote > 0:
                message_text = 'При поиске "{0}" найдено цитат - {1}.'.format(search_query, count_search_quote, )
            else:
                message_text = 'При поиске "{0}" не найдено ни одного совпадения'.format(search_query, )
        else:
            message_text = 'Для поиска цитат введите запрос и нажмите кнопку "Искать".'
    else:
        message_text = 'Для поиска цитат введите запрос и нажмите кнопку "Искать".'
    messages.info(request, message_text)
    context = {
        'title': 'Результаты поиска',
        'keywords': 'цитатник, цитаты, поиск цитат',
        'description': 'Цитатник различных цитат, поиск и просмотр цитат различных авторов и тематик. '
                       'Результаты поиска',
        'quotes_active': False,
        'quotes': list_search_quote,
        'search': search_query,
    }
    return render(request=request, template_name='quote/list.html', context=context)


######################################################################################################################


def create_quote(request):
    """
    Страница добавления цитаты
    :param request:
    :return:
    """
    if request.POST:
        form_author = FormAuthor(request.POST)
        form_quote = FormQuote(request.POST)
        if form_author.is_valid() and form_quote.is_valid():

            author, created = Author.objects.get_or_create(name=st(request.POST.get('name', '')))
            author.count_quote += 1
            author.save()
            quote = Quote(author=author, quote=st(request.POST.get('quote', '')), )
            quote.save()
            for received_tag in list(map(lambda x: x.strip().title(), st(request.POST.get('tag', '')).split(','))):
                if received_tag:
                    tag, created = Tag.objects.get_or_create(title=received_tag)
                    tag.count_quote += 1
                    tag.save()
                    quote_tag = QuoteTag(quote=quote, tag=tag, )
                    quote_tag.save()
            messages.success(request, 'Успешно добавлена новая цитата.')
            return redirect(reverse('show_quote', args=(quote.id,)))
        else:
            messages.error(request, 'Не правильно введенные данные')
    else:
        form_author = FormAuthor()
        form_quote = FormQuote()
    context = {
        'title': 'Добавление цитаты',
        'keywords': 'цитатник, цитаты, добавить цитату',
        'description': 'Цитатник различных цитат, поиск и просмотр цитат различных авторов и тематик',
        'form_author': form_author,
        'form_quote': form_quote,
        'list_author': list(Author.objects.all().values_list('name', flat=True)),
        'list_tag': list(Tag.objects.all().values_list('title', flat=True)),
    }
    return render(request=request, template_name='quote/create.html', context=context, )


######################################################################################################################


def handler403(request, *args):
    context = {
        'title': 'Ошибка 403',
        'keywords': 'цитатник, цитаты',
        'description': 'Цитатник различных цитат, поиск и просмотр цитат различных авторов и тематик',
    }
    return render(request=request, template_name='403.html', context=context, )


######################################################################################################################


def handler404(request, *args):
    context = {
        'title': 'Ошибка 404',
        'keywords': 'цитатник, цитаты',
        'description': 'Цитатник различных цитат, поиск и просмотр цитат различных авторов и тематик',
    }
    return render(request=request, template_name='404.html', context=context, )


######################################################################################################################
