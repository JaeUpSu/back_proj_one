# Generated by Django 4.1.5 on 2023-01-03 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0002_alter_user_is_business"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("content", models.TextField()),
                ("like", models.DecimalField(decimal_places=0, max_digits=9)),
                ("reply", models.CharField(max_length=30)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.user",
                    ),
                ),
            ],
        ),
    ]