from crispy_forms.helper import FormHelper
from django import forms


class BaseForm(forms.Form):
    """
    This is a base form for a non-model form class with crispy form.
    For creating a form without a model.

    Note: Use any view class with get method.
    """

    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'request') or self.request is None:
            self.request = kwargs.pop('request', None)
        super(BaseForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
