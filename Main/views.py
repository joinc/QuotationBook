from django.shortcuts import render

######################################################################################################################


def index(request):
    """
    Отображение главноей страницы сайта
    :param request: WSGIResponse
    :return: HttpResponse
    """
    context = {
        'title': 'Главная',
        'quotes': True,
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
