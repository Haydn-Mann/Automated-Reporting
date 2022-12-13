#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
style.use('seaborn-darkgrid')
get_ipython().run_line_magic('matplotlib', 'inline')

# Import the data
df = pd.read_csv('Deep Dive Table (7).csv')

#standardise all data into lower case to make it easier to clean
df['Placement Name String'] = df['Placement Name String'].apply(lambda x: x.lower())
df['Creative Name String'] = df['Creative Name String'].apply(lambda x: x.lower())

#Replace 'other' & NAN values in platform column with correct platform using the placement namestring column

df['Platform'] = np.where(df['Placement Name String'].str.contains('apex deal'), 'Apex Deal Partners', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('dv360'), 'DV360 OMP', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('youtube'), 'YouTube', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('facebook'), 'Facebook', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('snap'), 'SnapChat', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('snapchat'), 'SnapChat', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('instagram'), 'Facebook', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('trueview'), 'YouTube', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('twitter'), 'Twitter', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('reddit'), 'Reddit', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('amazon'), 'Amazon', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('twitch'), 'Twitch', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('spotify'), 'Spotify', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('acast'), 'Acast', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('imdb'), 'IMDB', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('samba'), 'Samba', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('venatus'), 'Venatus', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('dax'), 'Dax', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('audio xi'), 'Audio XI', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('bild'), 'Bild', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('fandom'), 'Fandom', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('tv2'), 'TV2', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('factor eleven'), 'Factor Eleven', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('ekstra bladet'), 'Ekstra Bladet', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('concept'), 'Concept', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('sky advance'), 'Sky', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('sky media'), 'Sky', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('all 4'), 'All 4', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('toogame'), 'Too Game', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('wetransfer'), 'WeTransfer', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('ruutu'), 'Ruutu', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('instant play'), 'Instant Play', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('ppn'), 'PPN', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('reklamup'), 'Reklamup', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('smartclip'), 'Smartclip', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('reklamup'), 'Reklamup', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('freewheel'), 'Freewheel', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains(' sky '), 'Sky', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('ogury'), 'Ogury', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('reklamup'), 'Reklamup', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('prosiebensat1puls4.com'), 'Prosiebensat1puls4', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('goldbach'), 'Goldbach', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('sdo'), 'SDO', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('webedia'), 'Webedia', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('talksmedia'), 'Talksmedia', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('webedia'), 'Webedia', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('planetv'), 'Planet V', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('webedia'), 'Webedia', df['Platform'])
df['Platform'] = np.where(df['Placement Name String'].str.contains('weborama.com'), 'Weborama', df['Platform'])


#cleaning the data in the creative free field
df['Platform'] = np.where(df['Creative Name String'].str.contains('apex deal'), 'Apex Deal Partners', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('dv360'), 'DV360 OMP', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('youtube'), 'YouTube', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('facebook'), 'Facebook', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('snap'), 'SnapChat', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('snapchat'), 'SnapChat', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('instagram'), 'Facebook', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('trueview'), 'YouTube', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('twitter'), 'Twitter', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('reddit'), 'Reddit', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('amazon'), 'Amazon', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('twitch'), 'Twitch', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('spotify'), 'Spotify', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('Acast'), 'Acast', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('imdb'), 'IMDB', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('samba'), 'Samba', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('venatus'), 'Venatus', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('dax'), 'Dax', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('audio xi'), 'Audio XI', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('bild'), 'Bild', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('fandom'), 'Fandom', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('tv2'), 'TV2', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('factor eleven'), 'Factor Eleven', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('ekstra bladet'), 'Ekstra Bladet', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('concept'), 'Concept', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('sky advance'), 'Sky', df['Platform'])
df['Platform'] = np.where(df['Creative Name String'].str.contains('sky media'), 'Sky', df['Platform'])

#clean the platform column
df['Platform'] = np.where(df['Platform'].str.contains('TrueView'), 'YouTube', df['Platform'])

#create new column for cleaned Audiences
df['Audience'] = np.nan

