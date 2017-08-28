from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import Header, News, About
from .forms import ContactForm


def index(request):
    context = {}
    context['header_text'] = Header.objects.filter(choose=1)
    post_title = News.objects.filter().order_by('-pub_date')
    paginator = Paginator(post_title,5)

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context['post_title'] = news
    return render(request, 'index.html', context)


def about(request):
    context = {}
    context['header_text'] = Header.objects.filter(choose=2)
    context['text'] = About.objects.all()
    return render(request, 'about.html', context)



def contact(request):
    context = {}
    context['header_text'] = Header.objects.filter(choose=3)
    context['form'] = ContactForm()
    if request.method== 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks for your feedback")
        else:
            return HttpResponse("You are missing something important in the form")
    else:
        pass
    return render(request, 'contact.html', context)


def post(request, news_id):
    try:
        context = {}
        context['post_title'] = News.objects.get(pk = news_id)
    except News.DoesNotExist:
        return redirect('/')
    return render(request, 'post.html', context)
