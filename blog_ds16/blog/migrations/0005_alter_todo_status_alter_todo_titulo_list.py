# Generated by Django 5.1.5 on 2025-02-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_todo_titulo_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='titulo_list',
            field=models.CharField(max_length=255),
        ),
    ]
