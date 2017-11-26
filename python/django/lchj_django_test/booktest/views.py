from django.shortcuts import render
from django.http import *
from .models import *
from django.template import RequestContext,loader


def index(request):
    print request
    author_list = AuthorInfo.objects.all()
    context = {'list': author_list}
    return render(request, 'booktest/index.html', context)


def show(request,id):
    author = AuthorInfo.objects.get(pk = id)
    book_list = author.bookinfo_set.all()
    context = {'list': book_list}
    return render(request, 'booktest/show.html', context)

