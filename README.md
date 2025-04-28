
# Recomendação de Produtos com Análise de Cesta de Mercado

## Resumo 

## 

### 1 Introdução
Compreender os hábitos de consumo dos clientes é um fator crítico para o sucesso de estratégias de vendas, marketing e organização de produtos. Conhecer quais itens são frequentemente adquiridos em conjunto permite otimizar desde a disposição de produtos em lojas físicas e virtuais até a definição de campanhas promocionais mais assertivas.

Este projeto tem como objetivo aplicar a técnica de Market Basket Analysis para identificar padrões de compra entre produtos, revelando associações que, muitas vezes, não são evidentes a partir da simples observação dos dados brutos.

A análise será conduzida com base em Regras de Associação, utilizando o algoritmo Apriori, uma técnica amplamente reconhecida por sua eficiência em encontrar combinações de itens que ocorrem com frequência nas transações.

A partir dos padrões identificados, será possível automatizar a geração de recomendações de produtos e embasar ações estratégicas como agrupamento inteligente de produtos e ofertas personalizadas, promovendo assim uma experiência de compra mais relevante e aumentando o potencial de receita.

###  1.1 Regras de Associação
As regras de associação são técnicas de mineração de dados que buscam identificar relacionamentos frequentes entre itens em grandes conjuntos de dados.
Esses relacionamentos são expressos em regras do tipo: 
- "Se o cliente compra o produto A, então é provável que também compre o produto B."
- Cada regra é formada por um antecedente (o que o cliente compra) e um consequente (o que tende a ser comprado junto).
Essas regras são usadas para criar recomendações de produtos, campanhas de vendas cruzadas e para otimizar a organização de lojas.

###  1.2 Market Basket Analysis
O Market Basket Analysis (MBA) é a aplicação prática das regras de associação para analisar quais produtos são frequentemente comprados juntos.

Ele ajuda a entender o comportamento de compra dos clientes e é usado para sugerir produtos complementares, criar promoções combinadas e melhorar estratégias de vendas.


### 1.3 Métricas utilizadas
Durante a construção das regras de associação, três métricas principais são avaliadas:

| Métrica |  Definição | Fórmula|
| :------:| --------- | :-------:| 
Suporte       | Mede a frequência com que um item ou conjunto de itens aparece nas transações. Pode ser calculado para um único item (k=1) ou para combinações de dois, três ou mais itens (k>1).| Suporte (A) =  Transações (A) / Total de Transações|
Confiança      | Indica a probabilidade de o consequente ser comprado, dado que o antecedente já foi comprado.| Confiança (A ➔ B) = Transações com A e B / Transações com A  |
Lift     | Avalia a força da associação, comparando a probabilidade real de compra conjunta com a que seria esperada se os itens fossem independentes.   | Lift (A ➔ B) = Confiança (A ➔ B) / Suporte (B) |

Essas métricas ajudam a garantir que apenas padrões fortes e relevantes sejam considerados no processo de recomendação.

### 1.4 Importância do Suporte Mínimo

Para otimizar o desempenho do algoritmo Apriori e garantir que os padrões identificados sejam realmente úteis, é necessário definir um suporte mínimo. Essa etapa é essencial porque:
- Considerar todos os itens, inclusive os muito raros, gera um número excessivo de combinações possíveis, aumentando o tempo e a complexidade de processamento.
- Focar apenas nos itens com suporte relevante melhora a qualidade das regras geradas e torna o processo mais eficiente.
- Ao aplicar um suporte mínimo, trabalhamos apenas com produtos que têm participação significativa nas transações, tornando os resultados mais relevantes para o negócio.

### 1.5 Cálculo de Suporte e Crescimento de Combinações (k-itens)
O algoritmo Apriori trabalha de forma progressiva, avaliando conjuntos de itens com tamanhos diferentes (k), e eliminando combinações que não atingem o suporte mínimo em cada etapa.
Esse processo ajuda a reduzir a complexidade e focar apenas nos padrões relevantes. O funcionamento é o seguinte:

- k = 1 (Itens individuais): Primeiro, verificamos quantas vezes cada item isolado aparece no total de transações. Eliminamos o item que não atingiu o suporte mínimo definido. 
- k = 2 (Pares de itens): Depois, formamos combinações de dois itens (pares) entre os itens que passaram da etapa anterior. Novamente, eliminamos os pares de itens cujo suporte for inferior ao suporte mínimo estabelecido.
- k = 3 (Trios de itens): A seguir, formamos combinações de três itens, apenas a partir dos pares que ainda atendem ao suporte mínimo. Então, verificamos em quantas transações esses conjuntos de três itens aparecem. Se o suporte mínimo for atendido, mantemos esses trios para formar regras futuras, caso contrário, eliminamos o conjunto que não atingiu o suporte mínimo.
- K > 3: O processo pode continuar ao unirmos trios que compartilham dois itens em comum para formar conjuntos de quatro itens. Lembrando que esse crescimento é controlado, pois, só combinamos conjuntos que têm elementos em comum e que atenderam o suporte mínimo nos passos anteriores.

Exemplo:

**Transações**
| ID | Itens |
|:--:|:-------------------------|
| 1  | Pão, Leite, Manteiga      |
| 2  | Pão, Leite, Manteiga      |
| 3  | Pão, Café                 |
| 4  | Pão, Leite, Manteiga      |
| 5  | Café, Refrigerante        |
| 6  | Pão, Café, Refrigerante   |


**Contagem dos Itens (k=1), Suporte = 2/6 - 33,33%**

