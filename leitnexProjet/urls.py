
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='leitnex/home.html'), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts_web')),
    path('cards/', include('cards.urls', namespace='accounts_web')),

]
