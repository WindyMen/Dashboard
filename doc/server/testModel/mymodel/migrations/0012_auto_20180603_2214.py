# Generated by Django 2.0.3 on 2018-06-03 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0011_auto_20180603_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_rooms', to='mymodel.User'),
        ),
    ]
