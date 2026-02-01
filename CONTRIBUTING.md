# 🤝 Contribuindo com o Projeto
## Regras Obrigatórias para Humanos e Codex

Este documento define **COMO** o código deste projeto deve ser alterado.

⚠️ Este projeto **não aceita contribuições sem evidência**  
⚠️ Este projeto **não aceita correções no chute**

---

## 🎯 Objetivo do Contributing
Garantir que:
- o sistema continue **autodiagnosticável**
- o código seja alterado com segurança
- o histórico seja preservado
- o Codex consiga se reorientar mesmo sem memória

---

## 🧠 Leitura Obrigatória (ANTES DE QUALQUER ALTERAÇÃO)

Antes de escrever uma única linha de código, LEIA:

1. `README.md`
2. `DIAGNOSTICO_AUTODIAGNOSTICAVEL.md`
3. `HISTORICO_DE_MUDANCAS.md`

❌ Se algum desses arquivos não for lido, a contribuição é inválida.

---

## 🧭 Fluxo Obrigatório de Contribuição

### 1️⃣ Entender o Problema
Antes de alterar código:
- identificar o problema com clareza
- procurar evidência na **Tela de Diagnóstico**
- coletar:
  - session_id
  - trace_id
  - request_id
  - eventos relevantes

Nunca partir direto para o código.

---

### 2️⃣ Classificar a Alteração
Toda mudança deve ser classificada como:
- `feature`
- `bugfix`
- `refactor`
- `diagnóstico`
- `infra`
- `segurança`

Essa classificação deve aparecer no histórico.

---

### 3️⃣ Planejar a Mudança
Antes de alterar:
- quais arquivos serão alterados
- qual o impacto esperado
- se afeta diagnóstico
- se cria dívida técnica

Se não souber responder isso, **não altere**.

---

### 4️⃣ Implementar com Evidência
Durante a implementação:
- não remover logs existentes sem justificativa
- não quebrar correlação de IDs
- manter mascaramento de dados
- manter compatibilidade com o sistema de diagnóstico

---

### 5️⃣ Registrar no Histórico (OBRIGATÓRIO)
Após concluir a alteração:
- registrar em `HISTORICO_DE_MUDANCAS.md`
- usar o modelo oficial
- descrever claramente:
  - o que mudou
  - por que mudou
  - quais arquivos foram afetados

❌ Pull requests sem histórico atualizado são inválidos.

---

## 🧪 Regras de Diagnóstico (NÃO QUEBRAR)

É PROIBIDO:
- remover `request_id`
- remover `trace_id`
- remover `session_id`
- remover eventos de erro
- desativar logs sem controle
- logar dados sensíveis

É OBRIGATÓRIO:
- manter correlação de eventos
- registrar exceções
- respeitar o modo diagnóstico

---

## 🧱 Regras de Código

### Código Geral
- clareza > esperteza
- código legível > código curto
- nomes explícitos
- comentários quando necessário

### Frontend
- toda ação importante gera `trace_id`
- todo clique relevante gera `ui.click`
- toda chamada de API deve propagar `trace_id` e `session_id`
- erros JS devem ser capturados

### Backend
- toda request gera `request_id`
- exceções devem ser registradas
- logs devem ser estruturados
- webhooks e workers devem gerar eventos

---

## 🔐 Segurança
- nunca logar senha, token ou segredo
- nunca salvar payloads completos sensíveis
- mascarar dados pessoais
- revisar impactos de segurança antes de subir mudanças

---

## 🧹 O que NÃO é permitido
- commits genéricos (“ajustes”, “correções”)
- apagar histórico
- alterar código sem registrar no histórico
- correções sem evidência
- alterar comportamento sem explicar antes/depois

---

## 🧭 Diretriz Especial para o Codex

Se o Codex:
- estiver perdido
- não souber o estado atual
- não lembrar o que foi feito
- não souber quais arquivos mexer

DEVE:
1. Ler `README.md`
2. Ler `DIAGNOSTICO_AUTODIAGNOSTICAVEL.md`
3. Ler `HISTORICO_DE_MUDANCAS.md`
4. Identificar a última alteração
5. Somente então propor mudanças

Nunca “adivinhar”.

---

## ✅ Checklist Final (ANTES DE FINALIZAR)

- [ ] Li o README
- [ ] Li o Diagnóstico
- [ ] Li o Histórico
- [ ] Entendi o problema com evidência
- [ ] Implementei sem quebrar diagnóstico
- [ ] Atualizei o Histórico de Mudanças

Se algum item estiver **não marcado**, a contribuição **não está pronta**.

---

## 📌 Nota Final
Este projeto foi desenhado para:
- sobreviver a resets de memória
- ser mantido por humanos e agentes
- explicar seus próprios problemas

O código não é o ativo principal.  
👉 **A evidência é.**
