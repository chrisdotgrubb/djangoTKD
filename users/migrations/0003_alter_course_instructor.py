# Generated by Django 4.0.2 on 2022-02-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_myuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ManyToManyField(related_name='course', to='users.UserProfile'),
        ),
    ]
