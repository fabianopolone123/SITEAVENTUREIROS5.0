import json

from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone

from backend.apps.members.models import Adventurer, ImageReleaseTerm, MedicalRecord, Responsible


class DraftModelForm(forms.ModelForm):
    def __init__(self, *args, save_draft=False, **kwargs):
        self.save_draft = save_draft
        super().__init__(*args, **kwargs)
        if save_draft:
            for field in self.fields.values():
                field.required = False


class ResponsibleForm(DraftModelForm):
    username = forms.CharField(
        label='Nome de usuário',
        max_length=150,
        required=False,
        help_text='Será usado como login para acessar a plataforma.',
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
        required=False,
    )
    password_confirm = forms.CharField(
        label='Confirmação da senha',
        widget=forms.PasswordInput(),
        required=False,
    )
    signature_data = forms.CharField(widget=forms.HiddenInput(), required=False)

    REQUIRED_FIELDS = [
        'father_name',
        'father_cpf',
        'father_email',
        'father_phone',
        'mother_name',
        'mother_cpf',
        'mother_email',
        'mother_phone',
        'legal_name',
        'legal_relationship',
        'legal_cpf',
        'legal_email',
        'legal_phone',
        'address_line',
        'neighborhood',
        'city',
        'state',
        'cep',
        'address_number',
    ]

    class Meta:
        model = Responsible
        fields = [
            'father_name',
            'father_cpf',
            'father_email',
            'father_phone',
            'mother_name',
            'mother_cpf',
            'mother_email',
            'mother_phone',
            'legal_type',
            'legal_name',
            'legal_relationship',
            'legal_cpf',
            'legal_email',
            'legal_phone',
            'nationality',
            'marital_status',
            'rg_or_cin',
            'address_line',
            'neighborhood',
            'city',
            'state',
            'cep',
            'address_number',
            'declaration_accepted',
        ]
        widgets = {'declaration_accepted': forms.CheckboxInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
        self.fields['username'].required = not self.save_draft

    def clean(self):
        cleaned = super().clean()
        if self.save_draft:
            return cleaned
        for name in self.REQUIRED_FIELDS:
            if not cleaned.get(name):
                self.add_error(name, 'Campo obrigatório para continuar.')
        if not cleaned.get('declaration_accepted'):
            self.add_error('declaration_accepted', 'Você precisa confirmar a declaração antes de continuar.')
        signature = cleaned.get('signature_data')
        if not signature:
            self.add_error('signature_data', 'Assine acima para validar o responsável.')
        username = cleaned.get('username')
        password = cleaned.get('password')
        password_confirm = cleaned.get('password_confirm')
        if not username:
            self.add_error('username', 'Informe um nome de usuário para acessar o sistema.')
        else:
            User = get_user_model()
            users = User.objects.filter(username__iexact=username)
            if self.instance and self.instance.user:
                users = users.exclude(pk=self.instance.user.pk)
            if users.exists():
                self.add_error('username', 'Este nome de usuário já está em uso.')
        requires_password = not self.instance.user
        if password or requires_password:
            if not password:
                self.add_error('password', 'Informe a senha do usuário.')
            if not password_confirm:
                self.add_error('password_confirm', 'Confirme a senha digitada.')
            if password and password_confirm and password != password_confirm:
                self.add_error('password_confirm', 'As senhas precisam coincidir.')
        self._check_duplicate_cpf(cleaned, 'father_cpf', 'CPF do pai')
        self._check_duplicate_cpf(cleaned, 'mother_cpf', 'CPF da mãe')
        self._check_duplicate_cpf(cleaned, 'legal_cpf', 'CPF do responsável legal')
        return cleaned

    def save(self, commit=True):
        responsible = super().save(commit=False)
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username:
            responsible.user = self._ensure_user(username, password)
        if commit:
            responsible.save()
        return responsible

    def _check_duplicate_cpf(self, cleaned, field_name, label):
        value = cleaned.get(field_name)
        if not value:
            return
        duplicates = Responsible.objects.filter(**{field_name: value})
        if self.instance and self.instance.pk:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            self.add_error(field_name, f'Já existe um cadastro com este {label}.')

    def _ensure_user(self, username, password):
        User = get_user_model()
        user = self.instance.user
        if user:
            user.username = username
            if password:
                user.set_password(password)
            user.save()
            return user
        return User.objects.create_user(username=username, password=password)


class AdventurerForm(DraftModelForm):
    photo_data = forms.CharField(widget=forms.HiddenInput(), required=False)
    signature_data = forms.CharField(widget=forms.HiddenInput(), required=False)
    photo = forms.FileField(required=False)

    class Meta:
        model = Adventurer
        fields = [
            'name',
            'sex',
            'birth_date',
            'grade_year',
            'school',
            'bolsa_familia',
            'invested_class',
            'document_type',
            'certificate_number',
            'rg_number',
            'rg_issuer',
            'cin_number',
            'cpf_number',
            'religion',
            'use_responsible_address',
            'address_line',
            'neighborhood',
            'city',
            'state',
            'cep',
            'tshirt_size',
        ]
        widgets = {'bolsa_familia': forms.RadioSelect(choices=[(False, 'Não'), (True, 'Sim')])}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['invested_class'] = forms.MultipleChoiceField(
            choices=Adventurer.CLASS_CHOICES,
            required=False,
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'invested-checkboxes'}),
            label='Classes investidas',
        )
        invested = []
        if self.instance and self.instance.invested_class:
            try:
                invested = json.loads(self.instance.invested_class)
            except Exception:
                invested = []
        self.fields['invested_class'].initial = invested
        self.fields['use_responsible_address'].widget.attrs['data-use-responsible'] = 'true'
        self.fields['photo_data'].widget.attrs['data-photo-target'] = 'true'
        self.fields['photo'].widget.attrs['data-photo-input'] = 'true'

    def clean(self):
        cleaned = super().clean()
        if self.save_draft:
            return cleaned
        doc_type = cleaned.get('document_type')
        if doc_type == 'certidao' and not cleaned.get('certificate_number'):
            self.add_error('certificate_number', 'Informe o número da certidão.')
        if doc_type == 'rg':
            if not cleaned.get('rg_number'):
                self.add_error('rg_number', 'Informe o número do RG.')
            if not cleaned.get('rg_issuer'):
                self.add_error('rg_issuer', 'Informe o órgão expedidor do RG.')
        if doc_type == 'cin' and not cleaned.get('cin_number'):
            self.add_error('cin_number', 'Informe o número do CIN.')
        if doc_type == 'cpf' and not cleaned.get('cpf_number'):
            self.add_error('cpf_number', 'Informe o CPF.')
        if not cleaned.get('tshirt_size'):
            self.add_error('tshirt_size', 'Selecione o tamanho da camiseta.')
        if not cleaned.get('photo_data'):
            self.add_error('photo_data', 'Envie a foto do aventureiro.')
        if not cleaned.get('signature_data'):
            self.add_error('signature_data', 'Assine no quadro para continuar.')
        invested = cleaned.get('invested_class') or []
        cleaned['invested_class'] = json.dumps(invested)
        self._check_duplicate_name(cleaned)
        return cleaned

    def _check_duplicate_name(self, cleaned):
        responsible = self.instance.responsible
        name = cleaned.get('name')
        birth_date = cleaned.get('birth_date')
        if not (responsible and name and birth_date):
            return
        duplicates = Adventurer.objects.filter(
            responsible=responsible,
            name__iexact=name.strip(),
            birth_date=birth_date,
        )
        if self.instance and self.instance.pk:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            self.add_error('name', 'Já existe um aventureiro com o mesmo nome e data de nascimento.')


