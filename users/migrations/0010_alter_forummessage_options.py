# Generated by Django 4.0.2 on 2022-03-04 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_contactus_message_alter_course_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forummessage',
            options={'ordering': ['updated', 'created']},
        ),
    ]