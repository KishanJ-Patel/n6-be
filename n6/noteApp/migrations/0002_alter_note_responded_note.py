# Generated by Django 4.1.4 on 2023-03-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='responded_note',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
