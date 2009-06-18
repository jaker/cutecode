"""
Models for poster app
Jake R
"""

import datetime, re
from django.db import models, connection
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import utilities


class Language(models.Model):
    """
    Represents a language that a given 'code' may be written in

    """

    name = models.CharField(max_length=50)
    highlight_style = models.CharField(max_length=20)
    slug = models.SlugField(editable=False)
    mime_type = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Language, self).save()

    def get_absolute_url(self):
        return ('poster.views.code.code_by_language', (), { 'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)


    def __unicode__(self):
        return self.name

class Tag(models.Model):
    """
    Represents a tag that may be applied to a piece of code

    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return ('poster.views.code.code_by_tag', (), { 'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)

    def __unicode__(self):
        return self.name


class Code(models.Model):
    """
    Represents a piece of code that should be cute

    """

    title = models.CharField(max_length=250)
    language = models.ForeignKey(Language)
    description = models.TextField()
    source = models.TextField()
    submitted = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    author = models.ForeignKey(User)
    tag_list = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag, editable=False)
    parent = models.ForeignKey('self', null=True, blank=True,
                                 help_text="This field should be optional.  Only changed when code is forked from existing snippet.")

    #objects = utilties.CodeManager()

    class Meta:
        ordering = ('-submitted',)

    class Admin:
        fields = (
            ('Metadata', {
            'fields': ('title', 'language', 'author', 'tag_list', 'parent')}),
            ('None', {
             'fields': ('description', 'code')}),
            )

    def save(self, *args, **kwargs):
        if not self.id:
            self.submitted = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        self.description = self.description
        self.source = self.source
        self.tag_list = self.tag_list.lower() # Tags are saved as lower case
        super(Code, self).save(*args, **kwargs)

        #Tag code from djangosnippets.org
        # Now that the Snippet is saved, deal with the tags.
        current_tags = list(self.tags.all()) # We only want to query this once.

        # Splitting to get the new tag list is tricky, because people
        # will stick commas and other whitespace in the darndest places.
        new_tag_list = [t for t in re.split('[\s,]+', self.tag_list) if t]

        # First, clear out tags that aren't on the Snippet anymore.
        for tag in current_tags:
            if tag.name not in new_tag_list:
                self.tags.remove(tag)

        # Then add any new tags.
        for tag_name in new_tag_list:
            if tag_name not in [tag.name for tag in current_tags]:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                self.tags.add(tag)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('poster.views.code.code_detail', (), { 'code_id': str(self.id) })
    get_absolute_url = models.permalink(get_absolute_url)



# TODO: Rating & Favorite model
