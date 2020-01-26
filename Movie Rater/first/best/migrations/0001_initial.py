# Generated by Django 3.0.2 on 2020-01-08 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=140)),
                ('last_name', models.CharField(default='', max_length=140)),
                ('born', models.DateField()),
                ('died', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Not Available', max_length=140)),
                ('plot', models.TextField(default='-Not Available-')),
                ('year', models.PositiveIntegerField(default=0)),
                ('rating', models.IntegerField(choices=[(0, 'NR - Not Rated'), (1, 'G - General Audiences'), (2, 'PG - Parental Guidence Suggested'), (3, 'R - Restricted')], default=0)),
                ('runtime', models.PositiveIntegerField(default=0)),
                ('website', models.URLField(blank=True)),
                ('actors', models.ManyToManyField(blank=True, related_name='acting_credits', to='best.Person')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='directed', to='best.Person')),
                ('writers', models.ManyToManyField(blank=True, related_name='writing_credits', to='best.Person')),
            ],
            options={
                'ordering': ('-year', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='best.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='best.Person')),
            ],
            options={
                'unique_together': {('movie', 'person', 'name')},
            },
        ),
    ]