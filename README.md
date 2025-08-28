# Algoritmo de Karatsuba

## O que é este projeto?
Este projeto apresenta uma implementação em python do algoritmo de Karatsuba, bem como a análise de complexidade assintótica e ciclomática deste algoritmo.

## O que é o Algoritmo de Karatsuba?
O algoritmo de Karatsuba é um método para realizar multiplicações de números grandes de uma maneira mais eficiente do que a tradicional que aprendemos na escola.
Esse trabalha utilizando a ideia de dividir para conquistar, pois apresenta uma implementação recursiva, dividindo os números ao meio a cada nova chamada. Com isso, ele reduz o número de multiplicações necessárias, o que é muito útil para números com muitos dígitos.

## Como rodar o projeto
Para rodar o projeto, é preciso ter o Python 3 instalado e uma IDE. A partir disso, execute no terminal o seguinte comando:
```bash
   python main.py
```
## Lógica da implementação

```python
def karatsuba(x, y):
```
A função começa recebendo como parâmetros os números a serem multiplicados, representados pelas variáveis x e y.


```python
 if x < 10 or y < 10:
        return x * y
```
Posteriormente, o algoritmo verifica a condicional que representa o caso base da recursão. Se os números tiverem apenas um dígito, é realizada a multiplicação entre eles e o resultado é retornado. Esse é o caso base porque com apenas um dígito, não é possível dividir os números.


```python
n = max(len(str(x)), len(str(y)))
```
Caso a condicional for falsa, o algoritmo continua a sua execução para a definição da variável n, que representa o número de dígitos do maior número. Ela é usada para decidir onde dividir os números ao meio.


```python
meio = n // 2
```
Em seguida, o algoritmo se encaminha para a definição da variável meio, que representa o índice do meio do número, servindo para separar os números em partes mais significativas (as partes maiores) e as partes menos significativas (as partes menores).


```python
x_maior = x // (10 ** meio)         
x_menor = x % (10 ** meio)

y_maior = y // (10 ** meio)
y_menor = y % (10 ** meio)
```
Em seguida, os números x e y são divididos em partes mais significativas e menos significativas.


```python
  a = karatsuba(x_maior, y_maior)
  c = karatsuba(x_maior + x_menor, y_maior + y_menor)
  b = karatsuba(x_menor, y_menor)
```
Posteriormente, são realizadas as chamadas recursivas. A chamada recusriva retornada para a variável a realiza o produto das partes mais significativas, enquanto a chamada recusiva que retorna para a variável b realiza o produto das menos significativas. Já a da variável c é usada para calcular a multiplicação da soma das partes.


```python
  d = c - a - b
```
A variável d recebe o valor do termo do meio do algoritmo de Karatsuba. 


```python
return a * (10**(2*meio)) + d * (10**meio) + b
```
E, por fim, é retornado o resultado final da multiplicação de x e y, realizando deslocamentos de dígitos e multiplicação de 3 termos.

## Análise ciclomática

Grafo criado:
![Grafo](grafo-karatsuba.png)
