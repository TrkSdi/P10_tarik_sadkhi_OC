# Generated by Django 4.1.7 on 2023-02-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=800)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=800)),
                ('tag', models.CharField(choices=[('BUG', 'BUG'), ('AMELIORATION', 'AMELIORATION'), ('TACHE', 'TACHE')], max_length=50)),
                ('priority', models.CharField(choices=[('FAIBLE', 'FAIBLE'), ('MOYENNE', 'MOYENNE'), ('ELEVEE', 'ELEVEE')], max_length=50)),
                ('status', models.CharField(choices=[('A faire', 'A faire'), ('En cours', 'En cours'), ('Terminé', 'Terminé')], max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=800)),
                ('project_type', models.CharField(choices=[('back-end', 'back-end'), ('front-end', 'front-end'), ('iOS', 'iOS'), ('Android', 'Android')], max_length=50)),
            ],
        ),
    ]
