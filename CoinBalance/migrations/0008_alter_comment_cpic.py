# Generated by Django 4.2.4 on 2023-09-08 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinBalance', '0007_comment_cpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cpic',
            field=models.CharField(max_length=255),
        ),
    ]
