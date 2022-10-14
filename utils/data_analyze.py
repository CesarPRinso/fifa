import matplotlib

matplotlib.use('macosx')

import matplotlib.pyplot as plt
import requests
import random
from math import pi
import matplotlib.image as mpimg
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
import seaborn as sns
import pandas as pd

# mostrar histograma
def load_hist(data_players):
    # obtener las 5 filas superiores
    data_players.head()
    # obtener información
    data_players.info()
    '''
    el método info() es útil para obtener una descripción rápida de los datos.
    en particular, número total de filas, tipo de cada atributo, el número de valores no nulo 
    '''
    # data_housing["ocean_proximity"].value_counts()  # para averiguar qué categorías existen y cuántos distritos
    # pertenecen a cada categoría.
    data_players.hist(bins=50, figsize=(20, 15))
    plt.show()


def vizualizate_data_geographical(data_player):
    data_player.plot(kind="scatter", x="Value", y="Overall", alpha=0.1)
    plt.show()


def details(row, title, image, age, nationality, photo, club, players):
    flag_image = "img_flag.jpg"
    player_image = "img_player.jpg"
    logo_image = "img_club_logo.jpg"

    '''img_flag = requests.get(image).content
    with open(flag_image, 'wb') as handler:
        handler.write(img_flag)

    player_img = requests.get(photo).content
    with open(player_image, 'wb') as handler:
        handler.write(player_img) '''

    '''logo_img = requests.get(logo).content
    with open(logo_image, 'wb') as handler:
        handler.write(logo_img)'''

    r = lambda: random.randint(0, 255)
    colorRandom = '#%02X%02X%02X' % (r(), r(), r())

    if colorRandom == '#ffffff': colorRandom = '#a5d6a7'

    basic_color = '#37474f'
    color_annotate = '#01579b'

    # img = mpimg.imread(flag_image)

    plt.figure(figsize=(15, 8))
    categories = list(players)[1:]
    coulumnDontUseGraph = ['Flag', 'Age', 'Nationality', 'Photo', 'Logo', 'Club']
    N = len(categories) - len(coulumnDontUseGraph)

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    ax = plt.subplot(111, projection='polar')
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories, color='black', size=17)
    ax.set_rlabel_position(0)
    plt.yticks([25, 50, 75, 100], ["25", "50", "75", "100"], color=basic_color, size=10)
    plt.ylim(0, 100)

    values = players.loc[row].drop('Name').values.flatten().tolist()
    valuesDontUseGraph = [image, age, nationality, photo, club]
    values = [e for e in values if e not in (valuesDontUseGraph)]
    values += values[:1]

    ax.plot(angles, values, color=basic_color, linewidth=1, linestyle='solid')
    ax.fill(angles, values, color=colorRandom, alpha=0.5)
    axes_coords = [0, 0, 1, 1]
    ax_image = plt.gcf().add_axes(axes_coords, zorder=-1)
    # ax_image.imshow(img, alpha=0.5)
    ax_image.axis('off')

    ax.annotate('Nationality: ' + nationality.upper(), xy=(10, 10), xytext=(103, 138),
                fontsize=12,
                color='white',
                bbox={'facecolor': color_annotate, 'pad': 7})

    ax.annotate('Age: ' + str(age), xy=(10, 10), xytext=(43, 180),
                fontsize=15,
                color='white',
                bbox={'facecolor': color_annotate, 'pad': 7})

    ax.annotate('Team: ' + club.upper(), xy=(10, 10), xytext=(92, 168),
                fontsize=12,
                color='white',
                bbox={'facecolor': color_annotate, 'pad': 7})

    '''arr_img_player = plt.imread(player_image, format='jpg')

    imagebox_player = OffsetImage(arr_img_player)
    imagebox_player.image.axes = ax
    abPlayer = AnnotationBbox(imagebox_player, (0.5, 0.7),
                              xybox=(313, 223),
                              xycoords='data',
                              boxcoords="offset points"
                              )
    arr_img_logo = plt.imread(logo_image, format='jpg')

    imagebox_logo = OffsetImage(arr_img_logo)
    imagebox_logo.image.axes = ax
    abLogo = AnnotationBbox(imagebox_logo, (0.5, 0.7),
                            xybox=(-320, -226),
                            xycoords='data',
                            boxcoords="offset points"
                            )

    ax.add_artist(abPlayer)
    ax.add_artist(abLogo)'''

    plt.title(title, size=50, color=basic_color)
    plt.show()


def graphPolar(id, data):
    if 0 <= id < len(data.ID):
        details(row=data.index[id],
                title=data['Name'][id],
                age=data['Age'][id],
                photo=data['Photo'][id],
                nationality=data['Nationality'][id],
                image=data['Flag'][id],
                club=data['Club'][id], players=data)
    else:
        print('The base has 17917 players. You can put positive numbers from 0 to 17917')


def players_wages(data):
    some_countries = ('England', 'Germany', 'Spain', 'Argentina', 'France', 'Brazil', 'Italy', 'Columbia')
    data_countries = data.loc[data['Nationality'].isin(some_countries) & data['Wage']]
    plt.rcParams['figure.figsize'] = (12, 7)
    ax = sns.barplot(x=data_countries['Nationality'], y=data_countries['Wage'], palette='Purples')
    ax.set_xlabel(xlabel='Countries', fontsize=9)
    ax.set_ylabel(ylabel='Wage', fontsize=9)
    ax.set_title(label='Distribution of Wages of players from different countries', fontsize=15)
    plt.show()


def age_distribution(fifa_df):
    useful_feat = ['Name',
                   'Age',
                   'Photo',
                   'Nationality',
                   'Flag',
                   'Overall',
                   'Potential',
                   'Club',
                   'Club Logo',
                   'Value',
                   'Wage',
                   'Preferred Foot',
                   'International Reputation',
                   'Weak Foot',
                   'Skill Moves',
                   'Work Rate',
                   'Body Type',
                   'Position',
                   'Joined',
                   'Contract Valid Until',
                   'Height',
                   'Weight',
                   'Crossing',
                   'Finishing',
                   'HeadingAccuracy',
                   'ShortPassing',
                   'Volleys',
                   'Dribbling',
                   'Curve',
                   'FKAccuracy',
                   'LongPassing',
                   'BallControl',
                   'Acceleration',
                   'SprintSpeed',
                   'Agility',
                   'Reactions',
                   'Balance',
                   'ShotPower',
                   'Jumping',
                   'Stamina',
                   'Strength',
                   'LongShots',
                   'Aggression',
                   'Interceptions',
                   'Positioning',
                   'Vision',
                   'Penalties',
                   'Composure',
                   'Marking',
                   'StandingTackle',
                   'SlidingTackle',
                   'GKDiving',
                   'GKHandling',
                   'GKKicking',
                   'GKPositioning',
                   'GKReflexes']
    df = pd.DataFrame(fifa_df, columns=useful_feat)
    plt.figure(1, figsize=(18, 7))
    sns.countplot(x='Age', data=df, palette='Accent')
    plt.title('Age distribution of all players')
    plt.show()


def preprocess_value(x):
    x = str(x).replace('€', '')
    if ('M' in str(x)):
        x = str(x).replace('M', '')
        x = float(x) * 1000000
    elif ('K' in str(x)):
        x = str(x).replace('K', '')
        x = float(x) * 1000
    return float(x)


def players_value(df):
    df['Value'] = df['Value'].apply(preprocess_value)
    plt.figure(1, figsize=(18, 7))
    sns.countplot(x='Value', data=df)
    plt.title('Value distribution of all players')
    plt.show()
