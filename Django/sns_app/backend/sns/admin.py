from django.contrib import admin
from .models import Users, Posts,Photos, Comments, Likes

# SNS_DB
admin.site.register(Users)
admin.site.register(Photos)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Likes)