from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.



@admin.register(Post)
class NowKnowHowThisGonnaWork(admin.ModelAdmin):
    filter_horizontal  = ('tags',)
    class Media: # This should be remain same 
        js = ('assets/js/tinyinjector.js',) # The file should be in statics, "comma" is important!

class CategoryAdmin(admin.ModelAdmin):
	filter_horizontal =('tags',)

# Restricting no. of featured posts
class FeaturedPostAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 6:
      return False
    else:
      return True

class CustomUserAdmin(admin.ModelAdmin):
	list_display = ('username','is_active','is_staff',)

admin.site.register(FeaturedPost, FeaturedPostAdmin)
admin.site.register(BlogComment)
admin.site.register(Tags)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(User, CustomUserAdmin)
