# Automação de Processamento de Faturas

Este repositório contém um projeto em Python para automatizar o preenchimento de faturas no [InvoiceHome](https://invoicehome.com/?locale=pt&utm_source=chatgpt.com), envio de faturas por e-mail, e processamento de faturas recebidas. Utiliza OCR para extrair informações relevantes de PDFs ou imagens e gera relatórios consolidados de pagamentos.

## Funcionalidades

- **Preenchimento automático de faturas**: Preenche os campos de faturas no [InvoiceHome](https://invoicehome.com/?locale=pt&utm_source=chatgpt.com) automaticamente.
- **Envio de faturas por e-mail**: Envia múltiplas faturas geradas para destinatários predefinidos.
- **Processamento de faturas recebidas**: Baixa as faturas recebidas por e-mail, processa com OCR e extrai dados como valores, datas e fornecedores.
- **Relatórios de pagamentos**: Gera relatórios detalhados a partir dos dados extraídos das faturas.

## Tecnologias

- **Python**: Linguagem de programação principal.
- **Selenium**: Automação de navegação em sites.
- **smtplib / imaplib**: Envio e recebimento de e-mails.
- **Tesseract OCR**: Reconhecimento óptico de caracteres para extração de texto de imagens e PDFs.
- **Pandas**: Manipulação e análise de dados para gerar relatórios.

## Como Usar

1. Clone este repositório para o seu ambiente local:
   ```bash

   git clone <https://github.com/souzatrixie/FaturaBot>
   ```

2. Instale as dependências necessárias:

   pip install -r requirements.txt


3. Configure suas credenciais de e-mail (Google, por exemplo) no arquivo de configuração do projeto.

4. Execute os scripts para automatizar o preenchimento, envio e processamento de faturas.

## Como Contribuir

1. Fork o repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie suas alterações (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request para revisão.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.