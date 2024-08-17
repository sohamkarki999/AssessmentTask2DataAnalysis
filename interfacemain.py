#Modules
import pandas as pd
import matplotlib.pyplot as plt

#Global Variables
exit_program = False

# Dataframe Setup
nba_df = pd.read_csv('data/big_mac_aud.csv',
                     header=None,
                     names=['Player', 'Team', 'Rebounds', 'Points'])

# Functions for Program
def displayOriginalData():
    print(nba_df)

def visualizePlayerRebounds():
    nba_df.plot(
                kind='bar',
                x='Player',
                y='Rebounds',
                color='black',
                alpha=0.3,
                title='Player Rebounds')
    plt.show()
