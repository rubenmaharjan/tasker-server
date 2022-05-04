# Generated by Django 4.0.3 on 2022-04-27 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_deliverable_subdeliverable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverable',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deliverables', to='project.project'),
        ),
        migrations.AlterField(
            model_name='subdeliverable',
            name='deliverable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_deliverables', to='project.deliverable'),
        ),
    ]
