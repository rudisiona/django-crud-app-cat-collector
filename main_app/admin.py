from django.contrib import admin
from .models import Cat, Feeding, Toy
# Register your models here.

# allow admin to manage cats

admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)

