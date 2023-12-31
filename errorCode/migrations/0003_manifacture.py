# Generated by Django 4.2.5 on 2023-10-24 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('errorCode', '0002_remove_bmw_category_remove_dodge_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manifacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
                ('manifacture', models.CharField(max_length=70)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='errorCode.category')),
            ],
        ),
    ]
