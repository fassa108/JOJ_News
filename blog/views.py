from django.shortcuts import get_object_or_404, redirect, render

from blog.forms import CommentaireForm
from blog.models import Article, Commentaire
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail


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
                titre = commentaire.article
                auteur = commentaire.auteur
                message = commentaire = commentaire.contenu
                message = f"Nouveau commentaire sur l'article {titre} | utilisateur : {auteur}"
                send_mail(titre, message, 'sambndeyefassa@gmail.com',['sambndeyefassa@gmail.com','alphonsedesirehaba17@gmail.com'])
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