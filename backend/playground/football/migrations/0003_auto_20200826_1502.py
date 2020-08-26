# Generated by Django 3.1 on 2020-08-26 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("football", "0002_auto_20200826_1455"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="manager",
            name="team",
        ),
        migrations.AddField(
            model_name="team",
            name="manager",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="football.manager",
            ),
        ),
    ]
