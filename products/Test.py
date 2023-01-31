from django.contrib.auth.models import User
from products.models import Product

default_user = User.objects.first()
Product.objects.all().update(user=default_user)