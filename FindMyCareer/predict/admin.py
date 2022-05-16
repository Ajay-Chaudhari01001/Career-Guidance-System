from django.contrib import admin
from .models import GuessCareer

# Register your models here.

# In this admin.py we register the database which we created in models to give an access to the admin in which admin can read, write, and delete the data from the databse.

@admin.register(GuessCareer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','Question', 'Option1', 'Option2', 'Option3', 'Option4', 'Option5')


# After this we did migration to convert this database model into sql via the ORM (Object Relation Model) Technology Which is used to convert the database modle into sql in python.    


# After doing migration we migrate this databse model into the database where admin can access this database.

