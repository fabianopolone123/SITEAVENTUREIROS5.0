
---

### ð AlteraÃ§Ã£o NÂº 0056
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> Ajustar o layout das seÃ§Ãµes crÃ­ticas (alergias, medicamentos e procedimentos) para que cada pergunta e campo fiquem alinhados em uma linha Ãºnica, evitando campos gigantes e espaÃ§os soltos.

#### ð ï¸ O que foi feito
- Reescrevi as seÃ§Ãµes de alergias, medicamentos crÃ´nicos e procedimentos recentes para usar o novo componente `field-row` que mantÃ©m o rÃ³tulo e o controle lado a lado em uma Ãºnica linha.
- Acrescentei os estilos de `field-row` no CSS, limitando alturas, aplicando bordas suaves e garantindo que os controles preencham a largura disponÃ­vel sem crescer demais.
- Mantive os demais blocos intactos e preservei o fluxo de assinatura com a nova estrutura sem duplicar seÃ§Ãµes.

#### ð Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/ficha.html
- backend/ui/static/css/cadastro.css

#### ð Relacionado a
- refactor: ficha mÃ©dica refinada

#### â ï¸ Impacto / ObservaÃ§Ãµes
- As seÃ§Ãµes agora ficam compactas e organizadas, tornando evidente a sequÃªncia de perguntas e eliminando campos excessivamente largos.
---

### ð AlteraÃ§Ã£o NÂº 0057
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> Tornei obrigatÃ³rio preencher o detalhe sempre que marcar  Sim nas seÃ§Ãµes crÃ­ticas da ficha mÃ©dica (alergias, medicamentos e procedimentos), garantindo evidÃªncia completa.

#### ð ï¸ O que foi feito
- Atualizei MedicalRecordForm.clean() para exigir os campos de notas/detalhes sempre que o booleano associado estiver em True (alergias, outros problemas, problemas recentes, medicamentos do ano, fraturas e cirurgias).
- Mantive a verificaÃ§Ã£o jÃ¡ existente para internaÃ§Ãµes e normalizei as mensagens para cada par.
- A validaÃ§Ã£o do backend agora bloqueia avanÃ§os quando o detalhe fica em branco apÃ³s marcar Sim.

#### ð Arquivos afetados
- backend/ui/forms/cadastro.py
- HISTORICO_DE_MUDANCAS.md

#### ð Relacionado a
- refactor: ficha mÃ©dica premium

#### â ï¸ Impacto / ObservaÃ§Ãµes
- O formulÃ¡rio reforÃ§a a coleta de contexto e evita campos vazios quando hÃ¡ indicaÃ§Ãµes positivas.
---

### ð AlteraÃ§Ã£o NÂº 0058
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> O botÃ£o  Finalizar cadastro parecia habilitado mesmo com pendÃªncias, e o checkbox do termo de imagem nÃ£o mostrava claramente o sinal quando marcado.

#### ð ï¸ O que foi feito
- Atualizei o CSS (cadastro.css) para tornar o botÃ£o principal totalmente cinza quando desabilitado, com cursor travado, e realÃ§ar o estado ativo com uma paleta diferente quando estiver pronto para clicar.
- Reestruturei o template do termo (	ermo.html) para envolver o checkbox do concordo em um novo label.checkbox-pill e adicionei estilos que desenham manualmente o tick quando o checkbox estiver selecionado, garantindo que o usuÃ¡rio veja a confirmaÃ§Ã£o.
- Mantive o layout da assinatura e demais seÃ§Ãµes intactos, apenas reforÃ§ando a sinalizaÃ§Ã£o visual da etapa final.

#### ð Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/termo.html
- backend/ui/static/css/cadastro.css

#### ð Relacionado a
- refactor: revisÃ£o final do cadastramento

#### â ï¸ Impacto / ObservaÃ§Ãµes
- O botÃ£o Finalizar agora fica claramente avulso (cinza) atÃ© que todas as etapas estejam prontas, e o termo mostra o tick ao marcar a caixa, fechando o fluxo visual do cadastro.
---

### ð AlteraÃ§Ã£o NÂº 0059
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> A etapa do responsÃ¡vel estava visualmente simples demais e dava a impressÃ£o de que campos se misturavam; era preciso um layout novo, organizado e com instruÃ§Ãµes claras para cada bloco (pai, mÃ£e, responsÃ¡vel legal, endereÃ§o e assinatura). 

