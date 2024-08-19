#Modules
import pandas as pd
import matplotlib.pyplot as plt

#Global Variables
exit_program = False

# Dataframe Setup & New .csv for data cleaning
file_path = 'data/all_seasons.csv'
original_df = pd.read_csv(file_path)

columns_to_delete = ['team_abbreviation', 'age', 'player_weight', 'college', 'country', 'draft_year', 'draft_round', 'draft_number', 'gp', 'pts', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct']
nba_df = original_df.drop(columns=columns_to_delete)

nba_df.to_csv('data/relevantstats', index=False)

nba_df = pd.read_csv('data/relevantstats.csv')

nba_df = pd.read_csv('data/relevantstats.csv',
                     header=None,
                     names=['Player', 'Height', 'Rebounds'])

# Functions for Program
def displayOriginalData():
    print(original_df)

def displayNewData():
    print(nba_df)

def visualisePlayerRebounds():
    plt.scatter(nba_df['Height'], nba_df['Rebounds'], color='blue', alpha=0.5)
    plt.title('Correlation between Player Height and Rebounds')
    plt.xlabel('Height (cm)')
    plt.ylabel('Average Rebounds per Game')
    plt.show()

def menuOptions():
    global exit_program

    print("""Welcome to the NBA Player Rebounds Database!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the new dataset
    3 - Visualise Player Rebounds
    4 - Quit Program
        """)
    
    try:
        selection = int(input('Enter Selection: '))

        if selection == 1:
            displayOriginalData()
        elif selection == 2:
            displayNewData()
        elif selection == 3:
            visualisePlayerRebounds()
        elif selection == 4:
            exit_program = True
        else:
            print('Please select a number between 1 and 5.')

    except ValueError:
        print('Please enter a valid number.')

# Main Program
while not exit_program:
    menuOptions()