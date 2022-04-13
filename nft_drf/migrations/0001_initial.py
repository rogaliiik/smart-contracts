# Generated by Django 4.0.3 on 2022-04-13 11:41

from django.db import migrations, models
import nft_drf.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_hash', models.CharField(default=nft_drf.models._createHashId, max_length=20, unique=True)),
                ('tx_hash', models.CharField(max_length=100)),
                ('media_url', models.URLField()),
                ('owner', models.GenericIPAddressField()),
            ],
        ),
    ]