| Item | Ocorrências |Suporte (Ocorrências/6) |Sobrevive? (≥2/6) |
|:-------------|:------------|:-----------|:-----------|
| Pão          | 5            | 83,3%     |  Sim         |
| Leite        | 3            | 50%       |  Sim         |
| Manteiga     | 3            | 50%       |  Sim         |
| Café         | 3            | 50%       |  Sim         |
| Refrigerante | 2            | 33,3%     |  Sim         |

**Contagem dos Itens (k=2), Suporte = 2/6 - 33,33%**
| Par | Ocorrências | Suporte (Ocorrências/6) | Sobrevive? (≥26)|
|:--------------|:-----------|:----------------|:--------|
| (Pão, Leite)  | 3          | 50%            | Sim      |
| (Pão, Manteiga)  | 3       | 50%            | Sim      |
| (Leite, Manteiga) | 3      | 50%            | Sim      |
| (Pão, Café)       | 2      | 33,3%          | Sim      |
| (Café, Refrigerante) | 2   | 33,3%          |  Sim     |
| (Pão, Refrigerante)  | 1   | 16,7%          |  Não     |
| (Leite, Café) | 0          | 0%             |  Não     |
| (Leite, Refrigerante) | 0  | 0%             |  Não     |
| (Manteiga, Café)  | 0      | 0%             |  Não     |
| (Manteiga, Refrigerante)| 0| 0%             |  Não     |


**Contagem dos Itens (k=3), Suporte = 2/6 - 33,33%**

| Trio | Ocorrências | Suporte (Ocorrências/6) | Sobrevive? (≥2/6)|
|:--------------|:-----------|:----------------|:--------|
| (Pão, Leite, Manteiga) | 3 | 50% | Sim |
| (Pão, Café, Refrigerante) | 1 | 16,7% | Não |


https://www.youtube.com/watch?v=YGEYty0xYc0
25 minutos. 
confiança 

## 7 Instalação e configuração

### 7.1 Instalação do Airflow

Para instalação do Airflow, vamos utilizar o Astro CLI via Homebrew, que é uma abordagem mais prática e produtiva do que rodá-lo diretamente com Docker puro. O Astro simplifica a configuração do ambiente, abstraindo toda a complexidade envolvida em montar arquivos docker-compose.yml e configurá-los manualmente. Com poucos comandos, conseguimos ter um projeto pronto com a estrutura adequada, incluindo a pasta dags, o arquivo requirements.txt, configurações do Airflow e integração com o Docker.

Passo a passo: 
- Instalar o Ubuntu via Windows Store: Baixe e instale o Ubuntu 22.04 LTS na Microsoft Store.
- Configurações iniciais:
    - Usuário: Defina um usário
    - Senha: Defina uma senha.

Para verificar se o Ubuntu foi instalado corretamente, no terminal do Windows, execute:

```bash 
wsl -l -v
```
- Para instalar o Homebrew, no Ubuntu, execute:

```bash 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- Adicionar o Homebrew ao PATH:

```bash 
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```

- Teste se o Homebrew foi instalado corretamente:
```bash
brew --version
```

- Instalar compiladores (necessários para o Astro CLI):

```bash
sudo apt-get update && sudo apt-get install -y build-essential clang
```
- Por que isso é necessário?
    - O Homebrew tenta instalar o Astro CLI de duas formas:
        - Pacote pronto ("bottle") – mais rápido, mas pode não funcionar no WSL.
        - Código-fonte ("from source") – exige compiladores como clang ou gcc.

- Instalar o Astro CLI:
```bash
brew install astronomer/tap/astro
```

- Verificar a instalação do Astro CLI:
```bash
astro version
```

- Criar a pasta para o projeto:

```bash
mkdir ~/nome-projeto
```

- Acessar a pasta do projeto: 
```bash
cd ~/nome-projeto
```

- Inicializar o projeto Astro: 
```bash
astro dev init
```

- Integrar o Docker Desktop com o WSL 
    - No Docker Desktop:
        - Acesse Settings → Resources → WSL Integration
        - Habilite a integração para o Ubuntu.

- Verificar se o Docker está visível no Ubuntu: 
```bash
docker --version
```

- Dar permissão ao seu usuário para usar o Docker:
```bash
sudo usermod -aG docker $USER
```
- Após isso, reinicie o terminal para que a permissão seja aplicada.

- Resolver possível conflito com PostgreSQL instalado no Windows:
  - Se houver PostgreSQL instalado em sua máquina, pode haver conflito na porta 5432. Crie um arquivo de override:

```bash
nano docker-compose.override.yml
```

  - Coloque o seguinte conteúdo:

```bash
services:
  postgres:
    ports:
      - "5433:5432"
```

- Reinicie o Docker.
- Para iniciar o Astro,  acesse a pasta do projeto e execute:

```bash
cd ~/nome-projeto

astro dev start
```

- Se tudo estiver correto, você verá a mensagem:
```bash
✔ Project image has been updated
✔ Project started
➤ Airflow Webserver: http://localhost:8080
➤ Postgres Database: postgresql://localhost:5432/postgres
➤ The default Airflow UI credentials are: admin:admin
➤ The default Postgres DB credentials are: postgres:postgres
```

- Acesse o Airflow via navegador:  http://localhost:8080/

- Para criar Dags ou editar arquivos do projeto, abra o VSCode com:

```bash
code .
```

- Esse comando abrirá a pasta do projeto diretamente no VSCode do Windows.
- Na primeira vez que você usar code . no Ubuntu (WSL), o VSCode poderá iniciar o download e instalação automática do VSCode Server.
- O VSCode Server é um pequeno serviço instalado dentro do Ubuntu, necessário para permitir que o VSCode do Windows consiga acessar, editar e rodar comandos em arquivos Linux de forma integrada.

### 7.2 Configuração do dbt Cloud:


### 7.2 Configuração do SnowFlake: