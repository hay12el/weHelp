# Generated by Django 3.2.9 on 2021-11-18 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('selected_help', models.CharField(choices=[('אוזן קשבת', 'אוזן קשבת'), ('עזרה בבית', 'עזרה בבית'), ('עזרה בקניות', 'עזרה בקניות'), ('קניית תרופות', 'קניית תרופות')], max_length=200, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('phone', models.IntegerField(blank=True)),
                ('city', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adult_post', to='accounts.adult')),
                ('youngs', models.ManyToManyField(to='accounts.young')),
            ],
        ),
    ]
