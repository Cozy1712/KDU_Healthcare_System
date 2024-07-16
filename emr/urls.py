
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.http import HttpResponse


# def home(request):
#     return HttpResponse('HomePage')

# def room(request):
#     return HttpResponse('Chat Romm')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)