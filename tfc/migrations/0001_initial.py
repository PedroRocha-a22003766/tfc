# Generated by Django 4.1.2 on 2023-05-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Condicao",
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
                ("dificuldade", models.CharField(max_length=16)),
                ("expo_solar", models.IntegerField(default=0)),
                ("quantidade_agua", models.IntegerField(default=0)),
                ("quantidade_fertilizante", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Planta",
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
                ("nome", models.CharField(max_length=64)),
                ("descricao", models.CharField(max_length=512)),
                ("imagem", models.ImageField(default="", upload_to="")),
                ("condicoes", models.ManyToManyField(to="tfc.condicao")),
            ],
        ),
        migrations.CreateModel(
            name="Utilizador",
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
                ("nome", models.CharField(max_length=64)),
                ("genero", models.CharField(max_length=16)),
                ("idade", models.IntegerField(default=0)),
                ("plantas", models.ManyToManyField(to="tfc.planta")),
            ],
        ),
    ]
