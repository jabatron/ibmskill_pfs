from django import forms


class DimensionForm(forms.Form):
    dimension = forms.IntegerField(label="Dimension (1 a 30)", max_value=30, min_value=1)