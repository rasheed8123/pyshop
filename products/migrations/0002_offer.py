# Generated by Django 3.0.6 on 2020-05-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField(max_length=5)),
            ],
        ),
    ]
