# Generated by Django 2.2 on 2020-06-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_management', '0002_auto_20200608_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(db_index=True),
        ),
    ]
