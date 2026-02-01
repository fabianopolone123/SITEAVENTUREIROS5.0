const state = {
  responsible: {
    saved: false,
    data: {},
    address: {},
    declaration: false,
    signature: null
  },
  adventurers: [],
  activeAdventurerId: null
};

let currentStep = 1;
let currentPhotoData = null;

const stepErrorSummary = document.getElementById('stepErrorSummary');
const progressButtons = document.querySelectorAll('.progress-step');
const wizardSteps = document.querySelectorAll('.wizard-step');
const responsibleForm = document.getElementById('responsibleForm');
const adventurerForm = document.getElementById('adventurerForm');
const medicalForm = document.getElementById('medicalForm');
const currentAdventurerLabel = document.getElementById('currentAdventurerLabel');
const medicalLabel = document.getElementById('medicalLabel');
const photoPreview = document.getElementById('photoPreview');
const pendingList = document.getElementById('pendingList');
const reviewAdventurers = document.getElementById('reviewAdventurers');
const reviewResponsible = document.querySelector('[data-review-type="responsible"]');
const finalizeButton = document.getElementById('finalizeButton');
const addAdventurerButton = document.getElementById('addAdventurer');
const termNextButton = document.querySelector('[data-next-step="7"]');
const step4NextButton = document.querySelector('[data-next-step="5"]');
const step5NextButton = document.querySelector('[data-next-step="6"]');
const step3NextButton = document.querySelector('[data-next-step="4"]');
const draftButton = document.querySelector('.draft-btn');
const signaturePads = {};

function initWizard() {
  setupSignaturePads();
  setupNavigation();
  setupFormListeners();
  updateDocumentFields();
  updateConditionals();
  updateAdventurerList();
  updateReviewPanel();
  updateProgress();
  updateStepAvailability();
  finalizeButton?.addEventListener('click', handleFinalize);
  addAdventurerButton?.addEventListener('click', () => {
    addNewAdventurer();
    goToStep(4);
  });
  draftButton?.addEventListener('click', () => {
    showTransientMessage('Rascunho salvo localmente.');
  });
}

function setupSignaturePads() {
  document.querySelectorAll('[data-signature]').forEach((canvas) => {
    const key = canvas.dataset.signature;
    signaturePads[key] = createSignaturePad(canvas);
  });
  document.querySelectorAll('[data-clear-signature]').forEach((button) => {
    const key = button.dataset.clearSignature;
    button.addEventListener('click', () => {
      signaturePads[key]?.clear();
    });
  });
}

function createSignaturePad(canvas) {
  const ctx = canvas.getContext('2d');
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';
  ctx.strokeStyle = '#1d4ed8';
  ctx.lineWidth = 3;
  let drawing = false;
  let hasStroke = false;

  const getPointer = (event) => {
    const rect = canvas.getBoundingClientRect();
    return {
      x: event.clientX - rect.left,
      y: event.clientY - rect.top
    };
  };

  const startStroke = (event) => {
    drawing = true;
    hasStroke = true;
    const { x, y } = getPointer(event);
    ctx.beginPath();
    ctx.moveTo(x, y);
  };

  const draw = (event) => {
    if (!drawing) return;
    const { x, y } = getPointer(event);
    ctx.lineTo(x, y);
    ctx.stroke();
  };

  const endStroke = () => {
    drawing = false;
  };

  canvas.addEventListener('pointerdown', startStroke);
  canvas.addEventListener('pointermove', draw);
  canvas.addEventListener('pointerup', endStroke);
  canvas.addEventListener('pointerleave', endStroke);
  canvas.addEventListener('contextmenu', (event) => event.preventDefault());

  return {
    hasStroke: () => hasStroke,
    toDataURL: () => canvas.toDataURL('image/png'),
    clear: () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      hasStroke = false;
    }
  };
}

function setupNavigation() {
  document.querySelectorAll('[data-next-step]').forEach((button) => {
    button.addEventListener('click', (event) => {
      if (button === termNextButton) return;
      const target = Number(button.dataset.nextStep);
      const from = Number(button.closest('.wizard-step').dataset.step);
      attemptStepMove(from, target);
    });
  });
  document.querySelectorAll('[data-prev-step]').forEach((button) => {
    button.addEventListener('click', () => {
      const target = Number(button.dataset.prevStep);
      goToStep(target);
    });
  });
  termNextButton?.addEventListener('click', (event) => {
    event.preventDefault();
    event.stopPropagation();
    clearStepErrors();
    if (!ensureActiveAdventurer()) return;
    const saved = saveTermData();
    if (saved) goToStep(7);
  });
}

