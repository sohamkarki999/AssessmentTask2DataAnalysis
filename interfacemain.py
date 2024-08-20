# Modules
import pandas as pd
import matplotlib.pyplot as plt

# Global Variables
exit_program = False  # Flag to control the exit of the program

# Dataframe Setup & New .csv for data cleaning
file_path = 'data/all_seasons.csv'  # Path to the original dataset
original_df = pd.read_csv(file_path)  # Load the original dataset

# Columns to remove for data cleaning
columns_to_delete = ['team_abbreviation', 'age', 'player_weight', 'college', 'country', 'draft_year', 'draft_round', 'draft_number', 'gp', 'pts', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'season']
nba_df = original_df.drop(columns=columns_to_delete)  # Drop unnecessary columns

# Save the cleaned dataset to a new CSV file
nba_df.to_csv('data/relevantstats.csv', index=False)  # Ensure the CSV is saved with the correct format

# Load the cleaned dataset
nba_df = pd.read_csv('data/relevantstats.csv')

# Load with specific column names (overwriting previous DataFrame)
nba_df = pd.read_csv('data/relevantstats.csv',
                     header=None,  # No header in the file
                     names=['Player', 'Height', 'Rebounds'])  # Assign specific column names

# Functions for Program
def displayOriginalData():
    print(original_df) # Prints the original dataset

def displayNewData():
    print(nba_df) # Prints the cleaned dataset

def visualisePlayerRebounds(): # Visualizes the correlation between player height and average rebounds.
    plt.scatter(nba_df['Height'], nba_df['Rebounds'], color='blue', alpha=0.5)
    plt.title('Correlation between Player Height and Rebounds')
    plt.xlabel('Height (cm)')
    plt.ylabel('Average Rebounds per Game')
    plt.show()

def plotHeightVsReboundsTrend(): # Plots a scatter plot of height vs rebounds with a trend line.
    plt.plot(nba_df['Height'], nba_df['Rebounds'], 'o', label='Data Points')
    plt.title('Height vs Rebounds Trend Line')
    plt.xlabel('Height (cm)')
    plt.ylabel('Average Rebounds per Game')
    plt.grid(True)
    plt.show()

def menuOptions():
    global exit_program

    print("""Welcome to the NBA Player Rebounds Database!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the new dataset
    3 - Visualise correlation between Height and Rebounds
    4 - Plot height vs rebounds trend line
    5 - Quit Program
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
            plotHeightVsReboundsTrend() 
        elif selection == 5:
            exit_program = True # Set flag to True to exit the program
        else:
            print('Please select a number between 1 and 5.')

    except ValueError:
        print('Please enter a valid number.')

# Main Program
while not exit_program:
    menuOptions() # Display the main menu and ask the user again for any actions.