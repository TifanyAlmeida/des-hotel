# Generated by Django 4.1.1 on 2022-09-29 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospedadore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sobre', models.CharField(max_length=150)),
                ('imagem', models.ImageField(upload_to='foto/%y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='ListaRecurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_recurso', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_recurso', models.CharField(max_length=60)),
                ('lista_recurso', models.ManyToManyField(to='home.listarecurso')),
            ],
        ),
        migrations.CreateModel(
            name='Hospedagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('preco_por', models.CharField(choices=[('Dia', 'Dia'), ('Semana', 'Semana'), ('M??s', 'M??s')], default='Dia', max_length=6)),
                ('taxa_limpeza', models.DecimalField(decimal_places=2, max_digits=8)),
                ('imagem_1', models.ImageField(upload_to='foto/%y/%m/%d')),
                ('imagem_2', models.ImageField(upload_to='foto/%y/%m/%d')),
                ('imagem_3', models.ImageField(upload_to='foto/%y/%m/%d')),
                ('imagem_4', models.ImageField(upload_to='foto/%y/%m/%d')),
                ('imagem_5', models.ImageField(upload_to='foto/%y/%m/%d')),
                ('disponibilidade_a_partir', models.DateField()),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.endereco')),
                ('hospedador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.hospedadore')),
                ('lista_recurso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.recurso')),
            ],
        ),
    ]