#### ð ï¸ O que foi feito
- Reestruturei 
esponsavel.html para usar blocos com tÃ­tulos, notas explicativas e o mesmo conjunto 
ield-row usado na ficha mÃ©dica, mantendo sempre rÃ³tulos em coluna fixa e controles alinhados Ã  direita.
- Fiz a transiÃ§Ã£o do grid simples para a nova 
ield-rows, removendo o grid padrÃ£o e realÃ§ando cada campo com o rÃ³tulo e o input lado a lado, inclusive para os selects e radio buttons jÃ¡ existentes.
- Mantive a Ã¡rea de assinatura intacta, mas reforcei o texto e o status da declaraÃ§Ã£o dentro da mesma seÃ§Ã£o visual.

#### ð Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/responsavel.html
- backend/ui/static/css/cadastro.css

#### ð Relacionado a
- refactor: fluxo responsÃ¡vel

#### â ï¸ Impacto / ObservaÃ§Ãµes
- O bloco do responsÃ¡vel agora estÃ¡ mais organizado, fÃ¡cil de navegar e segue o mesmo padrÃ£o de estÃ©tica premium jÃ¡ definido nas outras etapas do wizard.
---

### ð AlteraÃ§Ã£o NÂº 0060
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> Ao renderizar o formulÃ¡rio do responsÃ¡vel, o Django acusou erro de template por usar loops literais; o layout precisava permanecer organizado sem repetir estruturas invÃ¡lidas.

#### ð ï¸ O que foi feito
- SubstituÃ­ os 
or inline por linhas explÃ­citas para cada campo (pai, mÃ£e, responsÃ¡vel legal e endereÃ§o) mantendo o mesmo visual de 
ield-row e evitando instruÃ§Ãµes proibidas no template.
- Continuei usando os tÃ­tulos e notas das seÃ§Ãµes para orientar o responsÃ¡vel, garantindo que cada campo tenha o rÃ³tulo/campo alinhado e o estilo premium anterior.

#### ð Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/responsavel.html

#### ð Relacionado a
- refactor: fluxo responsÃ¡vel

#### â ï¸ Impacto / ObservaÃ§Ãµes
- A etapa do responsÃ¡vel permanece organizada e compatÃ­vel com os estilos jÃ¡ aplicados, e agora o template renderiza corretamente sem erros ao carregar a pÃ¡gina.
---

### ð AlteraÃ§Ã£o NÂº 0061
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> A pÃ¡gina  Dados do aventureiro estava usando 
ield-grid e labels soltos, o que dificultava enxergar quais campos estavam preenchidos; o cliente pediu um layout mais limpo e instrutivo similar ao do responsÃ¡vel.

#### ð ï¸ O que foi feito
- Reestruturei cadastro_aventureiro/dados.html para usar 
ield-rows com rÃ³tulos fixos e descriÃ§Ãµes curtas em cada card (dados pessoais, classe investida, documentos, endereÃ§o e informaÃ§Ãµes gerais).<br>
- Mantive as notas explicativas, reforÃ§ando as instruÃ§Ãµes e garantindo que os selects e campos de texto fiquem alinhados em duas colunas sem quebrar no mobile.

#### ð Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/dados.html

#### ð Relacionado a
- refactor: form adventureiro

#### â ï¸ Impacto / ObservaÃ§Ãµes
- O formulÃ¡rio ficou mais fÃ¡cil de ler e preencher, e segue o padrÃ£o visual renovado aplicado ao restante do cadastro.
---

### ð AlteraÃ§Ã£o NÂº 0062
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> O template dos dados do aventureiro estava usando 
or com tuplas literais, o que causava erro de sintaxe no Django e quebrava a renderizaÃ§Ã£o ao abrir a pÃ¡gina.

#### ð ï¸ O que foi feito
- SubstituÃ­ cada loop por linhas explÃ­citas (
ield-row) para cada campo essencial (nome, sexo, data, sÃ©rie, colÃ©gio, bolsa, documentos e endereÃ§o) mantendo os rÃ³tulos fixos e a nova estrutura de grids.
- Reforcei as descriÃ§Ãµes curtas de cada card (dados pessoais, classe investida, documentos e endereÃ§o) para que a etapa fique visualmente alinhada com o restante do formulÃ¡rio.

#### ð Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/dados.html

#### ð Relacionado a
- refactor: form do aventureiro

#### â ï¸ Impacto / ObservaÃ§Ãµes
- A pÃ¡gina volta a carregar sem erro e continua organizada para o responsÃ¡vel preencher os dados de forma sequencial.
---

