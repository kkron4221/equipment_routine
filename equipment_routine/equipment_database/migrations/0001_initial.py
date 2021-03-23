# Generated by Django 3.1.7 on 2021-03-23 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=200)),
                ('equipment_amount', models.IntegerField(default=0)),
            ],
        ),
    ]
