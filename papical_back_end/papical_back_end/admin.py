from django.contrib import admin
from papical_back_end.models import User, Hangout, FreeTime, Invitation

# class UserAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):

#         obj.added_by = request.user
#         super().save_model(request, obj, form, change)
# admin.site.register(User, UserAdmin)

admin.site.register(User)
admin.site.register(Hangout)
admin.site.register(FreeTime)
admin.site.register(Invitation)
