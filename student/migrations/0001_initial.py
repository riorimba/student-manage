# Generated by Django 4.1.5 on 2023-01-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]