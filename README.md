# **Juazeiro**
## Sistema de aferição de presença escolar utilizando RFID e autenticação via bluetooth

### Descrição
Este projeto propõe o desenvolvimento de um sistema automatizado para registro de presença em ambientes acadêmicos, visando eliminar o toil docente e aumentar a confiabilidade dos dados coletados. A solução utiliza dois fatores de autenticação: posse (tag RFID) e proximidade/localização (dispositivo móvel via Bluetooth). O fluxo consiste em um registro inicial via hardware e uma validação assíncrona por meio de uma interface web que consome a API bluetooth web. A arquitetura foca em escalabilidade, permitindo que múltiplos usuários validem sua presença simultaneamente sem gerar gargalos de conexão no microcontrolador.