### ð AlteraÃ§Ã£o NÂº 0063
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> O visual dos formulÃ¡rios de responsÃ¡vel e dados do aventureiro ainda estava bastante simples e precisava de um toque coerente com o restante do wizard renovado.

#### ð ï¸ O que foi feito
- Ajustei cadastro.css para aplicar gradientes suaves, sombras mais ricas e hover nos cards do responsÃ¡vel/aventureiro, alÃ©m de destacar o 
ield-row com bordas e preenchimentos internos mais elegantes sem alterar a estrutura dos formulÃ¡rios atuais.
- Mantive os rÃ³tulos fixos e controles alinhados, mas agora cada campo possui o mesmo espaÃ§amento e cores dos novos blocos da ficha mÃ©dica.

#### ð Arquivos afetados
- backend/ui/static/css/cadastro.css

#### ð Relacionado a
- refactor: estÃ©tica do wizard

#### â ï¸ Impacto / ObservaÃ§Ãµes
- A etapa responsÃ¡vel/aventureiro agora se integra visualmente com o restante do fluxo, parecendo mais premium e legÃ­vel sem alterar a lÃ³gica do Django.
---

### ð AlteraÃ§Ã£o NÂº 0064
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> A seÃ§Ã£o  Classe investida precisava de caixas de seleÃ§Ã£o uniformes e de regra visual para evitar marcar Nenhum junto com outras opÃ§Ãµes, mantendo tudo bonito como o restante do cadastramento.

#### ð ï¸ O que foi feito
- Adicionei o container .invested-wrapper em dados.html e organizei o bloco dentro de 
ield-row/invested-checkboxes, preparando o terreno para estilo uniforme e o script de exclusÃ£o de Nenhum.
- Atualizei cadastro.css para padronizar a largura, borda, fundo e hover das checkboxes da classe investida.
- IncluÃ­ um script pequeno que impede seleÃ§Ã£o simultÃ¢nea de Nenhum com outras classes e vice-versa.

#### ð Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/dados.html
- backend/ui/static/css/cadastro.css

#### ð Relacionado a
- refactor: classe investida

#### â ï¸ Impacto / ObservaÃ§Ãµes
- A base jÃ¡ respeita o estilo geral e garante que a seleÃ§Ã£o Nenhum Ã© mutuamente exclusiva, evitando inconsistÃªncias de dados sem depender de validaÃ§Ã£o adicional.
---

### ð AlteraÃ§Ã£o NÂº 0065
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> Ao salvar e avanÃ§ar dentro dos formulÃ¡rios do responsÃ¡vel ou do aventureiro, jÃ¡ existia uma lista de pendÃªncias no topo, mas nÃ£o havia indicaÃ§Ã£o visual direta nos campos que ainda estavam incompletos.

#### ð ï¸ O que foi feito
- Criei 
ield_row.html + 
ield_error.html para renderizar cada campo com rÃ³tulo fixo, mensagem de erro e a classe error automaticamente quando o Django reporta validaÃ§Ãµes falhadas.
- Atualizei 
esponsavel.html e dados.html para usar estes includes, eliminando repetiÃ§Ãµes e garantindo que as mensagens de erro fiquem prÃ³ximas aos campos.
- Ajustei cadastro.css para estilizar .field-row.error, os 
ield-error e o novo layout dos card/responsÃ¡vel com destaque vermelho suave quando uma pendÃªncia existe, facilitando a visualizaÃ§Ã£o do que ainda precisa ser preenchido.

#### ð Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/responsavel.html
- backend/ui/templates/cadastro_aventureiro/dados.html
- backend/ui/templates/cadastro_aventureiro/field_row.html
- backend/ui/templates/cadastro_aventureiro/field_error.html
- backend/ui/static/css/cadastro.css

#### ð Relacionado a
- refactor: visÃ£o de pendÃªncias

#### â ï¸ Impacto / ObservaÃ§Ãµes
- Os formulÃ¡rios agora destacam claramente quais campos ainda nÃ£o passaram na validaÃ§Ã£o, e os cards mantÃªm o visual premium graÃ§as aos novos includes e ao CSS refinado.
---

### ð AlteraÃ§Ã£o NÂº 0066
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### ð Contexto
> Mesmo com pendÃªncias, o usuÃ¡rio chegava Ã  revisÃ£o final sem um chamado claro sobre onde corrigir; o botÃ£o  Finalizar ficava cinza mas nÃ£o havia sugestÃ£o de voltar ao responsÃ¡vel ou aos aventureiros.

