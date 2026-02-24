from django.shortcuts import render

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.content.models import *


def index(request):
    return render(request=request,template_name='index.html')








# Category

class CategoryView(View):
    def get(self,request):
        categories = Category.objects.all()
        return render(request,'какой нибудь html',{'categories':categories})
    
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

# Article

class ArticleCreateView(CreateView):
    model = Article
    template_name = ''
    fields = '__all__'

class ArticleListView(ListView):
    model = Article
    template_name = ''
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset
    
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = ''
    success_url = reverse_lazy('')

class ArticleDetailView(DetailView):     #надо тест либо декоратор для авторизации добавить
    model = Article
    template_name = ''
    context_object_name = 'articles'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = ''
    fields = '__all__'

#Opportunity

class OpportunityListView(ListView):
    model = Opportunity
    template_name = ''
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
    template_name = ''
    context_object_name = 'opportunities'

class OpportunityCreateView(CreateView):
    model = Opportunity
    template_name = ''
    fields = '__all__'

class OpportunityDeleteView(DeleteView):
    model = Opportunity
    template_name = ''
    success_url = reverse_lazy('')

class OpportunityUpdateView(UpdateView):
    model = Opportunity
    template_name = ''
    fields = '__all__'


# Achievment

class AchievmentListView(ListView):
    model = Achievements
    template_name = ''
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
    template_name = ''
    context_object_name = 'achievments'

class AchievmentCreateView(CreateView):
    model = Achievements
    template_name = ''
    fields = '__all__'

class AchievmentDeleteView(DeleteView):
    model = Achievements
    template_name = ''
    success_url = reverse_lazy('')

class AchievmentUpdateView(UpdateView):
    model = Achievements
    template_name = ''
    fields = '__all__'

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

def create_review(request):
    if request.method == 'POST':
        form = Review(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'create_review.html', {'form': form})
    else:
        form = Review()
        return render(request, 'create_review.html', {'form': form})
