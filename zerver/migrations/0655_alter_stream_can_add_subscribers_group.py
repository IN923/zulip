# Generated by Django 5.0.9 on 2024-12-17 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0654_set_default_for_stream_can_add_subscribers_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stream",
            name="can_add_subscribers_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
    ]
