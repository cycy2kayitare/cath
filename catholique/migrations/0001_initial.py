# Generated by Django 3.1.2 on 2020-10-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateTimeField()),
                ('father_date_birth', models.DateTimeField()),
                ('mother_date_birth', models.DateTimeField()),
                ('id_no', models.CharField(max_length=16)),
                ('photocopy_id', models.ImageField(upload_to='id/')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
