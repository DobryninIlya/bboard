from django.contrib import admin
import datetime

from .models import AdvUser, SuperRubric, SubRubric, Bb, AdditionalImage
from .models import Comment
from .utilities import send_activation_notification
from .forms import SubRubricForm

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy



class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # list_filter = (NonactivatedFilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
             ('is_staff', 'is_superuser',
              'groups', 'user_permissions'), ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')
    # actions = (send_activation_notifications,)

admin.site.register(AdvUser, AdvUserAdmin)

class SubRubricInline(admin.TabularInline):
    model = SubRubric

class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)

admin.site.register(SuperRubric, SuperRubricAdmin)

class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm

admin.site.register(SubRubric, SubRubricAdmin)

class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'author', 'created_at')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'author')
    date_hierarchy = 'created_at'
    fields = (('rubric', 'author'), 'title', 'content', 'price', 'contacts', 'image', 'is_active')
    inlines = (AdditionalImageInline,)

admin.site.register(Bb, BbAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at', 'is_active')
    list_display_links = ('author', 'content')
    list_filter = ('is_active',)
    search_fields = ('author', 'content',)
    date_hierarchy = 'created_at'
    fields = ('author', 'content', 'is_active', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(Comment, CommentAdmin)


admin.site.site_header = "Администрирование сайта объявлений"
admin.site.index_title = "Управление"
admin.site.site_title = "Панель управления"