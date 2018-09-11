from django.contrib import admin
from Human_Relationship.models import Topic,Webpage,AccessRecord
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)