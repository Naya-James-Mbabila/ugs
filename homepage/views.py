from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill


class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        labels = []
        data = []        
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:5]
     
        context = {
            'labels'    : labels,
            'data'      : data,
            'sales'     : sales,
         
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"