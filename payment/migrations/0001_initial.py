# Generated by Django 4.2.2 on 2023-07-03 18:48

from django.db import migrations, models
import django.db.models.deletion
import django_enum.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("borrowing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    django_enum.fields.EnumPositiveSmallIntegerField(
                        blank=True, choices=[(0, "pending"), (1, "paid")], null=True
                    ),
                ),
                (
                    "type",
                    django_enum.fields.EnumPositiveSmallIntegerField(
                        blank=True, choices=[(1, "payment"), (0, "fine")], null=True
                    ),
                ),
                ("session_url", models.URLField(blank=True, null=True)),
                ("session_id", models.CharField(max_length=255)),
                ("money_to_pay", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "borrowing_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to="borrowing.borrowing",
                    ),
                ),
            ],
        ),
    ]
