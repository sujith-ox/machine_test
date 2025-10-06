from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expense
from django.db.models import Sum

class ExpenseSummaryView(APIView):
    def get(self, request):
        summary = Expense.objects.values('category__name').annotate(total=Sum('amount'))
        data = {item['category__name']: item['total'] for item in summary}
        return Response(data)
