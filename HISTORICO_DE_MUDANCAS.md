
---

### 📝 Alteração Nº 0056
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> Ajustar o layout das seções críticas (alergias, medicamentos e procedimentos) para que cada pergunta e campo fiquem alinhados em uma linha única, evitando campos gigantes e espaços soltos.

#### 🛠️ O que foi feito
- Reescrevi as seções de alergias, medicamentos crônicos e procedimentos recentes para usar o novo componente `field-row` que mantém o rótulo e o controle lado a lado em uma única linha.
- Acrescentei os estilos de `field-row` no CSS, limitando alturas, aplicando bordas suaves e garantindo que os controles preencham a largura disponível sem crescer demais.
- Mantive os demais blocos intactos e preservei o fluxo de assinatura com a nova estrutura sem duplicar seções.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/ficha.html
- backend/ui/static/css/cadastro.css

#### 🔗 Relacionado a
- refactor: ficha médica refinada

#### ⚠️ Impacto / Observações
- As seções agora ficam compactas e organizadas, tornando evidente a sequência de perguntas e eliminando campos excessivamente largos.
---

### 📝 Alteração Nº 0057
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> Tornei obrigatório preencher o detalhe sempre que marcar  Sim nas seções críticas da ficha médica (alergias, medicamentos e procedimentos), garantindo evidência completa.

#### 🛠️ O que foi feito
- Atualizei MedicalRecordForm.clean() para exigir os campos de notas/detalhes sempre que o booleano associado estiver em True (alergias, outros problemas, problemas recentes, medicamentos do ano, fraturas e cirurgias).
- Mantive a verificação já existente para internações e normalizei as mensagens para cada par.
- A validação do backend agora bloqueia avanços quando o detalhe fica em branco após marcar Sim.

#### 📁 Arquivos afetados
- backend/ui/forms/cadastro.py
- HISTORICO_DE_MUDANCAS.md

#### 🔗 Relacionado a
- refactor: ficha médica premium

#### ⚠️ Impacto / Observações
- O formulário reforça a coleta de contexto e evita campos vazios quando há indicações positivas.
---

### 📝 Alteração Nº 0058
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> O botão  Finalizar cadastro parecia habilitado mesmo com pendências, e o checkbox do termo de imagem não mostrava claramente o sinal quando marcado.

#### 🛠️ O que foi feito
- Atualizei o CSS (cadastro.css) para tornar o botão principal totalmente cinza quando desabilitado, com cursor travado, e realçar o estado ativo com uma paleta diferente quando estiver pronto para clicar.
- Reestruturei o template do termo (	ermo.html) para envolver o checkbox do concordo em um novo label.checkbox-pill e adicionei estilos que desenham manualmente o tick quando o checkbox estiver selecionado, garantindo que o usuário veja a confirmação.
- Mantive o layout da assinatura e demais seções intactos, apenas reforçando a sinalização visual da etapa final.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/termo.html
- backend/ui/static/css/cadastro.css

#### 🔗 Relacionado a
- refactor: revisão final do cadastramento

#### ⚠️ Impacto / Observações
- O botão Finalizar agora fica claramente avulso (cinza) até que todas as etapas estejam prontas, e o termo mostra o tick ao marcar a caixa, fechando o fluxo visual do cadastro.
---

### 📝 Alteração Nº 0059
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> A etapa do responsável estava visualmente simples demais e dava a impressão de que campos se misturavam; era preciso um layout novo, organizado e com instruções claras para cada bloco (pai, mãe, responsável legal, endereço e assinatura). 

#### 🛠️ O que foi feito
- Reestruturei esponsavel.html para usar blocos com títulos, notas explicativas e o mesmo conjunto ield-row usado na ficha médica, mantendo sempre rótulos em coluna fixa e controles alinhados à direita.
- Fiz a transição do grid simples para a nova ield-rows, removendo o grid padrão e realçando cada campo com o rótulo e o input lado a lado, inclusive para os selects e radio buttons já existentes.
- Mantive a área de assinatura intacta, mas reforcei o texto e o status da declaração dentro da mesma seção visual.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/responsavel.html
- backend/ui/static/css/cadastro.css

