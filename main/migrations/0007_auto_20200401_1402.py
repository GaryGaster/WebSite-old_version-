# Generated by Django 3.0.2 on 2020-04-01 14:02

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200331_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='unlike_total',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='unlike_total',
        ),
        migrations.RemoveField(
            model_name='serial',
            name='unlike_total',
        ),
        migrations.RemoveField(
            model_name='xvideo',
            name='unlike_total',
        ),
        migrations.AlterField(
            model_name='anime',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (4, 'YOUTUBE'), (2, 'NETFLIX'), (3, 'AMAZONPRIME')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (4, 'YOUTUBE'), (2, 'NETFLIX'), (3, 'AMAZONPRIME')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='serial',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (4, 'YOUTUBE'), (2, 'NETFLIX'), (3, 'AMAZONPRIME')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='xvideo',
            name='platforms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'HBO'), (4, 'YOUTUBE'), (2, 'NETFLIX'), (3, 'AMAZONPRIME')], max_length=7, null=True),
        ),
    ]
