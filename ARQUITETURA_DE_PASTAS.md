📁 Arquitetura de Pastas do Projeto
Organização Oficial do Código – Backend-First

Este documento define ONDE cada coisa deve morar no projeto.

⚠️ Qualquer código criado fora desta arquitetura é considerado ERRO
⚠️ Qualquer estrutura não prevista aqui deve ser recusada
⚠️ O Codex deve ler este arquivo ANTES de criar, mover ou sugerir arquivos

❗ DIRETRIZ FUNDAMENTAL

Este projeto é BACKEND-FIRST.

O Django (Python) é o núcleo do sistema

O frontend é apenas um cliente de interface

A arquitetura NÃO é decidida pelo frontend

🚫 PROIBIÇÕES ABSOLUTAS

É expressamente proibido:

usar Nx

usar Turborepo

usar Lerna

criar monorepo JavaScript

criar estruturas do tipo:

/apps

/libs

/packages

misturar código Python dentro de estruturas JavaScript

Qualquer tentativa de introduzir essas ferramentas ou padrões é considerada
ERRO DE ARQUITETURA.

🎯 Objetivo da Arquitetura

Garantir que:

o projeto seja fácil de entender

o diagnóstico não fique espalhado

integrações não virem gambiarra

o Codex não “invente” caminhos

cada responsabilidade tenha um lugar único e claro

🧱 Visão Geral da Estrutura
/project-root
│
├── README.md
├── CONTRIBUTING.md
├── CHECKLIST_DEBUG.md
├── HISTORICO_DE_MUDANCAS.md
├── DIAGNOSTICO_AUTODIAGNOSTICAVEL.md
├── ARQUITETURA_DE_PASTAS.md
│
├── backend/        # CORE DO SISTEMA (Django)
├── frontend/       # Interface (Next.js)
├── infra/          # Docker, Nginx, deploy
├── docs/           # Documentação auxiliar
└── scripts/        # Scripts utilitários


Qualquer variação dessa estrutura é inválida.

🖥️ FRONTEND (/frontend)

Tecnologia: Next.js (React – App Router)

Responsabilidades

interface do usuário

captura de eventos de diagnóstico

interceptação de requisições

geração de session_id e trace_id

Estrutura Oficial
frontend/
├── app/                    # Rotas e páginas
│   ├── (public)/
│   ├── (auth)/
│   ├── admin/
│   └── diagnostics/        # Tela de diagnóstico (admin)
│
├── components/
│   ├── ui/                 # Componentes visuais puros
│   ├── forms/
│   └── layout/
│
├── diagnostics/            # ⭐ DIAGNÓSTICO (FRONT)
│   ├── session.ts          # session_id
│   ├── trace.ts            # trace_id
│   ├── logger.ts           # envio de eventos
│   ├── interceptors.ts     # fetch / XHR
│   └── mask.ts             # mascaramento
│
├── services/
│   ├── api.ts
│   ├── auth.ts
│   └── payments.ts
│
├── hooks/
├── store/
├── utils/
└── styles/

Regras Críticas (Frontend)

❌ NÃO conter regra de negócio

❌ NÃO decidir arquitetura

❌ NÃO misturar UI com diagnóstico

✅ Todo diagnóstico fica em frontend/diagnostics/

✅ Toda ação relevante gera trace_id

✅ Toda API propaga session_id e trace_id

🧠 BACKEND (/backend)

Tecnologia: Django + Django REST Framework

👉 Este é o CORE do projeto

Responsabilidades

regras de negócio

autenticação

APIs

persistência

correlação de eventos

fila, workers e webhooks

Estrutura Oficial
backend/
├── manage.py
├── config/                 # settings, urls, wsgi, asgi
│
├── apps/
│   ├── accounts/           # usuários e permissões
│   ├── members/            # membros do clube
│   ├── documents/          # documentação interna
│   ├── store/              # lojinha interna
│   ├── payments/           # pagamentos
│   ├── notifications/      # WhatsApp / notificações
│   └── diagnostics/        # ⭐ APP DE DIAGNÓSTICO
│
├── diagnostics/             # ⭐ IMPLEMENTAÇÃO DO DIAGNÓSTICO
│   ├── middleware.py        # request_id
│   ├── models.py            # diagnostic_events
│   ├── serializers.py
│   ├── views.py             # /client-events, /stream
│   ├── services.py          # gravação / mascaramento
│   └── retention.py         # limpeza automática
│
├── integrations/
│   ├── mercadopago/
│   ├── whatsapp/
│   └── base.py
│
├── workers/
│   ├── payments.py
│   ├── notifications.py
│   └── diagnostics.py
│
├── common/
│   ├── logging.py
│   ├── masks.py
│   ├── ids.py
│   └── exceptions.py
│
└── requirements/

⭐ REGRA CRÍTICA: DIAGNÓSTICO É UM MÓDULO

Diagnóstico NÃO é um adendo.

Tudo relacionado a:

eventos

logs

SSE

correlação

retenção

análise

fica exclusivamente em:

backend/diagnostics/
frontend/diagnostics/


🚫 Nunca espalhar lógica de diagnóstico dentro de apps de negócio.

🔌 INTEGRAÇÕES (/backend/integrations)

Responsável apenas por:

comunicação com APIs externas

webhooks

adaptação de payloads

Regras

❌ NÃO conter regra de negócio

❌ NÃO acessar models diretamente

✅ Apenas mapear dados

✅ Emitir eventos de diagnóstico

⚙️ WORKERS (/backend/workers)

Responsável por:

tarefas assíncronas

retentativas

jobs longos

Regras

Todo worker DEVE emitir:

worker.start

worker.success

worker.error

Sempre carregando trace_id.

🏗️ INFRA (/infra)

Responsável por:

Docker

Nginx

variáveis de ambiente

deploy

infra/
├── docker/
├── nginx/
├── env/
└── deploy/

📄 DOCS (/docs)

Documentação complementar:

diagramas

decisões técnicas

fluxos

🧪 SCRIPTS (/scripts)

Scripts utilitários:

manutenção

limpeza

debug emergencial

tarefas manuais

🚫 O QUE NÃO É PERMITIDO

código solto na raiz

lógica duplicada

diagnóstico espalhado

workers misturados com views

integrações sem pasta própria

estruturas monorepo JS

uso de Nx sob qualquer forma

🧭 Diretriz Final para o Codex

Antes de criar QUALQUER arquivo:

Ler este documento

Identificar a responsabilidade

Escolher a pasta correta

Criar o arquivo

Registrar a alteração em HISTORICO_DE_MUDANCAS.md

Se houver dúvida:
👉 não criar arquivo novo até esclarecer.

📌 Nota Final

Esta arquitetura existe para:

escalar com segurança

manter diagnóstico limpo

evitar caos estrutural

permitir continuidade mesmo após reset de memória

O código cresce.
A arquitetura mantém tudo de pé.