adv_mla_at1
==============================
Kaggle user - [Kritz_23](https://www.kaggle.com/kritz23)

This is a repository for AT1 Adv MLA which is also a [Kaggle Competition](https://www.kaggle.com/competitions/advmla-2023-spring/overview) <br>
I have performed various [experiments](notebooks) on the given dataset in order to achieve the best AUCROC score on validation and test sets. The best score was pulled off in Week 3 with [Random Forest + SMOTE](notebooks/dhawale_kritika-24587661-week3_B_rand_forest.ipynb). 


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
## Saved Models
Scalers, one hot encoders and trained models are saved in [models](models). The best model which has the highest validation and test AUCROC score is saved as [nba_draft_prediction.joblib](models/best_model/nba_draft_prediction.joblib). 

---------

## Prediction
If you want to straight away make predictions on the test set(or any other set), in your terminal go to the project folder and follow these steps: <br>
1. Activate your venv with poetry <br>
    poetry shell
2. Run the python script to make predictions with the best model <br>
    python src/models/predict_model.py

Note: You can change the output file name in the [prediction script](src/models/predict_model.py) and you will have a csv file in [submission_files](submission_files).

