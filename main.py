#!/usr/bin/python3

import csv
import numpy
import json
from classes.communications import communications
# from classes.logging import myLog

# ::::::::::::::::::: TODO :::::::::::::::::::::::::::::::::::::::::::::::::::
# Exeption handling
# Logging improvement
# Graphical Interfaz (optional)
# Create dependences file

# ::::::::::::::::::: Globals ::::::::::::::::::::::::::::::::::::::::::::::::
#configPath = 'configFiles/config.json'
#csvPath_in = 'configFiles/config.json'

# csvPath_in = "tests/stag_cold.csv"
csvPath_in = "tests/dLogger_warm.csv"
csvPath_out = "tests/dLogger_warm_out.csv"


def roundTemp(temp):
    if (temp*10)%2==0:
        newTemp = temp
    else:
        newTemp = temp+0.1
    return round(newTemp,1)

#vector for storing xAxis, temperature values 
xAxis = numpy.arange(-10.2, 30.4, 0.2)
#for x in xAxis:
#    print(round(x,1))

#array of dicts for storing ocurrencies in xAxis
samplesArray = []
for x in xAxis:
    #ocurrencies.append( round(x,1))
    sample = {} #dictionary for each row
    sample["tempValue"] = round(x,1)
    sample["ocurrency"] = 0
    samplesArray.append(sample)


#ocurrencies["1.2"] = 3

#print(json.dumps(samplesArray))

# :::::::::::::::::::::::::::HELPERS::::::::::::::::::::::::::::::::::::::::::::
def convertCSV(csvfile_in, csvfile_out):
    fieldnames = ("Time","Temperature [ ºC ]")
    reader = csv.DictReader(csvfile_in, fieldnames, delimiter=',', quotechar='|')
    for idx, row in enumerate(reader):
        if (idx > 1):

            #extracting value of temperature from csv
            temp = float(row["Temperature [ ºC ]"])
            roundedTemp = roundTemp(temp)

            #Counting the ocurrencies of each value of temperature
            for x in samplesArray:
                if (x["tempValue"] == roundedTemp):
                    x["ocurrency"] = x["ocurrency"]+1
                    #ocurrencies[]

    #print(json.dumps(samplesArray)) # samplesArray is filled with tempValues and ocurrencies

    #putting info into the new csv
    csvfile_out.write("Graph type: Integral Processed Temperature , Total time: 250 hours ,  timeStamp: 2017-12-05 20:26:14 \n")
    csvfile_out.write("Temperature [ ºC ] , Time [ hours ]\n")
    for x in samplesArray:
        strRow = ""
        strRow = strRow + str(x["tempValue"]) + " , " + str(x["ocurrency"]) + "\n"
        csvfile_out.write(strRow)

# :::::::::::::::::::::MAIN:::::::::::::::::::::::::::::::::::::::::::::::::::::::

# with open(configPath) as f:
#     configData = json.load(f)
#     ĺogsPath = configData['logsPath']
#     csvPath = configData['csvPath']
#     jsonPath = configData['jsonPath']

# log = myLog.myLogClass({'logsFile': logsPath, 'type': '[H0]', 'verb': 0})
# configData['log'] = log
# log.logInfo('Starting Testo_Converter')




with open(csvPath_in, 'r') as csvfile_in:
    with open(csvPath_out, 'w') as csvfile_out:
        convertCSV(csvfile_in, csvfile_out)





# with open(csvPath_in, newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['Time'], row['Temperature'])

#comms = communications.Communications(configData)
#comms.sendTestoJSON(jsonPath)
