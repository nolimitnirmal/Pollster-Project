from django.contrib import admin

# Register your models here.

from .models import Question, Choice  # Importing the models we created earlier in models.py

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"


# the code below is for customizing the admin interface for the Question and Choice models

class ChoiceInline(admin.TabularInline):  # This class allows us to edit choices inline in the admin interface
    model = Choice  # We are using the Choice model
    extra = 3  # This shows how many empty choice fields to display by default

class QuestionAdmin(admin.ModelAdmin):  # This class customizes the admin interface for the Question model
    fieldsets = [(None, {'fields': ['question_text']}), 
                ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]
    # This defines the layout of the fields in the admin interface




# admin.site.register(Question) # Registering the Question model with the admin site
# admin.site.register(Choice)  # Registering the Choice model with the admin site
# This allows us to manage these models through the Django admin interface
# Now, when we run the server and go to the admin interface, we can add, edit, and delete questions and choices easily.
# The admin interface will automatically generate forms for these models
# and provide a user-friendly way to manage them.

admin.site.register(Question, QuestionAdmin)  # Registering the Question model with the custom admin interface