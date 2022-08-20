# Generated by Django 3.2.9 on 2022-01-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20220103_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='is_normal',
        ),
        migrations.AddField(
            model_name='consumption',
            name='gas',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consumption',
            name='water',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='has_bathroom',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='is_insulated',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
