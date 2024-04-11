from django.contrib import admin
from Home.models import Introduction
from Home.models import Description
from Home.models import Skill
from Home.models import Contact

# Register your models here.
admin.site.register(Introduction)
admin.site.register(Description)
admin.site.register(Skill)
admin.site.register(Contact)