class MedicalRecordForm(DraftModelForm):
    YES_NO_CHOICES = (
        ('true', 'Sim'),
        ('false', 'Não'),
    )
    signature_data = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = MedicalRecord
        exclude = ['adventurer', 'created_at', 'updated_at']

    def clean(self):
        cleaned = super().clean()
        if self.save_draft:
            return cleaned
        for field_name in ('has_health_plan', 'allergies', 'uses_medication'):
            value = cleaned.get(field_name)
            if value not in (True, False):
                self.add_error(field_name, 'Informe sim ou não.')
        if cleaned.get('has_health_plan') not in (True, False):
            self.add_error('has_health_plan', 'Informe se possui plano de saúde.')
        if cleaned.get('allergies') not in (True, False):
            self.add_error('allergies', 'Informe se possui alergias.')
        if cleaned.get('uses_medication') not in (True, False):
            self.add_error('uses_medication', 'Informe se usa medicamento.')
        if not cleaned.get('blood_type'):
            self.add_error('blood_type', 'Selecione o tipo sanguíneo.')
        if cleaned.get('hospitalizations') and not cleaned.get('hospitalizations_reason'):
            self.add_error('hospitalizations_reason', 'Informe o motivo da internação.')
        conditional_fields = [
            ('allergies', 'allergy_details', 'Descreva a alergia quando marcar "Sim".'),
            ('other_problems', 'other_problems_notes', 'Explique quais outros problemas de saúde existem.'),
            ('recent_problems', 'recent_problems_notes', 'Informe detalhes dos problemas recentes.'),
            ('medication_year', 'medication_year_notes', 'Informe a terapia ou medicamento usado no último ano.'),
            ('recent_fractures', 'recent_fractures_notes', 'Descreva a fratura recente.'),
            ('surgeries', 'surgeries_notes', 'Detalhe a cirurgia realizada.'),
        ]
        for flag_field, detail_field, message in conditional_fields:
            if cleaned.get(flag_field) and not cleaned.get(detail_field):
                self.add_error(detail_field, message)
        if not cleaned.get('declaration_accepted'):
            self.add_error('declaration_accepted', 'Confirme a declaração.')
        if not cleaned.get('signature_data'):
            self.add_error('signature_data', 'Assine a ficha médica.')
        return cleaned

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ('has_health_plan', 'allergies', 'uses_medication'):
            self.fields[field_name] = forms.TypedChoiceField(
                choices=self.YES_NO_CHOICES,
                coerce=lambda value: None if value in (None, '') else value == 'true',
                required=not self.save_draft,
                widget=forms.RadioSelect(attrs={'class': 'radio-group'}),
                label=self.fields[field_name].label,
            )


class ImageTermForm(DraftModelForm):
    signature_data = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = ImageReleaseTerm
        fields = ['agreed']

    def clean(self):
        cleaned = super().clean()
        if self.save_draft:
            return cleaned
        if not cleaned.get('agreed'):
            self.add_error('agreed', 'Confirme que leu e concorda com o termo.')
        if not cleaned.get('signature_data'):
            self.add_error('signature_data', 'Assine o termo para continuar.')
        return cleaned
