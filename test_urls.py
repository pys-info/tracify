from django.urls import path
from test_views import test_error_notifire

urlpatterns = [
    path('test_error_notifire/', test_error_notifire, name="test_error_notifire"),
]
