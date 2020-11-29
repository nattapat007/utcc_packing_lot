from django.views.generic import TemplateView
from django.shortcuts import redirect, render

from web.apps.parking.models import Park


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        parks = Park.objects.all()
        return render(request, self.template_name, {'parks': parks})


class DetectPageView(TemplateView):
    template_name = 'detect.html'


class CheckinPageView(TemplateView):
    template_name = 'checkin.html'


class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'
