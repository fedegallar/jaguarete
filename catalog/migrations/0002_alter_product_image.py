# Generated by Django 3.2.4 on 2021-07-07 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(height_field='image_height', upload_to='', width_field='image_width'),
        ),
    ]