
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
