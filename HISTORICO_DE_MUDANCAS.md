# ð§¾ HISTÃRICO DE MUDANÃAS DO PROJETO

ð **Arquivo obrigatÃ³rio de leitura antes de qualquer alteraÃ§Ã£o no cÃ³digo**

Este documento mantÃ©m o **registro cronolÃ³gico e tÃ©cnico** de TODAS as mudanÃ§as feitas no projeto.  
Ele existe para:

- recuperar contexto quando o Codex perder a memÃ³ria
- entender **o que foi feito, por quÃª e onde**
- evitar retrabalho
- facilitar diagnÃ³stico de bugs
- ajudar novos ciclos de desenvolvimento

---

## â ï¸ REGRA DE OURO (OBRIGATÃRIA)

Antes de:
- alterar cÃ³digo
- criar arquivos
- remover arquivos
- mudar comportamento
- refatorar
- corrigir bug

ð **LER este arquivo do comeÃ§o ao fim**

Depois de qualquer mudanÃ§a:  
ð **REGISTRAR A MUDANÃA AQUI**

---

## ð§  COMO O CODEX DEVE USAR ESTE ARQUIVO

Para **CADA modificaÃ§Ã£o feita**, o Codex DEVE registrar:

1. O que foi feito  
2. Por que foi feito  
3. Quais arquivos foram alterados  
4. Qual impacto esperado  
5. Se existe risco ou dependÃªncia  

Regras:
- Sempre escrever em **UTF-8 com caracteres portugueses**
- Nunca escrever frases vagas como:
  - â âajustes geraisâ
  - â âmelhoriasâ
  - â ârefatoraÃ§Ã£oâ
- Sempre ser **explÃ­cito e tÃ©cnico**

---

## ðï¸ MODELO PADRÃO DE REGISTRO (OBRIGATÃRIO)

Copiar e preencher exatamente este modelo:

---

### ð AlteraÃ§Ã£o NÂº XXXX
**Data:** YYYY-MM-DD  
**Autor:** Codex / Humano  
**Tipo:** feature | bugfix | refactor | infra | diagnÃ³stico | seguranÃ§a  

#### ð Contexto
> Por que essa alteraÃ§Ã£o foi necessÃ¡ria?

#### ð ï¸ O que foi feito
- item 1
- item 2
- item 3

#### ð Arquivos afetados
- caminho/arquivo.ext
- caminho/arquivo.ext

#### ð Relacionado a
- feature: nome  
- bug: descriÃ§Ã£o  
- diagnÃ³stico: trace_id / request_id (se houver)

#### â ï¸ Impacto / ObservaÃ§Ãµes
- impacto funcional
- impacto em diagnÃ³stico
- impacto em performance
- riscos conhecidos

---

## ð HISTÃRICO DE ALTERAÃÃES
> As alteraÃ§Ãµes devem ser adicionadas **sempre no final do arquivo**

---

### ð AlteraÃ§Ã£o NÂº 0001
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** arquitetura / diagnÃ³stico  

#### ð Contexto
CriaÃ§Ã£o da base documental do sistema autodiagnosticÃ¡vel para evitar perda de contexto e permitir que o Codex se reoriente apÃ³s reset de memÃ³ria.

#### ð ï¸ O que foi feito
- Definido padrÃ£o de arquitetura autodiagnosticÃ¡vel
- Criado documento `DIAGNOSTICO_AUTODIAGNOSTICAVEL.md`
- Definido uso de Next.js + Django + PostgreSQL
- Definido modelo `diagnostic_events`
- Definido fluxo de `request_id`, `trace_id` e `session_id`

#### ð Arquivos afetados
- DIAGNOSTICO_AUTODIAGNOSTICAVEL.md
- HISTORICO_DE_MUDANCAS.md

#### ð Relacionado a
- DiagnÃ³stico do sistema
- PersistÃªncia de contexto do projeto

#### â ï¸ Impacto / ObservaÃ§Ãµes
- Nenhuma mudanÃ§a funcional
- Base estrutural do projeto criada
- Documento deve ser tratado como fonte da verdade

---

### ð AlteraÃ§Ã£o NÂº 0002
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** feature  

#### ð Contexto
Implantar a tela de login do frontend com o estilo fornecido e garantir o logo oficial no local correto para a interface.

#### ð ï¸ O que foi feito
- Criada a base Next.js dentro de `frontend/`
- Definido layout global (`app/layout.tsx`) e estilos compartilhados
- ConstruÃ­da a pÃ¡gina de login (`app/page.tsx`) conforme mock visual
- Movido `logo.png` para `frontend/public/` e referenciado na tela

