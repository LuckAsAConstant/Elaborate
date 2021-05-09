# Generated by Django 3.2.2 on 2021-05-09 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Central',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('begin', models.FloatField()),
                ('end', models.FloatField()),
                ('nameCabinet', models.CharField(max_length=30)),
                ('placeCabinet', models.CharField(max_length=30)),
                ('idCentral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.central')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='trellis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('name', models.CharField(max_length=30)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('idLine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.line')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('idRegion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.region')),
            ],
        ),
        migrations.AddField(
            model_name='central',
            name='idCity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.city'),
        ),
    ]
