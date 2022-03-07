# Generated by Django 4.0.2 on 2022-03-04 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_forummessage_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_email', models.BooleanField(default=False)),
                ('show_last', models.BooleanField(default=False)),
                ('show_phone', models.BooleanField(default=False)),
                ('show_about', models.BooleanField(default=False)),
                ('show_location', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='settings',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='users.profilesettings'),
        ),
    ]