#### ð Arquivos afetados
- frontend/package.json
- frontend/tsconfig.json
- frontend/next.config.js
- frontend/next-env.d.ts
- frontend/app/layout.tsx
- frontend/app/globals.css
- frontend/app/page.tsx
- frontend/public/logo.png

#### ð Relacionado a
- feature: tela de login

#### â ï¸ Impacto / ObservaÃ§Ãµes
- Estrutura inicial do frontend criada
- Interface pronta para futura autenticaÃ§Ã£o
- Frontend alinhado Ã  arquitetura backend-first

---

### ð AlteraÃ§Ã£o NÂº 0003
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** feature  

#### ð Contexto
Iniciar o backend Django conforme a arquitetura backend-first e garantir um esqueleto extensÃ­vel.

#### ð ï¸ O que foi feito
- Configurado core do Django (`settings`, `urls`, `asgi`, `wsgi`)
- Criadas pastas de apps (accounts, members, documents, store, payments, notifications, diagnostics)
- Criados mÃ³dulos base de diagnÃ³sticos, integraÃ§Ãµes, workers e utilitÃ¡rios
- Documentadas dependÃªncias iniciais

#### ð Arquivos afetados
- backend/manage.py
- backend/config/*
- backend/apps/*
- backend/diagnostics/*
- backend/integrations/*
- backend/workers/*
- backend/common/*
- backend/requirements/base.txt

#### ð Relacionado a
- feature: backend Django inicial

#### â ï¸ Impacto / ObservaÃ§Ãµes
- Base do backend criada
- Ainda sem regras de negÃ³cio ou modelos reais

---

### ð AlteraÃ§Ã£o NÂº 0004
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** infra  

#### ð Contexto
Falha de importaÃ§Ã£o de `backend.diagnostics` ao executar `manage.py runserver` dentro da pasta backend.

#### ð ï¸ O que foi feito
- Criado `backend/__init__.py`
- Ajustado `manage.py` para inserir o diretÃ³rio raiz no `sys.path`

#### ð Arquivos afetados
- backend/__init__.py
- backend/manage.py

#### â ï¸ Impacto / ObservaÃ§Ãµes
- Imports passam a funcionar independentemente do diretÃ³rio atual

---

### ð AlteraÃ§Ã£o NÂº 0005
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** infra  

#### ð Contexto
Django bloqueava acesso via `127.0.0.1` por nÃ£o estar em `ALLOWED_HOSTS`.

#### ð ï¸ O que foi feito
- Ajustado `ALLOWED_HOSTS` para aceitar `127.0.0.1` por padrÃ£o

#### ð Arquivos afetados
- backend/config/settings.py

#### â ï¸ Impacto / ObservaÃ§Ãµes
- `runserver` funciona corretamente em ambiente local

---

### ð AlteraÃ§Ã£o NÂº 0006
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** infra  

#### ð Contexto
A rota raiz `/` retornava 404.

#### ð ï¸ O que foi feito
- Criada resposta padrÃ£o na rota raiz informando que o backend estÃ¡ ativo

#### ð Arquivos afetados
- backend/config/urls.py

#### â ï¸ Impacto / ObservaÃ§Ãµes
- Facilita testes manuais e validaÃ§Ã£o do ambiente

---

### ð AlteraÃ§Ã£o NÂº 0007
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** feature  

#### ð Contexto
Necessidade de exibir a tela de login sem depender do Next.js.

#### ð ï¸ O que foi feito
- Criado template `login.html` no backend
- Criado CSS especÃ­fico para a tela de login
- Configurado Django para servir templates e arquivos estÃ¡ticos
- Rota raiz passou a renderizar a tela de login

#### ð Arquivos afetados
- backend/config/settings.py
- backend/config/urls.py
- backend/templates/login.html
- backend/static/css/login.css
- backend/static/images/logo.png

#### â ï¸ Impacto / ObservaÃ§Ãµes
- Backend passa a exibir UI funcional sem frontend separado

---

### ð AlteraÃ§Ã£o NÂº 0009
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** infra  

#### ð Contexto
O backend nÃ£o possuÃ­a bootstrap completo para execuÃ§Ã£o do Django.

#### ð ï¸ O que foi feito
- Criada estrutura completa de `backend/config`
- Criado `manage.py` no root do projeto
- Garantido `backend/__init__.py`

#### ð Arquivos afetados
- backend/__init__.py
- backend/config/settings.py
- backend/config/urls.py
- backend/config/wsgi.py
- backend/config/asgi.py
- manage.py

#### â ï¸ Impacto / ObservaÃ§Ãµes
- Django pode ser iniciado corretamente
- Base pronta para expansÃ£o

---

### ð AlteraÃ§Ã£o NÂº 0010
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ð Contexto
Refinar a tela de login do backend para espelhar o mock visual.

#### ð ï¸ O que foi feito
- Reescrito template de login com layout em cartÃ£o central
- Aplicado degradÃª claro, sombras suaves e botÃµes arredondados
- Ajustada responsividade para mobile

#### ð Arquivos afetados
- backend/ui/templates/login.html
- backend/ui/static/css/login.css

#### â ï¸ Impacto / ObservaÃ§Ãµes
- UI alinhada ao mock
- Pronta para receber autenticaÃ§Ã£o real

---


---

### Alteração Nº 0014
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### Contexto
> A solicitação pediu para apagar o estilo atual e reescrever a tela de login com um padrão moderno consistente com o mock.

#### O que foi feito
- Substituí totalmente `backend/ui/static/css/login.css` por uma nova folha de estilo: fundo degradê, cartão elevado, linhas decorativas, halo do logo maior e inputs/botões com gradient suave.
- Mantive o template (`backend/ui/templates/login.html`) e acentuei o halo para garantir que o logo esteja sempre centralizado no cartão.

#### Arquivos afetados
- backend/ui/static/css/login.css
- backend/ui/templates/login.html

#### Relacionado a
- feature: tela de login

Aviso: Impacto / Observações
- A interface ficou com efeitos modernos e o logo não é mais cortado; validações futuras devem considerar o novo visual.


---

### Alteração Nº 0015
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### Contexto
> O estilo anterior da tela de login precisava ser apagado e recriado sob um novo padrão mais harmônico e moderno.

#### O que foi feito
- Eliminei o CSS antigo em `backend/ui/static/css/login.css` e inseri um novo conjunto totalmente reescrito com degradê de fundo, cartão elevado, halo amplo do logo, inputs com bordas suaves e botão gradient.
- Mantive o template do cartão, reforçando o halo para manter o logo completo.

#### Arquivos afetados
- backend/ui/static/css/login.css
- backend/ui/templates/login.html

#### Relacionado a
- feature: tela de login

Aviso: Impacto / Observações
- A experiência visual virou um layout limpo e moderno compatível com o mock e alinhado ao padrão backend-first.


---

### Alteração Nº 0016
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### Contexto
> O logo ainda aparecia cortado no topo, portanto precisei ajustar o cartão para dar espaço suficiente.

#### O que foi feito
- Aumentei o `padding-top` do cartão (`backend/ui/static/css/login.css`) e removi o `overflow: hidden`.
- Ajustei a margem negativa e o padding de `.logo-shell` para que a parte branca do medalhão fique totalmente visível acima do formulário.

#### Arquivos afetados
- backend/ui/static/css/login.css

#### Relacionado a
- refactor: UI

Aviso: Impacto / Observações
- O logo agora fica livre de cortes e o halo respira; o layout continua alinhado com o mock.


---

### Alteração Nº 0017
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### Contexto
> O halo ao redor do logo ainda se elevava demais e aparecia acima do cartão.

#### O que foi feito
- Ajustei `.logo-shell` em `backend/ui/static/css/login.css` para 200px com margem negativa menor, mantendo o halo mas impedindo que ele sobressaia acima do cartão.

#### Arquivos afetados
- backend/ui/static/css/login.css

#### Relacionado a
- refactor: UI

Aviso: Impacto / Observações
- O logo volta a ficar centrado dentro do cartão, mantendo o novo visual moderno.


---

### Alteração Nº 0018
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### Contexto
> O estilo ainda precisava ser repensado do zero, conforme pedido.

#### O que foi feito
- Reescrevi totalmente `backend/ui/static/css/login.css` com um novo padrão (fundo degradê com partículas suaves, cartão elevado, halo do logo maior, inputs com bordas reversas e botão gradient).
- Mantive o template do formulário e deixei o halo maior para garantir o logo completo.

#### Arquivos afetados
- backend/ui/static/css/login.css
- backend/ui/templates/login.html

#### Relacionado a
- feature: tela de login

Aviso: Impacto / Observações
- A tela agora tem efeito mais moderno, e a marca é plenamente visível.


---

### 🎯 Alteração Nº 0019
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> Cliente pediu o fluxo guiado “Cadastrar Aventureiro” acessível via “Cadastre-se”, com sete telas, reutilização de dados, validação por etapa, pendências visuais, assinaturas digitais e bloqueio da finalização até que tudo esteja completo.

#### ✅ O que foi feito
- Criado o app `backend.apps.members` com os modelos `Responsible`, `Adventurer`, `MedicalRecord` e `ImageReleaseTerm`, serviços de status/pendências e migração inicial.
- Atualizadas as configurações do Django (`settings`, `urls`) para registrar o app, habilitar sessões e servir mídia.
- Criados formulários de rascunho (pai, mãe, responsável, aventureiro, ficha médica e termo) e views que orquestram as sete etapas, salvam rascunhos, validam cada etapa, registram assinaturas baseadas em canvas e acompanham o progresso.
- Construídas as novas telas sob `backend/ui/templates/cadastro_aventureiro/`, adicionando o layout base, etapas específicas, resumo de pendências, link “Cadastre-se” no login e estilos em `cadastro.css`.
- Salvaguardado o salvamento parcial das etapas e mantido o status visual/pendências via serviço central.

#### 📁 Arquivos afetados
- backend/apps/__init__.py
- backend/apps/members/__init__.py
- backend/apps/members/apps.py
- backend/apps/members/migrations/0001_initial.py
- backend/apps/members/migrations/__init__.py
- backend/apps/members/models.py
- backend/apps/members/services.py
- backend/config/settings.py
- backend/config/urls.py
- backend/ui/forms/cadastro.py
- backend/ui/views.py
- backend/ui/urls.py
- backend/ui/static/css/cadastro.css
- backend/ui/templates/login.html
- backend/ui/templates/cadastro_aventureiro/base.html
- backend/ui/templates/cadastro_aventureiro/tipo.html
- backend/ui/templates/cadastro_aventureiro/responsavel.html
- backend/ui/templates/cadastro_aventureiro/lista.html
- backend/ui/templates/cadastro_aventureiro/dados.html
- backend/ui/templates/cadastro_aventureiro/ficha.html
- backend/ui/templates/cadastro_aventureiro/termo.html
- backend/ui/templates/cadastro_aventureiro/revisao.html

#### 🔗 Relacionado a
- feature: cadastro guiado do aventureiro

#### ⚠️ Impacto / Observações
- Novo fluxo guiado completo acessível da tela de login; mantém rastreabilidade das pendências e impede finalizar sem preencher tudo.
- O app `members` agora centraliza o domínio dos registros e pode alimentar APIs e diagnósticos futuros.
- O wizard persiste assinaturas e fotos (base64), garantindo rascunhos e revisões antes da finalização.

---

### 🎯 Alteração Nº 0020
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> Cliente pediu adaptar o layout do wizard ao padrão da tela de login, incluir tamanhos infantis de camiseta (2 a 12) e reforçar que o passo do responsável exige preenchimento completo e preenchimento automático para o responsável legal.

#### ✅ O que foi feito
- Estilizei a tela de cadastro para espelhar o cartão moderno da tela de login e garantir responsividade mobile.
- Inserimos script que copia dados do pai/mãe para o responsável legal, marca campos preenchidos automaticamente e evita que o formulário avance sem os campos obrigatórios.
- Adicionei as opções de tamanho 02 a 12 e tonifiquei o estilo das mensagens de erro do formulário.

#### 📁 Arquivos afetados
- backend/apps/members/models.py
- backend/ui/forms/cadastro.py
- backend/ui/static/css/cadastro.css
- backend/ui/templates/cadastro_aventureiro/base.html

#### 🔗 Relacionado a
- feature: usabilidade e responsividade do cadastro guiado

#### ⚠️ Impacto / Observações
- O wizard agora exige os campos obrigatórios do responsável, exibe indicadores claros de preenchimento automático e permanece utilizável em telas pequenas.
- As novas opções de camiseta cobrem o público infantil e facilitam futuras integrações com relatórios de uniformes.

---

### 🎯 Alteração Nº 0021
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> O responsável estava liberado para avançar sem aceitar a declaração ou registrar a assinatura digital da tela, o que viola a obrigatoriedade jurídica do cadastro.

#### ✅ O que foi feito
- Ajustado o `ResponsibleForm` para bloquear o avanço quando a declaração não for confirmada ou a assinatura digital estiver vazia, mantendo permissão para salvar rascunho.

#### 📁 Arquivos afetados
- backend/ui/forms/cadastro.py

#### 🔗 Relacionado a
- feature: validação do cadastro guiado

#### ⚠️ Impacto / Observações
- Agora é impossível salvar/continuar sem o obrigado aceite legal e sem o trace da assinatura, alinhando o fluxo com a exigência jurídica do termo.

---

### 🎯 Alteração Nº 0022
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> O usuário ainda conseguia avançar nas etapas seguintes sem preencher foto, camiseta, declaração médica ou termo, o que compromete o checklist completo.

#### ✅ O que foi feito
- Ajustei os formulários do aventureiro (foto, camiseta, assinatura), da ficha médica (campos obrigatórios, declaração, assinatura, tipo sanguíneo e motivo de internação) e do termo (deve marcar e assinar) para falhar a validação quando usados com “Salvar e continuar”.

#### 📁 Arquivos afetados
- backend/ui/forms/cadastro.py

#### 🔗 Relacionado a
- feature: validações do fluxo guiado

#### ⚠️ Impacto / Observações
- As etapas agora bloqueiam o avanço até que todos os campos críticos estejam preenchidos, mantendo o checklist organizado e juridicamente válido.

---

### 🎯 Alteração Nº 0023
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> A barra de progresso visual permanecia igual ao avançar pelas etapas, confundindo o usuário sobre qual fase estava ativa.

#### ✅ O que foi feito
- Ajustei o CSS dos passos do wizard para que os anteriores geometrizados fiquem verdes e os passos atuais ganhem fundo em gradient e sombra, dando feedback claro de progresso.

#### 📁 Arquivos afetados
- backend/ui/static/css/cadastro.css

#### 🔗 Relacionado a
- feature: indicativo visual do wizard

#### ⚠️ Impacto / Observações
- Agora o topo muda claramente de aparência conforme o usuário avança, deixando mais evidente qual etapa está ativa.
---

### 🎯 Alteração Nº 0024
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> O progresso no topo não atualizava visualmente porque a classe dos passos era recalculada de forma incorreta, então todos continuavam com o mesmo estilo mesmo mudando de etapa.

#### ✅ O que foi feito
- Simplifiquei o bloco do wizard para renderizar explicitamente `step`, `is-current` e `is-complete` conforme o índice atual, garantindo que cada etapa herde o estilo esperado sem dependência de `with` encadeados.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html

#### 🔗 Relacionado a
- feature: indicador visual do wizard

#### ⚠️ Impacto / Observações
- Agora o progresso reflete corretamente o índice atual logo quando a página for renderizada, evitando confusões sobre qual etapa está ativa.
-

--- 

### 🎯 Alteração Nº 0025
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> Diante do novo layout, a área “Pendências detectadas” desapareceu na etapa “Escolha do cadastro”, deixando o usuário sem visão da checklist inicial.

#### ✅ O que foi feito
- Passei a renderizar o bloco de pendências também durante a etapa inicial sempre que existirem alertas, mantendo o topo limpo mas ainda informativo antes mesmo de entrar nos formulários.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html

#### 🔗 Relacionado a
- feature: visibilidade de pendências

#### ⚠️ Impacto / Observações
- Agora é possível ver os alertas pendentes desde a primeira tela, o que ajuda a comunicar as obrigações antes de iniciar o fluxo.
---

### 🎯 Alteração Nº 0026
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> Após habilitar o destaque visual das etapas, a área de “Pendências detectadas” aparecia apenas quando havia itens e desaparecia totalmente ao limpar o checklist, deixando o topo sem informações.

#### ✅ O que foi feito
- Mantive o bloco de pendências sempre presente (tanto na etapa de escolha quanto nas demais), exibindo uma mensagem padrão “Nenhuma pendência no momento” quando não há itens, para nunca deixar o topo em branco.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html

#### 🔗 Relacionado a
- feature: visibilidade persistente de pendências

#### ⚠️ Impacto / Observações
- Mesmo que não existam pendências ativas, o usuário vê imediatamente a área de checklist, reforçando os próximos passos sem criar falsos vazios visuais.
-

---

### 🎯 Alteração Nº 0027
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> A tela inicial “Escolha do cadastro” voltou a ficar poluída após exibirmos o resumo das pendências e o usuário pediu o layout limpo como o card original.

#### ✅ O que foi feito
- Mantive o painel de pendências apenas nas demais etapas do wizard, removendo-o da primeira tela para reproduzir o visual compacto de “Escolha do cadastro”, mantendo a lógica de renderizar pendências assim que o usuário sair dessa etapa.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html

#### 🔗 Relacionado a
- feature: aparências do wizard

#### ⚠️ Impacto / Observações
- O topo fica limpo na fase inicial, reaparecendo pendências a partir da etapa seguinte, sem perder o checklist quando o usuário estiver preenchendo os formulários.
---

### 🎯 Alteração Nº 0028
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> Mesmo com o bloco de pendências visível, o usuário não conseguia saber qual era o problema real quando a lista estava vazia mas o formulário bloqueava a etapa (ex.: assinatura ausente).

#### ✅ O que foi feito
- Aproveitei os erros do formulário para alimentar o bloco de pendências quando não houver pendências detectadas ainda, garantindo que mensagens como “Assine o termo” apareçam no topo mesmo antes de salvar os dados.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html
- backend/ui/views.py

#### 🔗 Relacionado a
- feature: visibilidade de erros do wizard

#### ⚠️ Impacto / Observações
- A seção de pendências agora também mostra os erros do formulário atual, evitando que o topo reporte “nenhuma pendência” enquanto o formulário ainda exige ação.
---

### 🎯 Alteração Nº 0029
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> O responsável não via nenhum feedback visual indicando que a declaração havia sido confirmada, o que podia gerar dúvida mesmo após marcar a checkbox.

#### ✅ O que foi feito
- Adicionei um indicador “Não confirmado / Confirmado” ao lado da checkbox de declaração e atualizei o script para trocar o texto e a cor assim que o responsável marcar/desmarcar o campo.

#### 📁 Arquivos afetados
- backend/ui/static/css/cadastro.css
- backend/ui/templates/cadastro_aventureiro/base.html
- backend/ui/templates/cadastro_aventureiro/responsavel.html

#### 🔗 Relacionado a
- feature: feedback visual da declaração

#### ⚠️ Impacto / Observações
- O usuário agora vê imediatamente o status jurídico da declaração, reforçando que marcar a checkbox é obrigatório e visível.
---

### 🎯 Alteração Nº 0030
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🗂️ Contexto
> O formulário do aventureiro ainda exigia input manual para a data, não permitia selecionar mais de uma classe e os rótulos eram pequenos demais para uso em telas grandes.

#### ✅ O que foi feito
- Troquei o campo de data para um `DateInput`, permitindo usar o seletor nativo.  
- Transformei “Classes investidas” em múltipla escolha (checkboxes) com suporte para várias classes e armazeno o resultado em JSON no modelo.  
- Ampliei a tipografia dos labels para `1.05rem` e criei um grupo visual para os checkboxes.  
- Adicionei migração (`0002_alter_adventurer_invested_class_and_more.py`) para refletir a mudança no campo `invested_class`.

#### 📁 Arquivos afetados
- backend/apps/members/models.py  
- backend/apps/members/migrations/0002_alter_adventurer_invested_class_and_more.py  
- backend/ui/forms/cadastro.py  
- backend/ui/static/css/cadastro.css  
- backend/ui/templates/cadastro_aventureiro/responsavel.html  
- backend/ui/templates/cadastro_aventureiro/base.html

#### 🔗 Relacionado a
- feature: usabilidade do cadastro

#### ⚠️ Impacto / Observações
- A tela agora aceita datas com o picker do navegador, permite 0+ classes investidas e mantém os campos mais legíveis; a nova migração atualiza o schema para armazenar múltiplas classes.
---

### 🎯 Alteração Nº 0031
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** bugfix  

#### 📌 Contexto
> Os campos de texto da ficha m�dica permitiam redimensionamento livre via cantos do textarea, o que desorganizava o grid e deixava o layout inst�vel quando o usu�rio passava o cursor pela borda.

#### 🛠ï¸ O que foi feito
- Padronizei os grids dos blocos da ficha m�dica para manter `display: grid` com `gap` uniforme, igualando o alinhamento � outras se��es.
- Ajustei os textarea para altura m�nima consistente e limitei o redimensionamento ao eixo vertical, impedindo altera��es horizontais.

#### 📁 Arquivos afetados
- backend/ui/static/css/cadastro.css

#### 🔗 Relacionado a
- bug: campos da ficha m�dica mudavam de tamanho ao arrastar o canto do textarea

#### â ï¸ Impacto / Observações
- Layout permanece est�vel com colunas regulares.
- Usu�rio perde o comportamento estranho de redimensionar horizontalmente ao passar o mouse pela borda.
