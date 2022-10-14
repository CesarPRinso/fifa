'''
clase la cuál usaremos para descargar datos más recientes
'''
import os
import zipfile
import urllib.request
import pandas as pd
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

# DOWNLOAD_ROOT = "https://www.kaggle.com/datasets/sanjeetsinghnaik/fifa-23-players-dataset?resource=download/"
DOWNLOAD_ROOT = "sanjeetsinghnaik/fifa-23-players-dataset"
PLAYERS_PATH = os.path.join("/", "players")


# PLAYERS_URL = DOWNLOAD_ROOT + "datasets/sanjeetsinghnaik/fifa-23-players-dataset/download?datasetVersionNumber=2"


def fetch_fifa_data(download_root=DOWNLOAD_ROOT, player_path=PLAYERS_PATH):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file("sanjeetsinghnaik/fifa-23-players-dataset", "Fifa 23 Players Data.csv")
    zipfile.ZipFile("Fifa%2023%20Players%20Data.csv.zip", 'r').extractall()


'''
 os.makedirs(player_path, exist_ok=True)
    tgz_path = os.path.join(player_path, "archive.zip")
    urllib.request.urlretrieve(player_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=player_path)
    housing_tgz.close()
'''


# cargar los datos, devolverá un dataFrame que contiene todos los datos
def load_player_data(player_path=PLAYERS_PATH):
    csv_path = os.path.join("FootballPlayerRawDataset.csv")
    return pd.read_csv(csv_path)
