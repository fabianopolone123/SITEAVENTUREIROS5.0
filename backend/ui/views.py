from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from backend.apps.members.models import Adventurer, ImageReleaseTerm, MedicalRecord, Responsible
from backend.apps.members.services import (
    TERM_TEXT,
    can_finalize,
    get_or_create_responsible,
    get_pending_items,
    get_status_payload,
)
from backend.ui.forms.cadastro import (
    AdventurerForm,
    ImageTermForm,
    MedicalRecordForm,
    ResponsibleForm,
)

WIZARD_STEPS = [
    ('tipo', 'Escolha do cadastro'),
    ('responsavel', 'Dados do responsável'),
    ('lista', 'Lista de aventureiros'),
    ('dados', 'Dados do aventureiro'),
    ('ficha', 'Ficha médica'),
    ('termo', 'Termo de imagem'),
    ('revisao', 'Revisão final'),
]


def get_responsible_for_user(user):
    if not user or not user.is_authenticated:
        return None
    return Responsible.objects.filter(user=user).order_by('-created_at').first()


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bem-vindo de volta! Agora você pode continuar a gestão dos cadastros.')
            responsible = get_responsible_for_user(user)
            if responsible:
                return redirect('dashboard-responsavel')
            return redirect('dashboard-gen')
        messages.error(request, 'Credenciais inválidas. Verifique usuário e senha.')
    return render(request, 'login.html')


@login_required
def dashboard_responsavel(request):
    responsible = get_responsible_for_user(request.user)
    if not responsible:
        messages.info(request, 'Ainda não há dados de responsável vinculados a este usuário.')
        return redirect('dashboard-gen')

    selected = request.GET.get('selected', 'responsavel')
    adventurer_id = request.GET.get('adventurer_id')
    selected_person = 'responsavel'
    if selected == 'adventurer' and adventurer_id:
        exists = responsible.adventurers.filter(pk=adventurer_id).exists()
        if exists:
            selected_person = f'adventurer-{adventurer_id}'

    adventurer_profiles = []
    for adventurer in responsible.adventurers.all():
        try:
            medical = adventurer.medical_record
        except MedicalRecord.DoesNotExist:
            medical = None
        try:
            term = adventurer.image_term
        except ImageReleaseTerm.DoesNotExist:
            term = None
        adventurer_profiles.append({
            'adventurer': adventurer,
            'key': f'adventurer-{adventurer.pk}',
            'medical_status': 'Completa' if medical and medical.is_complete() else 'Incompleta' if medical else 'Pendente',
            'medical_class': 'success' if medical and medical.is_complete() else 'warning',
            'medical_pending': medical.pending_fields() if medical else [],
            'term_status': 'Assinado' if term and term.is_complete() else 'Pendente',
            'term_class': 'success' if term and term.is_complete() else 'warning',
            'term_pending': term.pending_fields() if term else [],
        })

    status_payload = get_status_payload(responsible)
    pendings = get_pending_items(responsible)
    welcome_name = responsible.legal_name or responsible.legal_type.title() or 'Responsável'

    context = {
        'responsible': responsible,
        'adventurer_profiles': adventurer_profiles,
        'status': status_payload,
        'pendings': pendings,
        'selected_person': selected_person,
        'welcome_name': welcome_name,
    }
    return render(request, 'dashboard/responsavel.html', context)


@login_required
def dashboard_generic(request):
    return render(request, 'dashboard/generic.html', {'user': request.user})


def wizard_context(request, responsible, current_step, extra=None):
    current_index = next(
        (index for index, step in enumerate(WIZARD_STEPS) if step[0] == current_step),
        0,
    )
    status_payload = get_status_payload(responsible)
    status_map = {adv['pk']: adv for adv in status_payload.get('adventurers', [])}
    context = {
        'steps': WIZARD_STEPS,
        'current_step': current_step,
        'current_index': current_index,
        'status': status_payload,
        'adventurer_status': status_map,
        'pendings': get_pending_items(responsible),
        'responsible': responsible,
    }
    if extra:
        context.update(extra)
    return context


def cadastro_tipo(request):
    responsible = get_or_create_responsible(request)
    return render(
        request,
        'cadastro_aventureiro/tipo.html',
        wizard_context(request, responsible, 'tipo'),
    )


def cadastro_responsavel(request):
    responsible = get_or_create_responsible(request)
    action = request.POST.get('action')
    save_draft = action == 'save_draft'
    form = ResponsibleForm(
        request.POST or None,
        instance=responsible,
        save_draft=save_draft,
    )
    if request.method == 'POST' and form.is_valid():
        responsible = form.save(commit=False)
        signature = form.cleaned_data.get('signature_data')
        if signature:
            responsible.signature_data = signature
            responsible.mark_signed()
        responsible.save()
        if action != 'save_draft':
            return redirect('cadastro-aventureiro-lista')
    return render(
        request,
        'cadastro_aventureiro/responsavel.html',
        wizard_context(
            request,
            responsible,
            'responsavel',
            {'form': form, 'form_errors': form.errors},
        ),
    )


