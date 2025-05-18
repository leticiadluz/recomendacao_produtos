FROM quay.io/astronomer/astro-runtime:12.7.1

# Instala dbt e adaptador Snowflake
RUN pip install dbt-core dbt-snowflake

# Git
USER root
RUN apt-get update && apt-get install -y git

# Garante que o diretório .dbt exista
RUN mkdir -p /home/astro/.dbt && chown astro:astro /home/astro/.dbt

USER astro
