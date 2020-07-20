from django.contrib import admin
from .models import City, Area, Shop, Item, Feedback, MerchantFeedback

admin.site.register(Feedback)
admin.site.register(MerchantFeedback)
