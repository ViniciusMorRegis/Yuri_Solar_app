# Solar

Aplicativo desktop para um painel solar que segue a luz: 180° com um servo motor e 360° com um motor de passo, controlados por um Arduino conectado ao PC.

Feito em Python com CustomTkinter e Matplotlib.

> Projeto em desenvolvimento. Os dados exibidos ainda são simulados e a comunicação serial com o Arduino ainda não está ativa.

## Telas

- **Login** com imagem de fundo
- **Dashboard**: geração de energia (W) em gráfico, ângulo dos motores, luminosidade dos 4 LDRs da cruz e botões de modo automático/manual
- **Diagnóstico**: calibração do motor de passo e do servo, referência dos eixos e status do sistema
- **Relatórios**: energia gerada, pico de potência, tempo de geração e histórico de desempenho
- **Configurações**: em construção

## Como executar

```bash
pip install -r requirements.txt
python Solar.py
```

Login de teste: usuário `1`, senha `1`.

## Estrutura

- `Solar.py`: aplicativo principal
- `imagens/`: plano de fundo e ícones

## Autor

Vinicius de Moraes Regis
