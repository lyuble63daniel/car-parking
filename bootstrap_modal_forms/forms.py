from django import forms

from bootstrap_modal_forms.mixins import CreateUpdateAjaxMixin, PopRequestMixin


class BSModalForm(PopRequestMixin, forms.Form):
    pass


class BSModalModelForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    pass
