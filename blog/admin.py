from django.contrib import admin
from blog.pages.base import BasePage
from blog.pages.home import HomePage

admin.site.register(BasePage)
admin.site.register(HomePage)