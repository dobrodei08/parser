# Generated by Django 2.2 on 2019-04-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lutner_parser', '0009_auto_20190425_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
