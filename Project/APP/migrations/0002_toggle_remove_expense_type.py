# Generated by Django 5.0.4 on 2024-04-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toggle',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('TypeOfExpense', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='expense',
            name='Type',
        ),
    ]
