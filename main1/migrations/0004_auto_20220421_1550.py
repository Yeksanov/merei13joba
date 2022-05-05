# Generated by Django 3.2 on 2022-04-21 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aty', models.CharField(max_length=50)),
                ('Tegi', models.CharField(max_length=50)),
                ('Jasy', models.CharField(max_length=50)),
                ('TýǵanQalasy', models.CharField(max_length=50)),
                ('Uıalytelefon', models.CharField(max_length=50)),
                ('Sýreti', models.ImageField(upload_to='')),
                ('Elektrondypochta', models.EmailField(blank=True, max_length=254)),
                ('Ózitýralyanyqtama', models.TextField(default='Anyqtama')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
