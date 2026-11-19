FROM ubuntu:24.04 AS build
RUN apt-get update && apt-get install -y ca-certificates libstdc++6 && rm -rf /var/lib/apt/lists/*
COPY --from=node:16-bullseye /usr/local/ /usr/local/
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install && npm install -g serve@14.2.4
COPY . .
ARG REACT_APP_BACKEND_URL=http://localhost:8080
ENV REACT_APP_BACKEND_URL=${REACT_APP_BACKEND_URL}
RUN npm run build

FROM node:16-alpine
COPY --from=build /usr/local/lib/node_modules/serve /usr/local/lib/node_modules/serve
WORKDIR /usr/src/app
COPY --from=build /usr/src/app/build ./build
EXPOSE 5001
CMD ["node", "/usr/local/lib/node_modules/serve/build/main.js", "-s", "-l", "5001", "build"]
