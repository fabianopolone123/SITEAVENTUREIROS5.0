from django import forms

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
            'declaration_accepted',
        ]
        widgets = {'declaration_accepted': forms.CheckboxInput()}


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
        return cleaned


class MedicalRecordForm(DraftModelForm):
    class Meta:
        model = MedicalRecord
        exclude = ['adventurer', 'created_at', 'updated_at']


class ImageTermForm(DraftModelForm):
    signature_data = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = ImageReleaseTerm
        fields = ['agreed']
