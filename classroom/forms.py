# # from django.forms.utils import ValidationError
# # from classroom.models import User, Customer
# # from django import forms
# # from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# # from .models import Customer,User
# # from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
# # from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
# # from django.contrib.auth import get_user_model
# # from django.core.signals import setting_changed
# # from django.dispatch import receiver


# # class CustomerForm(BSModalModelForm):
# #     def __init__(self, *args, **kwargs):
# #         super(CustomerForm, self).__init__(*args, **kwargs)
# #         self.fields['first_name'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['last_name'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['car_model'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['car_color'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['cost_per_day'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['phone_number'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['comment'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['is_payed'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #     class Meta:
# #         model = Customer
# #         fields = ('first_name', 'last_name', 'car_model', 'car_color', 'cost_per_day', 'phone_number', 'comment', 'is_payed')


# # class UserForm(BSModalModelForm):
# #     def __init__(self, *args, **kwargs):
# #         super(UserForm, self).__init__(*args, **kwargs)
# #         self.fields['username'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['first_name'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['last_name'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['email'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }
# #         self.fields['password'].widget.attrs = {
# #             'class': 'form-control col-md-6'
# #         }


# #     class Meta:
# #         model = User
# #         fields = ('username', 'first_name', 'last_name', 'email', 'password')
# from django.forms.utils import ValidationError
# from classroom.models import User, Customer
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import Customer, User
# from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
# from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
# from django.contrib.auth import get_user_model
# from django.core.signals import setting_changed
# from django.dispatch import receiver

# # Existing CustomerForm
# class CustomerForm(BSModalModelForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomerForm, self).__init__(*args, **kwargs)
#         self.fields['first_name'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['last_name'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['car_model'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['car_color'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['cost_per_day'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['phone_number'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['comment'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['is_payed'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }

#     class Meta:
#         model = Customer
#         fields = ('first_name', 'last_name', 'car_model', 'car_color', 'cost_per_day', 'phone_number', 'comment', 'is_payed')


# # Existing UserForm
# class UserForm(BSModalModelForm):
#     def __init__(self, *args, **kwargs):
#         super(UserForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['first_name'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['last_name'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['email'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }
#         self.fields['password'].widget.attrs = {
#             'class': 'form-control col-md-6'
#         }

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password')


# # New Custom Signup Form
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
#         'class': 'form-control col-md-6',
#         'placeholder': 'Email',
#     }))
#     first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
#         'class': 'form-control col-md-6',
#         'placeholder': 'First Name',
#     }))
#     last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
#         'class': 'form-control col-md-6',
#         'placeholder': 'Last Name',
#     }))

#     class Meta:
#         model = User  # Use your custom user model
#         fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'class': 'form-control col-md-6', 'placeholder': 'Username'})
#         self.fields['password1'].widget.attrs.update({'class': 'form-control col-md-6', 'placeholder': 'Password'})
#         self.fields['password2'].widget.attrs.update({'class': 'form-control col-md-6', 'placeholder': 'Confirm Password'})

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         if commit:
#             user.save()
#         return user


from django import forms
from django.contrib.auth.forms import UserCreationForm
from classroom.models import User, Customer
from bootstrap_modal_forms.forms import BSModalModelForm


# Existing CustomerForm
class CustomerForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control col-md-6'})

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'car_model', 'car_color',
                  'cost_per_day', 'phone_number', 'comment', 'is_payed')


# Existing UserForm
class UserForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control col-md-6'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


# New Signup Form with UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control col-md-6',
        'placeholder': 'Email',
    }))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control col-md-6',
        'placeholder': 'First Name',
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control col-md-6',
        'placeholder': 'Last Name',
    }))

    class Meta:
        model = User  # Use your custom user model
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control col-md-6', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control col-md-6', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control col-md-6', 'placeholder': 'Confirm Password'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
