# Generated by Django 2.1.1 on 2018-09-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20180922_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='tag',
            field=models.CharField(blank=True, choices=[('python', 'PYTHON'), ('django', 'DJANGO'), ('JAVA', 'JAVA'), ('MYSQL', 'MYSQL'), ('MACHINE_LEARNING', 'MACHINE_LEARNING'), ('JAVASCRIPT', 'JAVASCRIPT'), ('FRONT_END', 'FRONT_END')], max_length=100),
        ),
    ]