#### ð ï¸ O que foi feito
- Adicionei um bloco context-feedback com variante warning na pÃ¡gina da revisÃ£o e dois botÃµes que levam diretamente Ã s etapas do responsÃ¡vel e da lista de aventureiros, destacando com texto a necessidade de corrigir antes de finalizar.
- Estilizei o novo bloco com borda/vermelho suave e criei .review-actions no CSS para manter os botÃµes organizados sob essa mensagem.

#### ð Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/revisao.html
- backend/ui/static/css/cadastro.css

#### ð Relacionado a
- refactor: fluxo da revisÃ£o final

#### â ï¸ Impacto / ObservaÃ§Ãµes
- Agora o usuÃ¡rio consegue retornar rapidamente para corrigir pendÃªncias e sÃ³ finaliza quando todos os blocos estÃ£o completos, com ajuda visual contÃ­nua.

---

### ✨ Alteração Nº 0067
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### ✨ Contexto
> Depois de cadastrado, o responsável precisava de uma experiência pós-login que organize os dados, documentações e pendências em um painel claro com menu lateral.

#### ⚙️ O que foi feito
- Redirecionei o login para detectar perfis de responsável e enviei para um novo dashboard dedicado; perfis sem vínculo veem uma página genérica “em construção”.
- Criei views e rotas (`dashboard-responsavel` e `dashboard-gen`) que reúnem responsáveis, aventureiros, pendências e links diretos para edição.
- Desenvolvi as novas views em `dashboard/base.html`, `dashboard/responsavel.html` e `dashboard/generic.html` e um CSS próprio (`dashboard.css`) com sidebar, cards, seletor de pessoas e seções de documentos.

#### 📁 Arquivos afetados
- backend/ui/views.py
- backend/ui/urls.py
- backend/ui/templates/dashboard/base.html
- backend/ui/templates/dashboard/responsavel.html
- backend/ui/templates/dashboard/generic.html
- backend/ui/static/css/dashboard.css

#### ⚠️ Relacionado a
- feature: painel do responsável

#### ☑️ Impacto / Observações
- Usuários responsáveis agora chegam a um painel completo com menu “Meus Dados”, cards de status e atalhos para editar cadastros e acessar fichas médicas/termos; demais perfis observam mensagem de aguardando liberação.


---

### 🐞 Alteração Nº 0068
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** bugfix  

#### 🐞 Contexto
> O dashboard do responsável quebrava por usar operadores `or` diretamente no template, o que o Django não aceita.

#### ⚙️ O que foi feito
- Substituí as expressões que tentavam usar `or` para mostrar o nome do responsável e os números de documento por blocos `if/elif/else`, garantindo que o parser consiga renderizar mesmo sem dados opcionais.

#### 📁 Arquivos afetados
- backend/ui/templates/dashboard/responsavel.html

#### ⚠️ Relacionado a
- bugfix: dashboard responsavel

#### ☑️ Impacto / Observações
- O painel carrega com segurança, exibindo mensagens padrão quando campos ainda não foram preenchidos.


---

### 🎯 Alteração Nº 0069
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 🎯 Contexto
> O painel do responsável precisava manter o mesmo visual da tela de login, ganhar um layout base reutilizável, sidebar enxuta e rotas separadas para Dashboard e Meus Dados.

#### ⚙️ O que foi feito
- Criei `painel/base.html` e o CSS `panel.css` para replicar o gradiente, tipografia, cards e botões do login em todo o painel.
- Substituí o antigo fluxo único por duas views (`painel_dashboard` e `painel_meus_dados`) com rotas `/painel/` e `/painel/meus-dados/`, garantindo que o login redirecione inicialmente ao Dashboard.
- Reescrevi os templates `painel/dashboard.html` e `painel/meus_dados.html` para mostrar os cards, o seletor de pessoas e as chamadas para edição/documentos, mantendo sidebar fixa apenas com Dashboard e Meus Dados.

#### 📁 Arquivos afetados
- HISTORICO_DE_MUDANCAS.md
- backend/ui/views.py
- backend/ui/urls.py
- backend/ui/templates/painel/base.html
- backend/ui/templates/painel/dashboard.html
- backend/ui/templates/painel/meus_dados.html
- backend/ui/static/css/panel.css

#### ⚠️ Relacionado a
- refactor: painel responsavel

#### ☑️ Impacto / Observações
- O painel agora usa o mesmo design do login, rotas distintas e um layout reutilizável com sidebar fixa e conteúdo atualizado.


