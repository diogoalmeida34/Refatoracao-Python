# Orientações sobre a tarefa da matéria de Engenharia de Software sobre Refatoração de código fonte para Gilded Rose

![image](https://github.com/diogoalmeida34/Refatoracao-Python/assets/90733669/c879cefd-84a8-4388-a335-55400688d8f6)

<h2 align='center'>Relato de Refatoração do Código para Gilded Rose</h2> 
<p><Strong>Descrição do Processo de Refatoração:</Strong> O processo de refatoração do código da classe <i>GildedRose</i> envolveu revisar e reestruturar o método <i>update_quality</i> para torná-lo mais legível, modular e aderente às novas especificações fornecidas. Aqui estão os passos principais e considerações durante o processo:</p>
<ol>  
  <li><Strong>Análise das Especificações:</Strong> O primeiro passo foi compreender completamente as novas regras de negócio para os itens da pousada Gilded Rose. Isso incluiu entender como cada tipo de item deve ser tratado em termos de qualidade e prazo de venda.</li>
  <li><Strong>Identificação de Problemas no Código Original:</Strong> O código original tinha várias condições aninhadas e repetições de lógica para diferentes tipos de itens. Isso tornava difícil entender e modificar o comportamento dos itens de forma consistente.</li>
  <li><Strong>Estruturação do Novo Código:</Strong> O objetivo foi criar uma estrutura mais modular e clara, onde cada tipo de item tivesse seu próprio conjunto de regras de atualização de qualidade e prazo de venda. Isso implicou em criar blocos distintos de código para cada tipo de item, como "Aged Brie", "Backstage passes", "Conjurados" e itens normais.</li>
  <li><Strong>Uso de Funções Auxiliares:</Strong> Para evitar repetições e melhorar a legibilidade, foram usadas funções auxiliares para calcular a qualidade de cada tipo de item com base nas especificações fornecidas. Isso ajudou a simplificar o código principal do método <i>update_quality</i>.</li>
  <li><Strong>Teste e Validação:</Strong> Após a refatoração, foram realizados testes para garantir que o comportamento dos itens estava de acordo com as novas regras. Isso incluiu verificar se a qualidade não excedia 50 para itens que têm essa restrição e se itens com prazo de venda passado se comportavam corretamente.</li>
</ol>

<h2 align='center'>Dificuldades Encontradas</h2>
<p>Durante o processo de refatoração, algumas dificuldades foram encontradas:</p>
<ul>
  <li><Strong>Compreensão das Regras Complexas:</Strong> As regras específicas para cada tipo de item e como elas interagiam umas com as outras exigiram um entendimento detalhado. Isso foi crucial para evitar erros na implementação das novas lógicas.</li>
  <li><Strong>Integração com Código Existente:</Strong> O código original tinha sua própria estrutura e estilo. Integrar as novas funcionalidades sem quebrar o funcionamento existente foi um desafio, especialmente ao lidar com as exceções como "Sulfuras".</li>
  <li><Strong>Garantia de Qualidade:</Strong> Assegurar que todas as novas funcionalidades estavam corretamente implementadas e que não havia regressões nos comportamentos dos itens foi essencial. Testes meticulosos foram fundamentais para validar as mudanças.</li>
</ul>

<ul>
  <h2 align='center'>Lições Aprendidas</h2>

  <li><Strong>Clareza e Legibilidade:</Strong> A importância de escrever código claro e legível ficou evidente durante a refatoração. Isso não só facilita a manutenção futura, mas também ajuda na compreensão imediata das regras   de negócio implementadas.</li>
  <li><Strong>Modularidade:</Strong> Dividir o código em partes mais pequenas e específicas para cada tipo de funcionalidade (neste caso, cada tipo de item) simplifica o desenvolvimento e a depuração. Isso também facilita a adição de novas funcionalidades ou ajustes no futuro.</li>
  <li><Strong>Testes Rigorosos:</Strong> Investir tempo em testes robustos é crucial para garantir que as alterações não causem regressões ou comportamentos inesperados. Isso inclui testar não apenas casos comuns, mas também casos de borda e situações excepcionais.</li>
  <li>Conhecimento do Domínio: Compreender profundamente as regras de negócio é essencial para uma implementação precisa. Isso não apenas guia o desenvolvimento, mas também ajuda a explicar e justificar decisões de design durante o processo de refatoração.</li>
</ul>
<p>Em resumo, a refatoração da classe <i>GildedRose</i> foi um exercício valioso que não apenas melhorou o código existente, mas também proporcionou aprendizados importantes em termos de boas práticas de programação e gestão de complexidade em sistemas existentes.</p>
