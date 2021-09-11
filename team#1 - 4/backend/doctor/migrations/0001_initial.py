# Generated by Django 3.2.7 on 2021-09-10 20:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doc_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('specialization', models.TextField(verbose_name='Specialization')),
                ('address', models.TextField(verbose_name='Clinic Address')),
                ('profile_pic', models.ImageField(upload_to='uploads/profile_pic/')),
                ('patient_per_hr', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')])),
                ('description', models.TextField(verbose_name='Description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='uploads/degree/')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)], verbose_name='Day')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
            options={
                'unique_together': {('doc', 'day')},
            },
        ),
    ]