#### 🔗 Relacionado a
- refactor: fluxo responsável

#### ⚠️ Impacto / Observações
- O bloco do responsável agora está mais organizado, fácil de navegar e segue o mesmo padrão de estética premium já definido nas outras etapas do wizard.
---

### 📝 Alteração Nº 0060
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> Ao renderizar o formulário do responsável, o Django acusou erro de template por usar loops literais; o layout precisava permanecer organizado sem repetir estruturas inválidas.

#### 🛠️ O que foi feito
- Substituí os or inline por linhas explícitas para cada campo (pai, mãe, responsável legal e endereço) mantendo o mesmo visual de ield-row e evitando instruções proibidas no template.
- Continuei usando os títulos e notas das seções para orientar o responsável, garantindo que cada campo tenha o rótulo/campo alinhado e o estilo premium anterior.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/responsavel.html

#### 🔗 Relacionado a
- refactor: fluxo responsável

#### ⚠️ Impacto / Observações
- A etapa do responsável permanece organizada e compatível com os estilos já aplicados, e agora o template renderiza corretamente sem erros ao carregar a página.
---

### 📝 Alteração Nº 0061
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> A página  Dados do aventureiro estava usando ield-grid e labels soltos, o que dificultava enxergar quais campos estavam preenchidos; o cliente pediu um layout mais limpo e instrutivo similar ao do responsável.

#### 🛠️ O que foi feito
- Reestruturei cadastro_aventureiro/dados.html para usar ield-rows com rótulos fixos e descrições curtas em cada card (dados pessoais, classe investida, documentos, endereço e informações gerais).<br>
- Mantive as notas explicativas, reforçando as instruções e garantindo que os selects e campos de texto fiquem alinhados em duas colunas sem quebrar no mobile.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/dados.html

#### 🔗 Relacionado a
- refactor: form adventureiro

#### ⚠️ Impacto / Observações
- O formulário ficou mais fácil de ler e preencher, e segue o padrão visual renovado aplicado ao restante do cadastro.
---

### 📝 Alteração Nº 0062
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> O template dos dados do aventureiro estava usando or com tuplas literais, o que causava erro de sintaxe no Django e quebrava a renderização ao abrir a página.

#### 🛠️ O que foi feito
- Substituí cada loop por linhas explícitas (ield-row) para cada campo essencial (nome, sexo, data, série, colégio, bolsa, documentos e endereço) mantendo os rótulos fixos e a nova estrutura de grids.
- Reforcei as descrições curtas de cada card (dados pessoais, classe investida, documentos e endereço) para que a etapa fique visualmente alinhada com o restante do formulário.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/dados.html

#### 🔗 Relacionado a
- refactor: form do aventureiro

#### ⚠️ Impacto / Observações
- A página volta a carregar sem erro e continua organizada para o responsável preencher os dados de forma sequencial.
---

### 📝 Alteração Nº 0063
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> O visual dos formulários de responsável e dados do aventureiro ainda estava bastante simples e precisava de um toque coerente com o restante do wizard renovado.

#### 🛠️ O que foi feito
- Ajustei cadastro.css para aplicar gradientes suaves, sombras mais ricas e hover nos cards do responsável/aventureiro, além de destacar o ield-row com bordas e preenchimentos internos mais elegantes sem alterar a estrutura dos formulários atuais.
- Mantive os rótulos fixos e controles alinhados, mas agora cada campo possui o mesmo espaçamento e cores dos novos blocos da ficha médica.

#### 📁 Arquivos afetados
- backend/ui/static/css/cadastro.css

#### 🔗 Relacionado a
- refactor: estética do wizard

#### ⚠️ Impacto / Observações
- A etapa responsável/aventureiro agora se integra visualmente com o restante do fluxo, parecendo mais premium e legível sem alterar a lógica do Django.
---

