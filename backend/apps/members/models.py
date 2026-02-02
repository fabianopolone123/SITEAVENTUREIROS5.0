import json

from django.db import models
from django.utils import timezone


class Responsible(models.Model):
    LEGAL_TYPE_CHOICES = [
        ('pai', 'Pai'),
        ('mae', 'Mãe'),
        ('outro', 'Outro'),
    ]

    session_key = models.CharField(max_length=64, db_index=True)

    father_name = models.CharField('Nome do pai', max_length=150, blank=True)
    father_cpf = models.CharField('CPF do pai', max_length=20, blank=True)
    father_email = models.EmailField('E-mail do pai', blank=True)
    father_phone = models.CharField('Celular do pai', max_length=20, blank=True)

    mother_name = models.CharField('Nome da mãe', max_length=150, blank=True)
    mother_cpf = models.CharField('CPF da mãe', max_length=20, blank=True)
    mother_email = models.EmailField('E-mail da mãe', blank=True)
    mother_phone = models.CharField('Celular da mãe', max_length=20, blank=True)

    legal_type = models.CharField('Responsável legal', max_length=16, choices=LEGAL_TYPE_CHOICES, default='pai')
    legal_name = models.CharField('Nome do responsável legal', max_length=150, blank=True)
    legal_relationship = models.CharField('Grau de parentesco', max_length=80, blank=True)
    legal_cpf = models.CharField('CPF do responsável legal', max_length=20, blank=True)
    legal_email = models.EmailField('E-mail do responsável legal', blank=True)
    legal_phone = models.CharField('Celular do responsável legal', max_length=20, blank=True)
    nationality = models.CharField('Nacionalidade', max_length=80, blank=True)
    marital_status = models.CharField('Estado civil', max_length=80, blank=True)
    rg_or_cin = models.CharField('RG / CIN', max_length=50, blank=True)

    address_line = models.CharField('Endereço', max_length=200, blank=True)
    neighborhood = models.CharField('Bairro', max_length=120, blank=True)
    city = models.CharField('Cidade', max_length=120, blank=True)
    state = models.CharField('Estado (UF)', max_length=60, blank=True)
    cep = models.CharField('CEP', max_length=20, blank=True)

    declaration_accepted = models.BooleanField(default=False)
    signature_data = models.TextField(blank=True)
    signature_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    finalized = models.BooleanField(default=False)

    def mark_signed(self):
        if not self.signature_at:
            self.signature_at = timezone.now()

    def is_complete(self):
        required = [
            self.father_name,
            self.father_cpf,
            self.mother_name,
            self.mother_cpf,
            self.legal_name,
            self.legal_cpf,
            self.legal_phone,
            self.address_line,
            self.neighborhood,
            self.city,
            self.state,
            self.cep,
        ]
        return all(required) and self.declaration_accepted and self.signature_data

    def pending_fields(self):
        pending = []
        checks = [
            ('Pai', [self.father_name, self.father_cpf, self.father_email, self.father_phone]),
            ('Mãe', [self.mother_name, self.mother_cpf, self.mother_email, self.mother_phone]),
            ('Responsável legal', [self.legal_name, self.legal_cpf, self.legal_phone, self.legal_email, self.legal_relationship]),
            ('Endereço', [self.address_line, self.neighborhood, self.city, self.state, self.cep]),
        ]
        for label, values in checks:
            if not all(values):
                pending.append(f'{label} incompleto')
        if not self.declaration_accepted:
            pending.append('Declaração não assinada')
        if not self.signature_data:
            pending.append('Assinatura do responsável legal pendente')
        return pending

    def get_invested_classes(self):
        try:
            return json.loads(self.invested_class or '[]')
        except Exception:
            return []


