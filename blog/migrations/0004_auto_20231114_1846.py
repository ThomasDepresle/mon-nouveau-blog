# Generated by Django 2.2.28 on 2023-11-14 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20231114_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='id',
            new_name='id_character',
        ),
    ]
