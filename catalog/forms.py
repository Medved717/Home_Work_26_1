from django import forms

from catalog.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'buying_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }
        )

        self.fields['category'].widget.attrs.update(
            {
                'class': 'form-control'
            }
        )

        self.fields['image'].widget.attrs.update(
            {
                'class': 'form-control'
            }
        )

        self.fields['buying_price'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите сумму'
            }
        )



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите наименование'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }
        )