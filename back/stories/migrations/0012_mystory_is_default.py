# Generated by Django 2.2.15 on 2020-10-05 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0011_script_has_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystory',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
