#Modules
import pandas as pd
import matplotlib.pyplot as plt

#Global Variables
exit_program = False

# Dataframe Setup
file_path = 'data/all_seasons.csv'
og_df = pd.read_csv(file_path)

columns_to_delete = ['team_abbreviation', 'age', 'player_weight', 'college', 'country', 'draft_year', 'draft_round', 'draft_number', 'gp', 'pts', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'season']
nba_df = og_df.drop(columns=columns_to_delete)

nba_df.to_csv('data/relevantstats', index=False)

nba_df = pd.read_csv('data/all_seasons.csv')

nba_df = pd.read_csv('data/all_seasons.csv',
                     header=None,
                     names=['Player', 'Height', 'Rebounds'])

# Functions for Program
def displayOriginalData():
    print(og_df)

def visualizePlayerRebounds():
    nba_df.plot(
                kind='bar',
                x='Player',
                y='Rebounds',
                color='black',
                alpha=0.3,
                title='Player Rebounds')
    plt.show()


