from django.db import models
from shop.models import Product
# Create your models here.

class PromoBaner(models.Model):
    name = 'Банер'
    image = models.ImageField(upload_to='promo/%Y/%m/%d', blank=True)
    product = models.ForeignKey(Product, default=None, related_name='product_baner', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банер'

    def __str__(self):
        return self.name

class PromoSlider(models.Model):
    name = 'Слайдер'

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'

    def __str__(self):
        return self.name
    def get_slides(self):
        return PromoSlide.objects.filter(promo=self)
    def get_slides_count(self):
        return self.images.count()

class PromoSlide(models.Model):
    image = models.ImageField(upload_to='slider/%Y/%m/%d', blank=True)
    promo = models.ForeignKey(PromoSlider, default=None, related_name='images', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, default=None, related_name='product_slide', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def save(self, *args, **kwargs):
        if self.promo.get_slides_count() >= 3:
            return
        super(PromoSlide, self).save(*args, **kwargs)