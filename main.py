# César Pantoja
from utils import data as data, data_analyze as data_analyze, data_clean as data_clean

if __name__ == '__main__':
    print('Cargar los datos de Housing')
    # data.fetch_fifa_data()
    data_players = data.load_player_data()
    # data_analyze.load_hist(data_players)
    # data_players.head()
    # data_analyze.graphPolar(1, data_players)

    print("=====================================")
    print("Data Clean - cambiar los valores de columna wage por valores numéricos ")
    print("=====================================")
    data_players['Value'] = data_players['Value'].apply(lambda x: data_clean.extract_value_from(x))
    data_players['Wage'] = data_players['Wage'].apply(lambda x: data_clean.extract_value_from(x))
    print("=====================================")
    print("Lista de mejores jugadores")
    print("=====================================")
    data_top = data_players.iloc[data_players.groupby(data_players['Position'])['Overall'].idxmax()][
        ['Position', 'Name', 'Age', 'Club', 'Nationality']]
    print(data_top)
    print("=====================================")
    print("cantidad de jugadores por País")
    print("=====================================")
    print(data_players['Nationality'].value_counts().head(8))
    #data_analyze.players_wages(data_players)
    data_analyze.players_value(data_players)

