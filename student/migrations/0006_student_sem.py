# Generated by Django 2.1 on 2018-08-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20180823_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sem',
            field=models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth'), ('6', 'Sixth'), ('7', 'Seventh'), ('8', 'Eighth')], max_length=10, null=True),
        ),
    ]