function setupFormListeners() {
  responsibleForm?.addEventListener('submit', handleResponsibleSubmit);
  adventurerForm?.addEventListener('submit', handleAdventurerSubmit);
  medicalForm?.addEventListener('submit', handleMedicalSubmit);
  document.querySelectorAll('input[name="documentType"]').forEach((radio) => {
    radio.addEventListener('change', () => updateDocumentFields(radio.value));
  });
  adventurerForm?.querySelector('input[name="adventurerPhoto"]').addEventListener('change', handlePhotoUpload);
  adventurerForm?.querySelector('input[name="useResponsibleAddress"]').addEventListener('change', (event) => {
    applyResponsibleAddress(event.target.checked);
  });
  medicalForm?.addEventListener('change', () => updateConditionals(medicalForm));
  responsibleForm?.addEventListener('input', (event) => {
    if (event.target.name.startsWith('father') || event.target.name.startsWith('mother')) {
      applyLegalSelection();
    }
  });
  responsibleForm?.querySelectorAll('[data-auto-field]').forEach((field) => {
    field.addEventListener('input', () => {
      field.dataset.autoManual = 'true';
      field.closest('label')?.querySelector('.auto-tag')?.classList.remove('visible');
    });
  });
  applyLegalSelection();
}

function handleResponsibleSubmit(event) {
  event.preventDefault();
  clearStepErrors();
  clearFormErrors(responsibleForm);
  const requiredFields = [
    'fatherName', 'fatherCPF', 'fatherEmail', 'fatherPhone',
    'motherName', 'motherCPF', 'motherEmail', 'motherPhone',
    'legalName', 'legalRelation', 'legalCPF', 'legalEmail', 'legalPhone',
    'legalNationality', 'legalMarital', 'legalAddress', 'legalDistrict',
    'legalCity', 'legalState', 'legalCep'
  ];
  const errors = [];
  const formData = new FormData(responsibleForm);
  requiredFields.forEach((name) => {
    const value = formData.get(name)?.toString().trim();
    const field = responsibleForm.querySelector(`[name="${name}"]`);
    if (!value) {
      errors.push(`${field.dataset.label || 'Campo'} é obrigatório.`);
      setFieldError(field, 'Campo obrigatório');
    } else if (field?.dataset.type === 'cpf' && !validateCPF(value)) {
      errors.push(`${field.dataset.label || 'CPF'} inválido.`);
      setFieldError(field, 'CPF inválido');
    }
  });
  if (!formData.get('legalDeclaration')) {
    errors.push('A declaração deve ser confirmada.');
    const declaration = responsibleForm.querySelector('[name="legalDeclaration"]');
    declaration?.closest('label')?.querySelector('.error-message')?.textContent = 'Confirme a declaração.';
  }
  if (!signaturePads.responsible?.hasStroke()) {
    errors.push('Assinatura digital do responsável legal é obrigatória.');
  }
  if (errors.length) {
    showStepErrors(errors);
    return;
  }
  const fatherData = getParentValues('father');
  const motherData = getParentValues('mother');
  state.responsible.data = {
    ...Object.fromEntries(formData),
    father: fatherData,
    mother: motherData
  };
  state.responsible.address = {
    legalAddress: formData.get('legalAddress'),
    legalDistrict: formData.get('legalDistrict'),
    legalCity: formData.get('legalCity'),
    legalState: formData.get('legalState'),
    legalCep: formData.get('legalCep')
  };
  state.responsible.declaration = !!formData.get('legalDeclaration');
  state.responsible.signature = signaturePads.responsible.toDataURL();
  state.responsible.saved = true;
  clearStepErrors();
  updateTermFields();
  updateReviewPanel();
  goToStep(3);
}

