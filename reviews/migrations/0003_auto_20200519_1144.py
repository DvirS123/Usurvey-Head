# Generated by Django 2.2 on 2020-05-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_remove_review_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Votes_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='Votes',
            field=models.PositiveIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='3'),
        ),
    ]
