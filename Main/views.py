# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models.aggregates import Count
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
        'tags_active': True,
        'tags': Tag.objects.all(),
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
        'breadcrumbs': (
            ('show_list_tag', 'Тематики',),
        ),
        'tags_active': True,
        'tag': tag,
        'quotes': Quote.objects.filter(QuoteTag__tag=tag),
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
        'breadcrumbs': (
            ('show_list_quote', 'Цитаты',),
        ),
        'quotes_active': True,
        'quote': quote,
    }
    return render(request=request, template_name='quote/show.html', context=context)


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
            author, created = Author.objects.get_or_create(name=request.POST.get('name', ''))
            author.count_quote += 1
            author.save()
            quote = Quote(author=author, quote=request.POST.get('quote', ''),)
            quote.save()
            for received_tag in list(map(lambda x: x.strip().title(), request.POST.get('tag', '').split(','))):
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
        'form_author': form_author,
        'form_quote': form_quote,
        'list_author': list(Author.objects.all().values_list('name', flat=True)),
        'list_tag': list(Tag.objects.all().values_list('title', flat=True)),
    }
    return render(request=request, template_name='quote/create.html', context=context, )


######################################################################################################################
