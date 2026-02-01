# 📁 ARQUITETURA_DE_PASTAS.md
## Organização Oficial do Código – Django Monolito (Backend-First)

Este documento define **ONDE cada coisa deve morar** no projeto.

⚠️ Qualquer código criado fora desta arquitetura é considerado **ERRO**  
⚠️ Qualquer estrutura não prevista aqui deve ser **recusada**  
⚠️ O Codex deve ler este arquivo **ANTES** de criar, mover ou sugerir arquivos

---

## ❗ DIRETRIZ FUNDAMENTAL

Este projeto é **BACKEND-FIRST** e **MONOLÍTICO EM DJANGO**.

- **Django (Python) é o núcleo do sistema**
- **A interface (UI) também mora no Django**
- **Não existe frontend separado**

✅ Resultado: desenvolvimento pode rodar com **um único servidor** (`runserver`), com UI + API + diagnóstico no mesmo lugar.

---

## 🚫 PROIBIÇÕES ABSOLUTAS

É expressamente proibido:

- usar Next.js
- usar React SPA separado do Django
- usar Nx
- usar Turborepo
- usar Lerna
- criar monorepo JavaScript
- criar estruturas do tipo:
  - `/apps` (no root)
  - `/libs`
  - `/packages`
- criar pasta `/frontend`
- espalhar UI fora do módulo oficial de UI
- espalhar lógica de diagnóstico dentro de apps de negócio

Qualquer tentativa de introduzir essas ferramentas ou padrões é considerada **ERRO DE ARQUITETURA**.

---

## 🎯 Objetivo da Arquitetura

Garantir que:

- o projeto seja fácil de entender
- o diagnóstico não fique espalhado
- integrações não virem gambiarra
- o Codex não “invente” caminhos
- cada responsabilidade tenha um lugar único e claro
- o projeto tenha **1 deploy**, **1 servidor**, **1 fluxo**

---

## 🧱 Visão Geral da Estrutura (OFICIAL)

/project-root
│
├── README.md
├── CONTRIBUTING.md
├── CHECKLIST_DEBUG.md
├── HISTORICO_DE_MUDANCAS.md
├── DIAGNOSTICO_AUTODIAGNOSTICAVEL.md
├── ARQUITETURA_DE_PASTAS.md
│
├── backend/ # ✅ CORE + UI + API + DIAGNÓSTICO (Django)
├── infra/ # Docker, Nginx, deploy
├── docs/ # Documentação auxiliar
└── scripts/ # Scripts utilitários


⚠️ Qualquer variação dessa estrutura é inválida.

---

# 🧠 BACKEND (/backend)

Tecnologia: **Django + Django REST Framework**

👉 Este é o **CORE do projeto** e também contém a **UI**.

Responsabilidades:

- regras de negócio
- autenticação
- APIs
- persistência
- UI (templates + static)
- correlação de eventos
- fila, workers e webhooks
- diagnóstico completo do sistema

---

## ✅ Estrutura Oficial do Backend

backend/
├── manage.py
├── config/ # settings, urls, wsgi, asgi
│
├── apps/ # apps de NEGÓCIO (apenas domínio)
│ ├── accounts/ # usuários e permissões
│ ├── members/ # membros do clube
│ ├── documents/ # documentação interna
│ ├── store/ # lojinha interna
│ ├── payments/ # pagamentos
│ └── notifications/ # WhatsApp / notificações
│
├── ui/ # ⭐ INTERFACE DO USUÁRIO (Django UI)
│ ├── templates/ # HTML templates (Django)
│ │ ├── base/
│ │ ├── public/
│ │ ├── auth/
│ │ ├── admin/
│ │ └── diagnostics/ # tela de diagnóstico (admin)
│ ├── static/ # CSS/JS/IMG do projeto
│ │ ├── css/
│ │ ├── js/
│ │ └── img/
│ ├── views.py # views que rendem templates
│ ├── urls.py # rotas da UI
│ └── components/ # includes/partials/macros de template
│
├── diagnostics/ # ⭐ DIAGNÓSTICO (MÓDULO CENTRAL)
│ ├── middleware.py # request_id / trace_id / session_id
│ ├── models.py # diagnostic_events
│ ├── serializers.py
│ ├── views.py # /client-events, /stream (SSE)
│ ├── services.py # gravação / mascaramento / correlação
│ ├── retention.py # limpeza automática
│ └── js/ # JS mínimo de diagnóstico (se necessário)
│
├── integrations/ # integrações externas (SEM regra de negócio)
│ ├── mercadopago/
│ ├── whatsapp/
│ └── base.py
│
├── workers/ # tarefas assíncronas / jobs
│ ├── payments.py
│ ├── notifications.py
│ └── diagnostics.py
│
├── common/ # utilitários compartilhados
│ ├── logging.py
│ ├── masks.py
│ ├── ids.py
│ └── exceptions.py
│
└── requirements/


