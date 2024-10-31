#!/bin/bash
foi i in {1..1000}; do
  curl localhost:31000/clientes
  sleep $1
  done