# Project: Dockerize python flask application

This project helps us understand and know how to dockerize an application (python flask in this case)

## Overview

### Introduction

- Tech stack: `python`, `docker`, `flask`

### Prerequisite

- You have docker installed on your machine
- Basic knowledge about docker

## 1-Install docker

- Docker engine

## 2-Build the docker image

- Run `docker build -t my-flask-app .`

## 3-Run the Docker container based on the image

- Run `docker run -p 5000:5000 my-flask-app`

## 4-Verify the result

- `curl localhost:5000`
- Or open http://localhost:5000/ in your browser

----------------------------------------------------------------------------------------------

## 5- I have extented this more in Kubernetes

- Created a deployment and service yml files inside 'app-ns' namespace and added basic requirements for kubernetes with port: 80-external port and targetport: 5000
- I have set the number of replicas to 10 and added rolling update strategy with maxUnavailable: 3 and maxSurge: 3
- I have applied the deployment and service files using
 `kubectl apply -f k8s/deployment.yml`
 `kubectl apply -f k8s/service.yml`

## 6- To verify the result pod running

- Run `kubectl get pod -n app-ns`
- Run `kubectl get svc -n app-ns`

## 7- To access the app in browser

- Run `http://localhost:80/`