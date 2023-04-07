# Generated by Django 4.1.7 on 2023-04-07 22:43

import ContainerizedWorkshops.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('format', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TunneledPort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('container_port', models.IntegerField()),
                ('client_port', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.CharField(default=ContainerizedWorkshops.models.create_new_id, max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('docker_tag', models.CharField(max_length=100)),
                ('working_directory', models.CharField(max_length=120)),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('snippets', models.ManyToManyField(to='ContainerizedWorkshops.snippet')),
                ('tunneled_ports', models.ManyToManyField(to='ContainerizedWorkshops.tunneledport')),
            ],
        ),
    ]
