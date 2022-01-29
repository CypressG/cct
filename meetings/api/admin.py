from django.contrib import admin
from .models import User, Registry, Group, Meeting


# Register your models here.
admin.site.register(User)
admin.site.register(Registry)
admin.site.register(Group)
admin.site.register(Meeting)
