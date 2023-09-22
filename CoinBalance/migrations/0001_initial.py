# Generated by Django 4.2.4 on 2023-09-05 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('cnum', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('enum', models.IntegerField()),
                ('comment', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('enum', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('gnum', models.IntegerField()),
                ('expenseTotal', models.IntegerField()),
                ('paidBy', models.CharField(max_length=50)),
                ('ename', models.CharField(max_length=255)),
                ('edesc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('gnum', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('gname', models.CharField(max_length=255)),
                ('gdesc', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Groupmember',
            fields=[
                ('gmnum', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('gnum', models.IntegerField()),
                ('mnum', models.IntegerField()),
                ('mname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mnum', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='members/')),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('anum', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('sendernum', models.IntegerField()),
                ('receivernum', models.IntegerField()),
                ('content', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('adate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pnum', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('payernum', models.IntegerField()),
                ('receivernum', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('pdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('snum', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('enum', models.IntegerField()),
                ('mnum', models.IntegerField()),
                ('mname', models.CharField(max_length=255)),
                ('splitamount', models.FloatField()),
                ('owedto', models.IntegerField()),
                ('owedtoname', models.CharField(max_length=255)),
            ],
        ),
    ]
