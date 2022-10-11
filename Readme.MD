# Lambda para Ligar/Desligar Instâncias EC2

Lambda para desligar/ligar instâncias EC2 em horários determinados, se apoiando em Triggers/CRON (Eventbridge).

Da forma como foi configurada a Lambda, na mesma Lambda poderá executar os fluxos de Start/Stop da(s) instância(s), não sendo necessário criar uma Lambda para ligar e outra Lambda para Desligar.


&nbsp;

# Para configurar a Lambda, informar as especificações do Runtime:

## Runtime Settings

- NomeScript: lambda.py

- Runtime: Python 3.7

- Handler: lambda.handler

&nbsp;


# Permissions / Execution Role:

Uma vez que a Lambda precisa ter permissão para performar as ações de Start e Stop instance, adicionar em sua ROLE a policy:

```

{
      "Effect": "Allow",
      "Action": [
        "ec2:Start*",
        "ec2:Stop*"
      ],
      "Resource": "*"
}


```

&nbsp;


## Triggers:

Será necessário somente criar 2 Triggers, EventBridge (CloudWatch Events), com os agendamentos CRON desejados (ex: StartEC2, StopEC2).

Na criação do Event, além da expressão CRON em Event Schedule, em Targer especificar o `input constant`, o objeto/JSON correspondente.

No objeto/JSON, deverão ser definidos:

> **action**: start | stop
> **instances**: Array/List com o ID/IDs das instâncias;
> **region**: Região da instância, ex: us-east-1


- Exemplo: Start EC2:

```json

{
  "action": "start",
  "instances": [
    "i-0a031f700feabacfb"
  ],
  "region": "sa-east-1"
}


```


- Exemplo: Stop EC2:

```json

{
  "action": "stop",
  "instances": [
    "i-0a031f700feabacfb"
  ],
  "region": "sa-east-1"
}


```
