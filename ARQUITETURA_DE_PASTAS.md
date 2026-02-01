# 📁 Arquitetura de Pastas do Projeto
## Organização Oficial do Código

Este documento define **ONDE cada coisa deve morar** no projeto.

⚠️ Qualquer código criado fora desta arquitetura **é considerado erro**  
⚠️ O Codex deve ler este arquivo antes de criar ou mover arquivos

---

## 🎯 Objetivo da Arquitetura
Garantir que:
- o projeto seja fácil de entender
- o diagnóstico não fique espalhado
- integrações não virem gambiarra
- o Codex não “invente” caminhos
- cada responsabilidade tenha um lugar claro

---

## 🧱 Visão Geral da Estrutura

/project-root
│
├── README.md
├── CONTRIBUTING.md
├── CHECKLIST_DEBUG.md
├── HISTORICO_DE_MUDANCAS.md
├── DIAGNOSTICO_AUTODIAGNOSTICAVEL.md
├── ARQUITETURA_DE_PASTAS.md
│
├── frontend/
├── backend/
├── infra/
├── docs/
└── scripts/


---

## 🖥️ FRONTEND (`/frontend`)
Tecnologia: **Next.js**

Responsável por:
- interface do usuário
- captura de eventos de diagnóstico
- interceptação de requisições
- geração de `session_id` e `trace_id`

### Estrutura padrão
frontend/
├── app/ # Rotas e páginas (Next App Router)
│ ├── (public)/
│ ├── (auth)/
│ ├── admin/
│ └── diagnostics/ # Tela de diagnóstico (admin)
│
├── components/
│ ├── ui/ # Componentes visuais puros
│ ├── forms/
│ └── layout/
│
├── diagnostics/ # ⭐ DIAGNÓSTICO (FRONT)
│ ├── session.ts # session_id
│ ├── trace.ts # trace_id
│ ├── logger.ts # envio de eventos
│ ├── interceptors.ts # fetch/XHR
│ └── mask.ts # mascaramento
│
├── services/
│ ├── api.ts # cliente HTTP
│ ├── auth.ts
│ └── payments.ts
│
├── hooks/
├── store/
├── utils/
└── styles/


### Regras importantes (Frontend)
- ❌ NÃO misturar lógica de diagnóstico com UI
- ✅ Tudo de diagnóstico fica em `frontend/diagnostics/`
- ✅ Toda ação importante gera `trace_id`
- ✅ Toda API passa `session_id` e `trace_id`

---

## 🧠 BACKEND (`/backend`)
Tecnologia: **Django + DRF**

Responsável por:
- regras de negócio
- APIs
- autenticação
- persistência
- correlação de eventos
- fila e webhooks

### Estrutura padrão
backend/
├── manage.py
├── config/ # settings, urls, wsgi, asgi
│
├── apps/
│ ├── accounts/ # usuários e permissões
│ ├── members/ # membros do clube
│ ├── documents/ # documentação interna
│ ├── store/ # lojinha interna
│ ├── payments/ # pagamentos
│ ├── notifications/ # WhatsApp / notificações
│ └── diagnostics/ # ⭐ DIAGNÓSTICO (BACK)
│
├── diagnostics/
│ ├── middleware.py # request_id
│ ├── models.py # diagnostic_events
│ ├── serializers.py
│ ├── views.py # /client-events, /stream
│ ├── services.py # gravação / mascaramento
│ └── retention.py # limpeza automática
│
├── integrations/
│ ├── mercadopago/
│ │ ├── client.py
│ │ ├── webhooks.py
│ │ └── mappers.py
│ ├── whatsapp/
│ │ ├── client.py
│ │ └── webhooks.py
│ └── base.py
│
├── workers/
│ ├── payments.py
│ ├── notifications.py
│ └── diagnostics.py
│
├── common/
│ ├── logging.py
│ ├── masks.py
│ ├── ids.py
│ └── exceptions.py
│
└── requirements/


---

## ⭐ DIAGNÓSTICO É UM MÓDULO, NÃO UM ADENDO

Regra crítica:
> Diagnóstico **NÃO** fica espalhado dentro de apps de negócio.

Tudo relacionado a:
- eventos
- logs
- SSE
- correlação
- retenção

fica **exclusivamente** em:
backend/diagnostics/
frontend/diagnostics/


---

## 🔌 INTEGRAÇÕES (`/backend/integrations`)
Responsável por:
- APIs externas
- webhooks
- adaptação de payloads

Regras:
- ❌ NÃO colocar regra de negócio aqui
- ❌ NÃO acessar models diretamente
- ✅ Apenas adaptar dados
- ✅ Emitir eventos de diagnóstico

---

## ⚙️ WORKERS (`/backend/workers`)
Responsável por:
- tarefas assíncronas
- retentativas
- jobs de longa duração

Regras:
- todo worker deve emitir:
  - worker.start
  - worker.success
  - worker.error
- sempre carregar `trace_id`

---

## 🏗️ INFRA (`/infra`)
Responsável por:
- Docker
- Nginx
- deploy
- serviços

infra/
├── docker/
├── nginx/
├── env/
└── deploy/


---

## 📄 DOCS (`/docs`)
Documentação auxiliar:
- fluxos
- diagramas
- decisões técnicas

docs/
├── diagrams/
├── decisions/
└── flows/


---

## 🧪 SCRIPTS (`/scripts`)
Scripts utilitários:
- manutenção
- limpeza
- migrações manuais
- debug emergencial

---

## 🚫 O QUE NÃO É PERMITIDO
- código solto na raiz
- lógica de diagnóstico dentro de apps de negócio
- integrações sem pasta própria
- workers misturados com views
- duplicação de lógica

---

## 🧭 Diretriz Final para o Codex
Antes de criar qualquer arquivo:
1. Ler este documento
2. Identificar a responsabilidade
3. Escolher a pasta correta
4. Criar o arquivo
5. Registrar a mudança em `HISTORICO_DE_MUDANCAS.md`

Se houver dúvida:
👉 **não criar arquivo novo** até esclarecer.

---

## 📌 Nota Final
Esta arquitetura existe para:
- escalar o projeto
- manter diagnóstico limpo
- evitar caos estrutural
- permitir que agentes sem memória se orientem

O código cresce.
A estrutura segura o crescimento.