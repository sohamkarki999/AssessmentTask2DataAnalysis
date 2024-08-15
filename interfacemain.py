import pandas as pd
import matplotlib.pyplot as plt

quit = False

original_df = pd.read_csv('dataset/all_seasons.csv')


nba_df = pd.read_csv('dataset/all_seasons.csv',
                            header=None,
                            names=['Player Name', 'Player Height', 'Rebounds'])

#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(nba_df)

def showCharts():
    nba_df.plot(
                    kind='bar',
                    x='Player',
                    y='Rebounds',
                    color='blue',
                    alpha=0.3,
                    title='Cost of a Big Mac in AUD')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Big Mac Data Extraordinaire!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the cost of a big mac in AUD
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()