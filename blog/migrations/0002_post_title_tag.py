# Generated by Django 4.2.3 on 2023-12-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Our blog', max_length=255),
        ),
    ]
