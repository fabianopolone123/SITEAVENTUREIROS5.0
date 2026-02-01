# 🧾 Histórico de Mudanças do Projeto
📌 **Arquivo obrigatório de leitura antes de qualquer alteração no código**

Este documento mantém o **registro cronológico e técnico** de TODAS as mudanças feitas no projeto.

Ele existe para:
- recuperar contexto quando o Codex perder a memória
- entender **o que foi feito, por quê e onde**
- evitar retrabalho
- facilitar diagnóstico de bugs
- ajudar novos ciclos de desenvolvimento

---

## ⚠️ REGRA DE OURO (OBRIGATÓRIA)
Antes de:
- alterar código
- criar arquivos
- remover arquivos
- mudar comportamento
- refatorar
- corrigir bug

👉 **LER este arquivo do começo ao fim**

Depois de qualquer mudança:
👉 **REGISTRAR A MUDANÇA AQUI**

---

## 🧠 COMO O CODEX DEVE USAR ESTE ARQUIVO

Para CADA modificação feita, o Codex DEVE registrar:
1. O que foi feito
2. Por que foi feito
3. Quais arquivos foram alterados
4. Qual impacto esperado
5. Se existe risco ou dependência

Nunca escrever frases vagas como:
❌ “ajustes gerais”
❌ “melhorias”
❌ “refatoração”

Sempre ser **explícito e técnico**.

---

## 🗂️ MODELO PADRÃO DE REGISTRO (OBRIGATÓRIO)

Copiar e preencher exatamente este modelo:

---

### 🔄 Alteração Nº XXXX
**Data:** YYYY-MM-DD  
**Autor:** Codex / Humano  
**Tipo:** feature | bugfix | refactor | infra | diagnóstico | segurança  

#### 📌 Contexto
> Por que essa alteração foi necessária?

#### 🛠️ O que foi feito
- item 1
- item 2
- item 3

#### 📁 Arquivos afetados
- caminho/arquivo.ext
- caminho/arquivo.ext

#### 🔗 Relacionado a
- feature: nome
- bug: descrição
- diagnóstico: trace_id / request_id (se houver)

#### ⚠️ Impacto / Observações
- impacto funcional
- impacto em diagnóstico
- impacto em performance
- riscos conhecidos

---

## 📜 HISTÓRICO DE ALTERAÇÕES

> As alterações devem ser adicionadas **sempre no final do arquivo**.

---

### 🔄 Alteração Nº 0001
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** arquitetura / diagnóstico  

#### 📌 Contexto
Criação da base documental do sistema autodiagnosticável para evitar perda de contexto e permitir que o Codex se reoriente após reset de memória.

#### 🛠️ O que foi feito
- Definido padrão de arquitetura autodiagnosticável
- Criado documento `DIAGNOSTICO_AUTODIAGNOSTICAVEL.md`
- Definido uso de Next.js + Django + PostgreSQL
- Definido modelo `diagnostic_events`
- Definido fluxo de request_id, trace_id e session_id

#### 📁 Arquivos afetados
- DIAGNOSTICO_AUTODIAGNOSTICAVEL.md
- HISTORICO_DE_MUDANCAS.md

#### 🔗 Relacionado a
- Diagnóstico do sistema
- Persistência de contexto do projeto

#### ⚠️ Impacto / Observações
- Nenhuma mudança funcional
- Base estrutural do projeto criada
- Documento deve ser tratado como fonte da verdade

---

## 🧩 BOAS PRÁTICAS PARA O CODEX

- Sempre mencionar **arquivos reais**
- Se criou algo novo, deixar claro
- Se removeu algo, justificar
- Se mudou comportamento, explicar o antes e depois
- Se a mudança afeta diagnóstico, deixar explícito

---

## 🚫 O QUE NÃO FAZER
- Não apagar entradas antigas
- Não reescrever histórico
- Não alterar numeração passada
- Não registrar múltiplas mudanças diferentes na mesma entrada

---

## 🧭 DIRETRIZ FINAL
Este arquivo é o **mapa da memória do projeto**.

Se o Codex estiver perdido:
1. Ler `DIAGNOSTICO_AUTODIAGNOSTICAVEL.md`
2. Ler este `HISTORICO_DE_MUDANCAS.md`
3. Identificar última alteração
4. Entender estado atual antes de escrever código

Sem isso, nenhuma modificação deve ser feita.

### Altera��o N� 0002
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** feature

#### Contexto
> O usu�rio pediu uma tela inicial inspirada no layout fornecido para o Clube de Aventureiros com login e o logo oficial.

#### O que foi feito
- Criada a pasta `frontend` com os recursos necess�rios para hospedar a p�gina est�tica.  
- Constru�da a p�gina `index.html` e o arquivo `css/styles.css` que reproduzem o card central, formul�rios e estilos do login.  
- Movido `logo.png` para `frontend/public` para manter os ativos organizados com o frontend.

#### Arquivos afetados
- frontend/index.html
- frontend/css/styles.css
- frontend/public/logo.png

#### Relacionado a
- feature: landing page de login

#### Impacto / Observa��es
- Cria uma primeira tela responsiva e estilizada para o Clube, preparada para ser integrada a autentica��o real.  
- Risco m�nimo, pois a p�gina � est�tica e isolada; nenhuma l�gica de backend foi implementada.

### Altera��o N� 0003
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** feature

#### Contexto
O usu�rio solicitou o fluxo completo "Cadastrar Aventureiro" guiado, com telas sequenciais, controle de pend�ncias, estados visuais e valida��es espec�ficas para cada etapa.

#### O que foi feito
- Implementada a p�gina `frontend/index.html` com as sete telas (escolha, respons�vel, lista, dados, ficha m�dica, termo e revis�o), indicador de progresso, resumo de pend�ncias e bot�es que ativam somente quando os dados est�o validados.  
- Reescritos os estilos em `frontend/css/styles.css` para suportar o layout do wizard, incluindo m�scaras autom�ticas, componentes de status, cart�es de revis�o e notas visuais para assinaturas e campos pr�-preenchidos.  
- Criado `frontend/js/wizard.js` que coordena o estado do cadastro, valida��es (CPF, fotos, assinaturas, checkbox de aceite), reuso autom�tico de dados, upload de fotos, desenho de assinaturas digitais, status por aventureiro e bloqueio da finaliza��o at� todos os registros estarem completos.

#### Arquivos afetados
- frontend/index.html
- frontend/css/styles.css
- frontend/js/wizard.js

#### Relacionado a
- feature: cadastro guiado de aventureiros

#### Impacto / Observa��es
- A tela inicial agora � uma experi�ncia aut�noma pronta para integrar com APIs e mant�m o usu�rio dentro do fluxo at� todas as pend�ncias serem resolvidas.
- Assinaturas digitais simples e verifica��o visual garantem que o preenchimento seja jur�dico e rastre�vel.
