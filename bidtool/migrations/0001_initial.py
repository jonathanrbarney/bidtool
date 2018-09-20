# Generated by Django 2.1.1 on 2018-09-20 05:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Embassy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('long_country', models.CharField(max_length=1000)),
                ('short_country', models.CharField(max_length=10)),
                ('website', models.CharField(max_length=1000)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
        ),
    ]
