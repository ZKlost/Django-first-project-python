# Generated by Django 4.2.4 on 2023-08-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_category_is_activate_remove_news_is_activate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=300)),
                ('logo', models.CharField()),
                ('price', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]