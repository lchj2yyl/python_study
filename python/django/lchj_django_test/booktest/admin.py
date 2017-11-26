from django.contrib import admin
from models import *
# Register your models here.


# class HeroInfoInline(admin.TabularInline):
#     model = HeroInfo
#     extra = 3
#
#
# class BookInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'btitle', 'bpub_date']
#     list_filter = ['btitle']
#     search_fields = ['btitle']
#     list_per_page = 10
#     fieldsets = [
#         ('base',{'fields':['btitle']}),
#         ('super',{'fields':['bpub_date']})
#     ]
#     inlines = [HeroInfoInline]
#
# admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(HeroInfo)

class BookInfoInlines(admin.TabularInline):
    model = BookInfo
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInfoInlines]


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'author']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 10
    fieldsets = [
        ('base', {'fields': ['title']}),
        ('advance', {'fields': ['pub_date', 'author']})
    ]

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(AuthorInfo, AuthorAdmin)
admin.site.register(HeroInfo)

