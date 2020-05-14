from django.contrib import admin
from django.urls import path , include
from reviews import views
from Usurvey import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('Reviews/', include('reviews.urls')),
    path('Accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
