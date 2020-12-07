from django.views.generic import FormView

from web.apps.parking.forms import DateFilterForm
from web.apps.parking.serializers import ParkExportSerializer


class ParkingExportView(FormView):
    template_name = 'detect.html'
    form_class = DateFilterForm

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        park = ParkExportSerializer(**cleaned_data)
        return park.response
