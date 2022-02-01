"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro
do valor total mensal da distribuidora.
"""

fatSP = 67836.43
fatRJ = 36678.66
fatMG = 29229.88
fatES = 27165.48
fatOutros = 19849.53

totalFat = fatSP + fatRJ + fatMG + fatES + fatOutros

porcentSP = (fatSP * 100) / totalFat
porcentRJ = (fatRJ * 100) / totalFat
porcentMG = (fatMG * 100) / totalFat
porcentES = (fatES * 100) / totalFat
porcentOutros = (fatOutros * 100) / totalFat

print("Representação SP =", round(porcentSP, 2), "%")
print("Representação RJ =", round(porcentRJ, 2), "%")
print("Representação MG =", round(porcentMG, 2), "%")
print("Representação ES =", round(porcentES, 2), "%")
print("Representação Outros =", round(porcentOutros, 2), "%")