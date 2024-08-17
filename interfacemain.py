#Modules
import pandas as pd
import matplotlib.pyplot as plt

#Global Variables
exit_program = False

# Dataframe Setup & New .csv for data cleaning
file_path = 'data/all_seasons.csv'
og_df = pd.read_csv(file_path)

columns_to_delete = ['team_abbreviation', 'age', 'player_weight', 'college', 'country', 'draft_year', 'draft_round', 'draft_number', 'gp', 'pts', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct']
nba_df = og_df.drop(columns=columns_to_delete)

nba_df.to_csv('data/relevantstats', index=False)

nba_df = pd.read_csv('data/relevantstats.csv')

nba_df = pd.read_csv('data/relevantstats.csv',
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

def filterTopRebounders(min_rebounds):
    filtered_df = nba_df[nba_df['Rebounds'] > min_rebounds]
    print(f"Players with more than {min_rebounds} rebounds:")
    print(filtered_df)

def visualizeTopScorers(min_points):
    top_scorers_df = nba_df[nba_df['Points'] > min_points]
    top_scorers_df.plot(
                kind='bar',
                x='Player',
                y='Points',
                color='green',
                alpha=0.5,
                title=f'Players with more than {min_points} Points')
    plt.show()

def getPlayerStats(player_name):
    player_stats = nba_df[nba_df['Player'] == player_name]
    if not player_stats.empty:
        print(player_stats)
    else:
        print(f"No data found for player: {player_name}")
