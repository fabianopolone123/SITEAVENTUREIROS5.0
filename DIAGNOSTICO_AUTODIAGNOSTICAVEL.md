# 📊 Sistema Autodiagnosticável – Arquitetura e Diretrizes

## 🎯 Objetivo do Projeto
Este projeto é um **sistema web para controle de um clube de escotismo**, com:
- usuários cadastrados
- documentação interna
- lojinha interna
- pagamentos automáticos
- comunicação automática via WhatsApp
- painel administrativo

O **diferencial principal** do sistema é ser **AUTODIAGNOSTICÁVEL**:
> O próprio sistema deve registrar, correlacionar e exibir tudo o que acontece, permitindo diagnosticar bugs como:
> - “botão não faz nada”
> - erro silencioso no frontend
> - falha de integração (pagamento, WhatsApp)
> - erro de backend ou fila
> sem depender de achismo.

Este documento é a **fonte da verdade** da arquitetura e deve ser lido por humanos e pelo Codex.

---

## 🧠 Conceito Central: Autodiagnóstico
Autodiagnóstico = **rastro completo de evidências**, do clique do usuário até o backend.

O sistema registra:
- ações do usuário (cliques)
- erros de JavaScript
- chamadas de rede
- respostas do backend
- exceções no servidor
- jobs de fila
- webhooks externos

Tudo isso é **correlacionado por IDs** e exibido em uma **tela de diagnóstico interna**.

---

## 🧱 Tecnologias Utilizadas

### Frontend
- **Next.js (React)**
  - Facilita instrumentação de erros
  - Intercepta fetch/XHR
  - Captura erros de renderização
  - Excelente para diagnóstico de UI

### Backend
- **Python**
- **Django**
- **Django REST Framework (DRF)**

### Banco de Dados
- **PostgreSQL**
  - usado para dados do sistema
  - usado também para armazenar eventos de diagnóstico

### Fila / Assíncrono
- **Redis**
- **Celery**
  - processamento de webhooks
  - envio de WhatsApp
  - tarefas demoradas
  - retentativas

### Infraestrutura
- **Ubuntu Server (VPS)**
- **Docker**
- **Nginx**

### Observabilidade (complementar)
- **Sentry** (frontend e backend)
  - stack traces
  - agrupamento de erros
- Sistema interno de diagnóstico (principal fonte)

---

## 🆔 Sistema de Identificação (Correlação)

O sistema usa **3 IDs fundamentais**:

### 1️⃣ session_id (Frontend)
- Identifica a sessão do navegador
- Gerado no front
- Persistido em cookie ou localStorage

### 2️⃣ trace_id (Frontend)
- Identifica uma **ação do usuário**
- Gerado quando o usuário clica em algo importante
- Ex.: salvar cadastro, pagar, enviar mensagem

### 3️⃣ request_id (Backend)
- Gerado no backend para cada request HTTP
- Retornado no header da resposta (`X-Request-ID`)

### Regra de Ouro
Todos os logs e eventos devem conter **pelo menos um** desses IDs  
Idealmente: `session_id + trace_id + request_id`

---

## 🗃️ Modelo Central: diagnostic_events

### Tabela: `diagnostic_events`

Essa tabela é o **coração do sistema autodiagnosticável**.

#### Campos
- `id`
- `ts` (timestamp)
- `level` → debug | info | warn | error
- `source` → frontend | backend | worker | webhook
- `event_name` → ex: ui.click, js.error, net.request
- `message` (opcional)
- `session_id`
- `trace_id` (opcional)
- `request_id` (opcional)
- `user_id` (nullable)
- `route`
- `action`
- `duration_ms` (nullable)
- `http_method` (nullable)
- `http_status` (nullable)
- `tags` (JSON pequeno)
- `payload` (JSON **mascarado**)

#### Índices importantes
- `ts DESC`
- `(session_id, ts)`
- `(trace_id, ts)`
- `(request_id)`
- `(level, ts)`

