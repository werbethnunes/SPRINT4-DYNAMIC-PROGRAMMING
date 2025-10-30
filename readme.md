# Projeto de Programação Dinâmica – Sprint 4  
## Simulação de Reposição de Insumos

---

### Identificação do Grupo

- Turma: 2ESS  
- Alunos:  
  - Bento Rangel – RM559124  
  - Larissa Pereira Biusse – RM564068  
  - Thamiris Almeida – RM559155  
  - Werbeth Nunes – RM559067  

---

### Contexto

Nas unidades de diagnóstico, o controle do consumo de insumos como luvas, seringas e reagentes nem sempre é preciso.  
Isso dificulta a previsão de reposição e pode causar tanto falta quanto desperdício de materiais.  

Para resolver isso, foi criada uma **simulação em Python** que usa **Programação Dinâmica** para decidir automaticamente **quanto pedir por dia**, buscando equilibrar custo, estoque e consumo real.

---

### Solução Proposta

O programa simula o comportamento de 5 insumos diferentes durante 30 dias, cada um com uma demanda diária aleatória.  
Com base nessa demanda, ele calcula uma **política ótima de reposição**, que determina o melhor pedido diário para cada insumo.

A ideia é minimizar três tipos de custo:
- **Custo de pedido:** cada vez que é feito um novo pedido.  
- **Custo de estoque:** o que sobra e fica armazenado.  
- **Custo de falta:** quando o material acaba antes da reposição.

Assim, a solução **melhora a visibilidade do consumo** (mostrando as demandas diárias e os custos totais) e **reduz desperdícios**, pois evita comprar demais e também evita faltar material.

---

### Estrutura do Código

O código segue o mesmo padrão da Sprint 3, com funções simples e comentários diretos.  
Foram usadas três versões do algoritmo de Programação Dinâmica:

| Versão | Descrição | Objetivo |
|--------|------------|----------|
| **Recursiva** | Resolve o problema chamando a si mesma para cada dia | Base conceitual da DP |
| **Com memorização (memo)** | Usa cache para guardar resultados já calculados | Evita repetição e reduz tempo |
| **Iterativa (bottom-up)** | Monta uma tabela com os valores ótimos de trás pra frente | Mostra a lógica da DP em tabela |

---

### Funcionamento

1. São definidos os **parâmetros** principais:
   - 30 dias de simulação  
   - Estoque inicial, máximo e limites de pedido  
   - Custos de pedido, estoque e falta  

2. É criada uma **demanda aleatória** para cada um dos 5 insumos:  
   `Luva`, `Seringa`, `Reagente`, `Mascara`, `Alcool`

3. Para cada insumo, o algoritmo calcula:
   - O **custo total** da política de reposição  
   - A **quantidade ideal a pedir por dia**  
   - Compara os resultados das versões **memo** e **iterativa**

---

### Exemplo de Saída

```
Simulacao de reposicao de insumos

Luva : [7, 3, 8, 5, 12, 6, 4, ...]
Seringa : [10, 6, 9, 11, 4, 3, ...]
Reagente : [5, 8, 7, 9, 6, 10, ...]
Mascara : [4, 6, 5, 8, 9, 7, ...]
Alcool : [8, 7, 5, 4, 6, 10, ...]

Resultados:

Insumo: Luva  
Custo total (memo): 150.0  
Custo total (iterativo): 150.0  
Politica (primeiros 10 dias, memo): [10, 0, 5, 0, 6, 8, ...]  
Politica (primeiros 10 dias, iter): [10, 0, 5, 0, 6, 8, ...]

-----------------------------------
```

---

### Conclusão

A aplicação da **Programação Dinâmica** permitiu simular a reposição ideal de insumos em um ambiente de diagnóstico.  
Com isso, o código mostra como é possível reduzir custos, evitar desperdícios e melhorar a visibilidade do consumo — tudo de forma automatizada e com base em dados.

---

**Sprint 4 – Engenharia de Software (FIAP)**  
**Desafio DASA – Controle de Consumo e Reposição de Insumos**
