# Generated by Django 2.0.5 on 2018-09-04 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]