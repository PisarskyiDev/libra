# Generated by Django 4.2.2 on 2023-07-06 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("borrowing", "0002_initial"),
        ("payment", "0006_alter_payment_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="borrowing_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="borrowing_payments",
                to="borrowing.borrowing",
            ),
        ),
    ]