#cleaning the data in the Audience description field
df['Audience'] = np.where(df['Audience Description'].eq('A18-54'), 'A18+', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('A18-49'), 'A18+', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('A25-49'), 'Established Adults', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('A18-34'), 'Young Adults', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('Star Wars'), 'Star Wars Fans', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('Fans'), 'Star Wars Fans', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('Sci-Fi'), 'Genre Fans', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('Talent'), 'Talent Fans', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('Movie Fans'), 'General Streamers', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('Adult Streamers'), 'General Streamers', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('1 Child'), 'Parents', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('Fantasy Movie Fans'), 'Star Wars Fans', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('Video Game'), 'Gamers', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('TV Shows'), 'General Streamers', df['Audience Description'])
df['Audience'] = np.where(df['Audience Description'].eq('Entertainment'), 'General Streamers', df['Audience Description'])

df['Audience'] = np.where(df['Audience Description'].eq('A18-54'), 'A18+', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('A18-49'), 'A18+', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('A25-49'), 'Established Adults', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('A18-34'), 'Young Adults', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('A13-34'), 'Young Adults', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Star Wars'), 'Star Wars Fans', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Fans'), 'Star Wars Fans', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Sci-Fi'), 'Genre Fans', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Talent'), 'Talent Fans', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Movie Fans'), 'General Streamers', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Adult Streamers'), 'General Streamers', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('1 Child'), 'Parents', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Fantasy Movie Fans'), 'Star Wars Fans', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Video Game'), 'Gamers', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('TV Shows'), 'General Streamers', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Entertainment'), 'General Streamers', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Brand'), 'Disney+ Brand Targeting', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Disney+'), 'Disney+ Brand Targeting', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('DMP Audience'), 'DMP Audiences', df['Audience'])
df['Audience'] = np.where(df['Audience Description'].eq('Site Visitors'), 'Retargeting', df['Audience'])

df['Audience'] = np.where(df['Placement Name String'].str.contains('a18-55'), 'A18+', df['Audience'])
df['Audience'] = np.where(df['Placement Name String'].str.contains('a18-54'), 'A18+', df['Audience'])
df['Audience'] = np.where(df['Placement Name String'].str.contains('a18-49'), 'A18+', df['Audience'])
df['Audience'] = np.where(df['Placement Name String'].str.contains('a25-49'), 'Established Adults', df['Audience'])
df['Audience'] = np.where(df['Placement Name String'].str.contains('a18-34'), 'Young Adults', df['Audience'])
df['Audience'] = np.where(df['Placement Name String'].str.contains('a13-34'), 'Young Adults', df['Audience'])

#Creating empty columns for Ad type and video length
df['Ad_Type'] = np.nan
df['Video Length'] = np.nan

#Cleaning values and adding to empty columns
df['Ad_Type'] = np.where(df['Placement Name String'].str.contains('video'), 'Video Ad', df['Ad_Type'])
df['Ad_Type'] = np.where(df['Creative Name String'].str.contains('video'), 'Video Ad', df['Ad_Type'])
df['Ad_Type'] = np.where(df['Video Views'] > 1, 'Video Ad', df['Ad_Type'])
df['Ad_Type'] = np.where(df['Ad_Type'].eq('nan'), 'Display Ad', df['Ad_Type'])

