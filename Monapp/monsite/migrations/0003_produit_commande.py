# Generated by Django 4.2.2 on 2023-06-25 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monsite', '0002_alter_client_datenaissance_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='commande',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monsite.commande'),
        ),
    ]