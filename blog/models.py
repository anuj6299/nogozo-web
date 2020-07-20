from django.db import models

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.category_name

class Article(models.Model):
    article_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_text = models.TextField(blank=True, null=True)
    article_text2 = models.TextField(blank=True, null=True)
    article_text3 = models.TextField(blank=True, null=True)
    article_title = models.CharField(max_length=500, null=True)
    article_logo = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=500, null=True)
    author_profile_link = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    article_summary = models.CharField(max_length=50000, null=True)

    def __str__(self):
        return self.article_title