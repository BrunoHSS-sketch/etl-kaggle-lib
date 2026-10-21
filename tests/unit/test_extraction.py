from pipeline.extraction import Extraction


def test_dataset_downloader_success(tmp_path, monkeypatch, mock_settings, fake_kaggle_data):
    monkeypatch.setattr(
        "pipeline.extraction.kagglehub.dataset_download",
        lambda dataset_name: str(fake_kaggle_data)
    )

    fake_bronze_dir = mock_settings.data_root_dir / "bronze" / "olist"
    fake_bronze_dir.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr("pipeline.extraction.BRONZE_DIR", fake_bronze_dir)

    # Executa a extração
    extractor = Extraction(settings=mock_settings)
    extractor.dataset_dowloader()

    # Validação
    expected_parquet = fake_bronze_dir / "olist_customers_dataset.parquet"
    assert expected_parquet.exists()