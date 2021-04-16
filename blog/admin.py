from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Post)
class NowKnowHowThisGonnaWork(admin.ModelAdmin):
    filter_horizontal  = ('tags',)
    class Media: # This should be remain same 
        js = ('assets/js/tinyinjector.js',) # The file should be in statics, "comma" is important!

class CategoryAdmin(admin.ModelAdmin):
	filter_horizontal =('tags',)

class FeaturedPostAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 6:
      return False
    else:
      return True

admin.site.register(FeaturedPost, FeaturedPostAdmin)
admin.site.register(BlogComment)
admin.site.register(Tags)
admin.site.register(Category, CategoryAdmin)
