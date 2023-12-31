# Generated by Django 4.2.4 on 2023-08-15 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_setting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Setting', 'verbose_name_plural': 'Setting'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='created_up',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='update_up',
            new_name='update_at',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='created_up',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='update_up',
            new_name='update_at',
        ),
    ]
