"""Users Forms"""

# Django
from django import forms
from django.forms import inlineformset_factory, RadioSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
# Firmatec Model
from utils.models import Planta
#from users.models import Sexo, Civil

User = get_user_model()


class CrearUsuarioForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': "form-control-lg"}))
    first_name = forms.CharField(required=True, label="Nombres",
                                 widget=forms.TextInput(attrs={'class': "form-control-lg"}))
    last_name = forms.CharField(required=True, label="Apellidos",
                                widget=forms.TextInput(attrs={'class': "form-control-lg"}))
    group = forms.ModelChoiceField(queryset=Group.objects.none(), required=True, label="Perfil",
                                   widget=forms.Select(attrs={'class': 'selectpicker show-tick form-control-lg',
                                                              'data-size': '5',
                                                              'data-live-search': 'true',
                                                              'data-live-search-normalize': 'true'
                                                              })
                                   )
    plantas = forms.ModelMultipleChoiceField(queryset=Planta.objects.none(), required=True, label="Plantas",
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'selectpicker show-tick form-control-lg',
                                                       'data-size': '5',
                                                       'data-live-search': 'true',
                                                       'data-live-search-normalize': 'true'
                                                       })
                                            )
    planta = forms.ModelChoiceField(queryset=Planta.objects.none(), required=True, label="Planta",
                                   widget=forms.Select(attrs={'class': 'selectpicker show-tick form-control-lg',
                                                              'data-size': '5',
                                                              'data-live-search': 'true',
                                                              'data-live-search-normalize': 'true'
                                                              })
                                   )

    rut = forms.CharField(required=True, label="RUT",
                          widget=forms.TextInput(attrs={'class': "form-control-lg"}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CrearUsuarioForm, self).__init__(*args, **kwargs)
        if user.groups.filter(name='Trabajador'):
            self.fields.pop('plantas')
        if not user.groups.filter(name='Administrador').exists():
            self.fields['group'].queryset = Group.objects.exclude(name__in=['Administrador', ])
            self.fields['planta'].queryset = Planta.objects.filter(id__in=user.planta.all())
        else:
            self.fields['group'].queryset = Group.objects.all()
            self.fields['plantas'].queryset = Planta.objects.all()
            self.fields['planta'].queryset = Planta.objects.all()


    class Meta:
        model = User
        fields = ("first_name", "last_name", "sexo", "rut", "email", "telefono", "estado_civil", "fecha_nac", 
                  "nacionalidades", "domicilio", "sistema_salud", "sistema_prevision", "banco", "tipo_cta",
                  "cuenta", "group", "planta", "is_active", )
        exclude = ('password1', 'password2')


class EditarUsuarioForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': "form-control-lg"}))
    first_name = forms.CharField(required=True, label="Nombres",
                                 widget=forms.TextInput(attrs={'class': "form-control-lg"}))
    last_name = forms.CharField(required=True, label="Apellidos",
                                widget=forms.TextInput(attrs={'class': "form-control-lg"}))
    group = forms.ModelChoiceField(queryset=Group.objects.none(), required=True, label="Perfil",
                                   widget=forms.Select(attrs={'class': 'selectpicker show-tick form-control-lg',
                                                              'data-size': '5',
                                                              'data-live-search': 'true',
                                                              'data-live-search-normalize': 'true'
                                                              })
                                   )
    planta = forms.ModelMultipleChoiceField(queryset=Planta.objects.none(), required=True, label="Planta",
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'selectpicker show-tick form-control-lg',
                                                       'data-size': '5',
                                                       'data-live-search': 'true',
                                                       'data-live-search-normalize': 'true'
                                                       })
                                            )
    rut = forms.CharField(required=True, label="RUT",
                          widget=forms.TextInput(attrs={'class': "form-control-lg"}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EditarUsuarioForm, self).__init__(*args, **kwargs)
        if not user.groups.filter(name='Administrador').exists():
            self.fields['group'].queryset = Group.objects.exclude(name__in=['Administrador', ])
            self.fields['planta'].queryset = Planta.objects.filter(id__in=user.planta.all())
        else:
            self.fields['group'].queryset = Group.objects.all()
            self.fields['planta'].queryset = Planta.objects.all()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "sexo", "rut", "email", "telefono", "estado_civil", "fecha_nac", 
                  "nacionalidades", "domicilio", "sistema_salud", "sistema_prevision", "banco", "tipo_cta",
                  "cuenta", "group", "planta", "is_active", )
