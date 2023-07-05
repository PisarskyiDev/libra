# Generated by Django 4.2.2 on 2023-07-05 12:31

from django.db import migrations
import django_enum.fields


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0005_alter_payment_money_to_pay"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="type",
            field=django_enum.fields.EnumPositiveSmallIntegerField(
                blank=True, choices=[(0, "payment"), (1, "fine")], default=0, null=True
            ),
        ),
    ]