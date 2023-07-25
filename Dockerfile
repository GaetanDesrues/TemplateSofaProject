FROM gdesrues/sofa:23.06

WORKDIR /app

# A `.env` file must contain your github token
COPY .env .
RUN source /app/.env && pip install git+https://${TOKEN}@github.com/GaetanDesrues/SofaScene.git

VOLUME /app/src
WORKDIR /app/src
