# Generated by Django 4.1.3 on 2022-12-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tlaut_apps", "0003_kegiatan_remove_donasi_kode_alter_donasi_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kegiatan",
            name="jenis_aksi",
            field=models.CharField(max_length=50),
        ),
    ]
