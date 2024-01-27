import sys
from pathlib import Path

from sklearn.metrics import accuracy_score

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import Union
import pandas as pd
import numpy as np

from bikeshare_model import __version__ as _version
from bikeshare_model.config.core import config
from bikeshare_model.processing.data_manager import load_pipeline
from bikeshare_model.processing.validation import validate_inputs


pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
bikeshare_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data: Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model"""

    validated_data, errors = validate_inputs(input_df=pd.DataFrame(input_data))

    # validated_data = validated_data.reindex(columns = ['dteday', 'season', 'hr', 'holiday', 'weekday', 'workingday',
    #                                                   'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'yr', 'mnth'])
    validated_data = validated_data.reindex(columns=config.model_config.features)
    print(validated_data)
    results = {"predictions": None, "version": _version, "errors": errors}

    if not errors:
        predictions = bikeshare_pipe.predict(validated_data)
        results = {
            "predictions": np.floor(predictions),
            "version": _version,
            "errors": errors,
        }
        #print(results)

    #print(type(predictions))
    #print("Accuracy Score:" +  accuracy_score(np.array([139])), predictions)

    return results


if __name__ == "__main__":

    # data_in = {
    #     "dteday": ["2012-11-6"],
    #     "season": ["winter"],
    #     "hr": ["6pm"],
    #     "holiday": ["No"],
    #     "weekday": ["Tue"],
    #     "workingday": ["Yes"],
    #     "weathersit": ["Clear"],
    #     "temp": [16],
    #     "atemp": [17.5],
    #     "hum": [30],
    #     "windspeed": [10],
    # }

    data_in = {
        "dteday": ["2012-11-05"],
        "season": ["winter"],
        "hr": ["6am"],
        "holiday": ["No"],
        "weekday": ["Mon"],
        "workingday": ["Yes"],
        "weathersit": ["Mist"],
        "temp": [6.1],
        "atemp": [3.0014000000000003],
        "hum": [49.0],
        "windspeed": [19.0012],
    }

    make_prediction(input_data=data_in)

# dteday,     season, hr, holiday,weekday,workingday, weathersit, temp,   atemp,              hum,    windspeed,  casual, registered, cnt
# 2012-11-05, winter, 6am,No,     Mon,    Yes,        Mist,       6.1,    3.0014000000000003, 49.0,   19.0012,    4,      135,        139
    
# 2011-07-13,fall,    4am,No,     Wed,    Yes,        Clear,      26.78,  28.998799999999996, 57.99999999999999,16.997899999999998,0,5,5