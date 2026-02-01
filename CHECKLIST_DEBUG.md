🧪 CHECKLIST DE DEBUG E DIAGNÓSTICO
Procedimento Oficial para Investigar Qualquer Bug

Este documento define o passo a passo obrigatório para investigar problemas no sistema.

⚠️ NUNCA corrigir bugs no chute
⚠️ SEMPRE seguir este checklist do começo ao fim

🎯 Objetivo do Checklist

Garantir que:

todo bug seja investigado com evidência

o diagnóstico seja rastreável

a causa real seja identificada

o sistema continue autodiagnosticável

humanos e agentes (Codex) consigam atuar mesmo sem memória

🧠 Antes de Começar (OBRIGATÓRIO)

Antes de qualquer análise:

 Ler README.md

 Ler DIAGNOSTICO_AUTODIAGNOSTICAVEL.md

 Ler ARQUITETURA_DE_PASTAS.md

 Ler HISTORICO_DE_MUDANCAS.md

 Identificar a última alteração feita

Se o bug surgiu após uma alteração recente, suspeite primeiro dela.

0️⃣ (OBRIGATÓRIO) Checkpoint e Evidência via Git

Se você está no meio de um processo grande, ou percebeu que o agente perdeu contexto:

 STOP: pare alterações (não continue “tentando”)

 Fazer commit checkpoint (mesmo que incompleto) com mensagem clara:

checkpoint: <módulo> – <estado atual>

 Analisar o último commit (HEAD) e os 2 anteriores (HEAD~1 e HEAD~2)

Evidências mínimas (Git)

 git log -3 --oneline

 git show --name-only --oneline HEAD

 git diff --stat HEAD~1..HEAD

📌 Se o bug apareceu “do nada”, geralmente ele nasceu em um desses commits.

🧯 Se a Tela de Diagnóstico Ainda Não Existe (ou Modo OFF)

Quando o autodiagnóstico ainda não está totalmente ativo, coletar evidência manual (rápido):

Frontend (browser)

 F12 → Console: copiar erros (vermelho) e warnings

 F12 → Network (Preserve log): clicar na ação e verificar:

se houve request

status HTTP

response/erro

Servidor (se aplicável)

 logs do Next/Django:

pm2: pm2 logs

systemd: journalctl -u <servico> -f

docker: docker logs -f <container>

📌 Esses dados devem ser anexados ao relato do bug.

1️⃣ Identificar o Sintoma (FATOS, sem interpretação)

Descrever o problema apenas com fatos:

O que o usuário tentou fazer?

O que era esperado?

O que aconteceu de fato?

Em qual tela/rota?

Em qual ambiente? (dev / prod)

Qual horário aproximado?

✅ Exemplo correto:

Ao clicar no botão "Continuar", nada acontece. Nenhuma navegação, nenhum alerta e nenhuma request visível.

❌ Exemplo incorreto:

O botão está quebrado.

2️⃣ Identificar Sessão e Usuário

Na Tela de Diagnóstico (se disponível):

 Localizar a sessão

 Anotar session_id

 Anotar user_id (se houver)

 Identificar intervalo de tempo do problema

Se não houver tela ainda:

 registrar URL

 registrar navegador/dispositivo

 salvar Console + Network

3️⃣ Verificar Eventos de UI (Frontend)

Procurar eventos:

ui.click

ui.action.start

ui.action.end

Perguntas obrigatórias:

O clique foi registrado?

O botão estava disabled?

O handler realmente executou?

Resultado

❌ Não há ui.click → problema de UI (evento nem disparou)

✅ Há ui.click → continuar

4️⃣ Verificar Erros JavaScript

Procurar eventos:

js.error

js.unhandledrejection

console.error

console.warn

Perguntas:

Algum erro ocorreu logo após o clique?

O erro interrompeu execução?

Existe stack trace?

Resultado

❌ Erro JS encontrado → corrigir frontend

✅ Nenhum erro → continuar

5️⃣ Verificar Rede (API / Fetch)

Procurar eventos:

net.request

net.response

net.error

Perguntas:

A requisição foi enviada?

Para qual endpoint?

Qual método?

Houve resposta?

Qual status HTTP?

Resultado

❌ Nenhuma request → handler não executou / botão sem ação / componente server-side

❌ net.error → rede/timeout/CORS

❌ 401/403 → auth/permissão

❌ 5xx → erro backend

✅ 2xx → continuar

Anotar:

trace_id

request_id (se houver)

6️⃣ Verificar Backend (API)

Com request_id:

 api.request

 api.response

 api.exception

Perguntas:

A request chegou no servidor?

Houve exceção?

Qual endpoint?

Em qual ponto do código?

Resultado

❌ Exception encontrada → corrigir backend

✅ Nenhuma exceção → continuar

7️⃣ Verificar Regras de Negócio

Se não houve erro técnico:

validação de dados

permissões

estado do registro

regras do fluxo

Perguntas:

O sistema bloqueou por regra?

A mensagem para usuário existe e é clara?

A regra está correta?

8️⃣ Verificar Processos Assíncronos (Fila/Webhooks)

Se envolve fila/webhook:

 webhook.received

 worker.start

 worker.success

 worker.error

Perguntas:

Job foi enfileirado?

Executou?

Falhou?

Vai retentar?

9️⃣ Verificar Infraestrutura (ÚLTIMA HIPÓTESE)

Somente se tudo acima estiver ok:

conexão com banco

Redis ativo

fila rodando

DNS/certificados

recursos (CPU/RAM/disco)

Infra é última hipótese, não primeira.

🔁 Correção do Problema

Antes de corrigir:

 causa raiz identificada?

 evidência clara coletada?

 correção não quebra diagnóstico?

Durante a correção:

manter logs

manter IDs

manter mascaramento

📝 Após Corrigir (OBRIGATÓRIO)

 Registrar em HISTORICO_DE_MUDANCAS.md

 Descrever causa raiz

 Descrever correção

 Listar arquivos alterados

 Indicar impacto

🚫 O QUE NÃO FAZER

não apagar logs para “resolver”

não silenciar erros sem entender

não corrigir sem evidência

não assumir causa sem prova

não pular etapas

📩 Modelo de Mensagem para o Codex (copiar e colar)
PARE. Não faça correções no chute.

Bug:
- Sintoma (fatos): <descrever>
- URL/rota: <...>
- Ambiente: dev/prod
- Horário: <...>

Evidências:
- Console (F12): <colar>
- Network (F12): <colar>
- Git (últimos commits):
  - git log -3 --oneline: <colar>
  - git show --name-only HEAD: <colar>
  - git diff --stat HEAD~1..HEAD: <colar>

Tarefa:
1) Identificar causa raiz com base nas evidências.
2) Corrigir sem quebrar diagnóstico (IDs + logs).
3) Dizer quais arquivos foram alterados e por quê.
4) Atualizar HISTORICO_DE_MUDANCAS.md.
Aguarde minha confirmação antes de mudanças grandes.

🧭 Diretriz Final

Se em algum momento você:

não souber onde está o problema

não entender o fluxo

não lembrar o que foi feito

👉 Volte para o Passo 1.

O sistema foi projetado para mostrar o caminho.
Este checklist é o mapa.