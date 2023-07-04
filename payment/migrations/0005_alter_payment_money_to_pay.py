# Generated by Django 4.2.2 on 2023-07-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0004_alter_payment_borrowing_id_alter_payment_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="money_to_pay",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
