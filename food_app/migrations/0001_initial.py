# Generated by Django 5.0.1 on 2024-02-07 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('short_description', models.TextField()),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('image', models.ImageField(upload_to='food_images/')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_app.productcategory')),
            ],
            options={
                'verbose_name': 'fast food mahsuloti',
                'verbose_name_plural': 'faqat fast food mahsulotlari',
            },
        ),
    ]
