# Generated by Django 2.2.15 on 2020-10-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_storyimage_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystory',
            name='finished',
            field=models.IntegerField(default=0),
        ),
    ]
