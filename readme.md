Kenzie Academy Brasil

📖 Atividade - 🧠 Lógica - Exercitando Funções e Builtins
Tópicos do conteúdo
Introdução
Nessa atividade exercitaremos o conteúdo visto sobre funções e builtins.

Ao final do desafio, terá uma seção de consulta com a solução de cada um dos tópicos. Para não sabotar seu próprio aprendizado, não a consulte na primeira dificuldade que aparecer, tente raciocinar e pesquisar formas de executar o que é pedido.

Você deverá criar duas funções, delta e bhaskara, seguindo as orientações:

delta
O cálculo de delta deve seguir a seguinte fórmula matemática:

https://i.imgur.com/76ABVgO.png

Parâmetros:
Essa função recebe 3 parâmetros, a, b e c. Consideremos que sempre serão inteiros positivos.
Procedimento:
Crie uma lógica que faça o cálculo necessário seguindo a fórmula.
Retorno:
A função retorna o resultado de delta.
bhaskara
O cálculo de bhaskara deve utilizar a função delta como auxiliar para calcular as possíveis raízes (x1, x2) da equação. O cálculo deve ser feito a partir das seguintes fórmulas matemáticas:

https://i.imgur.com/K94FAiP.png

Parâmetros:
Essa função recebe 3 parâmetros, a, b e c. Consideremos que sempre serão inteiros positivos.
Procedimento:
Crie uma lógica que faça o cálculo necessário seguindo a fórmula. Utilize da função anterior delta para calcular o delta separadamente.
Retorno:
Caso o delta seja negativo, a função deve retornar uma string 'Delta Negativo'. Caso o delta seja positivo, a função de retornar as duas raízes com arredondamento de 2 casas decimais, seguindo o exemplo de formatação abaixo:
