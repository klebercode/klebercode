# coding: utf-8
from django.contrib import admin

from klebercode.core.models import (Enterprise, Social, Category, Banner,
                                    Content)


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'phone2', 'phone3', 'email')
    search_fields = ('name', 'description', 'address', 'number', 'complement',
                     'cep', 'district', 'city', 'state',
                     'phone1', 'phone2', 'phone3', 'email')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('area',)
    list_display = ('name', 'acronym', 'area')
    search_fields = ('name', 'acronym', 'area')
    prepopulated_fields = {'slug': ('name',)}


class BannerAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('admin_image', 'title', 'type', 'publish')
    search_fields = ('title',)


class ContentAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('category', 'admin_body')
    search_fields = ('body',)


admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Social)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Content, ContentAdmin)
