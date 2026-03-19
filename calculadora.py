#!/bin/bash 

echo "--- calculadora simples ---"
read -p "digite o primeiro número: " n1
read -p "digite a operação (+, -, *, /): " op
read -p "digite o segundo número: " n2


resultado=$(echo "$n1 $op $n2" | bc -l)

echo "Resultado: $resultado"
