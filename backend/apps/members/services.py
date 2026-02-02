from typing import Dict, List

from backend.apps.members.models import (
    Adventurer,
    ImageReleaseTerm,
    MedicalRecord,
    Responsible,
)

TERM_TEXT = """
Autorizo o uso da imagem para fins institucionais do Clube de Aventureiros Pinhal Júnior e entendo que as fotos podem ser utilizadas em materiais digitais e impressos sem ônus adicional, mesmo depois do evento, pelo tempo necessário à comunicação oficial.
"""


def get_session_key(session) -> str:
    if not session.session_key:
        session.save()
    return session.session_key


def get_or_create_responsible(session) -> Responsible:
    key = get_session_key(session)
    responsible = (
        Responsible.objects.filter(session_key=key, finalized=False)
        .order_by('-created_at')
        .first()
    )
    if not responsible:
        responsible = Responsible.objects.create(session_key=key)
    session['responsible_id'] = responsible.pk
    return responsible


def get_pending_items(responsible: Responsible) -> List[Dict[str, List[str]]]:
    pendings = []
    if not responsible.is_complete():
        pending = responsible.pending_fields()
        if pending:
            pendings.append({'section': 'Responsável', 'items': pending})
    for adventurer in responsible.adventurers.all():
        data_missing = adventurer.pending_fields()
        medical_missing = []
        term_missing = []
        try:
            medical_missing = adventurer.medical_record.pending_fields()
        except MedicalRecord.DoesNotExist:
            medical_missing = ['Ficha médica não iniciada']
        try:
            term_missing = adventurer.image_term.pending_fields()
        except ImageReleaseTerm.DoesNotExist:
            term_missing = ['Termo de uso de imagem não iniciado']
        if data_missing:
            pendings.append({'section': f'{adventurer.name} • Dados', 'items': data_missing})
        if medical_missing:
            pendings.append({'section': f'{adventurer.name} • Ficha médica', 'items': medical_missing})
        if term_missing:
            pendings.append({'section': f'{adventurer.name} • Termo de imagem', 'items': term_missing})
    return pendings


def get_status_payload(responsible: Responsible) -> Dict[str, str]:
    status = {'responsible': '⚠', 'adventurers': []}
    if responsible.is_complete():
        status['responsible'] = '✅'
    for adventurer in responsible.adventurers.all():
        data_flag = '✅' if adventurer.data_complete() else '⚠'
        try:
            medical_flag = '✅' if adventurer.medical_record.is_complete() else '⚠'
        except MedicalRecord.DoesNotExist:
            medical_flag = '⚠'
        try:
            term_flag = '✅' if adventurer.image_term.is_complete() else '⚠'
        except ImageReleaseTerm.DoesNotExist:
            term_flag = '⚠'
        status['adventurers'].append(
            {
                'name': adventurer.name,
                'data': data_flag,
                'medical': medical_flag,
                'term': term_flag,
                'pk': adventurer.pk,
            }
        )
    return status


def can_finalize(responsible: Responsible) -> bool:
    if not responsible.is_complete():
        return False
    for adventurer in responsible.adventurers.all():
        if not adventurer.data_complete():
            return False
        try:
            if not adventurer.medical_record.is_complete():
                return False
        except MedicalRecord.DoesNotExist:
            return False
        try:
            if not adventurer.image_term.is_complete():
                return False
        except ImageReleaseTerm.DoesNotExist:
            return False
    return True
