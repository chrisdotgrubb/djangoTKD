# Generated by Django 4.0.2 on 2022-03-09 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_profilesettings_show_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directmessage',
            name='message',
            field=models.TextField(default='was null', max_length=1000),
            preserve_default=False,
        ),
    ]
