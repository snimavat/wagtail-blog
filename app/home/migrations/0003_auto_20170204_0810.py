# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 08:10
from __future__ import unicode_literals

import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks
from django.db import migrations

import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blogpage_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('groovy', 'Groovy'), ('java', 'Java'), ('python', 'Python'), ('bash', 'Bash/Shell'), ('html', 'HTML'), ('css', 'CSS')])), ('code', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='Insert code', required=True))))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock())), icon='image', label='Aligned image')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('page_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Page chooser')))),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('groovy', 'Groovy'), ('java', 'Java'), ('python', 'Python'), ('bash', 'Bash/Shell'), ('html', 'HTML'), ('css', 'CSS')])), ('code', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='Insert code', required=True))))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock())), icon='image', label='Aligned image')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('page_link', wagtail.wagtailcore.blocks.PageChooserBlock(label='Page chooser')))),
        ),
    ]
