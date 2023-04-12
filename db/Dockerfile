FROM mongo:4.4.8

ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=admin
ENV MONGO_INITDB_DATABASE=pyposterdb

COPY /docker-entrypoint-initdb.d/init-mongo.js /docker-entrypoint-initdb.d/
