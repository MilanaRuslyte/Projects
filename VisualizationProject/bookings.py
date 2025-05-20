import pandas as pd
import matplotlib.pyplot as plt

validFile = False
#validating if file does not exist
while not validFile:
    fileName = input("Please enter file name to process, make sure it ends with .xlsx: ")

    if not fileName.endswith('.xlsx'):
        print("Invalid file type. Please enter a file that ends with .xlsx\n")
        continue # back to the start of the loop

  
    if fileName not in ["_hotelBookings.xlsx","countries.xlsx"]:
        print(f"File called '{fileName}' does not exist. Please try entering again and make sure it ends with .xlsx: \n")
        continue

    df = pd.read_excel(fileName) #read in table dataframe
    print(df) #print all
    #print(df.head(8)) prints a few rows, which i use to display more quickly and neatly
    #print(df.columns) shows up columns 

    if len(df) == 1: # If the file has only one row of data 
        data = df.iloc[0] #gets one row
        data.plot(kind='bar') #creats a barchart
        plt.title('Hotel Booking Data')
        plt.ylabel('Count')
        plt.xticks(rotation=45) #rotating label so it doesnt overlap
        plt.tight_layout() #spacing adjusted
        plt.show() 
#for if countries file is entered in
    if "countries" in fileName.lower(): 
        filtered_df = df[df[df.columns[1]] > 1500]#gets rows from the table,️gets a column from the table and gets column's name
        plt.figure(figsize=(8, 6)) #plotting with width of 8 inches and height of 6 inches
        plt.pie(filtered_df[filtered_df.columns[1]], #get second column of nums to draw pie chart through filter
                labels=filtered_df[filtered_df.columns[0]], #label slice from column 1 in filter
                autopct='%1.1f%%') #percentage of each slice with one decimal place
        plt.title("Countries that have more than 1500")
        plt.tight_layout() #spacing
        plt.show()

    validFile = True #break loop
