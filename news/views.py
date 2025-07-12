from django.shortcuts import render, get_object_or_404

from news.models import New, Category
# Create your views here.

def news_list(request):
    news = New.objects.all()
    categories = Category.objects.all()
    context = {
        "latest_news" : news,
        "categories" : categories
    }
    
    return render(request, 'index.html', context=context)


def news_detail(request, pk):
    news_item = get_object_or_404(New, pk=pk)
    return render(request, 'news_detail.html', {'news': news_item})
