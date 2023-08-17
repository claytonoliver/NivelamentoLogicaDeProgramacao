# NivelamentoLogicaDeProgramacao
Cap. 3 Desvio encadeado, Composto e Simples


Capítulo 3: Cálculo do Imposto de Renda utilizando entrada e saída de dados com estruturas condicionais compostas.

| :placard: FIAP |    |
| -------------  | --- |
| :sparkles: Nome        | **Calculo De Imposto**
| :label: Tecnologias | Python


## Pseudo código

**Calculo de imposto de renda**

Critérios

Base de cálculo	                Alíquota

Até R$ 2.112,00	-	-           isento
De R$ 2.112,01 até R$ 2.826,65	7,5% <br/>
De R$ 2.826,66 até R$ 3.751,05	15,0%<br/>
De R$ 3.751,06 até R$ 4.664,68	22,5%<br/>
Acima de R$ 4.664,68	        27,5%<br/>

Início

// Solicitar o valor da renda ao usuário <br/>
Escreva "Digite o valor da renda: "<br/>
Leia renda


// Verificar as faixas de imposto e calcular o imposto de renda<br/>
Se renda <= 2112.00 Então<br/>
    imposto = 0<br/>
Senão Se renda <= 2826.65 Então<br/>
    imposto = renda * 0.075<br/>
Senão Se renda <= 3751.05 Então<br/>
    imposto = renda * 0.15<br/>
Senão Se renda <= 4664.68 Então<br/>
    imposto = renda * 0.225<br/>
Senão
    imposto = renda * 0.275<br/>
Fim Se

// Exibir o valor do imposto de renda
Escreva "O valor do Imposto de Renda é: ", imposto

Fim
