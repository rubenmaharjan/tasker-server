# Generated by Django 4.0.3 on 2022-04-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_deliverable_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverable',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subdeliverable',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
