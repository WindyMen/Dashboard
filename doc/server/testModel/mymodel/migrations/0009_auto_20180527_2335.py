# Generated by Django 2.0.3 on 2018-05-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0008_auto_20180527_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
