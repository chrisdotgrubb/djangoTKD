# Generated by Django 4.0.2 on 2022-02-09 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('users', '0001_initial'),
	]
	
	operations = [
		migrations.AlterField(
			model_name='myuser',
			name='is_active',
			field=models.BooleanField(default=True),
		),
	]
