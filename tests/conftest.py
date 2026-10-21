from pathlib import Path
import pytest


@pytest.fixture
def mock_settings(tmp_path):
    """
    Fixture global que retorna um objeto de configuração fake
    apontando para uma pasta temporária em disco.
    """

    class MockSettings:
        dataset = "olistbr/brazilian-ecommerce"
        extension = "csv"
        data_root_dir = tmp_path / "data"

    return MockSettings()


@pytest.fixture
def fake_kaggle_data(tmp_path):
    """
    Fixture que simula a estrutura de arquivos CSV baixados do Kaggle.
    """
    kaggle_dir = tmp_path / "kaggle_raw"
    kaggle_dir.mkdir(parents=True, exist_ok=True)

    # Cria um CSV de exemplo (ex: customers)
    csv_file = kaggle_dir / "olist_customers_dataset.csv"
    csv_file.write_text("customer_id,customer_city\n12345,Jaragua do Sul\n67890,Blumenau\n")

    return kaggle_dir