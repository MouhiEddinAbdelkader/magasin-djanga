from django.urls import path
from . import views
from .views import DetailPost, CreerPost
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"
urlpatterns = [
    path('posts/', views.Posts, name='posts'),
    path('<int:pk>/', DetailPost.as_view(), name='detail_post'),
    path('ajouter/', CreerPost.as_view(), name='creer_post'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
