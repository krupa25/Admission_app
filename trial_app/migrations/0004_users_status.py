# Generated by Django 3.0.3 on 2020-02-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial_app', '0003_remove_users_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='status',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]