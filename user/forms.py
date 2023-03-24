from typing import Optional

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, get_user_model, forms, UsernameField
from django.core.exceptions import ValidationError
from django.db.models import QuerySet

from .models import StudentMeta, School, TeacherMeta, ParentMeta, User


class RegisterForm(UserCreationForm):
    UserCreationForm.error_messages.update({
        "invalid_code": "Код не был найден",
        "invalid_choice": "Выберите группу",
        "used_code": "Код уже был использован",
    })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.meta: Optional[StudentMeta] = None
        self.groups_selected = False

        self.meta_model = None
        self.is_owner = False

    def clean_groups(self):
        value = self.cleaned_data.get('groups')
        if not value:
            raise ValidationError(self.error_messages['invalid_choice'], code='invalid_choice')
        self.groups_selected = True
        return value

    def clean_code(self):
        code = self.cleaned_data['code']
        if not self.groups_selected:
            return code
        if len(User.objects.filter(code=code)) >= 1:
            raise ValidationError(self.error_messages['used_code'], code='used_code')
        metas_choice = {
            "Учителя": TeacherMeta,
            "Ученики": StudentMeta,
            "Родители": ParentMeta,
        }
        if self.cleaned_data['groups'].name == "Владельцы":
            self.is_owner = True
            return '1'
        self.meta_model = meta_model = metas_choice[self.cleaned_data['groups'].name]
        query: QuerySet = meta_model.objects.filter(code=code)
        if len(query) == 0:
            raise ValidationError(self.error_messages['invalid_code'], code='invalid_code')
        self.meta = query.first()
        return code

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("email", "groups", "code")
        field_classes = {"username": UsernameField, "groups": forms.ModelChoiceField}

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.is_owner:
            attrs = {StudentMeta: 'student_meta', TeacherMeta: 'teacher_meta', ParentMeta: 'parent_meta'}
            setattr(user, attrs[self.meta_model], self.meta)
            user.school = self.meta.school
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    pass


class SchoolRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = School
        fields = ("name", "email", "number")
