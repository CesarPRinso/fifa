from zlib import crc32

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit


def test_estrato(housing):
    strat_train_set = None
    strat_test_set = None
    housing["quality"] = pd.cut(housing["Value(in Euro)"],
                                bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                labels=[1, 2, 3, 4, 5])
    # housing["income_cat"].hist() para visualizar muestreo estratificado basado en categoria de ingresos.
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]
    # test_size -> es para deternimar el porcentaje que destinaremos a test
    # random_state -> parámetro para indicar semilla aleatoria del generador
    # print("data para entrenar " + str(len(train_set)))
    # print("data para probar " + str(len(test_set)))
    return strat_train_set, strat_test_set
