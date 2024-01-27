import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from bikeshare_model.config.core import config
from bikeshare_model.processing.features import WeathersitImputer


def test_weathersit_imputation(sample_input_data):
    # Given
    imputer = WeathersitImputer(config.model_config.weathersit_var)

    # When
    imputed = imputer.fit(sample_input_data).transform(sample_input_data)

    # Then
    assert imputed.loc[12230, "weathersit"] is not None
