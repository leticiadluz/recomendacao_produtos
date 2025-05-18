FROM quay.io/astronomer/astro-runtime:12.7.1

#dbt e adaptador Snowflake
RUN pip install dbt-core dbt-snowflake

#Git
USER root
RUN apt-get update && apt-get install -y git

USER astro