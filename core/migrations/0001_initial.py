# Generated by Django 5.0.1 on 2024-02-05 11:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('about', models.CharField(max_length=150)),
                ('logo', models.TextField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
