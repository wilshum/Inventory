from django.shortcuts import render
from .models import Product, Category, Tag


def product_list(request):
    ## Product listing view with search and filtering functionality

    # Base queryset for performance
    products = Product.objects.select_related("category").prefetch_related("tags").all()

    # Filtering based on description
    desc = request.GET.get("q", "").strip()
    if desc:
        products = products.filter(description__icontains=desc)

    # Filtering based on category
    category_id = request.GET.get("category", "")
    if category_id:
        products = products.filter(category_id=category_id)

    # Filtering based on tags
    tag_ids = request.GET.getlist("tags")
    if tag_ids:
        for tag_id in tag_ids:
            products = products.filter(tags__id=tag_id)
        products = products.distinct()

    context = {
        "products": products,
        "description": desc,
        "categories": Category.objects.all(),
        "selected_category": category_id,
        "tags": Tag.objects.all(),
        "selected_tags": tag_ids,
    }

    return render(request, "catalog/product_list.html", context)
