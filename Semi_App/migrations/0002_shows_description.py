# Generated by Django 2.2 on 2020-03-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Semi_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
