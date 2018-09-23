from django.db import models


# Create your models here.
class UserTable(models.Model):
    phone = models.CharField(unique=True, blank=False, primary_key=True, max_length=15)
    userName = models.CharField(max_length=250)


class ParentTable(models.Model):
    userId = models.ForeignKey('self', UserTable, related_name='parentTable')
    fatherName = models.CharField(max_length=250)
    fatherPhone = models.CharField(unique=True, blank=True, max_length=15)
    motherName = models.CharField(max_length=250)
    motherPhone = models.CharField(unique=True, blank=True, max_length=15)


class SiblingsTable(models.Model):
    userId = models.ForeignKey('self', UserTable, related_name='siblingsTable')
    brother = models.CharField(max_length=250)
    brotherPhone = models.CharField(unique=True, blank=True, max_length=15)
    sister = models.CharField(max_length=250)
    sisterPhone = models.CharField(unique=True, blank=True, max_length=15)


class ChildrenTable(models.Model):
    userId = models.ForeignKey('self', UserTable, related_name='childrenTable')
    son = models.CharField(max_length=250)
    sonPhone = models.CharField(unique=True, blank=True, max_length=15)
    daughter = models.CharField(max_length=250)
    daughterPhone = models.CharField(unique=True, blank=True, max_length=15)


class WifeTable(models.Model):
    userId = models.ForeignKey('self', UserTable, related_name='wifeTable')
    wife = models.CharField(max_length=250)
    wifePhone = models.CharField(unique=True, blank=True, max_length=15)
