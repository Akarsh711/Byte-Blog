from django.apps import AppConfig

# Depricated 
# class PostsConfig(AppConfig):
#     name = 'posts'


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'