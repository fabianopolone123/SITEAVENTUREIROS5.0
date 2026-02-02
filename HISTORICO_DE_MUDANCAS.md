# Ã°ÂŸÂ§Â¾ HISTÃƒÂ“RICO DE MUDANÃƒÂ‡AS DO PROJETO

Ã°ÂŸÂ“ÂŒ **Arquivo obrigatÃƒÂ³rio de leitura antes de qualquer alteraÃƒÂ§ÃƒÂ£o no cÃƒÂ³digo**

Este documento mantÃƒÂ©m o **registro cronolÃƒÂ³gico e tÃƒÂ©cnico** de TODAS as mudanÃƒÂ§as feitas no projeto.  
Ele existe para:

- recuperar contexto quando o Codex perder a memÃƒÂ³ria
- entender **o que foi feito, por quÃƒÂª e onde**
- evitar retrabalho
- facilitar diagnÃƒÂ³stico de bugs
- ajudar novos ciclos de desenvolvimento

---

## Ã¢ÂšÂ Ã¯Â¸Â REGRA DE OURO (OBRIGATÃƒÂ“RIA)

Antes de:
- alterar cÃƒÂ³digo
- criar arquivos
- remover arquivos
- mudar comportamento
- refatorar
- corrigir bug

Ã°ÂŸÂ‘Â‰ **LER este arquivo do comeÃƒÂ§o ao fim**

Depois de qualquer mudanÃƒÂ§a:  
Ã°ÂŸÂ‘Â‰ **REGISTRAR A MUDANÃƒÂ‡A AQUI**

---

## Ã°ÂŸÂ§Â  COMO O CODEX DEVE USAR ESTE ARQUIVO

Para **CADA modificaÃƒÂ§ÃƒÂ£o feita**, o Codex DEVE registrar:

1. O que foi feito  
2. Por que foi feito  
3. Quais arquivos foram alterados  
4. Qual impacto esperado  
5. Se existe risco ou dependÃƒÂªncia  

Regras:
- Sempre escrever em **UTF-8 com caracteres portugueses**
- Nunca escrever frases vagas como:
  - Ã¢ÂÂŒ Ã¢Â€Âœajustes geraisÃ¢Â€Â
  - Ã¢ÂÂŒ Ã¢Â€ÂœmelhoriasÃ¢Â€Â
  - Ã¢ÂÂŒ Ã¢Â€ÂœrefatoraÃƒÂ§ÃƒÂ£oÃ¢Â€Â
- Sempre ser **explÃƒÂ­cito e tÃƒÂ©cnico**

---

## Ã°ÂŸÂ—Â‚Ã¯Â¸Â MODELO PADRÃƒÂƒO DE REGISTRO (OBRIGATÃƒÂ“RIO)

Copiar e preencher exatamente este modelo:

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº XXXX
**Data:** YYYY-MM-DD  
**Autor:** Codex / Humano  
**Tipo:** feature | bugfix | refactor | infra | diagnÃƒÂ³stico | seguranÃƒÂ§a  

#### Ã°ÂŸÂ“ÂŒ Contexto
> Por que essa alteraÃƒÂ§ÃƒÂ£o foi necessÃƒÂ¡ria?

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- item 1
- item 2
- item 3

#### Ã°ÂŸÂ“Â Arquivos afetados
- caminho/arquivo.ext
- caminho/arquivo.ext

#### Ã°ÂŸÂ”Â— Relacionado a
- feature: nome  
- bug: descriÃƒÂ§ÃƒÂ£o  
- diagnÃƒÂ³stico: trace_id / request_id (se houver)

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- impacto funcional
- impacto em diagnÃƒÂ³stico
- impacto em performance
- riscos conhecidos

---

## Ã°ÂŸÂ“Âœ HISTÃƒÂ“RICO DE ALTERAÃƒÂ‡ÃƒÂ•ES
> As alteraÃƒÂ§ÃƒÂµes devem ser adicionadas **sempre no final do arquivo**

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº 0001
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** arquitetura / diagnÃƒÂ³stico  

#### Ã°ÂŸÂ“ÂŒ Contexto
CriaÃƒÂ§ÃƒÂ£o da base documental do sistema autodiagnosticÃƒÂ¡vel para evitar perda de contexto e permitir que o Codex se reoriente apÃƒÂ³s reset de memÃƒÂ³ria.

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- Definido padrÃƒÂ£o de arquitetura autodiagnosticÃƒÂ¡vel
- Criado documento `DIAGNOSTICO_AUTODIAGNOSTICAVEL.md`
- Definido uso de Next.js + Django + PostgreSQL
- Definido modelo `diagnostic_events`
- Definido fluxo de `request_id`, `trace_id` e `session_id`

#### Ã°ÂŸÂ“Â Arquivos afetados
- DIAGNOSTICO_AUTODIAGNOSTICAVEL.md
- HISTORICO_DE_MUDANCAS.md

#### Ã°ÂŸÂ”Â— Relacionado a
- DiagnÃƒÂ³stico do sistema
- PersistÃƒÂªncia de contexto do projeto

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- Nenhuma mudanÃƒÂ§a funcional
- Base estrutural do projeto criada
- Documento deve ser tratado como fonte da verdade

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº 0002
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** feature  

#### Ã°ÂŸÂ“ÂŒ Contexto
Implantar a tela de login do frontend com o estilo fornecido e garantir o logo oficial no local correto para a interface.

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- Criada a base Next.js dentro de `frontend/`
- Definido layout global (`app/layout.tsx`) e estilos compartilhados
- ConstruÃƒÂ­da a pÃƒÂ¡gina de login (`app/page.tsx`) conforme mock visual
- Movido `logo.png` para `frontend/public/` e referenciado na tela

#### Ã°ÂŸÂ“Â Arquivos afetados
- frontend/package.json
- frontend/tsconfig.json
- frontend/next.config.js
- frontend/next-env.d.ts
- frontend/app/layout.tsx
- frontend/app/globals.css
- frontend/app/page.tsx
- frontend/public/logo.png

#### Ã°ÂŸÂ”Â— Relacionado a
- feature: tela de login

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- Estrutura inicial do frontend criada
- Interface pronta para futura autenticaÃƒÂ§ÃƒÂ£o
- Frontend alinhado ÃƒÂ  arquitetura backend-first

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº 0003
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** feature  

