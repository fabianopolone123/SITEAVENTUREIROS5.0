from django import forms
from django.utils import timezone
import json

from backend.apps.members.models import Adventurer, ImageReleaseTerm, MedicalRecord, Responsible


class DraftModelForm(forms.ModelForm):
    def __init__(self, *args, save_draft=False, **kwargs):
        self.save_draft = save_draft
        super().__init__(*args, **kwargs)
        if save_draft:
            for field in self.fields.values():
                field.required = False


class ResponsibleForm(DraftModelForm):
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
        return cleaned


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
        return cleaned


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
