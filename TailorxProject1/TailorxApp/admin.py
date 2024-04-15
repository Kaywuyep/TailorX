from django.contrib import admin
from .models import Post, Client, Tailor, Picture, Profile
from .models import Message, State, City, Place


admin.site.register(Profile)
 
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post Details', {'fields': ['title', 'author', 'body']}),
    ]
    list_display = ('title', 'author', 'body')

admin.site.register(Post)

class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['first_name', 'last_name', 'username', 'address']}),
    ]
    list_display = ('first_name', 'last_name', 'username', 'address')  # Corrected list_display

admin.site.register(Client, ClientAdmin)
class TailorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'first_name', 'last_name', 'username', 'business_name', 'address']}),
        ('Location', {'fields': ['location']}),
        ('Pictures', {'fields': ['tailor_pictures']}),
    ]
    list_display = ('user', 'first_name', 'last_name', 'username', 'business_name', 'address', 'location')
    filter_horizontal = ('tailor_pictures',)

admin.site.register(Tailor, TailorAdmin)

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Details', {'fields': ['sender', 'recipient', 'content']}),
    ]
    list_display = ('sender', 'recipient', 'content')

admin.site.register(Message, MessageAdmin)

class PictureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tailor']}),
        ('Image Details', {'fields': ['caption', 'image']}),
    ]
    list_display = ('tailor', 'caption', 'image',)
    # list_filter = ('uploaded_at',)  # Optional: Adds a filter sidebar

admin.site.register(Picture, PictureAdmin)

class StateAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    list_display = ('name',)  # Display the name of the state in the admin list view

admin.site.register(State, StateAdmin)

class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'state']}),
    ]
    list_display = ('name', 'state')  # Display the name of the city and its associated state in the admin list view
    list_filter = ('state',)  # Add a filter sidebar to filter cities by their associated state

admin.site.register(City, CityAdmin)

class PlaceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'city']}),
        ('Description', {'fields': ['description']}),
    ]
    list_display = ('name', 'city', 'description')

admin.site.register(Place, PlaceAdmin)
