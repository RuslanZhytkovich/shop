from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):             # Клиент
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Product(models.Model):           # Продукт который покупает клиент
    name = models.CharField(max_length=200,null = True)
    price = models.FloatField()
    digital = models.BooleanField(default = False, null = True, blank = False)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name

    @property                   # пишем эту функцию в html при выводе фото
    def imageURL(self):         # без этой функции при отсутствии фото на какой-нибудь из записей
        try:                    # при попытке запуска сервера будет бросаться исключение
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):            # Заказ
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True, blank = True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null = True, blank=False)
    transaction_id = models.CharField(max_length=200, null = True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()   # получаем querrySet
        total = sum([item.get_total for item in orderitems])
        return total


    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total





    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):          # Единица заказа, т.е сам продукт но с количеством
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null = True)
    quantity = models.IntegerField(default=0, null = True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        return self.product.price * self.quantity


    class Meta:
        verbose_name = 'Составляющее заказа'
        verbose_name_plural = 'Составляющeе заказа'



class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank = True, null = True)
    name = models.CharField(max_length=200, null = True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'






