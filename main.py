import os
import logging
from src.invoices_creator import InvoiceCreator
from src.config_utils import setup_logging, load_config, load_invoice_data

def main():
    """Função principal para orquestrar o processamento de faturas."""
    setup_logging()
    config_path = os.path.join(os.path.dirname(__file__), "config/config.ini")
    logging.info(f"Carregando configuração de: {config_path}")

    try:
        # Carrega o arquivo de configuração
        config = load_config(config_path)

        # Carrega os dados da fatura
        invoice_data = load_invoice_data(config)

        # Cria a fatura usando o InvoiceCreator
        driver_path = "chromedriver"  # Substitua pelo caminho correto do ChromeDriver
        invoice_creator = InvoiceCreator(driver_path=driver_path)
        invoice_creator.create_invoice(
            "https://invoicehome.com/invoices/160979804/edit?doc_type=INVOICE&locale=pt",
            invoice_data,
        )

        logging.info("Processamento de faturas concluído com sucesso."),m

    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()