# Climate-Toronto-ML
Project to forecast Toronto's climate
Working in progress

## Install with setup.py
```
- Create a new environment: conda create -n toronto_climate python=3.11
- Activate the environment: conda activate toronto_climate
- Install the packages: pip install -r requirements.txt
- Install PyTorch: pip install torch --index-url https://download.pytorch.org/whl/cu121 (Read more: https://pytorch.org/get-started/locally/)
- Install Keras 3.0.0: pip install keras==3.0.0
```

## Data Source
- [Climate Data Online](https://climate.weather.gc.ca/historical_data/search_historic_data_e.html)

## TODO
- [X] Notebooks - Data ingestion and merging
- [ ] Notebooks - Data viz, preprocessing, statistics, feature engineering, model selection, etc
- [ ] Convert to a package
- [ ] Add tests
- [ ] Update docs
