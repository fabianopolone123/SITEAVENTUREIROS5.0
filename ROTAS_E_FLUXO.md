# 🌐 ROTAS_E_FLUXO.md
## Organização Oficial de URLs – Django Monolito

---

## 🧭 CATEGORIAS DE ROTAS (OFICIAIS)

O sistema possui **3 categorias de rotas**:

1. 🖥️ UI (HTML)
2. 🔌 API (JSON)
3. 🧠 Diagnóstico (Observabilidade)

Nenhuma outra categoria é permitida.

---

## 🖥️ ROTAS DE UI (INTERFACE)

**Responsabilidade**
- Renderizar páginas HTML
- Navegação do usuário
- Telas administrativas

**Prefixo**
/


**Arquivo**
backend/ui/urls.py


**Exemplos**
/
/login
/logout
/dashboard
/admin-ui
/diagnostics


---

## 🔌 ROTAS DE API

**Responsabilidade**
- Retornar JSON
- Executar regras de negócio
- Integrações internas

**Prefixo obrigatório**
/api/


**Arquivos**
backend/apps/<app>/urls.py


**Exemplos**
/api/accounts/login
/api/accounts/logout
/api/members/list
/api/members/create
/api/payments/pay
/api/payments/status


---

## 🧠 ROTAS DE DIAGNÓSTICO

**Responsabilidade**
- Receber eventos
- Expor logs e streams
- Health-check

**Prefixo obrigatório**
/diagnostics/


**Arquivo**
backend/diagnostics/urls.py


**Exemplos**
/diagnostics/client-events
/diagnostics/stream
/diagnostics/health
/diagnostics/metrics


---

## 🚫 O QUE NÃO É PERMITIDO

- API sem `/api`
- Diagnóstico fora de `/diagnostics`
- HTML em API
- JSON em UI
- Rotas soltas no `config/urls.py`

---

## 🧭 AMARRAÇÃO CENTRAL

**Arquivo único**
backend/config/urls.py


Responsável apenas por:
- incluir UI
- incluir API
- incluir Diagnóstico

Nenhuma lógica é permitida aqui.

---

## 📌 REGRA FINAL

Se não souber **qual prefixo usar** → **não crie a rota**.