function getParentValues(prefix) {
  const fields = ['Name', 'CPF', 'Email', 'Phone'];
  return fields.reduce((acc, suffix) => {
    const key = `${prefix}${suffix}`;
    const input = responsibleForm.querySelector(`[name="${key}"]`);
    acc[key] = input?.value?.trim() || '';
    return acc;
  }, {});
}

function handleAdventurerSubmit(event) {
  event.preventDefault();
  clearStepErrors();
  clearFormErrors(adventurerForm);
  if (!ensureActiveAdventurer()) return;
  const { valid, errors, values } = validateAdventurerForm();
  if (!valid) {
    showStepErrors(errors);
    return;
  }
  saveAdventurerData(values);
  updateAdventurerList();
  updateReviewPanel();
  updateStepAvailability();
}

function handleMedicalSubmit(event) {
  event.preventDefault();
  clearStepErrors();
  clearFormErrors(medicalForm);
  if (!ensureActiveAdventurer()) return;
  const { valid, errors, values } = validateMedicalForm();
  if (!valid) {
    showStepErrors(errors);
    return;
  }
  saveMedicalData(values);
  updateReviewPanel();
  updateStepAvailability();
}

function handlePhotoUpload(event) {
  const file = event.target.files?.[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = () => {
    currentPhotoData = reader.result;
    if (photoPreview) {
      photoPreview.src = reader.result;
      photoPreview.hidden = false;
    }
  };
  reader.readAsDataURL(file);
}

function attemptStepMove(from, target) {
  clearStepErrors();
  if (from === 3 && target === 4 && !ensureActiveAdventurer()) return;
  const active = getActiveAdventurer();
  if (from === 4 && target === 5 && (!active || !active.dataSaved)) {
    showStepErrors(['Salve os dados do aventureiro antes de avançar.']);
    return;
  }
  if (from === 5 && target === 6 && (!active || !active.medicalSaved)) {
    showStepErrors(['Salve a ficha médica antes de avançar.']);
    return;
  }
  goToStep(target);
}

function goToStep(step) {
  currentStep = step;
  wizardSteps.forEach((section) => {
    section.classList.toggle('active', Number(section.dataset.step) === step);
  });
  updateProgress();
  updateStepAvailability();
}

function updateProgress() {
  progressButtons.forEach((button) => {
    const step = Number(button.dataset.step);
    button.classList.toggle('active', step === currentStep);
    button.classList.toggle('completed', step < currentStep);
  });
}

function updateStepAvailability() {
  const active = getActiveAdventurer();
  if (active) {
    currentAdventurerLabel.textContent = `Aventureiro ativo: ${active.name}`;
    medicalLabel.textContent = `Ficha Médica – ${active.name}`;
  } else {
    currentAdventurerLabel.textContent = 'Selecione um aventureiro para preencher os dados.';
    medicalLabel.textContent = 'Selecione um aventureiro para registrar a ficha médica.';
  }
  const disable = !active;
  [...adventurerForm.querySelectorAll('input, select')].forEach((control) => {
    control.disabled = disable;
  });
  adventurerForm.querySelectorAll('button').forEach((button) => {
    if (button.dataset.nextStep === '5' || button.type === 'submit') {
      button.disabled = disable;
    }
  });
  medicalForm.querySelectorAll('input, select').forEach((control) => {
    control.disabled = disable;
  });
  medicalForm.querySelectorAll('button').forEach((button) => {
    if (button.dataset.nextStep === '6' || button.type === 'submit') {
      button.disabled = disable;
    }
  });
  if (step4NextButton) step4NextButton.disabled = !active || !active.dataSaved;
  if (step5NextButton) step5NextButton.disabled = !active || !active.medicalSaved;
}

function showStepErrors(errors) {
  if (!errors.length) {
    stepErrorSummary.textContent = '';
    return;
  }
  stepErrorSummary.innerHTML = `<ul>${errors.map((error) => `<li>${error}</li>`).join('')}</ul>`;
}

function clearStepErrors() {
  stepErrorSummary.textContent = '';
  stepErrorSummary.style.color = '';
}

function clearFormErrors(form) {
  form.querySelectorAll('.error-message').forEach((span) => {
    span.textContent = '';
  });
}

function setFieldError(field, message) {
  if (!field) return;
  const container = field.closest('label') || field.parentElement;
  const error = container?.querySelector('.error-message');
  if (error) error.textContent = message;
}

function updateDocumentFields(activeType) {
  const selected = activeType || document.querySelector('input[name="documentType"]:checked')?.value;
  document.querySelectorAll('.document-fields').forEach((block) => {
    block.hidden = block.dataset.doc !== selected;
  });
}

function updateConditionals(context) {
  const parent = context || document;
  parent.querySelectorAll('[data-show-when]').forEach((block) => {
    const [name, value] = block.dataset.showWhen.split(':');
    const control = document.querySelector(`[name="${name}"]`);
    block.hidden = control?.value !== value;
  });
}

function ensureActiveAdventurer() {
  if (!state.adventurers.length) {
    showStepErrors(['Adicione ao menos um aventureiro antes de prosseguir.']);
    return false;
  }
  if (!state.activeAdventurerId) {
    showStepErrors(['Selecione o aventureiro que deseja editar.']);
    return false;
  }
  return true;
}

function addNewAdventurer() {
  const id =
    window.crypto && window.crypto.randomUUID
      ? window.crypto.randomUUID()
      : `adv-${Date.now()}`;
  const number = state.adventurers.length + 1;
  const newAdventurer = {
    id,
    name: `Aventureiro ${number}`,
    data: {},
    dataSaved: false,
    medical: {},
    medicalSaved: false,
    term: {},
    termSaved: false,
    signatureData: null,
    medicalSignature: null,
    termSignature: null
  };
  state.adventurers.push(newAdventurer);
  state.activeAdventurerId = id;
  populateAdventurerForm();
  updateStepAvailability();
  updateAdventurerList();
}

function updateAdventurerList() {
  const list = document.getElementById('adventurerList');
  list.innerHTML = '';
  if (!state.adventurers.length) {
    list.innerHTML = '<p class="muted-text">Nenhum aventureiro cadastrado.</p>';
    return;
  }
  state.adventurers.forEach((adventurer) => {
    const card = document.createElement('article');
    card.className = 'adventurer-card';
    card.dataset.adventurerId = adventurer.id;
    card.innerHTML = `
      <div class="name-row">
        <strong>${adventurer.name}</strong>
        <button type="button" class="link-btn" data-edit-adventurer="${adventurer.id}">Editar</button>
      </div>
      <div class="status-dots">
        <span class="${adventurer.dataSaved ? 'complete' : ''}">Dados: ${adventurer.dataSaved ? '✅' : '⚠'}</span>
        <span class="${adventurer.medicalSaved ? 'complete' : ''}">Ficha médica: ${adventurer.medicalSaved ? '✅' : '⚠'}</span>
        <span class="${adventurer.termSaved ? 'complete' : ''}">Termo: ${adventurer.termSaved ? '✅' : '⚠'}</span>
      </div>
    `;
    list.appendChild(card);
  });
  list.querySelectorAll('[data-edit-adventurer]').forEach((button) => {
    button.addEventListener('click', () => {
      state.activeAdventurerId = button.dataset.editAdventurer;
      populateAdventurerForm();
      updateStepAvailability();
      goToStep(4);
    });
  });
}

function populateAdventurerForm() {
  const active = getActiveAdventurer();
  if (!active) {
    adventurerForm.reset();
    photoPreview.hidden = true;
    currentPhotoData = null;
    return;
  }
  const data = active.data;
  adventurerForm.querySelector('[name="adventurerName"]').value = data.name || '';
  adventurerForm.querySelector('[name="adventurerGender"]').value = data.gender || '';
  adventurerForm.querySelector('[name="adventurerDob"]').value = data.dob || '';
  adventurerForm.querySelector('[name="adventurerSeries"]').value = data.series || '';
  adventurerForm.querySelector('[name="adventurerSchool"]').value = data.school || '';
  adventurerForm.querySelector('[name="adventurerBolsa"]').value = data.bolsa || '';
  const classInput = adventurerForm.querySelector(`input[name="adventurerClass"][value="${data.classValue || 'abelhinhas'}"]`);
  if (classInput) classInput.checked = true;
  const docRadio = adventurerForm.querySelector(`input[name="documentType"][value="${data.documentType || 'certidao'}"]`);
  if (docRadio) docRadio.checked = true;
  updateDocumentFields(data.documentType || 'certidao');
  ['docCertidao', 'docRg', 'docRgOrg', 'docCin', 'docCpf'].forEach((name) => {
    const input = adventurerForm.querySelector(`[name="${name}"]`);
    if (input) input.value = data[name] || '';
  });
  adventurerForm.querySelector('[name="adventurerReligion"]').value = data.religion || '';
  ['adventurerAddress', 'adventurerDistrict', 'adventurerCity', 'adventurerState', 'adventurerCep'].forEach((name) => {
    const input = adventurerForm.querySelector(`[name="${name}"]`);
    if (input) input.value = data[name] || '';
  });
  adventurerForm.querySelector('[name="adventurerShirt"]').value = data.shirt || '';
  ['allergyFood', 'allergyFoodDetail', 'allergyMedicine', 'allergyMedicineDetail'].forEach((name) => {
    const input = adventurerForm.querySelector(`[name="${name}"]`);
    if (input) input.value = data[name] || '';
  });
  adventurerForm.querySelector('[name="useResponsibleAddress"]').checked = data.useResponsibleAddress || false;
  if (data.cropPhoto) {
    photoPreview.src = data.photo || data.cropPhoto;
    photoPreview.hidden = false;
  } else if (data.photo) {
    photoPreview.src = data.photo;
    photoPreview.hidden = false;
  } else {
    photoPreview.hidden = true;
  }
  currentPhotoData = data.photo || null;
}

function getActiveAdventurer() {
  return state.adventurers.find((adventurer) => adventurer.id === state.activeAdventurerId);
}

function showTransientMessage(message) {
  const previousColor = stepErrorSummary.style.color;
  stepErrorSummary.textContent = message;
  stepErrorSummary.style.color = 'var(--success-color)';
  setTimeout(() => {
    stepErrorSummary.textContent = '';
    stepErrorSummary.style.color = previousColor;
  }, 2600);
}

function applyLegalSelection() {
  const selection = responsibleForm.querySelector('input[name="legalPicker"]:checked')?.value || 'pai';
  const father = getParentValues('father');
  const mother = getParentValues('mother');
  const mapping = selection === 'pai' ? father : selection === 'mae' ? mother : null;
  const relationLabel = selection === 'pai' ? 'Pai' : selection === 'mae' ? 'Mãe' : '';
  const autoFields = [
    { name: 'legalName', value: mapping?.fatherName || mapping?.motherName || '' },
    { name: 'legalRelation', value: relationLabel },
    { name: 'legalCPF', value: mapping?.fatherCPF || mapping?.motherCPF || '' },
    { name: 'legalEmail', value: mapping?.fatherEmail || mapping?.motherEmail || '' },
    { name: 'legalPhone', value: mapping?.fatherPhone || mapping?.motherPhone || '' }
  ];
  autoFields.forEach(({ name, value }) => {
    const field = responsibleForm.querySelector(`[name="${name}"]`);
    if (!field) return;
    if (field.dataset.autoManual === 'true') return;
    field.value = selection === 'outro' ? '' : value;
    const autoTag = field.closest('label')?.querySelector('.auto-tag');
    field.dataset.autoManual = selection === 'outro' ? 'true' : 'false';
    if (selection === 'outro' || !value) {
      autoTag?.classList.remove('visible');
    } else if (value) {
      autoTag?.classList.add('visible');
    }
  });
}

function applyResponsibleAddress(checked) {
  if (!checked) {
    ['adventurerAddress', 'adventurerDistrict', 'adventurerCity', 'adventurerState', 'adventurerCep'].forEach((name) => {
      const input = adventurerForm.querySelector(`[name="${name}"]`);
      if (input) input.readOnly = false;
    });
    return;
  }
  const address = state.responsible.address;
  ['legalAddress', 'legalDistrict', 'legalCity', 'legalState', 'legalCep'].forEach((legalKey, index) => {
    const names = ['adventurerAddress', 'adventurerDistrict', 'adventurerCity', 'adventurerState', 'adventurerCep'];
    const target = adventurerForm.querySelector(`[name="${names[index]}"]`);
    if (target) {
      target.value = address[legalKey] || '';
      target.readOnly = true;
    }
  });
}

function validateAdventurerForm() {
  const errors = [];
  const values = {};
  const form = adventurerForm;
  const requiredFields = [
    'adventurerName', 'adventurerGender', 'adventurerDob', 'adventurerSeries',
    'adventurerSchool', 'adventurerBolsa', 'adventurerReligion', 'adventurerShirt'
  ];
  requiredFields.forEach((name) => {
    const input = form.querySelector(`[name="${name}"]`);
    if (input && !input.value.trim()) {
      errors.push(`${input.dataset.label || name} é obrigatório.`);
      setFieldError(input, 'Campo obrigatório');
    }
    values[name] = input?.value?.trim() || '';
  });
  const classChecked = form.querySelector('input[name="adventurerClass"]:checked');
  if (!classChecked) {
    errors.push('Selecione uma classe investida.');
    const groupError = form.querySelector('.radio-group + .field-note');
    if (groupError) groupError.textContent = 'Selecione uma opção';
  } else {
    values.classValue = classChecked.value;
  }
  const documentType = form.querySelector('input[name="documentType"]:checked')?.value || 'certidao';
  values.documentType = documentType;
  if (documentType === 'certidao') {
    const cert = form.querySelector('[name="docCertidao"]');
    if (!cert?.value.trim()) {
      errors.push('Informe o número da certidão.');
      setFieldError(cert, 'Campo obrigatório');
    }
    values.docCertidao = cert?.value?.trim() || '';
  }
  if (documentType === 'rg') {
    const rg = form.querySelector('[name="docRg"]');
    const rgOrg = form.querySelector('[name="docRgOrg"]');
    if (!rg?.value.trim()) {
      errors.push('Informe o número do RG.');
      setFieldError(rg, 'Campo obrigatório');
    }
    if (!rgOrg?.value.trim()) {
      errors.push('Informe o órgão expedidor do RG.');
      setFieldError(rgOrg, 'Campo obrigatório');
    }
    values.docRg = rg?.value?.trim() || '';
    values.docRgOrg = rgOrg?.value?.trim() || '';
  }
  if (documentType === 'cin') {
    const cin = form.querySelector('[name="docCin"]');
    if (!cin?.value.trim()) {
      errors.push('Informe o número do CIN.');
      setFieldError(cin, 'Campo obrigatório');
    }
    values.docCin = cin?.value?.trim() || '';
  }
  if (documentType === 'cpf') {
    const cpf = form.querySelector('[name="docCpf"]');
    if (!cpf?.value.trim()) {
      errors.push('Informe o CPF do aventureiro.');
      setFieldError(cpf, 'Campo obrigatório');
    } else if (!validateCPF(cpf.value)) {
      errors.push('CPF do aventureiro inválido.');
      setFieldError(cpf, 'CPF inválido');
    }
    values.docCpf = cpf?.value?.trim() || '';
  }
  ['adventurerAddress', 'adventurerDistrict', 'adventurerCity', 'adventurerState', 'adventurerCep'].forEach((name) => {
    const input = form.querySelector(`[name="${name}"]`);
    if (input && !input.value.trim()) {
      errors.push(`${input.dataset.label || name} é obrigatório.`);
      setFieldError(input, 'Campo obrigatório');
    }
    values[name] = input?.value?.trim() || '';
  });
  if (!currentPhotoData && !getActiveAdventurer()?.photo) {
    const photoInput = form.querySelector('[name="adventurerPhoto"]');
    errors.push('A foto do aventureiro é obrigatória.');
    setFieldError(photoInput, 'Envie uma foto');
  }
  const signature = signaturePads.adventurer;
  if (!signature?.hasStroke() && !getActiveAdventurer()?.signatureData) {
    errors.push('Assinatura do responsável pelo aventureiro é obrigatória.');
  }
  return { valid: errors.length === 0, errors, values };
}

function saveAdventurerData(values) {
  const active = getActiveAdventurer();
  if (!active) return;
  active.data = {
    ...values,
    name: values.adventurerName,
    photo: currentPhotoData || active.photo || '',
    classValue: values.classValue,
    documentType: values.documentType,
    documentNumber:
      values.documentType === 'rg'
        ? values.docRg
        : values.documentType === 'cin'
        ? values.docCin
        : values.documentType === 'cpf'
        ? values.docCpf
        : values.docCertidao,
    useResponsibleAddress: adventurerForm.querySelector('[name="useResponsibleAddress"]').checked
  };
  active.photo = active.data.photo;
  active.signatureData = signaturePads.adventurer.hasStroke()
    ? signaturePads.adventurer.toDataURL()
    : active.signatureData;
  active.dataSaved = true;
  currentPhotoData = null;
  adventurerForm.reset();
  photoPreview.hidden = true;
  applyLegalSelection();
}

function validateMedicalForm() {
  const errors = [];
  const values = {};
  const form = medicalForm;
  const requiredSelects = [
    'medicalPlan', 'bloodType', 'allergyFood', 'allergyMedicine', 'conditionChronic',
    'conditionOthers', 'conditionRecent', 'conditionMedYear', 'conditionFracture',
    'conditionSurgery', 'conditionHospital'
  ];
  requiredSelects.forEach((name) => {
    const select = form.querySelector(`[name="${name}"]`);
    if (select && !select.value) {
      errors.push(`${select.dataset.label || name} é obrigatório.`);
      setFieldError(select, 'Campo obrigatório');
    }
    values[name] = select?.value || '';
  });
  const planName = form.querySelector('[name="medicalPlanName"]');
  if (values.medicalPlan === 'sim' && !planName?.value.trim()) {
    errors.push('Informe o nome do plano de saúde.');
    setFieldError(planName, 'Campo obrigatório');
  }
  const conditionBlocks = [
    { toggle: 'allergyFood', detail: 'allergyFoodDetail' },
    { toggle: 'allergyMedicine', detail: 'allergyMedicineDetail' },
    { toggle: 'conditionChronic', detail: 'conditionMedication' },
    { toggle: 'conditionOthers', detail: 'conditionOthersDetail' },
    { toggle: 'conditionRecent', detail: 'conditionRecentDetail' },
    { toggle: 'conditionHospital', detail: 'conditionHospitalReason' }
  ];
  conditionBlocks.forEach(({ toggle, detail }) => {
    const select = form.querySelector(`[name="${toggle}"]`);
    const detailField = form.querySelector(`[name="${detail}"]`);
    if (select?.value === 'sim' && detailField && !detailField.value.trim()) {
      errors.push(`${detailField.dataset.label || detail} é obrigatório.`);
      setFieldError(detailField, 'Campo obrigatório');
    }
    values[detail] = detailField?.value.trim() || '';
  });
  values.medicalPlanName = planName?.value.trim() || '';
  values.medicalSus = form.querySelector('[name="medicalSus"]')?.value.trim() || '';
  values.diseases = Array.from(form.querySelectorAll('input[type="checkbox"]:checked')).map(
    (checkbox) => checkbox.value
  );
  const signature = signaturePads.medical;
  if (!signature?.hasStroke()) {
    errors.push('Assinatura da ficha médica é obrigatória.');
  }
  return { valid: errors.length === 0, errors, values };
}

function saveMedicalData(values) {
  const active = getActiveAdventurer();
  if (!active) return;
  active.medical = { ...values };
  active.medicalSignature = signaturePads.medical.hasStroke()
    ? signaturePads.medical.toDataURL()
    : active.medicalSignature;
  active.medicalSaved = true;
  medicalForm.reset();
  updateConditionals();
}

function saveTermData() {
  if (!state.responsible.saved) {
    showStepErrors(['Finalize os dados do responsável antes de finalizar o termo.']);
    return false;
  }
  const active = getActiveAdventurer();
  if (!active) {
    showStepErrors(['Selecione um aventureiro antes de fechar o termo.']);
    return false;
  }
  const agreement = document.querySelector('[name="termAgreement"]');
  if (!agreement?.checked) {
    showStepErrors(['Confirme que leu e concorda com o termo.']);
    return false;
  }
  const signature = signaturePads.term;
  if (!signature?.hasStroke()) {
    showStepErrors(['Assinatura do termo é obrigatória.']);
    return false;
  }
  active.term = {
    agreement: true,
    childName: active.data.name,
    responsibleName: state.responsible.data.legalName,
    responsibleCpf: state.responsible.data.legalCPF,
    responsibleId: state.responsible.data.legalId || ''
  };
  active.termSignature = signature.toDataURL();
  active.termSaved = true;
  updateReviewPanel();
  updateStepAvailability();
  return true;
}

function updateTermFields() {
  const active = getActiveAdventurer();
  const mapping = {
    childName: active?.data?.name || '',
    responsibleName: state.responsible.data.legalName || '',
    responsibleCpf: state.responsible.data.legalCPF || '',
    responsibleId: state.responsible.data.legalId || '',
    responsibleAddress: `${state.responsible.address.legalAddress || ''} ${state.responsible.address.legalDistrict || ''}`.trim(),
    municipality: state.responsible.address.legalCity || '',
    nationality: state.responsible.data.legalNationality || '',
    marital: state.responsible.data.legalMarital || '',
    phone: state.responsible.data.legalPhone || ''
  };
  document.querySelectorAll('[data-term-field]').forEach((input) => {
    const key = input.dataset.termField;
    input.value = mapping[key] || '—';
  });
}

function validateCPF(cpf) {
  const clean = cpf.replace(/[\.\-\s]/g, '');
  if (clean.length !== 11 || /^(.)(\1)*$/.test(clean)) return false;
  const digits = clean.split('').map(Number);
  const calc = (factor) => {
    return digits
      .slice(0, factor - 1)
      .reduce((sum, digit, index) => sum + digit * (factor - index), 0);
  };
  const firstCheck = (calc(10) * 10) % 11;
  const secondCheck = (calc(11) * 10) % 11;
  return firstCheck % 10 === digits[9] && secondCheck % 10 === digits[10];
}

function updateReviewPanel() {
  const { pending, canFinalize } = computePending();
  pendingList.innerHTML = pending.length
    ? pending.map((message) => `<li>${message}</li>`).join('')
    : '<li>Sem pendências.</li>';
  finalizeButton.disabled = !canFinalize;
  const responsibleComplete = state.responsible.saved && state.responsible.signature && state.responsible.declaration;
  reviewResponsible.innerHTML = responsibleComplete
    ? '<p>✅ Responsável completo</p>'
    : '<p>⚠ Responsável incompleto</p>';
  reviewAdventurers.innerHTML = '';
  if (!state.adventurers.length) {
    reviewAdventurers.innerHTML = '<p class="muted-text">Nenhum aventureiro registrado.</p>';
    return;
  }
  state.adventurers.forEach((adventurer) => {
    const card = document.createElement('div');
    card.className = 'review-card';
    card.innerHTML = `
      <strong>${adventurer.name}</strong>
      <div class="status-dots">
        <span class="${adventurer.dataSaved ? 'complete' : ''}">Dados: ${adventurer.dataSaved ? '✅' : '⚠'}</span>
        <span class="${adventurer.medicalSaved ? 'complete' : ''}">Ficha médica: ${adventurer.medicalSaved ? '✅' : '⚠'}</span>
        <span class="${adventurer.termSaved ? 'complete' : ''}">Termo: ${adventurer.termSaved ? '✅' : '⚠'}</span>
      </div>
    `;
    reviewAdventurers.appendChild(card);
  });
}

function computePending() {
  const pending = [];
  if (!state.responsible.saved) {
    pending.push('Responsável ainda não registrado.');
  } else {
    if (!state.responsible.declaration) pending.push('Declaração do responsável pendente.');
    if (!state.responsible.signature) pending.push('Assinatura do responsável ausente.');
  }
  if (!state.adventurers.length) {
    pending.push('Nenhum aventureiro cadastrado.');
  } else {
    state.adventurers.forEach((adventurer, index) => {
      const label = adventurer.name || `Aventureiro ${index + 1}`;
      if (!adventurer.dataSaved) pending.push(`${label}: dados iniciais incompletos.`);
      if (!adventurer.medicalSaved) pending.push(`${label}: ficha médica pendente.`);
      if (!adventurer.termSaved) pending.push(`${label}: termo de imagem pendente.`);
    });
  }
  return { pending, canFinalize: pending.length === 0 };
}

function handleFinalize() {
  if (finalizeButton.disabled) return;
  showTransientMessage('Cadastro finalizado (simulado).');
}

initWizard();
