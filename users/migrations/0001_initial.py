# Generated by Django 2.0 on 2018-10-10 00:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.IntegerField(choices=[(1, 'student'), (2, 'company')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ChosenInterests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=64)),
                ('about', models.TextField(blank=True, default='', max_length=100)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('tax', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=users.models.scramble_uploaded_image, verbose_name='Avatar')),
                ('linked_in_website', models.URLField(blank=True, null=True)),
                ('twitter_website', models.URLField(blank=True, null=True)),
                ('facebook_website', models.URLField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_name', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=30)),
                ('institute', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=80)),
            ],
            options={
                'ordering': ['edu_name'],
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inte_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['inte_name'],
            },
        ),
        migrations.CreateModel(
            name='OwnedSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=80)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='users.CompanyProfile')),
            ],
            options={
                'ordering': ['policy_name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('skill_type', models.IntegerField(choices=[(1, 'technical skill'), (2, 'soft skill')], default=1)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SkillTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=30)),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['skill_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=64)),
                ('about', models.TextField(blank=True, default='', max_length=100)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=users.models.scramble_uploaded_image, verbose_name='Avatar')),
                ('linked_in_website', models.URLField(blank=True, null=True)),
                ('twitter_website', models.URLField(blank=True, null=True)),
                ('facebook_website', models.URLField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('chosen_interests', models.ManyToManyField(to='users.Interest')),
                ('owned_skills', models.ManyToManyField(to='users.Skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transcript_name', models.CharField(default='', max_length=50)),
                ('transcript', models.FileField(blank=True, null=True, upload_to=users.models.scramble_uploaded_transcript, verbose_name='Transcript')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('studentprofile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transcripts', to='users.StudentProfile')),
            ],
            options={
                'ordering': ['transcript_name'],
            },
        ),
        migrations.CreateModel(
            name='Wh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('studentprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_history', to='users.StudentProfile')),
            ],
            options={
                'ordering': ['work_name'],
            },
        ),
        migrations.AddField(
            model_name='skilltest',
            name='studentprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_test', to='users.StudentProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='skill',
            unique_together={('name',)},
        ),
        migrations.AddField(
            model_name='ownedskills',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Skill'),
        ),
        migrations.AddField(
            model_name='ownedskills',
            name='studentprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.StudentProfile'),
        ),
        migrations.AddField(
            model_name='education',
            name='studentprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='users.StudentProfile'),
        ),
        migrations.AddField(
            model_name='choseninterests',
            name='interest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Interest'),
        ),
        migrations.AddField(
            model_name='choseninterests',
            name='studentprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.StudentProfile'),
        ),
    ]
