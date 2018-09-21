from django.contrib import admin
from courses.models import Course, Inscricao
# Register your models here.



class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','slug','start_date','created_at']
    search_fields = ['name','slug']
    #preenchendo o slug automaticamente
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Course, CourseAdmin)
admin.site.register(Inscricao)