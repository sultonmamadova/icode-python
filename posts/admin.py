from django.contrib import admin
from posts.models import Post

# Register your models here.
# decorator - 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]