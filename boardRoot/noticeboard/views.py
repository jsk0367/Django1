from django.shortcuts import render, get_object_or_404
from noticeboard.models import Notice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

def index(request):
    article_list = Notice.objects.all().order_by('-writeDate')
    context = {'article_list': article_list}
    return render(request, 'noticeboard/index.html',context)

def write_article(request):
    return render(request, 'noticeboard/writeArticle.html')

def add_article(request):
    notice = Notice()
    notice.title = request.POST['title']
    notice.content =request.POST['content']
    notice.writeID = 'bit'
    notice.save()

    return HttpResponseRedirect(reverse("noticeboard:index"))

def view_article(request, article_id):
    notice = get_object_or_404(Notice, pk=article_id)
    return render(request, 'noticeboard/detail.html', {'article': notice})

def update_article(request, article_id):
    notice = Notice.objects.get(id=article_id)
    if request.method == 'POST':
        notice.title = request.POST['title']
        notice.content = request.POST['content']
        notice.writeDate = timezone.datetime.now()
        notice.save()
        return HttpResponseRedirect(reverse('noticeboard:view', args=(article_id,)))
    else:
        return render(request, 'noticeboard/detail.html', {'article': notice})

def delete_article(request, article_id):
    notice = Notice.objects.get(id=article_id)
    notice.delete()
    return HttpResponseRedirect(reverse('noticeboard:index'))

# Create your views here.
