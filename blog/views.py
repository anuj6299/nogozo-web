from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def index(request):
    all_articles = Article.objects.all().order_by("article_id").reverse()
    variable = 'NOGOZO | Entertainment'
    seoimage = 'https://raw.githubusercontent.com/anuj6299/ecomfiles/master/nogozopreview.jpg'
    seodescription = "India's First Local Market E-Commerce Company"
    seotitle = 'NOGOZO | Entertainment'
    context = {
        'all_articles' : all_articles,
        'variable' : variable,
        'seoimage' : seoimage,
        'seodescription' : seodescription,
        'seotitle' : seotitle,
     }
    return render(request, 'blog/index.html', context)

def article(request, article_id):
    article = Article.objects.get(article_id=article_id)
    variable = article.article_title+' | NOGOZO'
    seoimage = article.article_logo
    seodescription = article.article_summary
    seotitle = article.article_title
    context = {
        'article' : article,
        'variable' : variable,
        'seoimage' : seoimage,
        'seodescription' : seodescription,
        'seotitle' : seotitle,
     }
    return render(request, 'blog/article.html', context)


