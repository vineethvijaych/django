# Generated by Django 4.2.1 on 2023-07-11 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student_cname'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=20)),
            ],
        ),
    ]