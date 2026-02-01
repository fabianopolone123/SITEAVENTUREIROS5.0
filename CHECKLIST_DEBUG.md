# 🧪 CHECKLIST DE DEBUG E DIAGNÓSTICO
## Procedimento Oficial para Investigar Qualquer Bug

Este documento define o **passo a passo obrigatório** para investigar problemas no sistema.

⚠️ **NUNCA corrigir bugs no chute**  
⚠️ **SEMPRE seguir este checklist do começo ao fim**

---

## 🎯 Objetivo do Checklist
Garantir que:
- todo bug seja investigado com evidência
- o diagnóstico seja rastreável
- a causa real seja identificada
- o sistema continue autodiagnosticável
- o Codex consiga atuar mesmo sem memória

---

## 🧠 Antes de Começar (OBRIGATÓRIO)

Antes de qualquer análise:
- [ ] Ler `README.md`
- [ ] Ler `DIAGNOSTICO_AUTODIAGNOSTICAVEL.md`
- [ ] Ler `HISTORICO_DE_MUDANCAS.md`
- [ ] Identificar a **última alteração feita**

Se o bug surgiu após uma alteração recente, **suspeite primeiro dela**.

---

## 1️⃣ Identificar o Sintoma
Descrever o problema **sem interpretação**, apenas fatos:

- O que o usuário tentou fazer?
- O que era esperado?
- O que aconteceu de fato?
- Em qual tela/rota?
- Em qual ambiente? (dev / prod)

📌 Exemplo correto:
> Ao clicar no botão "Salvar Cadastro", nada acontece. Nenhuma mensagem visual é exibida.

❌ Exemplo incorreto:
> O botão está quebrado.

---

## 2️⃣ Identificar Sessão e Usuário
Na tela de Diagnóstico:
- [ ] Localizar a **sessão do usuário**
- [ ] Anotar `session_id`
- [ ] Anotar `user_id` (se houver)
- [ ] Identificar o intervalo de tempo do problema

---

## 3️⃣ Verificar Eventos de UI (Frontend)
Procurar eventos do tipo:

- `ui.click`
- `ui.action.start`

Perguntas obrigatórias:
- O clique foi registrado?
- O botão estava desabilitado?
- O handler foi chamado?

### Resultado:
- ❌ **Não há `ui.click`** → problema de UI / evento não disparou
- ✅ Há `ui.click` → continuar

---

## 4️⃣ Verificar Erros JavaScript
Procurar eventos:

- `js.error`
- `js.unhandledrejection`
- `console.error`
- `console.warn`

Perguntas:
- Algum erro ocorreu logo após o clique?
- O erro interrompeu a execução?
- Existe stack trace?

### Resultado:
- ❌ Erro JS encontrado → corrigir frontend
- ✅ Nenhum erro → continuar

---

## 5️⃣ Verificar Rede (API / Fetch)
Procurar eventos:

- `net.request`
- `net.response`
- `net.error`

Perguntas:
- A requisição foi enviada?
- Qual endpoint?
- Qual método?
- Houve resposta?
- Qual status HTTP?

### Resultado:
- ❌ Nenhuma request → handler não executou
- ❌ net.error → erro de rede / timeout / CORS
- ❌ 401 / 403 → problema de autenticação/permissão
- ❌ 5xx → erro no backend
- ✅ 2xx → continuar

Anotar:
- `trace_id`
- `request_id` (se houver)

---

## 6️⃣ Verificar Backend (API)
Com o `request_id`:
- [ ] Procurar `api.request`
- [ ] Procurar `api.response`
- [ ] Procurar `api.exception`

Perguntas:
- A request chegou no servidor?
- A exceção foi registrada?
- Em qual ponto do código?
- O erro é reproduzível?

### Resultado:
- ❌ Exception encontrada → corrigir backend
- ✅ Nenhuma exceção → continuar

---

## 7️⃣ Verificar Regras de Negócio
Se não houve erro técnico:
- validação de dados
- regras de permissão
- estado do registro
- flags de negócio

Perguntas:
- O sistema bloqueou a ação por regra?
- Existe mensagem adequada para o usuário?
- A regra está correta?

---

## 8️⃣ Verificar Processos Assíncronos
Se a ação envolve fila, webhook ou tarefa:
- [ ] `worker.start`
- [ ] `worker.success`
- [ ] `worker.error`
- [ ] `webhook.received`

Perguntas:
- O job foi enfileirado?
- Foi executado?
- Falhou?
- Vai retentar?

---

## 9️⃣ Verificar Infraestrutura (se necessário)
Somente se tudo acima estiver correto:
- conexão com banco
- Redis ativo
- fila rodando
- DNS
- certificados
- recursos (CPU, RAM, disco)

Infra é **última hipótese**, não a primeira.

---

## 🔁 Correção do Problema
Antes de corrigir:
- [ ] A causa raiz foi identificada?
- [ ] Existe evidência clara?
- [ ] A correção não quebra o diagnóstico?

Durante a correção:
- manter logs
- manter IDs
- manter mascaramento

---

## 📝 Após Corrigir (OBRIGATÓRIO)

- [ ] Registrar a alteração em `HISTORICO_DE_MUDANCAS.md`
- [ ] Descrever causa raiz
- [ ] Descrever correção
- [ ] Listar arquivos alterados
- [ ] Indicar impacto

---

## 🚫 O QUE NÃO FAZER
- não apagar logs para “resolver”
- não silenciar erros sem entender
- não corrigir sem evidência
- não assumir causa sem prova
- não pular etapas deste checklist

---

## 🧭 Diretriz Final
Se em algum momento você:
- não souber onde está o problema
- não entender o fluxo
- não lembrar o que foi feito

👉 Volte para o **Passo 1**.

O sistema foi projetado para **mostrar o caminho**.  
Este checklist é o mapa.
