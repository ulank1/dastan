from django.contrib import admin


from post.models import Category, Food

# Register your models here.

from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)


class FoodAdmin(admin.StackedInline):
    model = Food
    extra = 1
    readonly_fields = 'created_at updated_at'.split()


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

    readonly_fields = 'created_at updated_at'.split()
    inlines = [FoodAdmin]


admin.site.register(Category, CategoryAdmin)
