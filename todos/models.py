from django.db import models


class Users(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)


class UserData(models.Model):
	user_id = models.IntegerField()
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=512)