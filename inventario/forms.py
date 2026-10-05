from django import forms
from .models import MovimientoInventario


class MovimientoForm(forms.ModelForm):

    class Meta:

        model = MovimientoInventario

        fields = [
            'tipo',
            'producto',
            'cantidad',
            'justificacion'
        ]

        widgets = {
            'justificacion': forms.TextInput(
                attrs={
                    'placeholder': 'Ej. Factura #4589'
                }
            )
        }