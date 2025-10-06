from django.urls import path
from .views import ExpenseSummaryView

urlpatterns = [
    path('expenses/summary/', ExpenseSummaryView.as_view()),
]
