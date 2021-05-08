from django.contrib import admin
from app01.models import clsmember
# Register your models here.
for (_, model) in clsmember:
    admin.site.register(model)
# admin.site.register(models.User)
# admin.site.register(models.UserInfo)
# admin.site.register(models.UserOf)
# admin.site.register(models.Learn)
# admin.site.register(models.SectionOf)
# admin.site.register(models.Section)
# admin.site.register(models.Thinking)
# admin.site.register(models.Album)
# admin.site.register(models.Picture)
# admin.site.register(models.PictureOf)
# admin.site.register(models.File)
# admin.site.register(models.Navigation)
# admin.site.register(models.Label)
# admin.site.register(models.LabelOf)