df['Video Length'] = np.where(df['Creative Name String'].str.contains('6s'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains('06s'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains('10s'), 10, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains('15s'), 15, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains('20s'), 20, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains('25s'), 25, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains('30s'), 30, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains('60s'), 60, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains('90s'), 90, df['Video Length'])

df['Video Length'] = np.where(df['Placement Name String'].str.contains('6s'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains('06s'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains('10s'), 10, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains('15s'), 15, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains('20s'), 20, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains('25s'), 25, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains('30s'), 30, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains('60s'), 60, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains('90s'), 90, df['Video Length'])

df['Video Length'] = np.where(df['Placement Name String'].str.contains(':6'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains(':06'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains(':10'), 10, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains(':15'), 15, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains(':20'), 20, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains(':25'), 25, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains(':30'), 30, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains(':60'), 60, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains(':90'), 90, df['Video Length'])
df['Video Length'] = np.where(df['Placement Name String'].str.contains(':180'), 180, df['Video Length'])

df['Video Length'] = np.where(df['Creative Name String'].str.contains(':06'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(':6'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(':10'), 10, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(':13'), 10, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(':15'), 15, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(':20'), 20, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(':25'), 25, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(':30'), 30, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(':60'), 60, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(':90'), 90, df['Video Length'])

df['Video Length'] = np.where(df['Creative Name String'].str.contains(' 6'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(' 06'), 6, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(' 10'), 10, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(' 15'), 15, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(' 20'), 20, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(' 25'), 25, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(' 30'), 30, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(' 60'), 60, df['Video Length'])
df['Video Length'] = np.where(df['Creative Name String'].str.contains(' 90'), 90, df['Video Length'])

#Moving the day column to position one and renaming it
first_column = df.pop('Day')
df.insert(0, 'Date', first_column)

#Creating empty columns
df.insert(1, 'Campaign Stage', '')
df.insert(2, 'Episode Number', '')

#Calculating required metrics and adding them to dataframe
df['VTR'] = df['Video Views']/df['Impressions']
df['Video Completion Rate (25%)'] = df['25% Video Views']/df['Impressions']
df['Video Completion Rate (50%)'] = df['50% Video Views']/df['Impressions']
df['Video Completion Rate (75%)'] = df['75% Video Views']/df['Impressions']
df['Video Completion Rate (100%)'] = df['100% Video Views']/df['Impressions']

df['CTR'] = df['Clicks']/df['Impressions']

df['CPCV'] = df['Media Cost']/df['100% Video Views']


#Creating an input field for users to enter the number of episodes

#convert Date to datetime format
df['Date']= pd.to_datetime(df['Date'])

## Set a flag to indicate whether the user-entered value is valid
valid = False

# Loop until the user enters a valid input
while not valid:
    try:
        # Prompt the user to enter a number
        epnum = input("Enter the number of episode release dates the show has (Note: If all episodes release at once enter '1' & if a show had 10 episodes, but two released at launch, you would enter '9'): ")

        # Convert the user-entered value to an integer
        epnum = int(epnum)

        # Set the flag to indicate that the input is valid
        valid = True
    except ValueError:
        # Handle the error if the user-entered value is not a valid integer
        print("Invalid input 😭: please enter a valid number.")

# Print the number if it is a valid integer
print("Thanks!😃 The show has",epnum, "episode release dates 🎊")


#Creating an input field for users to input the episode number and its corresponding release date; with the output forming a dictionary

### from datetime import datetime
from datetime import datetime
# Store the number of input fields to create
num_fields = epnum

# Create an empty dictionary to store the input values
ep_dictionary = {}

# Loop for the specified number of input fields
for i in range(num_fields):
    # Prompt the user to enter a value
    ep_num = input("Enter the Episode Number: ")
    ep_date = input("Enter the date (format: YYYY-MM-DD): ")
    ep_date1 = datetime.strptime(ep_date, '%Y-%m-%d')

   
    # Save the input value in the dictionary using the input description as the key
    ep_dictionary[ep_date1] = str('EP')+ep_num


#Add episoide numbers to dataframe by matching to relevent date
df['Episode Number'] = df['Date'].map(ep_dictionary)
df["Episode Number"] = df["Episode Number"].fillna("")

#Create dataframe from episodic dictionary
episode_dict_df = pd.DataFrame(ep_dictionary.items(), columns=['Release Date', 'Episode Number'])

#Create variable for first release date
first_release_date = episode_dict_df.iloc[0,0]

#Adding campaign stage periods to dataframe by matching episodic dates to those in main table
df['Campaign Stage'] = np.where(df['Date'] < episode_dict_df.iloc[0,0], 'Pre-Launch',df['Campaign Stage'])
df['Campaign Stage'] = np.where(df['Date'] == episode_dict_df.iloc[0,0], 'Launch',df['Campaign Stage'])
df['Campaign Stage'] = np.where(df['Date'] > episode_dict_df.iloc[0,0], 'Sustain',df['Campaign Stage'])
df['Campaign Stage'] = np.where(df['Date'] >= episode_dict_df.iloc[-1,0], 'All Eps',df['Campaign Stage'])

df.to_csv('Cleaned_data.csv')

