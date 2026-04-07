from django.shortcuts import get_object_or_404, redirect, render

from blog.forms import CommentaireForm, InscriptionForm
from blog.models import Article, Commentaire
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def accueil(request) :
    article = Article.objects.all()
    context = {
        'article' : article
    }
    return render(request,'accueil.html',context)

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
                first_name=form.cleaned_data['nom'],
                last_name=form.cleaned_data['prenom'],
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

        email = request.POST['email']
        mot_de_passe = request.POST['mot_de_passe']

        user = authenticate(request, username=email, password=mot_de_passe)

        if user is not None:
            login(request, user)
            return redirect('inscription')

    return render(request, 'connexion.html')