#### Retenção
- eventos `info/debug`: 7 dias
- eventos `error`: 30 dias
- limpeza automática via job agendado

---

## 🔐 Política de Segurança e Mascaramento

NUNCA salvar:
- senha
- token
- cookie
- authorization
- dados sensíveis de pagamento

Em vez disso:
- salvar apenas IDs (payment_id, external_reference)
- mascarar PII (email, telefone, CPF)
- salvar apenas **chaves** do payload quando necessário

---

## 🖥️ O que o FRONTEND registra

### Eventos de Interface (UI)
- `ui.click`
- `ui.action.start`
- `ui.action.end`

Usado para detectar:
- clique não disparado
- handler JS quebrado
- botão desabilitado

### Erros JavaScript
- `js.error` → window.onerror
- `js.unhandledrejection`
- `console.error`
- `console.warn`

### Rede (Fetch / XHR)
- `net.request`
- `net.response`
- `net.error`

Campos importantes:
- url
- method
- status
- duration
- request_id retornado pelo backend

### Performance (opcional)
- `perf.route`
- `perf.api_slow`

---

## 🔌 Endpoint de Coleta do Front

### Endpoint
`POST /api/diagnostics/client-events`

### Função
- receber eventos do frontend
- validar session_id
- aplicar mascaramento
- gravar em `diagnostic_events`

### Regras
- aceita eventos em lote
- rate limit por sessão/IP
- respeita “modo diagnóstico”

---

## 🧩 Backend: Middleware de Request ID

Todo request:
- gera `request_id`
- adiciona em `request.context`
- retorna no header `X-Request-ID`
- registra:
  - api.request
  - api.response
  - api.exception

---

## ⚙️ Workers, Fila e Webhooks

### Webhooks (MercadoPago / WhatsApp)
Eventos:
- `webhook.received`
- `worker.start`
- `worker.success`
- `worker.error`

Todos com:
- trace_id
- external_id
- status

Isso permite ver:
- webhook chegou
- job rodou
- falhou ou concluiu

---

## 📡 Real-Time (Diagnóstico ao Vivo)

### Tecnologia
- **SSE (Server-Sent Events)**

### Endpoint
`GET /api/diagnostics/stream`

### Função
- enviar eventos novos em tempo quase real
- alimentar tela de diagnóstico

Fallback:
- polling a cada 2 segundos (se SSE indisponível)

---

## 🧪 Modo Diagnóstico

Tabela: `diagnostic_sessions`

Campos:
- `session_id`
- `enabled`
- `expires_at`
- `created_by`
- `notes`

### Comportamento
- OFF:
  - só erros críticos
- ON:
  - cliques
  - console
  - rede detalhada
  - performance

Ativável por:
- admin
- tempo limitado (ex.: 15 min)

---

## 🧭 Tela “Diagnóstico” (Admin)

### Visões
1️⃣ Sessões recentes  
2️⃣ Timeline de eventos  
3️⃣ Filtro por:
- usuário
- sessão
- trace_id
- apenas erros
- intervalo de tempo

### Diagnóstico típico (“botão não faz nada”)
1. Procurar `ui.click`
2. Ver se houve `net.request`
3. Se não houve → erro JS
4. Se houve e falhou → backend
5. Usar `request_id` para rastrear exceção

---

## 🧪 Ordem de Implementação (desde o começo)

### Fase 1 (obrigatória)
- request_id
- diagnostic_events
- js.error
- net.request / net.response

### Fase 2
- ui.click
- tela diagnóstico (polling)

### Fase 3
- SSE
- modo diagnóstico
- fila + webhooks instrumentados

---

## 🧠 Diretriz Final para o Codex
Sempre que houver um bug:
- NÃO corrigir no chute
- SEMPRE procurar evidência em `diagnostic_events`
- Seguir a trilha:
  session → trace → request → erro

Este sistema foi projetado para **se explicar sozinho**.
