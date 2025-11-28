from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Nom utilisateur",
        help_text="150 caractères ou moins. Lettres, chiffres et @ . + - _ uniquement.",
        strip=False,
    )
    password1 = forms.CharField(
        label="Nouveau mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Confirmez le mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    email = forms.EmailField(
        required=True,
        label="Votre email",
        widget=forms.EmailInput(attrs={'autocomplete': 'new-email', 'placeholder': '@'}),
    )
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("username", "email", "password1", "password2")