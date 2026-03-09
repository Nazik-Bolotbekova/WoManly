

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from apps.content.models import *
from .forms import ReviewForm
from apps.users.utils import is_admin,is_editor
from apps.users.mixins import RoleContextMixin



# Category

# class CategoryView(View):
#     def get(self,request):
#         categories = Category.objects.all()
#         return render(request,'какой нибудь html',{'categories':categories})
    
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'         # я думаю это нам не нужно, просто с админки сразу в шаблон
    context_object_name = 'category'

# Article

class MyArticlesView(LoginRequiredMixin,UserPassesTestMixin,RoleContextMixin,ListView):         # чтобы автор мог видеть свои статьи   
    model = Article
    template_name = 'articles/my_articles.html'

    def test_func(self):
        return is_editor(self.request.user)
    
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,RoleContextMixin,CreateView):
    model = Article
    template_name = 'articles/create.html'
    fields = '__all__'

    def test_func(self):
        return is_editor(self.request.user) or is_admin(self.request.user)

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset
    

class ArticleDetailView(DetailView):     #надо тест либо декоратор для авторизации добавить
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'articles'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,RoleContextMixin,UpdateView):
    model = Article
    template_name = 'articles/update.html'
    fields = '__all__'

    def test_func(self):
        return is_editor(self.request.user) or is_admin(self.request.user)

#Opportunity

class OpportunityListView(ListView):
    model = Opportunity
    template_name = 'opportunities/list.html'
    context_object_name = 'opportunities'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset
    
class OpportunityDetailView(DetailView):
    model = Opportunity
    template_name = 'opportunities/detail.html'
    context_object_name = 'opportunities'




# Achievment

class AchievmentListView(ListView):
    model = Achievements
    template_name = 'achievments/list.html'
    context_object_name = 'achievments'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

class AchievmentDetailView(DetailView):
    model = Achievements
    template_name = 'achievments/detail.html'
    context_object_name = 'achievments'


# SupportRequest

class SupportRequestListView(ListView):
    model = SupportRequest
    template_name = ''
    context_object_name ='support'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

class SupportRequestDetailView(DetailView):
    model = SupportRequest
    template_name = ''
    context_object_name = 'support'

class SupportRequestCreateView(CreateView):
    model = SupportRequest
    template_name = ''
    fields = '__all__'

class SupportRequestDeleteView(DeleteView):
    model = SupportRequest
    template_name = ''
    success_url = reverse_lazy('')

class SupportRequestUpdateView(UpdateView):
    model = SupportRequest
    template_name = ''
    fields = '__all__'



# Review
@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form})