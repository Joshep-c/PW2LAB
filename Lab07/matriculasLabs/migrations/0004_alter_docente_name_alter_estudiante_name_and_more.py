# Generated by Django 4.2.2 on 2023-07-13 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculasLabs', '0003_alter_delegado_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='delegado',
            unique_together={('asignatura',)},
        ),
    ]
