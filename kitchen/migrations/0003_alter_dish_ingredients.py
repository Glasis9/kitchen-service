# Generated by Django 4.1.2 on 2022-11-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="ingredients",
            field=models.ManyToManyField(
                blank=True, related_name="dishes", to="kitchen.ingredient"
            ),
        ),
    ]
