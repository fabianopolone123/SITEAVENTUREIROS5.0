Contribuindo com o Projeto
Regras Obrigatórias para Humanos e Agentes Automáticos (Codex)

Este documento define COMO o código deste projeto deve ser alterado.

⚠️ Este projeto não aceita contribuições sem evidência
⚠️ Este projeto não aceita correções no chute
⚠️ Este projeto não aceita decisões arquiteturais implícitas

🎯 Objetivo do CONTRIBUTING

Garantir que:

o sistema continue autodiagnosticável

o código seja alterado com segurança

a arquitetura permaneça consistente

o histórico seja preservado

o Codex consiga se reorientar mesmo sem memória

❗ DIRETRIZ FUNDAMENTAL (OBRIGATÓRIA)

Este projeto é BACKEND-FIRST.

Django (Python) é o núcleo do sistema

Frontend é apenas cliente

Arquitetura não é decidida pelo frontend

🚫 PROIBIÇÕES ABSOLUTAS

É expressamente proibido:

usar Nx

usar Turborepo

usar Lerna

criar monorepo JavaScript

criar pastas do tipo:

/apps

/libs

/packages

misturar código Python dentro de estruturas JS

Qualquer tentativa de introduzir essas ferramentas ou estruturas é considerada
ERRO DE ARQUITETURA e deve ser revertida.

🧠 Leitura Obrigatória (ANTES DE QUALQUER ALTERAÇÃO)

Antes de escrever uma única linha de código, é obrigatório ler:

README.md

DIAGNOSTICO_AUTODIAGNOSTICAVEL.md

ARQUITETURA_DE_PASTAS.md

HISTORICO_DE_MUDANCAS.md

❌ Se algum desses arquivos não for lido, a contribuição é inválida.

🧭 Fluxo Obrigatório de Contribuição
1️⃣ Entender o Problema (ANTES DO CÓDIGO)

Antes de alterar qualquer coisa:

identificar o problema com clareza

procurar evidência na Tela de Diagnóstico

coletar, quando aplicável:

session_id

trace_id

request_id

eventos relevantes

🚫 Nunca partir direto para o código.
🚫 Nunca “supor” a causa.

2️⃣ Classificar a Alteração

Toda mudança deve ser classificada como uma das opções:

feature

bugfix

refactor

diagnóstico

infra

segurança

Essa classificação é obrigatória no histórico de mudanças.

3️⃣ Planejar a Mudança

Antes de implementar, deve ser possível responder claramente:

quais arquivos serão alterados

qual o impacto esperado

se afeta o sistema de diagnóstico

se cria ou reduz dívida técnica

❌ Se não souber responder, não altere o código.

4️⃣ Implementar com Evidência

Durante a implementação é obrigatório:

não remover logs existentes sem justificativa explícita

não quebrar a correlação de IDs

manter mascaramento de dados sensíveis

manter compatibilidade com o sistema autodiagnosticável

respeitar a arquitetura definida nos .md

5️⃣ Registrar no Histórico (OBRIGATÓRIO)

Após concluir a alteração:

registrar em HISTORICO_DE_MUDANCAS.md

usar o modelo oficial

descrever claramente:

o que mudou

por que mudou

quais arquivos foram afetados

riscos conhecidos

❌ Pull requests ou alterações sem histórico atualizado são inválidas.

🧪 Regras de Diagnóstico (NÃO QUEBRAR)

É PROIBIDO:

remover request_id

remover trace_id

remover session_id

remover eventos de erro

desativar logs sem controle explícito

logar dados sensíveis (senha, token, segredo)

É OBRIGATÓRIO:

manter correlação de eventos

registrar exceções

respeitar o modo diagnóstico

garantir rastreabilidade ponta a ponta

🧱 Regras de Código
Código Geral

clareza > esperteza

código legível > código curto

nomes explícitos

comentários quando necessário

Frontend

toda ação relevante gera trace_id

todo clique relevante gera ui.click

toda chamada de API propaga trace_id e session_id

erros JS devem ser capturados e registrados

Backend

toda request gera request_id

exceções devem ser registradas

logs devem ser estruturados

webhooks e workers devem gerar eventos de diagnóstico

🔐 Segurança

nunca logar senha, token ou segredo

nunca salvar payloads sensíveis completos

sempre mascarar dados pessoais

revisar impacto de segurança antes de subir alterações

🧹 O que NÃO é permitido

commits genéricos (“ajustes”, “correções”)

apagar ou reescrever histórico

alterar código sem registrar no histórico

correções sem evidência

mudanças arquiteturais implícitas

introdução de ferramentas não aprovadas

🧭 Diretriz Especial para o Codex

Se o Codex:

estiver perdido

não souber o estado atual

não lembrar o que foi feito

não souber quais arquivos mexer

DEVE obrigatoriamente:

Ler README.md

Ler DIAGNOSTICO_AUTODIAGNOSTICAVEL.md

Ler ARQUITETURA_DE_PASTAS.md

Ler HISTORICO_DE_MUDANCAS.md

Identificar a última alteração registrada

Somente então propor mudanças

🚫 Nunca adivinhar
🚫 Nunca assumir
🚫 Nunca alterar no escuro

✅ Checklist Final (ANTES DE FINALIZAR)

 Li o README

 Li o Diagnóstico

 Li a Arquitetura

 Li o Histórico

 Entendi o problema com evidência

 Não usei Nx nem monorepo

 Não quebrei o sistema de diagnóstico

 Atualizei o Histórico de Mudanças

Se algum item não estiver marcado, a contribuição não está pronta.

📌 Nota Final

Este projeto foi desenhado para:

sobreviver a resets de memória

ser mantido por humanos e agentes

explicar seus próprios problemas

O código não é o ativo principal.
👉 A evidência é.