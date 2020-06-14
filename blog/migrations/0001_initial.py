# Generated by Django 3.0.7 on 2020-06-14 20:33

import blog.mixins
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('custom_image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('og_title', models.CharField(blank=True, help_text='Fallbacks to seo title if empty', max_length=40, null=True, verbose_name='Facebook title')),
                ('og_description', models.CharField(blank=True, help_text='Fallbacks to seo description if empty', max_length=300, null=True, verbose_name='Facebook description')),
                ('twitter_title', models.CharField(blank=True, help_text='Fallbacks to facebook title if empty', max_length=40, null=True, verbose_name='Twitter title')),
                ('twitter_description', models.CharField(blank=True, help_text='Fallbacks to facebook description if empty', max_length=300, null=True, verbose_name='Twitter description')),
                ('robot_noindex', models.BooleanField(default=False, help_text='Check to add noindex to robots', verbose_name='No index')),
                ('robot_nofollow', models.BooleanField(default=False, help_text='Check to add nofollow to robots', verbose_name='No follow')),
                ('canonical_link', models.URLField(blank=True, null=True, verbose_name='Canonical link')),
                ('og_image', models.ForeignKey(blank=True, help_text='If you want to override the image used on Facebook for                     this item, upload an image here.                     The recommended image size for Facebook is 1200 × 630px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='custom_image.CustomImage')),
                ('twitter_image', models.ForeignKey(blank=True, help_text='Fallbacks to facebook image if empty', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='custom_image.CustomImage', verbose_name='Twitter image')),
            ],
            options={
                'abstract': False,
            },
            bases=(blog.mixins.EnhancedEditHandlerMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.BasePage')),
            ],
            options={
                'verbose_name': 'Home',
            },
            bases=('blog.basepage',),
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtm_id', models.CharField(blank=True, max_length=50)),
                ('google_site_verification', models.CharField(blank=True, max_length=255)),
                ('cookie_content', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Cookie bar content')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Site setting',
                'verbose_name_plural': 'Site settings',
            },
        ),
    ]
