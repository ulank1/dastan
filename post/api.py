from sqlite3 import IntegrityError

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest

from tastypie.resources import ModelResource

from post.models import Category, Food


class CategoryResources(ModelResource):
    class Meta:
        resource_name = 'category'
        queryset = Category.objects.order_by('position')
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']



class FoodResource(ModelResource):
    dish = fields.ForeignKey(CategoryResources, 'dish', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Food.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'food'
        filtering = {
            'dish': ALL_WITH_RELATIONS,
        }