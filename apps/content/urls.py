from django.urls import path
from . import views

urlpatterns = [
    
    # articles
    path('articleslist/', views.ArticleListView.as_view(), name='list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('create/', views.ArticleCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.ArticleUpdateView.as_view(), name='update'),


    # opportunities
    path('opportunities_list/',views.OpportunityListView.as_view(),name='opportunities list'),
    path('opportunity_detail',views.OpportunityDetailView.as_view(),name='opportunity detail'),


    # achievments
    path('achievments_list/',views.AchievmentListView.as_view(),name='achievments list'),
    path('achievmentdetail/',views.AchievmentDetailView.as_view(),name='achievment detail'),


    # categories
    path('category_detail/',views.CategoryDetailView.as_view(),name='category detail'),


    # review
    path('review/',views.create_review,name='review')
]