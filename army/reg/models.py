# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Armyunit(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'armyunit'


class Freqgrant(models.Model):
    duration = models.CharField(max_length=255, blank=True, null=True)
    etype = models.CharField(max_length=255, blank=True, null=True)
    espec = models.CharField(max_length=255, blank=True, null=True)
    flower = models.CharField(max_length=255, blank=True, null=True)
    fupper = models.CharField(max_length=255, blank=True, null=True)
    aid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'freqgrant'


class Headquarters(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'headquarters'
