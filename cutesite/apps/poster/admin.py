from django.contrib import admin
from models import Language, Tag, Code

class LanguageAdmin(admin.ModelAdmin):
    pass
#    fields = (
#        ('Language Information', {
#        'fields': ('name', 'mime_type')})
#        )
admin.site.register(Language, LanguageAdmin)

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)

class CodeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Code, CodeAdmin)

