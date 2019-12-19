# Generated by Django 2.2.4 on 2019-11-28 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('order_by', models.CharField(max_length=50)),
                ('order_location', models.CharField(max_length=200)),
            ],
        ),
    ]