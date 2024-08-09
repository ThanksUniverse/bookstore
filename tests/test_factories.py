import pytest
from product.models import Product, Category
from order.models import Order
from django.contrib.auth.models import User
from product.factories import ProductFactory, CategoryFactory
from order.factories import OrderFactory, UserFactory

@pytest.mark.django_db
def test_category_factory():
    category = CategoryFactory()
    assert Category.objects.count() == 1
    assert category.title
    assert category.slug
    assert category.description
    assert isinstance(category.active, bool)

@pytest.mark.django_db
def test_product_factory():
    product = ProductFactory()
    assert Product.objects.count() == 1
    assert product.title
    assert product.categories.count() == 1
    assert isinstance(product.price, int)

@pytest.mark.django_db
def test_user_factory():
    user = UserFactory()
    assert User.objects.count() == 1
    assert user.email
    assert user.username

@pytest.mark.django_db
def test_order_factory():
    order = OrderFactory()
    assert Order.objects.count() == 1
    assert order.user
    assert order.user.email
    assert order.user.username

@pytest.mark.django_db
def test_order_with_products():
    product1 = ProductFactory()
    product2 = ProductFactory()
    order = OrderFactory(product=[product1, product2])
    assert order.product.count() == 2
    assert product1 in order.product.all()
    assert product2 in order.product.all()
