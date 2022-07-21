# Generated by Django 4.0.4 on 2022-07-17 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('num_pages', models.IntegerField(default=0)),
                ('published_date', models.DateField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('color', models.CharField(max_length=200)),
                ('ISBN', models.CharField(max_length=200)),
            ],
        ),
    ]