from django import forms

from backend.apps.members.models import Adventurer, Responsible


class PanelResponsibleForm(forms.ModelForm):
    declaration_accepted = forms.TypedChoiceField(
        choices=((True, 'Sim'), (False, 'Não')),
        coerce=lambda value: value == 'True' or value is True,
        required=False,
    )

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
            'legal_name',
            'legal_relationship',
            'legal_cpf',
            'legal_email',
            'legal_phone',
            'nationality',
            'marital_status',
            'rg_or_cin',
            'address_line',
            'address_number',
            'neighborhood',
            'city',
            'state',
            'cep',
            'declaration_accepted',
        ]


class PanelAdventurerForm(forms.ModelForm):
    use_responsible_address = forms.TypedChoiceField(
        choices=((True, 'Sim'), (False, 'Não')),
        coerce=lambda value: value == 'True' or value is True,
        required=False,
    )

    class Meta:
        model = Adventurer
        fields = [
            'name',
            'sex',
            'birth_date',
            'grade_year',
            'school',
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
        ]
