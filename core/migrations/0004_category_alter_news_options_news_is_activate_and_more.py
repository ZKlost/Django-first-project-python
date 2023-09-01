# Generated by Django 4.2.4 on 2023-08-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_news_options_alter_setting_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('is_activate', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={},
        ),
        migrations.AddField(
            model_name='news',
            name='is_activate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='setting',
            name='is_activate',
            field=models.BooleanField(default=False),
        ),
    ]