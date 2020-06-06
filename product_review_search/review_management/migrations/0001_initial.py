# Generated by Django 2.2 on 2020-06-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=20)),
                ('profile_name', models.CharField(max_length=50)),
                ('helpfulness', models.CharField(max_length=50)),
                ('score', models.FloatField()),
                ('time', models.DateTimeField()),
                ('summary', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('helpfulness_score', models.FloatField()),
            ],
        ),
    ]