from django.shortcuts import render, HttpResponse
from django.utils.translation import gettext as _
from django.views import generic
from . import models, forms

class HomePageView(generic.TemplateView):
    template_name = 'product_app/home.html'


class ProductListView(generic.ListView):
    template_name = 'product_app/product_list.html'
    paginate_by = 2
    model = models.Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.PRODUCT_CATEGORY
        return context
    

class ProductDetailView(generic.DetailView):
    template_name = 'product_app/product_detail.html'
    model = models.Product


class ProductCreateView(generic.CreateView):
    template_name = 'product_app/product_form.html'
    form_class = forms.ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = "create"
        return context


class ProductUpdateView(generic.UpdateView):
    template_name = 'product_app/product_form.html'
    model = models.Product
    form_class = forms.ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = "update"
        return context


def searchProduct(request, cat):
    template = 'product_app/product_list.html'
    products = models.Product.objects.filter(category=cat)


    print(products)

    context = {
        'object_list': products,
        'categories' : models.PRODUCT_CATEGORY,
        'searched': 1
    }
    return render(request, template, context)
