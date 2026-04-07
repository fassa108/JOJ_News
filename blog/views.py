from django.shortcuts import get_object_or_404, render

from blog.models import Article

# Create your views here.
def accueil(request) :
    article = Article.objects.all()
    context = {
        'article' : article
    }
    return render(request,'accueil.html',context)

def detail(request, pk) :
    element = get_object_or_404(Article, pk = pk)
    article = {
        'article' : element
    }
    return render(request, 'detail.html',article)