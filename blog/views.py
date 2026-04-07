from django.shortcuts import get_object_or_404, redirect, render

from blog.forms import CommentaireForm, InscriptionForm
from blog.models import Article, Commentaire, Categorie
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.db.models import Count

def accueil(request):
    categories = Categorie.objects.annotate(article_count=Count('article')).order_by('-article_count')[:5]
    articles = Article.objects.order_by('-date_publication')[:6]
    context = {
        'categories': categories,
        'articles': articles,
    }
    return render(request, 'accueil.html', context)

# Create your views here.
def articles(request) :
    categorie_id = request.GET.get('categorie')
    current_category = None
    
    if categorie_id:
        article_list = Article.objects.filter(categorie_id=categorie_id).order_by('-date_publication')
        current_category = get_object_or_404(Categorie, id=categorie_id)
    else:
        article_list = Article.objects.all().order_by('-date_publication')

    context = {
        'article' : article_list,
        'current_category': current_category
    }
    return render(request,'article.html',context)

def categorie(request):
    categories = Categorie.objects.all()
    context = {
        'categories' : categories
    }
    return render(request,'categorie.html',context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    commentaires = Commentaire.objects.filter(article=article)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentaireForm(request.POST)
            if form.is_valid():
                commentaire = form.save(commit=False)
                commentaire.article = article
                commentaire.auteur = request.user
                commentaire.save()
                return redirect('detail', pk=article.pk)
    else:
        form = CommentaireForm()

    return render(request, 'detail.html', {
        'article': article,
        'commentaires': commentaires,
        'form': form
    })






class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Commentaire
    fields = ['contenu']
    template_name = 'modifier_commentaire.html'

    def test_func(self):
        commentaire = self.get_object()
        return self.request.user == commentaire.auteur

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.article.pk})
    



class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Commentaire
    template_name = 'supprimer_commentaire.html'

    def test_func(self):
        commentaire = self.get_object()
        return self.request.user == commentaire.auteur

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.article.pk})
    
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                first_name=form.cleaned_data['prenom'],
                last_name=form.cleaned_data['nom'],
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['mot_de_passe']
            )
            login(request, user)
            return redirect('accueil')
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('accueil')

        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')

        user = authenticate(request, username=email, password=mot_de_passe)

        if user is not None:
            login(request, user)
            return redirect('accueil')

    return render(request, 'connexion.html')