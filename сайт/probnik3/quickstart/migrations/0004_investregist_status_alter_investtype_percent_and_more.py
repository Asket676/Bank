# Generated by Django 4.2.6 on 2023-11-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_bankworkers_investregist_investtype_moneycourse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='investregist',
            name='status',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='investtype',
            name='percent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moneycourse',
            name='course',
            field=models.FloatField(),
        ),
    ]
