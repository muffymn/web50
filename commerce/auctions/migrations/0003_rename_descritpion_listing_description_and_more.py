# Generated by Django 4.2.2 on 2023-07-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='descritpion',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='listing',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]