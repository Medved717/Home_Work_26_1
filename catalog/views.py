from .forms import ProductForm, CategoryForm
from .models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.forms.models import inlineformset_factory


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    context_object_name = 'category'
    success_url = reverse_lazy('catalog:product_list')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    context_object_name = 'category'
    success_url = reverse_lazy('catalog:product_list')
