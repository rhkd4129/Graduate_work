# Generated by Django 4.1.7 on 2023-04-06 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('keywords', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AdviceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='advice_images/')),
                ('trans_image', models.ImageField(null=True, upload_to='trans_images/')),
                ('advice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a', to='coloring.advice')),
            ],
        ),
    ]
