# Generated by Django 4.1.1 on 2023-01-06 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SD', '0002_murid_alter_sekolah_nama_sekolah'),
    ]

    operations = [
        migrations.RenameField(
            model_name='murid',
            old_name='Jmlhmurid',
            new_name='jmlhmurid',
        ),
        migrations.RenameField(
            model_name='murid',
            old_name='nama_sekolah',
            new_name='nama',
        ),
    ]
