from django.shortcuts import render, redirect, reverse, get_object_or_404
from Main.models import Quote, Tag, Author
from django.db.models.aggregates import Count, Max
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


def tag_show(request, tag_id):
    """
    Отображает выбранную тематику и цитаты в этой тематике
    :param request:
    :param tag_id:
    :return:
    """
    tag = get_object_or_404(Tag, id=tag_id)
    context = {
        'title': tag.title,
        'tags_active': True,
        'tag': tag,
        'quotes': Quote.objects.filter(QuoteTag__tag=tag),
    }
    return render(request=request, template_name='tag_show.html', context=context)


######################################################################################################################

def author_show(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {
        'title': author.name,
        'authors_active': True,
        'author': author,
        'quotes': Quote.objects.filter(author=author),
    }
    return render(request=request, template_name='author_show.html', context=context)
