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

def visualisePlayerRebounds():
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

def menuOptions():
    global exit_program

    print("""Welcome to the NBA Player Stats Visualizer!
          
    Please select an option:
    1 - Show the original dataset
    2 - Visualize Player Rebounds
    3 - Filter Players by Rebounds
    4 - Quit Program
        """)
    
    try:
        selection = int(input('Enter Selection: '))

        if selection == 1:
            displayOriginalData()
        elif selection == 2:
            visualisePlayerRebounds()
        elif selection == 3:
            min_rebounds = int(input('Enter minimum rebounds to filter players: '))
            filterTopRebounders(min_rebounds)
        elif selection == 4:
            exit_program = True
        else:
            print('Please select a number between 1 and 4.')

    except ValueError:
        print('Please enter a valid number.')

# Main Program
while not exit_program:
    menuOptions()