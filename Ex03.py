"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média;
"""

import json

with open("dados.json", encoding="UTF-8") as dados:
  faturamento = json.load(dados)


diaMenorFaturamento = []
valorMenorFaturamento = 999999999

for i in faturamento:
  if(i["valor"] < valorMenorFaturamento):
    valorMenorFaturamento = i["valor"]

for i in faturamento:
  if(i["valor"] == valorMenorFaturamento):
    diaMenorFaturamento.append(i["dia"])

print("Data(s) de menor faturamento:", diaMenorFaturamento,
  "\n" + "Valor de faturamento na(s) data(s) = R$", round(valorMenorFaturamento, 2))

print("--------------------------------------------------------------------------")

diaMaiorFaturamento = []
valorMaiorFaturamento = -1

for i in faturamento:
  if(i["valor"] > valorMaiorFaturamento):
    valorMaiorFaturamento = i["valor"]

for i in faturamento:
  if(i["valor"] == valorMaiorFaturamento):
    diaMaiorFaturamento.append(i["dia"])

print("Data(s) de maior faturamento:", diaMaiorFaturamento,
  "\n" + "Valor de faturamento na(s) data(s) = R$", round(valorMaiorFaturamento, 2))

print("--------------------------------------------------------------------------")

soma = 0
qtdDiasPeriodo = 0

for i in faturamento:
  if(i["valor"] > 0):
    soma += i["valor"]

for i in faturamento:
  if(i["valor"] > 0):
    qtdDiasPeriodo += 1

media = soma / qtdDiasPeriodo

contAcimaMedia = 0
for i in faturamento:
  if(i["valor"] > media):
    contAcimaMedia += 1

print("Quantidade de dias em que o valor diário foi superior a media mensal:", contAcimaMedia)