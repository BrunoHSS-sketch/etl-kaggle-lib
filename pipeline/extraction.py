from pathlib import Path

import kagglehub
from core.config import settings, logger, BRONZE_DIR
import polars as pl

class Extraction():
    def __init__(self, settings):
        self.settings = settings

    def dataset_dowloader(self):

        logger.info(f"Baixando dataset para: {self.settings.data_path}")
        raw_dataset = kagglehub.dataset_download(self.settings.dataset)

        if getattr(self.settings, "extesion", "csv") == "csv":
            for csv_file in Path(raw_dataset).glob("*.csv"):
                try:
                    parquet_file = BRONZE_DIR / f"{csv_file.stem}.parquet"
                    pl.scan_csv(csv_file).sink_parquet(parquet_file)
                    logger.info(f"Convertido com sucesso: {csv_file.name} -> {parquet_file.name}")
                except Exception as e:
                    logger.error(f"Erro na conversão do arquiv {csv_file.name}: {e}")