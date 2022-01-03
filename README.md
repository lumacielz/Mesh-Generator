# Mesh-Generator
Ao executar o arquivo, serão pedidas informações das dimensões em x e y respectivamente, caso a malha seja unidimensional, basta passar o comprimento como 0 na dimensão desejada. O numero de elementos em cada direção também deve ser passado.

Caso seja passado um valor inválido, será mostrada uma mensagem de erro e o programa volta a coletar os dados do início.

Em seguida, deve-se escolher a opção de tamanho de elemento variável ou uniforme, sendo 0 para uniforme e 1 para variável. Caso seja uniforme, o tamanho dos elementos será calculado por $\frac{Li}{ni}$ sendo L o comprimento na direção i, e n o número de elementos passado. Caso contrário, o tamanho de cada elemento deve ser passado, separado por vírgula.

Por fim, deve-se escolher a forma dos elementos da malha, sendo TRI para triangular e QUAD para quadrada. Essa etapa só será executada se ambas as dimensões forem maiores que zero. 

Dispondo de todos os dados, serão calculados os pontos na dimensão x e y, e a matriz IEN, que relaciona cada elemento com seus respectivos pontos. 

Será plotado um gráfico com os elementos da malha e mostrada uma lista indicando quais elementos pertencem ou não ao contorno da forma.
