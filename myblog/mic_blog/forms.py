from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment


class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
            bio = self.cleaned_data.get('bio', '')
            avatar = self.cleaned_data.get('avatar', None)

            UserProfile.objects.create(
                user=user,
                bio=bio,
                avatar=avatar,
                username=user.username,
            )
        return user
class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

###############

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'username']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'image']