class Adventurer(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    CLASS_CHOICES = [
        ('abelhinhas', 'Abelhinhas'),
        ('luminares', 'Luminares'),
        ('edificadores', 'Edificadores'),
        ('maos_ajudadoras', 'Mãos Ajudadoras'),
        ('nenhum', 'Nenhum'),
    ]

    DOCUMENT_CHOICES = [
        ('certidao', 'Certidão de nascimento'),
        ('rg', 'RG'),
        ('cin', 'CIN'),
        ('cpf', 'CPF'),
    ]

    TSHIRT_SIZES = [
        ('02', '02'),
        ('04', '04'),
        ('06', '06'),
        ('08', '08'),
        ('10', '10'),
        ('12', '12'),
        ('PP', 'PP'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
        ('GG', 'GG'),
    ]

    responsible = models.ForeignKey(
        Responsible,
        related_name='adventurers',
        on_delete=models.CASCADE,
    )
    name = models.CharField('Nome', max_length=150)
    sex = models.CharField('Sexo', max_length=2, choices=SEX_CHOICES)
    birth_date = models.DateField('Data de nascimento')
    grade_year = models.CharField('Série', max_length=50)
    school = models.CharField('Colégio', max_length=200)
    bolsa_familia = models.BooleanField('Beneficiário do Bolsa Família', default=False)
    invested_class = models.TextField('Classes investidas', blank=True, default='[]')
    document_type = models.CharField('Documento principal', max_length=20, choices=DOCUMENT_CHOICES)
    certificate_number = models.CharField('Número da certidão', max_length=80, blank=True)
    rg_number = models.CharField('Número do RG', max_length=80, blank=True)
    rg_issuer = models.CharField('Órgão expedidor', max_length=60, blank=True)
    cin_number = models.CharField('Número do CIN', max_length=80, blank=True)
    cpf_number = models.CharField('Número do CPF', max_length=20, blank=True)
    religion = models.CharField('Religião', max_length=80)
    use_responsible_address = models.BooleanField('Usar endereço do responsável', default=True)
    address_line = models.CharField('Endereço', max_length=200, blank=True)
    neighborhood = models.CharField('Bairro', max_length=120, blank=True)
    city = models.CharField('Cidade', max_length=120, blank=True)
    state = models.CharField('Estado', max_length=60, blank=True)
    cep = models.CharField('CEP', max_length=20, blank=True)
    tshirt_size = models.CharField('Tamanho da camiseta', max_length=4, choices=TSHIRT_SIZES)
    photo_data = models.TextField('Foto (base64)', blank=True)
    signature_data = models.TextField('Assinatura', blank=True)
    signature_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_signed(self):
        if not self.signature_at:
            self.signature_at = timezone.now()

    def data_complete(self):
        doc_check = {
            'certidao': self.certificate_number,
            'rg': self.rg_number and self.rg_issuer,
            'cin': self.cin_number,
            'cpf': self.cpf_number,
        }
        mandatory = [
            self.name,
            self.sex,
            self.birth_date,
            self.grade_year,
            self.school,
            self.religion,
            self.tshirt_size,
            self.document_type,
        ]
        if not all(mandatory):
            return False
        if not doc_check.get(self.document_type):
            return False
        if self.use_responsible_address:
            return self.responsible and all([
                self.responsible.address_line,
                self.responsible.neighborhood,
                self.responsible.city,
                self.responsible.state,
                self.responsible.cep,
            ]) and self.photography_ready()
        photo_and_signature = self.photography_ready()
        address_ready = all([self.address_line, self.neighborhood, self.city, self.state, self.cep])
        return address_ready and photo_and_signature

    def photography_ready(self):
        return bool(self.photo_data and self.signature_data)

    def pending_fields(self):
        missing = []
        if not self.name:
            missing.append('Nome do aventureiro')
        doc_needed = {
            'certidao': self.certificate_number,
            'rg': self.rg_number,
            'cin': self.cin_number,
            'cpf': self.cpf_number,
        }
        if not doc_needed.get(self.document_type):
            missing.append('Documento principal incompleto')
        if not self.photography_ready():
            missing.append('Foto ou assinatura pendente')
        if self.use_responsible_address:
            if not self.responsible or not all([
                    self.responsible.address_line,
                    self.responsible.neighborhood,
                    self.responsible.city,
                    self.responsible.state,
                    self.responsible.cep,
            ]):
                missing.append('Endereço do responsável faltando')
        else:
            if not all([self.address_line, self.neighborhood, self.city, self.state, self.cep]):
                missing.append('Endereço do aventureiro incompleto')
        return missing


class MedicalRecord(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('NAO_SABE', 'Não sabe'),
    ]

    adventurer = models.OneToOneField(
        Adventurer,
        on_delete=models.CASCADE,
        related_name='medical_record',
    )
    has_health_plan = models.BooleanField('Possui plano de saúde', null=True)
    health_plan = models.CharField('Nome do plano', max_length=150, blank=True)
    sus_number = models.CharField('Nº do SUS', max_length=80, blank=True)
    diseases = models.TextField('Doenças já tidas', blank=True)
    allergies = models.BooleanField('Possui alergias', null=True)
    allergy_details = models.TextField('Qual alergia', blank=True)
    conditions = models.TextField('Condições de saúde', blank=True)
    uses_medication = models.BooleanField('Usa medicamento', null=True)
    other_problems = models.BooleanField('Outros problemas', default=False)
    other_problems_notes = models.TextField('Detalhes de outros problemas', blank=True)
    recent_problems = models.BooleanField('Problemas recentes', default=False)
    recent_problems_notes = models.TextField('Detalhes de problemas recentes', blank=True)
    medication_year = models.BooleanField('Medicamentos no ano', default=False)
    medication_year_notes = models.TextField('Detalhes de medicamentos', blank=True)
    recent_fractures = models.BooleanField('Fraturas recentes', default=False)
    recent_fractures_notes = models.TextField('Detalhes de fraturas', blank=True)
    surgeries = models.BooleanField('Cirurgias', default=False)
    surgeries_notes = models.TextField('Detalhes de cirurgias', blank=True)
    hospitalizations = models.BooleanField('Internações', default=False)
    hospitalizations_reason = models.TextField('Motivo das internações', blank=True)
    blood_type = models.CharField('Tipo sanguíneo', max_length=10, choices=BLOOD_TYPES, blank=True)
    declaration_accepted = models.BooleanField(default=False)
    signature_data = models.TextField(blank=True)
    signature_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_signed(self):
        if not self.signature_at:
            self.signature_at = timezone.now()

    def is_complete(self):
        booleans_required = [
            self.has_health_plan in (True, False),
            self.allergies in (True, False),
            self.uses_medication in (True, False),
            self.blood_type,
            self.declaration_accepted,
            self.signature_data,
        ]
        if self.hospitalizations and not self.hospitalizations_reason:
            return False
        return all(booleans_required)

    def pending_fields(self):
        missing = []
        if self.has_health_plan is None:
            missing.append('Plano de saúde indefinido')
        if self.allergies is None:
            missing.append('Alergias não respondidas')
        if self.uses_medication is None:
            missing.append('Uso de medicamento não informado')
        if not self.blood_type:
            missing.append('Tipo sanguíneo ausente')
        if not self.declaration_accepted:
            missing.append('Declaração médica não assinada')
        if not self.signature_data:
            missing.append('Assinatura médica pendente')
        if self.hospitalizations and not self.hospitalizations_reason:
            missing.append('Motivo da internação obrigatório')
        return missing


class ImageReleaseTerm(models.Model):
    adventurer = models.OneToOneField(
        Adventurer,
        on_delete=models.CASCADE,
        related_name='image_term',
    )
    responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    agreed = models.BooleanField(default=False)
    signature_data = models.TextField(blank=True)
    signature_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def mark_signed(self):
        if not self.signature_at:
            self.signature_at = timezone.now()

    def is_complete(self):
        return self.agreed and bool(self.signature_data)

    def pending_fields(self):
        missing = []
        if not self.agreed:
            missing.append('Termo não confirmado')
        if not self.signature_data:
            missing.append('Assinatura do termo pendente')
        return missing
