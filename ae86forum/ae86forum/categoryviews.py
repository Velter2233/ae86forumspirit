from django.shortcuts import render
from spirit.category.models import Category
from spirit.topic.models import Topic

def home_with_category(request):
    # Пример — выбрать только одну категорию
    category = Category.objects.get(pk=3)
    topics = Topic.objects.filter(category=category)

    return render(request, 'custom_home.html', {
        'category': category,
        'topics': topics
    })