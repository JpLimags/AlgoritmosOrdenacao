# Algoritmos de Ordenação
  
  ## Merge Sort
  
   - Esse algoritmo foi criado em 1945 pelo matemático Jonh Von Neumann é um exemplo de algoritmo de ordenação que faz uso de uma estratégia muito conhecida que é "dividir para conquistar", buscando dessa dfroma resolver problemas complexos. É considerado um algoritmo estável, possuindo uma complexidade de C(n) = O(n log n) para todos os casos.
   
   - Como já é de imaginar de um usuário da técnica "dividir para conquistar", esse algoritmo divid o problema em partes menores e, resolvendo cada pedaço e depois junta(merge) os resultados . O vetor será dividido em duas partes iguais, que serão cada uma divididas em duas partes, e assim até ficar um ou dois elementos cuja ordenação é trivial.
   
   - Imagem que mostar o comportamento deste algoritmo
  
   ![img](https://d2m498l008ebpa.cloudfront.net/2016/12/merge-sort.gif) 
   
  ## Bubble Sort
  
  - O bubble é um algoritmo de ordenação simples, dessa forma sua utilização é mais indicadas em problemas mais simples, mas agora vamos entender o funcionamento deste algoritmo.
  - O funcionamento do bubble sort ocorre da seguinte forma nós vamos ter uma lista por onde ele vai realizar múltiplas passagens. Durante as interações ele compara os itens adjacentes e troca aqueles que estão fora de ordem. Portanto, a cada passagem pela lista ele colocará o próximo maior valor mais próxim de sua posição correta. Dessa forma cada item se desloca com uma "bolha", por isso o nome Bubble Sort.
  
   
  ### Uma importante informação !!!
   "Um método de ordenação é estável se a ordem relativa dos itens iguais não se altera durante a ordenação."
