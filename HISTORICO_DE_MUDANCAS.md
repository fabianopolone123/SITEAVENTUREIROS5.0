
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
