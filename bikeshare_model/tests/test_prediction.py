"""
Note: These tests will fail if you have not first trained the model.
"""

import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np
from bikeshare_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    #expected_no_predictions = 179

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)
    assert result.get("errors") is None

    #print(predictions)
        # for i,x in enumerate(predictions):
        #     assert(abs(x - sample_input_data["cnt"][i+1]) < 1)

    #assert(abs(predictions[0] - sample_input_data["cnt"][0]) < 1)

    #print(predictions)

    # i = 0
    # for index, row in sample_input_data.iterrows():
    #     assert(abs(row["cnt"] - predictions[i]) < 300)
    #     print(i)
    #     i = i + 1 



    #assert(abs(predictions - sample_input_data["cnt"]) < 1)
    #assert len(predictions) == expected_no_predictions
    # _predictions = list(predictions)
    #y_true = sample_input_data["cnt"]
