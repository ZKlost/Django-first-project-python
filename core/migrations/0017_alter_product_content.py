# Generated by Django 4.2.4 on 2023-08-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(),
        ),
    ]
