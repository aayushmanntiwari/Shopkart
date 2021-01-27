# Generated by Django 3.1 on 2021-01-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_auto_20210115_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Color',
            new_name='Display_Color',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='RAM',
            new_name='Domestic_Warranty',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='GPRS',
            new_name='Infrared',
        ),
        migrations.AddField(
            model_name='product',
            name='Flash',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Graphics_PPI',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Ringtones_Format',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='SIM_Size',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Sensors',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Touchscreen_Type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Video_Formats',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='gpu',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='nfc',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=225, null=True),
        ),
    ]