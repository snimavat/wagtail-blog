from __future__ import absolute_import, unicode_literals

from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import StreamBlock, CharBlock, RichTextBlock, FieldBlock, StructBlock, RawHTMLBlock, PageChooserBlock, ChoiceBlock
from wagtail.wagtailcore.blocks import TextBlock
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index


class CodeBlock(StructBlock):
    """
    Code Highlighting Block
    """
    LANGUAGE_CHOICES = (
        ('groovy', 'Groovy'),
        ('java', 'Java'),
        ('python', 'Python'),
        ('bash', 'Bash/Shell'),
        ('html', 'HTML'),
        ('css', 'CSS')


    )

    language = ChoiceBlock(choices=LANGUAGE_CHOICES)
    code = RawHTMLBlock(required=True, help_text="Insert code")

    class Meta:
        template = 'home/blocks/code.html'
        icon = 'code'
        label = "Code"




class ImageAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageAlignmentChoiceBlock()


class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), ('full', 'Full width'),
    ))


class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"


class FlexiStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    code = CodeBlock()
    paragraph = RichTextBlock(icon="pilcrow")
    image = ImageBlock(label="Aligned image", icon="image")
    document = DocumentChooserBlock(icon="doc-full-inverse")
    page_link = PageChooserBlock(label="Page chooser")


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class HomePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.HomePage', related_name='related_links')


class HomePage(Page):
    body = StreamField(FlexiStreamBlock())
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    class Meta:
        verbose_name = "Homepage"


HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('body'),
    InlinePanel('related_links', label="Related links"),
]

HomePage.promote_panels = Page.promote_panels


class BlogIndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.BlogIndexPage', related_name='related_links')


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    @property
    def blogs(self):
        # Get list of live blog pages that are descendants of this page
        blogs = BlogPage.objects.live().descendant_of(self)

        # Order by most recent date first
        blogs = blogs.order_by('-date')

        return blogs

    def get_context(self, request):
        # Get blogs
        blogs = self.blogs

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__name=tag)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(blogs, 10)  # Show 10 blogs per page
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        # Update template context
        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        return context


BlogIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    InlinePanel('related_links', label="Related links"),
]

BlogIndexPage.promote_panels = Page.promote_panels


class BlogPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.BlogPage', related_name='related_links')


class BlogPage(Page):
    intro = RichTextField(blank=True)
    body = StreamField(FlexiStreamBlock())
    date = models.DateField("Post date")

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('intro')
    ]


BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('intro', classname='full'),
    StreamFieldPanel('body'),
    InlinePanel('related_links', label="Related links"),
]

BlogPage.promote_panels = Page.promote_panels
