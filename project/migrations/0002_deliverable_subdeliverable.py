# Generated by Django 4.0.3 on 2022-04-27 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverable', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliverables', to='project.project')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SubDeliverable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_deliverable', models.CharField(max_length=100)),
                ('deliverable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_deliverables', to='project.deliverable')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
