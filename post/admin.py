from django.contrib import admin

from post.models import Category, Food


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

    readonly_fields = 'created_at updated_at'.split()


admin.site.register(Category, CategoryAdmin)



class FoodAdmin(admin.ModelAdmin):
    class Meta:
        model = Food

    readonly_fields = 'created_at updated_at'.split()


admin.site.register(Food, FoodAdmin)
