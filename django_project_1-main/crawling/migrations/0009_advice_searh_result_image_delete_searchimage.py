# Generated by Django 4.1.7 on 2023-04-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0008_remove_advice_searh_result_image_searchimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='searh_result_image',
            field=models.ImageField(blank=True, upload_to='crawing/%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='SearchImage',
        ),
    ]