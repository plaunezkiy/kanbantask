# Generated by Django 3.1.7 on 2021-03-24 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanbanapp', '0002_auto_20210323_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='card',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
