# O Pikachu Leiturista

<div align="center">
  
  <img src="https://github.com/matheus-srego/PikachuLeiturista/blob/main/Pikachu/Docs/Images/PikachuWallpaper.png" width="45%" height="65%"/>
  
  **Dataset retirada do Kaggle:** [Smart Home Dataset with weather Information](https://www.kaggle.com/taranvee/smart-home-dataset-with-weather-information)
  
</div>


## Índice

## Objetivo

> *“Implementar um sistema de predição baseado em dados obtidos a partir de sensores de dispositivos IoT conectados à nuvem, documentando a solução e explicando a modelagem utilizada.”*

Utilizando tecnologias AWS, Python 3, análise e predição de dados, o projeto de Bloco em IoT e Data Science denominado Pikachu realiza a coleta, predição e avisos sobre o uso de energia doméstica. Desta forma, o projeto tem como finalidade auxiliar o usuário em uma utilização e controle conscientes da energia de sua residência.

## Arquitetura do Projeto

<img align="center" src="https://github.com/matheus-srego/PikachuLeiturista/blob/main/Pikachu/Docs/Images/WorkflowPikachu.png"/>

## Stack

 - ```Docker```
 - ```Python 3```
   - ```Pandas```
   - ```Numpy```
   - ```Matplotlib```
   - ```Seaborn```
 - ```AWS IoT Core```
 - ```AWS Cloud9```

## Descrição
O projeto Pikachu Leiturista faz parte do desenvolvimento do projeto de bloco de IoT, do Instituto Infnet. Este projeto realizará a medição e predição da energia residencial gasta durante o ano.

Pikachu tem como finalidade resolver o problema de desperdício de energia doméstico. O projeto deverá realizar análises do consumo de energia de forma diária, mensal e anual.
Coletando todos os dados durante o dia (24h) realizará a análises de:

 - Maior e menor consumo.
 - Contagem da falta de energia (guardando horário que faltou e retornou a energia).
 - Comparação dos gastos em 12 meses.
 - Armazenar os dados em nuvem.
 - Calcular o consumo, em reais.
   - *Consumo=(potência em watt / 1000) * (tempo em horas) = total em KWh*
 - Pegar os dados e predizer os gastos futuros da residência.

Desta forma todos os dados e serviços serão disponibilizados em uma web service, assim facilitando o entendimento por parte do usuário.

## Como executar o projeto

**Passo 0:** Faça o clone do Projeto.
```bash
git clone https://github.com/matheus-srego/PikachuLeiturista.git
```

**Passo 1:** Entre na pasta do projeto.
```bash
cd ~/PikachuLeiturista/Pikachu/
```

**Passo 2:** Execute o comando.
```bash
python /Code/main.py
```

## Licença
Este repositório utiliza o [MIT Licensed](https://github.com/matheus-srego/PikachuLeiturista/blob/main/LICENSE).