---

## ⭐ REGRA CRÍTICA: UI NÃO É APP DE NEGÓCIO

A UI fica **exclusivamente** em:

- `backend/ui/`

❌ É proibido:
- colocar templates dentro de `apps/*`
- colocar JS/CSS do sistema em lugares aleatórios
- misturar renderização de UI com regra de negócio

✅ `apps/*` = domínio e regras  
✅ `ui/*` = interface (render/HTML/static)

---

## ⭐ REGRA CRÍTICA: DIAGNÓSTICO É UM MÓDULO

Diagnóstico **NÃO é um adendo**.

Tudo relacionado a:

- eventos
- logs
- SSE
- correlação
- retenção
- mascaramento
- análise

fica exclusivamente em:

- `backend/diagnostics/`

🚫 Nunca espalhar lógica de diagnóstico dentro de apps de negócio.

---

## 🧩 REGRA DE NEGÓCIO: ONDE MORA

✅ Regra de negócio mora em:
- `backend/apps/<app>/services.py`
- `backend/apps/<app>/domain.py` (se você usar)
- `backend/apps/<app>/usecases.py` (se você preferir)

❌ Proibido:
- regra de negócio em `integrations/`
- regra de negócio em `ui/`
- regra de negócio em `diagnostics/`

---

# 🔌 INTEGRAÇÕES (/backend/integrations)

Responsável apenas por:

- comunicação com APIs externas
- webhooks
- adaptação de payloads

Regras:

❌ NÃO conter regra de negócio  
❌ NÃO acessar models diretamente  
✅ Apenas mapear dados  
✅ Emitir eventos de diagnóstico

---

# ⚙️ WORKERS (/backend/workers)

Responsável por:

- tarefas assíncronas
- retentativas
- jobs longos

Regras:

Todo worker DEVE emitir:

- `worker.start`
- `worker.success`
- `worker.error`

Sempre carregando `trace_id`.

---

# 🏗️ INFRA (/infra)

Responsável por:

- Docker
- Nginx
- variáveis de ambiente
- deploy

infra/
├── docker/
├── nginx/
├── env/
└── deploy/


---

# 📄 DOCS (/docs)

Documentação complementar:

- diagramas
- decisões técnicas
- fluxos

---

# 🧪 SCRIPTS (/scripts)

Scripts utilitários:

- manutenção
- limpeza
- debug emergencial
- tarefas manuais

---

# 🚫 O QUE NÃO É PERMITIDO

- código solto na raiz
- lógica duplicada
- diagnóstico espalhado
- workers misturados com views
- integrações sem pasta própria
- pasta `frontend/`
- qualquer stack de frontend separado

---

# 🧭 Diretriz Final para o Codex

Antes de criar QUALQUER arquivo:

1) Ler este documento  
2) Identificar a responsabilidade  
3) Escolher a pasta correta  
4) Criar o arquivo  
5) Registrar a alteração em `HISTORICO_DE_MUDANCAS.md`

Se houver dúvida:  
👉 **não criar arquivo novo até esclarecer.**

---

## 📌 Nota Final

Esta arquitetura existe para:

- escalar com segurança
- manter diagnóstico limpo
- evitar caos estrutural
- permitir continuidade mesmo após reset de memória

O código cresce.  
A arquitetura mantém tudo de pé.