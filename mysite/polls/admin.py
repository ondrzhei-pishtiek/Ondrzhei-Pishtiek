from django.contrib import admin
from django.contrib import admin
from .models import Question, Choice
from .models import Product

admin.site.register(Question)
admin.site.register(Choice)

from django.contrib import admin
from .models import Product  # імпортуємо модель

admin.site.register(Product)  # реєструємо модель в адмінці

# Register your models here.
