from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('check_booking/' , check_booking),
    path('home/', home , name='home'),
    path('hotel-detail/<uid>/' , hotel_detail , name="hotel_detail"),
    path('register/', register_page , name='register_page'),
    path('', index_page , name='index_page'),
    path('payment/', payment_page , name='payment_page'),
    path('contact/', contact_page , name='contact_page'),
    path('about/', about_page , name='about_page'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()