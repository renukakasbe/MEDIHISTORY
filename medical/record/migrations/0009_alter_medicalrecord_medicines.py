# Generated by Django 3.2.3 on 2021-05-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0008_alter_medicalrecord_medicines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='medicines',
            field=models.CharField(max_length=300),
        ),
    ]
