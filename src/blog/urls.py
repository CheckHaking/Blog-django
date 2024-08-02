from django.contrib import admin
from django.urls import path, include
#Las siguientes importaciones son para terminar de configurar el uso de staticos para el blog
from django.conf import settings
from django.conf.urls.static import static
#Importamos nuestras vistas de posts 
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #Esta linea biene de django allauth
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<slug>/', PostDetailView.as_view(), name='detail'),
    path('<slug>/update', PostUpdateView.as_view(), name='update'),
    path('<slug>/delete', PostDeleteView.as_view(), name='delete'),
    #fUNCION QUE LE PASAMOS PARA DAR LIKE
    path('like/<slug>/', like, name='like'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    