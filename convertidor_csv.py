
#importing pandas as pd
import pandas as pd
  
# Read and store content
# of an excel file 
read_file = pd.read_excel ("datos_estapa2.xlsx")
  
# Write the dataframe object
# into csv file
read_file.to_csv ("datos_etapa2.csv", 
                  index = None,
                  header=True)