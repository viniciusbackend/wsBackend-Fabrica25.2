from django.urls import path
from .app.views import FrutasView, FrutaView

urlpatterns = [
    path('frutas', FrutasView.as_view()),
    path('fruta/<pk>', FrutaView.as_view())
]