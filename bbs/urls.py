from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('login/signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    

    path('', views.PostList.as_view()),
    # IP주소/bbs/category/slug/
    path('category/<str:slug>/', views.category_list),
]
