# Generated by Django 2.0 on 2019-08-16 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20190816_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Business'),
        ),
    ]
