# Generated by Django 4.2.6 on 2024-04-28 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("spam_mailing", "0003_mailing"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                    "subject",
                    models.CharField(max_length=255, verbose_name="Тема письма"),
                ),
                ("body", models.TextField(verbose_name="Содержание письма")),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spam_mailing.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
        ),
    ]
