from django.contrib import admin
from .models import PromoSlide, PromoSlider, PromoBaner

# Register your models here.

class PromoSlideInline(admin.TabularInline):
    model = PromoSlide
    extra = 0
    min_num = 3
    max_num = 3

class PromoSlideAdmin(admin.ModelAdmin):
    list_display = ['image','product']
admin.site.register(PromoSlide, PromoSlideAdmin)

class PromoBanerAdmin(admin.ModelAdmin):
    list_display = ['name', 'image','product']
admin.site.register(PromoBaner, PromoBanerAdmin)

class PromoSliderAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [PromoSlideInline]
admin.site.register(PromoSlider, PromoSliderAdmin)
