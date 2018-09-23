from django.contrib import admin
from mlm.models import UserTable, ParentTable, SiblingsTable, ChildrenTable, WifeTable
# Register your models here.

admin.site.register(UserTable)
admin.site.register(ParentTable)
admin.site.register(SiblingsTable)
admin.site.register(ChildrenTable)
admin.site.register(WifeTable)