# Generated by Django 2.0.3 on 2018-06-03 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0012_auto_20180603_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_comments', to='mymodel.Room'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='mymodel.User'),
        ),
        migrations.AlterField(
            model_name='order',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_order', to='mymodel.Room'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to='mymodel.User'),
        ),
    ]
