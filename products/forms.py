  
from django import forms
from .models import Product, bike_type, condition, brand, deals


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        types = bike_type.objects.all()
        type_friendly = [(c.id, c.get_friendly_name()) for c in types]
        isused = condition.objects.all()
        isused_friendly = [(c.id, c.get_friendly_name()) for c in isused]
        yesno = deals.objects.all()
        yesno_friendly = [(c.id, c.get_friendly_name()) for c in yesno]
        brands = brand.objects.all()
        brands_friendly = [(c.id, c.get_friendly_name()) for c in brands]

        self.fields['bike_type'].choices = type_friendly
        self.fields['condition'].choices = isused_friendly
        self.fields['deals'].choices = yesno_friendly
        self.fields['brand'].choices = brands_friendly
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'