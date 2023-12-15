from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CcnJobCard, User, Profile, Division, ProblemCategory

# Register your models here.

app_name = 'users'




admin.site.register(Division)
admin.site.register(Profile)
admin.site.register(ProblemCategory)
# admin.site.register(Profiles)
admin.site.register(CcnJobCard)





class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
       
class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = AuthUserAdmin.fieldsets + (
            ('Extended Field', {'fields': ('division_name', 'is_hod',
                                         'is_ccn_hod', 'is_engineer', 'is_user',)}),
    )
    list_display = ('username', 'is_hod','is_ccn_hod','division_name')
    search_fields = ['username']