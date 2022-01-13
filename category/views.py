from django.shortcuts import render

from category.models import Category

# Create your views here.
def index(request):

    return render(request, 'category/categories.html')

def category(request, category_id):
    category=Category.objects.all()

    context={
        'category': category
    }

    return render(request, 'category/category.html', context)    