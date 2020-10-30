# Generated by Django 3.1.2 on 2020-10-30 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201030_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike_type',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='brand',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='condition',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='deals',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_url',
            field=models.URLField(blank=True, default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller_notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]
