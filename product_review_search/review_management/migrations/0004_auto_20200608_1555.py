# Generated by Django 2.2 on 2020-06-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_management', '0003_auto_20200608_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(),
        ),
    ]