def cadastro_lista_aventureiros(request):
    responsible = get_or_create_responsible(request)
    context = wizard_context(request, responsible, 'lista')
    status_map = context.get('adventurer_status', {})
    adventurers_data = []
    for adventurer in responsible.adventurers.all():
        status = status_map.get(adventurer.pk, {'data': '⚠', 'medical': '⚠', 'term': '⚠'})
        adventurers_data.append({'instance': adventurer, 'status': status})
    context['adventurers'] = adventurers_data
    return render(request, 'cadastro_aventureiro/lista.html', context)


def cadastro_dados_aventureiro(request, pk=None):
    responsible = get_or_create_responsible(request)
    if pk:
        adventurer = get_object_or_404(Adventurer, pk=pk, responsible=responsible)
    else:
        adventurer = Adventurer(responsible=responsible)
    action = request.POST.get('action')
    save_draft = action == 'save_draft'
    form = AdventurerForm(
        request.POST or None,
        request.FILES or None,
        instance=adventurer,
        save_draft=save_draft,
    )
    if request.method == 'POST' and form.is_valid():
        adventurer = form.save(commit=False)
        adventurer.responsible = responsible
        photo_data = form.cleaned_data.get('photo_data')
        if photo_data:
            adventurer.photo_data = photo_data
        signature = form.cleaned_data.get('signature_data')
        if signature:
            adventurer.signature_data = signature
            adventurer.mark_signed()
        if adventurer.use_responsible_address:
            for field in ['address_line', 'neighborhood', 'city', 'state', 'cep']:
                setattr(adventurer, field, getattr(responsible, field))
        adventurer.save()
        if action != 'save_draft':
            return redirect('cadastro-aventureiro-ficha', pk=adventurer.pk)
    context = wizard_context(
        request,
        responsible,
        'dados',
        {
            'form': form,
            'adventurer': adventurer,
            'form_errors': form.errors,
        },
    )
    return render(request, 'cadastro_aventureiro/dados.html', context)


def cadastro_ficha_medica(request, pk):
    responsible = get_or_create_responsible(request)
    adventurer = get_object_or_404(Adventurer, pk=pk, responsible=responsible)
    medical, _ = MedicalRecord.objects.get_or_create(adventurer=adventurer)
    action = request.POST.get('action')
    save_draft = action == 'save_draft'
    form = MedicalRecordForm(
        request.POST or None,
        instance=medical,
        save_draft=save_draft,
    )
    if request.method == 'POST' and form.is_valid():
        medical = form.save()
        if medical.signature_data:
            medical.mark_signed()
            medical.save()
        if action != 'save_draft':
            return redirect('cadastro-aventureiro-termo', pk=adventurer.pk)
    disease_fields = [form[field] for field in [
        'pneumonia',
        'sarampo',
        'tetano',
        'catapora',
        'meningite',
        'hepatite',
        'dengue',
        'febre_amarela',
        'h1n1',
        'colera',
        'rubelola',
        'coqueluche',
        'difteria',
        'caxumba',
        'rinite',
        'bronquite',
        'malaria',
        'variola',
    ]]
    history_fields = [form[field] for field in [
        'other_problems',
        'other_problems_notes',
        'recent_problems',
        'recent_problems_notes',
        'medication_year',
        'medication_year_notes',
        'recent_fractures',
        'recent_fractures_notes',
        'surgeries',
        'surgeries_notes',
        'hospitalizations',
        'hospitalizations_reason',
    ]]
    context = wizard_context(
        request,
        responsible,
        'ficha',
        {
            'form': form,
            'adventurer': adventurer,
            'form_errors': form.errors,
            'disease_fields': disease_fields,
            'history_fields': history_fields,
        },
    )
    return render(request, 'cadastro_aventureiro/ficha.html', context)


def cadastro_termo_imagem(request, pk):
    responsible = get_or_create_responsible(request)
    adventurer = get_object_or_404(Adventurer, pk=pk, responsible=responsible)
    term, _ = ImageReleaseTerm.objects.get_or_create(
        adventurer=adventurer,
        defaults={'responsible': responsible},
    )
    action = request.POST.get('action')
    save_draft = action == 'save_draft'
    form = ImageTermForm(
        request.POST or None,
        instance=term,
        save_draft=save_draft,
    )
    if request.method == 'POST' and form.is_valid():
        term = form.save(commit=False)
        term.responsible = responsible
        signature = form.cleaned_data.get('signature_data')
        if signature:
            term.signature_data = signature
            term.mark_signed()
        term.save()
        if action != 'save_draft':
            return redirect('cadastro-aventureiro-revisao')
    context = wizard_context(
        request,
        responsible,
        'termo',
        {
            'form': form,
            'adventurer': adventurer,
            'term_text': TERM_TEXT,
            'form_errors': form.errors,
        },
    )
    return render(request, 'cadastro_aventureiro/termo.html', context)


def cadastro_revisao(request):
    responsible = get_or_create_responsible(request)
    if request.method == 'POST' and request.POST.get('action') == 'finalizar':
        if can_finalize(responsible):
            responsible.finalized = True
            responsible.save()
            request.session.pop('responsible_id', None)
            messages.success(
                request,
                'Cadastro concluído com sucesso! Faça login para continuar.',
            )
            return redirect('login')
    context = wizard_context(
        request,
        responsible,
        'revisao',
        {
            'can_finalize': can_finalize(responsible),
        },
    )
    return render(request, 'cadastro_aventureiro/revisao.html', context)
