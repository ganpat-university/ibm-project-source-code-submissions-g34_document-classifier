# Generated by Django 3.1 on 2022-04-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0002_remove_uploadimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='cheque',
            field=models.FileField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='driving',
            field=models.FileField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='pancard',
            field=models.FileField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='salaryslip',
            field=models.FileField(upload_to='images'),
        ),
    ]
