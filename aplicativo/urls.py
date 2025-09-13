from django.urls import path
from .app.views import FrutaView

urlpatterns = [
    path('', FrutaView.as_view())
]