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
        return cleaned


class MedicalRecordForm(DraftModelForm):
    class Meta:
        model = MedicalRecord
        exclude = ['adventurer', 'created_at', 'updated_at']

    def clean(self):
        cleaned = super().clean()
        if self.save_draft:
            return cleaned
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
        if not cleaned.get('declaration_accepted'):
            self.add_error('declaration_accepted', 'Confirme a declaração.')
        if not cleaned.get('signature_data'):
            self.add_error('signature_data', 'Assine a ficha médica.')
        return cleaned


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
