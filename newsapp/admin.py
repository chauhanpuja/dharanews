from django.contrib import admin
from .models import Category,Sub_Category,Post,StudentUser,Footer
# Register your models here.

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Post)
admin.site.register(StudentUser)
admin.site.register(Footer)
