import logging
from configparser import ConfigParser

def setup_logging():
    """Configura o sistema de logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def load_config(config_path):
    """Carrega o arquivo de configuração."""
    config = ConfigParser()
    config.read(config_path)
    return config

def load_invoice_data(config):
    """Carrega os dados da fatura a partir do arquivo de configuração."""
    try:
        invoice_data = [
            {"xpath": '//*[@id="nickname"]', "value": config.get("invoice_data", "invoice_number")},
            {"xpath": '//*[@id="companieName"]', "value": config.get("invoice_data", "provider_name")},
            {"xpath": '//*[@id="__next"]/div/section/div/div[1]/div[2]/div[2]/div/div/div[2]/div/input', "value": config.get("invoice_data", "provider_cnpj")},
            {"xpath": '//*[@id="address"]', "value": config.get("invoice_data", "client_address")},
            {"xpath": '//*[@id="client-phone"]', "value": config.get("invoice_data", "phone_number")},
            {"xpath": '//*[@id="client-email"]', "value": config.get("invoice_data", "email")},
            {"xpath": '//*[@id="customerName"]', "value": config.get("invoice_data", "client_name")},
            {"xpath": '//*[@id="__next"]/div/section/div/div[1]/div[5]/div[2]/div/div/div[2]/div/input', "value": config.get("invoice_data", "cnpj_cliente")},
            {"xpath": '//*[@id="opening-balance"]', "value": config.get("invoice_data", "item_price")},
            {"xpath": '//*[@id="fatura-vencimento"]', "value": config.get("invoice_data", "invoice_date")},
            {"xpath": '//*[@id="nickname"]', "value": config.get("invoice_data", "title")},
            {"xpath": '//*[@id="description"]', "value": config.get("invoice_data", "description")}
        ]
        return invoice_data
    except Exception as e:
        logging.error(f"Erro ao carregar os dados da fatura: {e}")
        raise