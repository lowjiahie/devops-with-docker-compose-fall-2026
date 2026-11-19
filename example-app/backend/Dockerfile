FROM golang:1.16 AS build
WORKDIR /usr/src/app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build

FROM ubuntu:24.04
RUN apt-get update && apt-get install -y ca-certificates libstdc++6 && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
COPY --from=build /usr/src/app/server ./server
EXPOSE 8080
CMD ["./server"]
