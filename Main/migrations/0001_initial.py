# Generated by Django 3.2.12 on 2022-04-06 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True, unique=True)),
                ('symbol', models.CharField(max_length=20, null=True)),
                ('constituency', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_votes', models.IntegerField(null=True)),
                ('candidate_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Main.candidates')),
            ],
        ),
    ]
