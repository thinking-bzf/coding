from django.contrib import admin

# Register your models here.
from data_deal.models import FirstZY, original_file, Today_CleanedFile, Today_MergedFile
admin.site.register(FirstZY)
admin.site.register(original_file)
admin.site.register(Today_CleanedFile)
admin.site.register(Today_MergedFile)