---

### 🎨 Alteração Nº 0070
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 🎨 Contexto
> Refaça completamente a UI do painel para torná-lo um layout de aplicação com sidebar fixa, base reutilizável e visual moderno, mantendo apenas duas rotas (Dashboard e Meus Dados).

#### ⚙️ O que foi feito
- Criei `painel/base.html` com sidebar fixa, bloco “Perfil” e conteúdo em destaque, usando apenas o novo tema `panel.css` (gradientes escuros, cards volumosos e botões modernos).
- Reescrevi os templates `painel/dashboard.html` e `painel/meus_dados.html` para separar as páginas, simplificar o dashboard a uma saudação e manter Meus Dados com seletor, cards e acessos a documentos.
- Atualizei as views para direcionar o login a `/painel/`, manter `painel_dashboard`/`painel_meus_dados`, e entregar o novo contexto com dados de aventureiros e documentos.

#### 📁 Arquivos afetados
- HISTORICO_DE_MUDANCAS.md
- backend/ui/views.py
- backend/ui/urls.py
- backend/ui/templates/painel/base.html
- backend/ui/templates/painel/dashboard.html
- backend/ui/templates/painel/meus_dados.html
- backend/ui/static/css/panel.css

#### ⚠️ Relacionado a
- refactor: painel responsavel

#### ☑️ Impacto / Observações
- O painel agora é um app layout fixo com sidebar e perfil, o dashboard é minimalista, Meus Dados exibe os dados organizados e o tema reforça a identidade visual moderna do sistema.


---

### 🎨 Alteração Nº 0071
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 🎨 Contexto
> O painel precisava seguir o padrão visual do login com palette azul claro, sidebar branca fixa e interface mais leve/infantil, simplificando o dashboard e mantendo Meus Dados funcional.

#### ⚙️ O que foi feito
- Redefini `panel.css` com variáveis como `--brand-50`, `--brand-500` e botões suaves, sombras leves e cards arredondados, criando um novo tema infantil do painel.
- Atualizei `painel/base.html` para mostrar o logo no topo da sidebar, o bloco “Perfil/Responsável”, menu branco fixo e remover quaisquer estilos antigos que centralizavam o layout.
- Garanti que as páginas `painel/dashboard.html` e `painel/meus_dados.html` reutilizem o template base e exibam o conteúdo reduzido (saudação mínima) e os cards organizados, mantendo links de edição e documentos.

#### 📁 Arquivos afetados
- HISTORICO_DE_MUDANCAS.md
- backend/ui/templates/painel/base.html
- backend/ui/templates/painel/dashboard.html
- backend/ui/templates/painel/meus_dados.html
- backend/ui/static/css/panel.css

#### ⚠️ Relacionado a
- refactor: painel responsavel

#### ☑️ Impacto / Observações
- O painel agora parece parte do mesmo site (mesma paleta azul clara), a sidebar fica branca e fixa com bloco de perfil e os botões/documentos seguem o novo tema suave.


---

### 🛠️ Alteração Nº 0072
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** feature  

#### 🛠️ Contexto
> “Meus Dados” precisa ser um único fluxo inline, com blocos expansíveis de responsável e aventureiros que mostram os campos por linha e permitem editar tudo no mesmo painel.

#### ⚙️ O que foi feito
- Incluí `PanelResponsibleForm` e `PanelAdventurerForm`, tratei submissões via POST dentro de `painel_meus_dados` e mantive a validação já existente dos formulários de cadastro.
- Refatorei `painel/meus_dados.html` para manter somente os botões de pessoa, mostrar as linhas de dados e permitir que o botão “Editar” habilite inputs inline, com “Salvar/Cancelar” e placeholders para ficha médica/termo.
- Atualizei `panel.css` com as classes `.line`, `.line-input`, `.panel-message` e o estado `.is-editing` para que o painel azul claro exiba os campos num layout leve, organizado e pronto para edição inline.

#### 📁 Arquivos afetados
- HISTORICO_DE_MUDANCAS.md
- backend/ui/forms/panel.py
- backend/ui/views.py
- backend/ui/templates/painel/meus_dados.html
- backend/ui/static/css/panel.css

#### ⚠️ Relacionado a
- feature: painel responsavel

#### ☑️ Impacto / Observações
- Agora o responsável e cada aventureiro expandem as informações na mesma tela, permitem edição de todos os campos simultaneamente via POST e mantêm os botões de documentos prontos para receber o comportamento futuro.

