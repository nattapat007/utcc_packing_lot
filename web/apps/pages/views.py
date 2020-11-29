from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from pip._vendor import requests

from web.apps.parking.models import Park


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        parks = Park.objects.all()
        return render(request, self.template_name, {'parks': parks})


class DetectPageView(TemplateView):
    template_name = 'detect.html'

    def post_checkin(self):
        url = "http://localhost:8000/api/checkin/"
        payload = ""
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