### 📝 Alteração Nº 0064
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> A seção  Classe investida precisava de caixas de seleção uniformes e de regra visual para evitar marcar Nenhum junto com outras opções, mantendo tudo bonito como o restante do cadastramento.

#### 🛠️ O que foi feito
- Adicionei o container .invested-wrapper em dados.html e organizei o bloco dentro de ield-row/invested-checkboxes, preparando o terreno para estilo uniforme e o script de exclusão de Nenhum.
- Atualizei cadastro.css para padronizar a largura, borda, fundo e hover das checkboxes da classe investida.
- Incluí um script pequeno que impede seleção simultânea de Nenhum com outras classes e vice-versa.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/dados.html
- backend/ui/static/css/cadastro.css

#### 🔗 Relacionado a
- refactor: classe investida

#### ⚠️ Impacto / Observações
- A base já respeita o estilo geral e garante que a seleção Nenhum é mutuamente exclusiva, evitando inconsistências de dados sem depender de validação adicional.
---

### 📝 Alteração Nº 0065
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> Ao salvar e avançar dentro dos formulários do responsável ou do aventureiro, já existia uma lista de pendências no topo, mas não havia indicação visual direta nos campos que ainda estavam incompletos.

#### 🛠️ O que foi feito
- Criei ield_row.html + ield_error.html para renderizar cada campo com rótulo fixo, mensagem de erro e a classe error automaticamente quando o Django reporta validações falhadas.
- Atualizei esponsavel.html e dados.html para usar estes includes, eliminando repetições e garantindo que as mensagens de erro fiquem próximas aos campos.
- Ajustei cadastro.css para estilizar .field-row.error, os ield-error e o novo layout dos card/responsável com destaque vermelho suave quando uma pendência existe, facilitando a visualização do que ainda precisa ser preenchido.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/responsavel.html
- backend/ui/templates/cadastro_aventureiro/dados.html
- backend/ui/templates/cadastro_aventureiro/field_row.html
- backend/ui/templates/cadastro_aventureiro/field_error.html
- backend/ui/static/css/cadastro.css

#### 🔗 Relacionado a
- refactor: visão de pendências

#### ⚠️ Impacto / Observações
- Os formulários agora destacam claramente quais campos ainda não passaram na validação, e os cards mantêm o visual premium graças aos novos includes e ao CSS refinado.
---

### 📝 Alteração Nº 0066
**Data:** 2026-02-02  
**Autor:** Codex  
**Tipo:** refactor  

#### 📝 Contexto
> Mesmo com pendências, o usuário chegava à revisão final sem um chamado claro sobre onde corrigir; o botão  Finalizar ficava cinza mas não havia sugestão de voltar ao responsável ou aos aventureiros.

#### 🛠️ O que foi feito
- Adicionei um bloco context-feedback com variante warning na página da revisão e dois botões que levam diretamente às etapas do responsável e da lista de aventureiros, destacando com texto a necessidade de corrigir antes de finalizar.
- Estilizei o novo bloco com borda/vermelho suave e criei .review-actions no CSS para manter os botões organizados sob essa mensagem.

#### 📁 Arquivos afetados
- backend/ui/templates/cadastro_aventureiro/revisao.html
- backend/ui/static/css/cadastro.css

#### 🔗 Relacionado a
- refactor: fluxo da revisão final

#### ⚠️ Impacto / Observações
- Agora o usuário consegue retornar rapidamente para corrigir pendências e só finaliza quando todos os blocos estão completos, com ajuda visual contínua.

### � � Alteração Nº 0067; Add-Content HISTORICO_DE_MUDANCAS.md -Value **Data:** 2026-02-02 ; Add-Content HISTORICO_DE_MUDANCAS.md -Value  **Autor:** Codex ; Add-Content HISTORICO_DE_MUDANCAS.md -Value  **Tipo:** feature ; Add-Content HISTORICO_DE_MUDANCAS.md -Value 