#### Ã°ÂŸÂ“ÂŒ Contexto
Iniciar o backend Django conforme a arquitetura backend-first e garantir um esqueleto extensÃƒÂ­vel.

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- Configurado core do Django (`settings`, `urls`, `asgi`, `wsgi`)
- Criadas pastas de apps (accounts, members, documents, store, payments, notifications, diagnostics)
- Criados mÃƒÂ³dulos base de diagnÃƒÂ³sticos, integraÃƒÂ§ÃƒÂµes, workers e utilitÃƒÂ¡rios
- Documentadas dependÃƒÂªncias iniciais

#### Ã°ÂŸÂ“Â Arquivos afetados
- backend/manage.py
- backend/config/*
- backend/apps/*
- backend/diagnostics/*
- backend/integrations/*
- backend/workers/*
- backend/common/*
- backend/requirements/base.txt

#### Ã°ÂŸÂ”Â— Relacionado a
- feature: backend Django inicial

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- Base do backend criada
- Ainda sem regras de negÃƒÂ³cio ou modelos reais

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº 0004
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** infra  

#### Ã°ÂŸÂ“ÂŒ Contexto
Falha de importaÃƒÂ§ÃƒÂ£o de `backend.diagnostics` ao executar `manage.py runserver` dentro da pasta backend.

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- Criado `backend/__init__.py`
- Ajustado `manage.py` para inserir o diretÃƒÂ³rio raiz no `sys.path`

#### Ã°ÂŸÂ“Â Arquivos afetados
- backend/__init__.py
- backend/manage.py

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- Imports passam a funcionar independentemente do diretÃƒÂ³rio atual

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº 0005
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** infra  

#### Ã°ÂŸÂ“ÂŒ Contexto
Django bloqueava acesso via `127.0.0.1` por nÃƒÂ£o estar em `ALLOWED_HOSTS`.

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- Ajustado `ALLOWED_HOSTS` para aceitar `127.0.0.1` por padrÃƒÂ£o

#### Ã°ÂŸÂ“Â Arquivos afetados
- backend/config/settings.py

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- `runserver` funciona corretamente em ambiente local

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº 0006
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** infra  

#### Ã°ÂŸÂ“ÂŒ Contexto
A rota raiz `/` retornava 404.

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- Criada resposta padrÃƒÂ£o na rota raiz informando que o backend estÃƒÂ¡ ativo

#### Ã°ÂŸÂ“Â Arquivos afetados
- backend/config/urls.py

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- Facilita testes manuais e validaÃƒÂ§ÃƒÂ£o do ambiente

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº 0007
**Data:** 2026-02-01  
**Autor:** Codex  
**Tipo:** feature  

#### Ã°ÂŸÂ“ÂŒ Contexto
Necessidade de exibir a tela de login sem depender do Next.js.

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- Criado template `login.html` no backend
- Criado CSS especÃƒÂ­fico para a tela de login
- Configurado Django para servir templates e arquivos estÃƒÂ¡ticos
- Rota raiz passou a renderizar a tela de login

#### Ã°ÂŸÂ“Â Arquivos afetados
- backend/config/settings.py
- backend/config/urls.py
- backend/templates/login.html
- backend/static/css/login.css
- backend/static/images/logo.png

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- Backend passa a exibir UI funcional sem frontend separado

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº 0009
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** infra  

#### Ã°ÂŸÂ“ÂŒ Contexto
O backend nÃƒÂ£o possuÃƒÂ­a bootstrap completo para execuÃƒÂ§ÃƒÂ£o do Django.

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- Criada estrutura completa de `backend/config`
- Criado `manage.py` no root do projeto
- Garantido `backend/__init__.py`

#### Ã°ÂŸÂ“Â Arquivos afetados
- backend/__init__.py
- backend/config/settings.py
- backend/config/urls.py
- backend/config/wsgi.py
- backend/config/asgi.py
- manage.py

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- Django pode ser iniciado corretamente
- Base pronta para expansÃƒÂ£o

---

### Ã°ÂŸÂ”Â„ AlteraÃƒÂ§ÃƒÂ£o NÃ‚Âº 0010
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### Ã°ÂŸÂ“ÂŒ Contexto
Refinar a tela de login do backend para espelhar o mock visual.

#### Ã°ÂŸÂ›Â Ã¯Â¸Â O que foi feito
- Reescrito template de login com layout em cartÃƒÂ£o central
- Aplicado degradÃƒÂª claro, sombras suaves e botÃƒÂµes arredondados
- Ajustada responsividade para mobile

#### Ã°ÂŸÂ“Â Arquivos afetados
- backend/ui/templates/login.html
- backend/ui/static/css/login.css

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃƒÂ§ÃƒÂµes
- UI alinhada ao mock
- Pronta para receber autenticaÃƒÂ§ÃƒÂ£o real

---


---

### AlteraÃ§Ã£o NÂº 0014
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### Contexto
> A solicitaÃ§Ã£o pediu para apagar o estilo atual e reescrever a tela de login com um padrÃ£o moderno consistente com o mock.

#### O que foi feito
- SubstituÃ­ totalmente `backend/ui/static/css/login.css` por uma nova folha de estilo: fundo degradÃª, cartÃ£o elevado, linhas decorativas, halo do logo maior e inputs/botÃµes com gradient suave.
- Mantive o template (`backend/ui/templates/login.html`) e acentuei o halo para garantir que o logo esteja sempre centralizado no cartÃ£o.

#### Arquivos afetados
- backend/ui/static/css/login.css
- backend/ui/templates/login.html

#### Relacionado a
- feature: tela de login

Aviso: Impacto / ObservaÃ§Ãµes
- A interface ficou com efeitos modernos e o logo nÃ£o Ã© mais cortado; validaÃ§Ãµes futuras devem considerar o novo visual.


---

### AlteraÃ§Ã£o NÂº 0015
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### Contexto
> O estilo anterior da tela de login precisava ser apagado e recriado sob um novo padrÃ£o mais harmÃ´nico e moderno.

#### O que foi feito
- Eliminei o CSS antigo em `backend/ui/static/css/login.css` e inseri um novo conjunto totalmente reescrito com degradÃª de fundo, cartÃ£o elevado, halo amplo do logo, inputs com bordas suaves e botÃ£o gradient.
- Mantive o template do cartÃ£o, reforÃ§ando o halo para manter o logo completo.

#### Arquivos afetados
- backend/ui/static/css/login.css
- backend/ui/templates/login.html

#### Relacionado a
- feature: tela de login

Aviso: Impacto / ObservaÃ§Ãµes
- A experiÃªncia visual virou um layout limpo e moderno compatÃ­vel com o mock e alinhado ao padrÃ£o backend-first.


---

### AlteraÃ§Ã£o NÂº 0016
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### Contexto
> O logo ainda aparecia cortado no topo, portanto precisei ajustar o cartÃ£o para dar espaÃ§o suficiente.

#### O que foi feito
- Aumentei o `padding-top` do cartÃ£o (`backend/ui/static/css/login.css`) e removi o `overflow: hidden`.
- Ajustei a margem negativa e o padding de `.logo-shell` para que a parte branca do medalhÃ£o fique totalmente visÃ­vel acima do formulÃ¡rio.

#### Arquivos afetados
- backend/ui/static/css/login.css

#### Relacionado a
- refactor: UI

Aviso: Impacto / ObservaÃ§Ãµes
- O logo agora fica livre de cortes e o halo respira; o layout continua alinhado com o mock.


---

### AlteraÃ§Ã£o NÂº 0017
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### Contexto
> O halo ao redor do logo ainda se elevava demais e aparecia acima do cartÃ£o.

#### O que foi feito
- Ajustei `.logo-shell` em `backend/ui/static/css/login.css` para 200px com margem negativa menor, mantendo o halo mas impedindo que ele sobressaia acima do cartÃ£o.

#### Arquivos afetados
- backend/ui/static/css/login.css

#### Relacionado a
- refactor: UI

Aviso: Impacto / ObservaÃ§Ãµes
- O logo volta a ficar centrado dentro do cartÃ£o, mantendo o novo visual moderno.


---

### AlteraÃ§Ã£o NÂº 0018
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### Contexto
> O estilo ainda precisava ser repensado do zero, conforme pedido.

#### O que foi feito
- Reescrevi totalmente `backend/ui/static/css/login.css` com um novo padrÃ£o (fundo degradÃª com partÃ­culas suaves, cartÃ£o elevado, halo do logo maior, inputs com bordas reversas e botÃ£o gradient).
- Mantive o template do formulÃ¡rio e deixei o halo maior para garantir o logo completo.

#### Arquivos afetados
- backend/ui/static/css/login.css
- backend/ui/templates/login.html

#### Relacionado a
- feature: tela de login

Aviso: Impacto / ObservaÃ§Ãµes
- A tela agora tem efeito mais moderno, e a marca Ã© plenamente visÃ­vel.


---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0019
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> Cliente pediu o fluxo guiado â€œCadastrar Aventureiroâ€ acessÃ­vel via â€œCadastre-seâ€, com sete telas, reutilizaÃ§Ã£o de dados, validaÃ§Ã£o por etapa, pendÃªncias visuais, assinaturas digitais e bloqueio da finalizaÃ§Ã£o atÃ© que tudo esteja completo.

#### âœ… O que foi feito
- Criado o app `backend.apps.members` com os modelos `Responsible`, `Adventurer`, `MedicalRecord` e `ImageReleaseTerm`, serviÃ§os de status/pendÃªncias e migraÃ§Ã£o inicial.
- Atualizadas as configuraÃ§Ãµes do Django (`settings`, `urls`) para registrar o app, habilitar sessÃµes e servir mÃ­dia.
- Criados formulÃ¡rios de rascunho (pai, mÃ£e, responsÃ¡vel, aventureiro, ficha mÃ©dica e termo) e views que orquestram as sete etapas, salvam rascunhos, validam cada etapa, registram assinaturas baseadas em canvas e acompanham o progresso.
- ConstruÃ­das as novas telas sob `backend/ui/templates/cadastro_aventureiro/`, adicionando o layout base, etapas especÃ­ficas, resumo de pendÃªncias, link â€œCadastre-seâ€ no login e estilos em `cadastro.css`.
- Salvaguardado o salvamento parcial das etapas e mantido o status visual/pendÃªncias via serviÃ§o central.

#### ðŸ“ Arquivos afetados
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

#### ðŸ”— Relacionado a
- feature: cadastro guiado do aventureiro

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- Novo fluxo guiado completo acessÃ­vel da tela de login; mantÃ©m rastreabilidade das pendÃªncias e impede finalizar sem preencher tudo.
- O app `members` agora centraliza o domÃ­nio dos registros e pode alimentar APIs e diagnÃ³sticos futuros.
- O wizard persiste assinaturas e fotos (base64), garantindo rascunhos e revisÃµes antes da finalizaÃ§Ã£o.

---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0020
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> Cliente pediu adaptar o layout do wizard ao padrÃ£o da tela de login, incluir tamanhos infantis de camiseta (2 a 12) e reforÃ§ar que o passo do responsÃ¡vel exige preenchimento completo e preenchimento automÃ¡tico para o responsÃ¡vel legal.

#### âœ… O que foi feito
- Estilizei a tela de cadastro para espelhar o cartÃ£o moderno da tela de login e garantir responsividade mobile.
- Inserimos script que copia dados do pai/mÃ£e para o responsÃ¡vel legal, marca campos preenchidos automaticamente e evita que o formulÃ¡rio avance sem os campos obrigatÃ³rios.
- Adicionei as opÃ§Ãµes de tamanho 02 a 12 e tonifiquei o estilo das mensagens de erro do formulÃ¡rio.

#### ðŸ“ Arquivos afetados
- backend/apps/members/models.py
- backend/ui/forms/cadastro.py
- backend/ui/static/css/cadastro.css
- backend/ui/templates/cadastro_aventureiro/base.html

#### ðŸ”— Relacionado a
- feature: usabilidade e responsividade do cadastro guiado

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- O wizard agora exige os campos obrigatÃ³rios do responsÃ¡vel, exibe indicadores claros de preenchimento automÃ¡tico e permanece utilizÃ¡vel em telas pequenas.
- As novas opÃ§Ãµes de camiseta cobrem o pÃºblico infantil e facilitam futuras integraÃ§Ãµes com relatÃ³rios de uniformes.

---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0021
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> O responsÃ¡vel estava liberado para avanÃ§ar sem aceitar a declaraÃ§Ã£o ou registrar a assinatura digital da tela, o que viola a obrigatoriedade jurÃ­dica do cadastro.

#### âœ… O que foi feito
- Ajustado o `ResponsibleForm` para bloquear o avanÃ§o quando a declaraÃ§Ã£o nÃ£o for confirmada ou a assinatura digital estiver vazia, mantendo permissÃ£o para salvar rascunho.

#### ðŸ“ Arquivos afetados
- backend/ui/forms/cadastro.py

#### ðŸ”— Relacionado a
- feature: validaÃ§Ã£o do cadastro guiado

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- Agora Ã© impossÃ­vel salvar/continuar sem o obrigado aceite legal e sem o trace da assinatura, alinhando o fluxo com a exigÃªncia jurÃ­dica do termo.

---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0022
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> O usuÃ¡rio ainda conseguia avanÃ§ar nas etapas seguintes sem preencher foto, camiseta, declaraÃ§Ã£o mÃ©dica ou termo, o que compromete o checklist completo.

#### âœ… O que foi feito
- Ajustei os formulÃ¡rios do aventureiro (foto, camiseta, assinatura), da ficha mÃ©dica (campos obrigatÃ³rios, declaraÃ§Ã£o, assinatura, tipo sanguÃ­neo e motivo de internaÃ§Ã£o) e do termo (deve marcar e assinar) para falhar a validaÃ§Ã£o quando usados com â€œSalvar e continuarâ€.

#### ðŸ“ Arquivos afetados
- backend/ui/forms/cadastro.py

#### ðŸ”— Relacionado a
- feature: validaÃ§Ãµes do fluxo guiado

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- As etapas agora bloqueiam o avanÃ§o atÃ© que todos os campos crÃ­ticos estejam preenchidos, mantendo o checklist organizado e juridicamente vÃ¡lido.

---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0023
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> A barra de progresso visual permanecia igual ao avanÃ§ar pelas etapas, confundindo o usuÃ¡rio sobre qual fase estava ativa.

#### âœ… O que foi feito
- Ajustei o CSS dos passos do wizard para que os anteriores geometrizados fiquem verdes e os passos atuais ganhem fundo em gradient e sombra, dando feedback claro de progresso.

#### ðŸ“ Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ðŸ”— Relacionado a
- feature: indicativo visual do wizard

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- Agora o topo muda claramente de aparÃªncia conforme o usuÃ¡rio avanÃ§a, deixando mais evidente qual etapa estÃ¡ ativa.
---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0024
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> O progresso no topo nÃ£o atualizava visualmente porque a classe dos passos era recalculada de forma incorreta, entÃ£o todos continuavam com o mesmo estilo mesmo mudando de etapa.

#### âœ… O que foi feito
- Simplifiquei o bloco do wizard para renderizar explicitamente `step`, `is-current` e `is-complete` conforme o Ã­ndice atual, garantindo que cada etapa herde o estilo esperado sem dependÃªncia de `with` encadeados.

#### ðŸ“ Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html

#### ðŸ”— Relacionado a
- feature: indicador visual do wizard

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- Agora o progresso reflete corretamente o Ã­ndice atual logo quando a pÃ¡gina for renderizada, evitando confusÃµes sobre qual etapa estÃ¡ ativa.
-

--- 

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0025
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> Diante do novo layout, a Ã¡rea â€œPendÃªncias detectadasâ€ desapareceu na etapa â€œEscolha do cadastroâ€, deixando o usuÃ¡rio sem visÃ£o da checklist inicial.

#### âœ… O que foi feito
- Passei a renderizar o bloco de pendÃªncias tambÃ©m durante a etapa inicial sempre que existirem alertas, mantendo o topo limpo mas ainda informativo antes mesmo de entrar nos formulÃ¡rios.

#### ðŸ“ Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html

#### ðŸ”— Relacionado a
- feature: visibilidade de pendÃªncias

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- Agora Ã© possÃ­vel ver os alertas pendentes desde a primeira tela, o que ajuda a comunicar as obrigaÃ§Ãµes antes de iniciar o fluxo.
---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0026
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> ApÃ³s habilitar o destaque visual das etapas, a Ã¡rea de â€œPendÃªncias detectadasâ€ aparecia apenas quando havia itens e desaparecia totalmente ao limpar o checklist, deixando o topo sem informaÃ§Ãµes.

#### âœ… O que foi feito
- Mantive o bloco de pendÃªncias sempre presente (tanto na etapa de escolha quanto nas demais), exibindo uma mensagem padrÃ£o â€œNenhuma pendÃªncia no momentoâ€ quando nÃ£o hÃ¡ itens, para nunca deixar o topo em branco.

#### ðŸ“ Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html

#### ðŸ”— Relacionado a
- feature: visibilidade persistente de pendÃªncias

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- Mesmo que nÃ£o existam pendÃªncias ativas, o usuÃ¡rio vÃª imediatamente a Ã¡rea de checklist, reforÃ§ando os prÃ³ximos passos sem criar falsos vazios visuais.
-

---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0027
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> A tela inicial â€œEscolha do cadastroâ€ voltou a ficar poluÃ­da apÃ³s exibirmos o resumo das pendÃªncias e o usuÃ¡rio pediu o layout limpo como o card original.

#### âœ… O que foi feito
- Mantive o painel de pendÃªncias apenas nas demais etapas do wizard, removendo-o da primeira tela para reproduzir o visual compacto de â€œEscolha do cadastroâ€, mantendo a lÃ³gica de renderizar pendÃªncias assim que o usuÃ¡rio sair dessa etapa.

#### ðŸ“ Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html

#### ðŸ”— Relacionado a
- feature: aparÃªncias do wizard

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- O topo fica limpo na fase inicial, reaparecendo pendÃªncias a partir da etapa seguinte, sem perder o checklist quando o usuÃ¡rio estiver preenchendo os formulÃ¡rios.
---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0028
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> Mesmo com o bloco de pendÃªncias visÃ­vel, o usuÃ¡rio nÃ£o conseguia saber qual era o problema real quando a lista estava vazia mas o formulÃ¡rio bloqueava a etapa (ex.: assinatura ausente).

#### âœ… O que foi feito
- Aproveitei os erros do formulÃ¡rio para alimentar o bloco de pendÃªncias quando nÃ£o houver pendÃªncias detectadas ainda, garantindo que mensagens como â€œAssine o termoâ€ apareÃ§am no topo mesmo antes de salvar os dados.

#### ðŸ“ Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/base.html
- backend/ui/views.py

#### ðŸ”— Relacionado a
- feature: visibilidade de erros do wizard

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- A seÃ§Ã£o de pendÃªncias agora tambÃ©m mostra os erros do formulÃ¡rio atual, evitando que o topo reporte â€œnenhuma pendÃªnciaâ€ enquanto o formulÃ¡rio ainda exige aÃ§Ã£o.
---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0029
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> O responsÃ¡vel nÃ£o via nenhum feedback visual indicando que a declaraÃ§Ã£o havia sido confirmada, o que podia gerar dÃºvida mesmo apÃ³s marcar a checkbox.

#### âœ… O que foi feito
- Adicionei um indicador â€œNÃ£o confirmado / Confirmadoâ€ ao lado da checkbox de declaraÃ§Ã£o e atualizei o script para trocar o texto e a cor assim que o responsÃ¡vel marcar/desmarcar o campo.

#### ðŸ“ Arquivos afetados
- backend/ui/static/css/cadastro.css
- backend/ui/templates/cadastro_aventureiro/base.html
- backend/ui/templates/cadastro_aventureiro/responsavel.html

#### ðŸ”— Relacionado a
- feature: feedback visual da declaraÃ§Ã£o

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- O usuÃ¡rio agora vÃª imediatamente o status jurÃ­dico da declaraÃ§Ã£o, reforÃ§ando que marcar a checkbox Ã© obrigatÃ³rio e visÃ­vel.
---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0030
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ðŸ—‚ï¸ Contexto
> O formulÃ¡rio do aventureiro ainda exigia input manual para a data, nÃ£o permitia selecionar mais de uma classe e os rÃ³tulos eram pequenos demais para uso em telas grandes.

#### âœ… O que foi feito
- Troquei o campo de data para um `DateInput`, permitindo usar o seletor nativo.  
- Transformei â€œClasses investidasâ€ em mÃºltipla escolha (checkboxes) com suporte para vÃ¡rias classes e armazeno o resultado em JSON no modelo.  
- Ampliei a tipografia dos labels para `1.05rem` e criei um grupo visual para os checkboxes.  
- Adicionei migraÃ§Ã£o (`0002_alter_adventurer_invested_class_and_more.py`) para refletir a mudanÃ§a no campo `invested_class`.

#### ðŸ“ Arquivos afetados
- backend/apps/members/models.py  
- backend/apps/members/migrations/0002_alter_adventurer_invested_class_and_more.py  
- backend/ui/forms/cadastro.py  
- backend/ui/static/css/cadastro.css  
- backend/ui/templates/cadastro_aventureiro/responsavel.html  
- backend/ui/templates/cadastro_aventureiro/base.html

#### ðŸ”— Relacionado a
- feature: usabilidade do cadastro

#### âš ï¸ Impacto / ObservaÃ§Ãµes
- A tela agora aceita datas com o picker do navegador, permite 0+ classes investidas e mantÃ©m os campos mais legÃ­veis; a nova migraÃ§Ã£o atualiza o schema para armazenar mÃºltiplas classes.
---

### ðŸŽ¯ AlteraÃ§Ã£o NÂº 0031
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** bugfix  

#### ðŸ“Œ Contexto
> Os campos de texto da ficha médica permitiam redimensionamento livre via cantos do textarea, o que desorganizava o grid e deixava o layout instável quando o usuário passava o cursor pela borda.

#### ðŸ› Ã¯Â¸Â O que foi feito
- Padronizei os grids dos blocos da ficha médica para manter `display: grid` com `gap` uniforme, igualando o alinhamento à outras seções.
- Ajustei os textarea para altura mínima consistente e desativei o redimensionamento, mantendo o layout intacto mesmo com o cursor próximo à borda.

#### ðŸ“ Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ðŸ”— Relacionado a
- bug: campos da ficha médica mudavam de tamanho ao arrastar o canto do textarea

#### Ã¢ÂšÂ Ã¯Â¸Â Impacto / ObservaÃ§Ãµes
- Layout permanece estável com colunas regulares e os blocos não saltam quando o textarea recebe foco.
- O formulário agora impede qualquer redimensionamento (horizontal ou vertical), eliminando o comportamento estranho de aumentar o campo ao arrastar o canto.
---

### ?? Alteração Nº 0032
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O layout da ficha médica ainda parecia “quadrado demais” e os campos não estavam alinhados com a proposta retangular moderna das demais seções, então o usuário pediu redistribuição e posicionamento mais limpo.

#### ??? O que foi feito
- Refinei `.ficha-card` para que cada bloco de campos use `display: grid` com `gap` consistente e cada item receba um cartão retangular leve com bordas suaves, sombra e padding uniforme.
- Apliquei estilos específicos aos `label` e aos inputs dentro da ficha médica, deixando-os maiúsculos, mais estreitos e com fundo uniforme escuro-claro para reforçar o formato retangular e o foco visual.
- Padronizei os campos (`input`, `select`, `textarea`) dentro da ficha médica para que mantenham o mesmo preenchimento e sombra, fortalecendo o alinhamento e a sensação de estrutura.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: layout do fluxo de cadastro

#### ?? Impacto / Observações
- Cada campo agora parece um cartão retangular com espaçamento homogêneo e a ficha médica combina visualmente com os outros cards do wizard.
- A leitura dos rótulos e a navegação pelos campos ficaram mais claras sem alterar a lógica funcional do formulário.
---

### ?? Alteração Nº 0033
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O usuário pediu uma reconstrução total da ficha médica: campos retangulares, melhor distribuição e grid consistente com os demais cards do wizard.

#### ??? O que foi feito
- Reescrevi `backend/ui/templates/cadastro_aventureiro/ficha.html` para encerrar cada campo em `<div class="ficha-field">` e usei variações de `.ficha-fields` (`--single`, `--grid`, `--checkbox`) para controlar a dispersão e o comportamento dos campos.
- Criei os estilos `.ficha-fields`, `.ficha-field`, `.ficha-field-input` e `.ficha-field--checkbox` em `backend/ui/static/css/cadastro.css`, definindo cartões retangulares com bordas suaves, sombra, padding uniforme e labels em caixa alta.
- Ajustei os inputs/selects/textarea da ficha médica para manter o mesmo padding e fundo, além de garantir que `textarea` mantenha altura fixa e que os cartões respeitem um gap consistente para preservar a estrutura retangular.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css
- backend/ui/templates/cadastro_aventureiro/ficha.html

#### ?? Relacionado a
- refactor: layout completo da ficha médica

#### ?? Impacto / Observações
- A ficha médica agora se comporta como cartões retangulares alinhados, com espaçamento homogêneo e visual coerente com todo o wizard.
- A usabilidade melhorou sem alterar os fluxos e validações existentes; basta navegar pela página para perceber o novo espaço visual.
---

### ?? Alteração Nº 0034
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> Requisitaram um alinhamento mais fiel ao mock (cartões retangulares com efeitos e linhas preenchidas) e uma distribuição mais harmônica dos campos médicos.

#### ??? O que foi feito
- Ajustei os cartões `.ficha-field` para aplicar gradiente sutil, borda iluminada e sombra suave, além de um hover que eleva o cartão e reforça o contorno.
- Reestilizei `.ficha-field-input` para parecer um bloco retangular preenchido (padding interno, fundo claro, borda suave) enquanto os inputs/selects/textarea ficam transparentes, mantendo o texto alinhado.
- Aproveitei as variações `ficha-fields--grid/--single/--checkbox` para garantir distribuição e alinhamento coerente dos radio buttons verticalmente, como no mock.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css
- backend/ui/templates/cadastro_aventureiro/ficha.html

#### ?? Relacionado a
- refactor: aspecto visual da ficha médica

#### ?? Impacto / Observações
- A ficha médica agora reproduz o layout retangular do exemplo, com linhas preenchidas e um destaque suave ao passar o mouse.
- A visualização dos campos fica mais clara e alinhada, preservando as regras funcionais do formulário.
---

### ?? Alteração Nº 0035
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> A solicitação atual pediu remover todo o CSS adicional aplicado à ficha médica para ver como o layout se comporta sem os efeitos personalizados.

#### ??? O que foi feito
- Apaguei as regras de `.ficha-fields`, `.ficha-field`, `.ficha-field-input` e `.ficha-field--checkbox` do CSS, devolvendo o controle visual ao grid original da página.
- Mantive a marcação do template, mas agora os campos são renderizados com o CSS base (sem efeitos extras), permitindo inspecionar o comportamento padrão.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: ficha médica (experimento visual)

#### ?? Impacto / Observações
- O formulário volta a usar estilos básicos e o mock original fica “desligado” do bloco atual; se precisar restabelecer o visual avançado, basta reintroduzir as classes depois.
---

### ?? Alteração Nº 0036
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O pedido foi tornar a ficha médica responsiva com `display:flex`, removendo caixas internas feias e mantendo caixas retangulares alinhadas às bordas laterais (condições de saúde, alergias, doenças, detalhes dos campos de texto).

#### ??? O que foi feito
- Reestruturei `.ficha-fields` como flex container com flex-wrap e `align-items: stretch`, garantindo que cada `.ficha-field` ocupe metade da largura em desktops e full width em telas menores.
- Apliquei bordas retangulares simples nas caixas, com padding, sombra leve e label com caixa alta para destacar e acompanhei os inputs em blocos transparentes dentro do cartão.
- Mantive o layout dos campos críticos (Condições de saúde, Doenças já tidas, Alergias, Detalhes de outros problemas, detalhes de fraturas/cirurgias/internações) e deixei as caixas alinhadas às bordas direita e esquerda do cartão principal.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: responsividade da ficha médica

#### ?? Impacto / Observações
- A ficha médica agora se adapta a diferentes larguras e as caixas retangulares permanecem coladas às laterais, sem o visual quadrado interno anterior.
- O estilo segue leve e legível, mantendo a lógica sem sobrecarregar a interface.
---

### ?? Alteração Nº 0037
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O usuário pediu remover qualquer ênfase visual e diminuir o tamanho dos campos da ficha médica para um visual mais compacto.

#### ??? O que foi feito
- Reduzi a largura base de `.ficha-field` e o padding interno, fazendo com que cada cartão ocupe cerca de 35% da largura e fique menor em altura.
- Ajustei `.ficha-field-input` para um padding mais enxuto (8px x 10px) e altura mínima menor, preservando a borda retangular sem aumentar o espaço.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: ficha médica compacta

#### ?? Impacto / Observações
- O conjunto de campos ficou mais discreto e compacto, sem alterar o conteúdo ou comportamento.
---

### ?? Alteração Nº 0038
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O cliente quer trocar as caixas por opções “Sim/Não” em texto para a ficha médica e mostrar esses valores como blocos retangulares simples.

#### ??? O que foi feito
- Adicionei regras CSS para `.radio-group` (uso das classes geradas pelo `RadioSelect`) com itens inline, escondendo o controle padrão e desenhando rótulos retangulares com fundo claro e sombra sutil.
- Garanti que o estado ativo (Sim/Não) fique destacado com fundo escuro e texto branco, mantendo o comportamento acessível sem novos widgets JS.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: interação Sim/Não da ficha médica

#### ?? Impacto / Observações
- O formulário agora exibe “Sim” e “Não” como botões textuais retangulares, preservando a lógica do backend e eliminando checkboxes visuais.
---

### ?? Alteração Nº 0039
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> Para testar o comportamento puro, foi solicitado retirar qualquer estilo específico da ficha médica enquanto mantemos o restante do formulário intacto.

#### ??? O que foi feito
- Apaguei as regras relacionadas a `.ficha-fields`, `.ficha-field`, `.ficha-field-input`, `.ficha-field--checkbox`, `.radio-group` e variantes para que a ficha médica volte a usar o CSS base do formulário.
- Mantive os demais estilos globais do `cadastro.css` (responsável, aventureiro, etc.) para que apenas a ficha “perca” o visual customizado.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: ficha médica sem estilo

#### ?? Impacto / Observações
- A ficha médica agora depende exclusivamente do estilo comum do wizard; se quiser reativar os cartões, basta restaurar as regras removidas.
---

### ?? Alteração Nº 0040
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O pedido agora é reduzir os campos de texto da ficha médica sem reativar todo o visual customizado anterior, apenas deixando as caixas menores e mais discretas.

#### ??? O que foi feito
- Acrescentei regras leves para `.ficha-field` e `.ficha-field-input`, definindo margens pequenas, bordas arredondadas e preenchimento enxuto para que os campos fiquem menores e alinhados.
- Limitei o `textarea` a 70px de altura mínima e permiti redimensionamento vertical somente quando necessário, evitando blocos altos demais.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: ficha médica enxuta

#### ?? Impacto / Observações
- Os campos da ficha médica agora usam caixas menores sem reintroduzir todo o estilo pesado anterior, mantendo o restante do formulário intacto.
---

### ?? Alteração Nº 0041
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O textarea corta o espaço interno mas a cor do card continua muito maior; preciso limitar somente o campo de resposta e manter o tom claro ao redor.

#### ??? O que foi feito
- Ajustei `.ficha-field-input` para ter `max-width: 420px` e `align-self: flex-start`, mantendo o cartão claro com base porém limitando o bloco de resposta ao tamanho desejado.\n- Garantir que os próprios inputs/textarea usem `width: 100%` para preencher apenas a área do bloco reduzido.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: campos compactos da ficha médica

#### ?? Impacto / Observações
- Os campos de texto agora ficam inspirados na cor de fundo mas não preenchem o card inteiro; só a própria caixa reduzida fica visível.
---

### ?? Alteração Nº 0042
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> Para alinhar visualmente a ficha médica com as demais seções, foi pedido novamente retornar aos grids base e remover os blocos customizados para que o comportamento fique idêntico ao restante do formulário.

#### ??? O que foi feito
- Atualizei `ficha.html` para usar apenas `field-grid` e `section-card`, eliminando os wrappers `.ficha-field` e mantendo cada label/componente juntos como nas outras etapas.
- O CSS agora não contém regras específicas de `ficha-fields`/`.ficha-field` e os `textarea`/inputs usam os estilos globais da seção padrão, igualando a aparência das caixas de texto.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css
- backend/ui/templates/cadastro_aventureiro/ficha.html

#### ?? Relacionado a
- refactor: ficha médica igual ao restante do formulário

#### ?? Impacto / Observações
- A ficha médica voltou a ter a mesma aparência de linha e caixas que o resto do cadastro, garantindo consistência visual completa.
---

### ?? Alteração Nº 0043
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O textarea da ficha médica ainda ocupava todo o cartão; o objetivo agora é reduzir a caixa de resposta para parecer com as demais linhas.

#### ??? O que foi feito
- Defini regras globais para `textarea` dentro de `.field-grid` (max-width de 420px, altura mínima 60px e largura 100%) para limitar a área de digitação e deixá-la mais compacta.
- Mantive o estilo geral do formulário para que os campos não voltem a ter caixas extras.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: textarea compacto

#### ?? Impacto / Observações
- Os campos agora exibem “linhas” menores e mais alinhadas com as outras seções, mantendo o resto do formulário inalterado.
---

### ?? Alteração Nº 0044
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ?? Contexto
> A ficha médica precisa abranger o histórico completo de doenças solicitado pelo briefing de captação.

#### ??? O que foi feito
- Acrescentei campos booleanos no modelo `MedicalRecord` para cada doença listada, permitindo marcar os casos positivos diretamente.
- Atualizei o template `ficha.html` para renderizar essas opções dentro de um novo bloco de “Histórico de doenças”, mantendo os demais campos dentro dos mesmos `field-grid` usados no resto do cadastro.

#### ?? Arquivos afetados
- backend/apps/members/models.py
- backend/ui/templates/cadastro_aventureiro/ficha.html

#### ?? Relacionado a
- feature: histórico médico detalhado

#### ?? Impacto / Observações
- Agora é possível coletar e exibir todas as doenças do checklist e manter a consistência visual com as demais etapas do formulário.
• Migration members.0003 aplicada para adicionar booleanos do histórico de doenças.
---

### ?? Alteração Nº 0045
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O cliente deseja rever o visual da ficha médica para torná-la mais elegante, com efeitos de gradiente, bordas luminosas e tipografia refinada.

#### ??? O que foi feito
- Reestilizei `.ficha-card` com gradiente radial, borda iluminada, sombras internas e externo, além de cabeçalho maior e texto descritivo refinado.
- Adicionei máscaras com gradiente na borda usando pseudo-elemento para dar o efeito de contorno brilhante sem comprometer o conteúdo.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: visual da ficha médica

#### ?? Impacto / Observações
- A ficha médica agora se destaca como um painel elegante, mantendo o restante do formulário inalterado e preservando o fluxo backend-first.
---

### ?? Alteração Nº 0046
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> Queremos destacar as perguntas da seção “Outras informações”, deixando os textos maiores e as caixas de resposta mais discretas, como no restante do formulário.

#### ??? O que foi feito
- Criei estruturas `question-line` no template `ficha.html` para separar o label do input, colocando o texto em um lado e o campo pequeno no outro, mantendo o mesmo grid geral.
- Adicionei estilos `.question-line`, `.question-label` e `.answer-field` no CSS para engrossar os rótulos, aplicar divisórias suaves e limitar a largura dos inputs/areas.

#### ?? Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/ficha.html
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: questionamento visual da ficha médica

#### ?? Impacto / Observações
- As perguntas agora ocupam mais espaço com fonte maior e o espaço de respostas ficou estreito; o layout segue consistente com o restante da ficha.
---

### ?? Alteração Nº 0047
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O termo de autorização de imagem precisava sair da caixa e ficar centralizado com o texto completo solicitado, com os dados preenchidos automaticamente e visual mais premium.

#### ??? O que foi feito
- Substituí o textarea por um painel customizado (`term-panel`) que inclui o conteúdo do termo completo, preenchendo automaticamente nome, nacionalidade, RG, CPF e endereço do responsável e do aventureiro.
- Estilizei o painel com máscara gradiente, bordas iluminadas, títulos maiores e campos preenchidos destacados, mantendo o restante da página intacto.

#### ?? Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/termo.html
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: termo de autorização

#### ?? Impacto / Observações
- O termo agora aparece como um painel centralizado bonito e completo, com o texto exigido disposto diretamente na página e as confirmações mantendo a assinatura e o checkbox como antes.
---

### ?? Alteração Nº 0048
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> Solicitaram remover o parágrafo inicial redundante do termo e pré-preencher nacionalidade como “Brasileiro”, além de garantir que o campo “nº” (nº da casa) seja o espaço padrão no termo.

#### ??? O que foi feito
- Deletei o parágrafo introdutório sobre a autorização institucional e mantive apenas o título + texto obrigatório do termo.
- Ajustei os campos preenchidos para usar `responsible.nationality` com fallback “Brasileiro” e mantive linha do número da casa associado ao texto (deixando o placeholder como `responsible.address_number`).

#### ?? Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/termo.html

#### ?? Relacionado a
- refactor: termo de autorização minimalista

#### ?? Impacto / Observações
- O termo agora mostra apenas o texto necessário, e os placeholders continuam visíveis quando o dado não estiver preenchido, mas sem reescrever o parágrafo inicial.
- Migration `members.0004_responsible_address_number` criada/aplicada para armazenar o número do endereço do responsável e nada mais.
---

• Campo `address_number` agora aparece no formulário do responsável e na declaração do termo para preencher o número da casa.
- Ajustei o termo para deixar claro a “qualidade de responsável legal” e preencher as nacionalidades com “Brasileiro” quando os campos estiverem vazios.
---

### ?? Alteração Nº 0049
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> Os cards de “Dados do aventureiro” perderam os estilos de grid depois das últimas alterações na ficha médica; precisamos restaurar o visual padrão sem mexer nas partes já ajustadas.

#### ??? O que foi feito
- Reintroduzi a definição completa de `.field-grid` (grid responsivo, gap, margens) e normalizei os estilos básicos de label/input/select/textarea com cores suaves, borda arredondada e foco iluminado.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: grid geral do formulário

#### ?? Impacto / Observações
- Todos os blocos de `field-grid`, inclusive Dados do aventureiro e os campos de termo, voltaram ao layout original e agora exibem a borda/linha consistente com o restante do cadastro.
---

### ?? Alteração Nº 0050
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O campo “Beneficiário do Bolsa Família” precisava ficar mais legível, com os botões “Sim” e “Não” alinhados ao lado do rótulo, como no mock original.

#### ??? O que foi feito
- Ajustei o CSS das `radio-group` dentro de `.field-grid` para que os botões ocupem o mesmo nível do rótulo, com bordas arredondadas, fundo claro e estado ativo escuro, reproduzindo o layout “Não   Sim”.
- Escondi os inputs nativos e estilizei os labels para parecerem botões, mantendo a arrumação em linha uniforme com as demais perguntas.

#### ?? Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: controles de resposta da ficha médica

#### ?? Impacto / Observações
- O campo agora mostra claramente as opções “Não” e “Sim” com destaque e alinhamento, e o resto do formulário continua igual.
---

### ?? Alteração Nº 0051
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> O radio “Possui plano de saúde?” não mostrava qual opção estava marcada porque o widget estava dentro do grid padrão; precisamos uma estrutura onde o Sim/Não apareça junto do label e destaque a escolha.

#### ??? O que foi feito
- Substituí a renderização padrão de `form.has_health_plan` por um bloco `radio-question` com label do campo e cada opção de rádio seguida do próprio label, para que o estilo escuro funcione corretamente.
- Atualizei o CSS para ajustar o alinhamento `.radio-question` (label + botões) sem quebrar o estilo geral e garantir que o clique apareça como esperado.

#### ?? Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/ficha.html
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: interação Sim/Não do plano de saúde

#### ?? Impacto / Observações
- Agora é visível qual opção está marcada (“Sim” ou “Não”) e o campo fica alinhado como nos outros blocos de perguntas.
---

### ?? Alteração Nº 0052
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ?? Contexto
> Valorizar todo o formulário da ficha médica exigiu reescrever o template com seção limpa e novas seções de doenças, alergias, condições e histórico breve.

#### ??? O que foi feito
- Substituí o template `ficha.html` por uma versão nova que organiza o conteúdo em `section-card` por área, usa `field-grid` para inputs e radio buttons e adiciona grid próprio de checkboxes para o histórico de doenças.
- Atualizei o CSS para estilizar esses grids adicionais e manter botões “Sim/Não” e checkboxes aparentes dentro do mesmo layout bonito já aplicado no restante do cadastro.

#### ?? Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/ficha.html
- backend/ui/static/css/cadastro.css

#### ?? Relacionado a
- refactor: ficha médica reescrita

#### ?? Impacto / Observações
- O formulário inteiro agora segue o mesmo padrão visual, com as perguntas e respostas ordenadas por bloco e os checkboxes de doenças alinhados em grade, eliminando o estilo legado anterior.
---

• Ajustei o template para usar os contextos `disease_fields` e `history_fields`, evitando listas literais no HTML e permitindo iterar conforme o view controla os campos.
---

• Corrigi o template para iterar sobre listas de campos já ligados (`disease_fields` e `history_fields`) desde a view, evitando o acesso via `form[fieldname]` no template e eliminando o erro de sintaxe.
---

• Simplifiquei os blocos de radio (“plano de saúde”, “alergias”, “condições”, “usa medicamento”) para renderizar diretamente `{{ form.field }}` dentro de `.radio-group`, evitando loops personalizados e resolvendo o erro de `choice_label`, além de manter o layout alinhado.
---

• Reconstruí integralmente `ficha.html` com o layout textual pedido (título, seções, listas e checkboxes) e mantive o CSS refinado para o painel, garantindo que o formulário fique parecido com o termo.
---

• Reforcei a legenda “(Marque X apenas nas opções positivas)” dentro da seção de doenças para garantir que o texto apareça mesmo após a refatoração do template.
