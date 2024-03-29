from django.urls import path

from test_views import APITest, TemplateViewTest, test_error_notifier

urlpatterns = [
    path("test_error_notifier/", test_error_notifier, name="test_error_notifier"),
    path("template-view-test/", TemplateViewTest.as_view(), name="template_view_test"),
    path("api-test/<int:pk>/", APITest.as_view(), name="api_test"),
]
