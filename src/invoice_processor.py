# invoice_processor.py

import os
import pandas as pd
from ocr_engine import extract_text_from_image
from email_handler import download_invoices

class InvoiceProcessor:
    def __init__(self, invoice_directory, report_directory):
        self.invoice_directory = invoice_directory
        self.report_directory = report_directory

    def process_invoices(self):
        invoices = self._get_invoice_files()
        for invoice in invoices:
            text = extract_text_from_image(invoice)
            data = self._extract_invoice_data(text)
            self._save_report(data)

    def _get_invoice_files(self):
        return [os.path.join(self.invoice_directory, f) for f in os.listdir(self.invoice_directory) if f.endswith(('.png', '.jpg', '.pdf'))]

    def _extract_invoice_data(self, text):
        # Implementar a lógica para extrair dados relevantes do texto
        # Exemplo: valores, datas, fornecedores
        data = {
            'value': None,  # Extrair valor
            'date': None,   # Extrair data
            'supplier': None  # Extrair fornecedor
        }
        # Lógica de extração a ser implementada
        return data

    def _save_report(self, data):
        report_path = os.path.join(self.report_directory, 'invoice_report.csv')
        df = pd.DataFrame([data])
        df.to_csv(report_path, mode='a', header=not os.path.exists(report_path), index=False)