import sys
import json

def toInt(val: int):
    return "{:02d}".format(int(float(val)))

def getDate(data: list):
    year = toInt(data[0])
    month = toInt(data[1])
    day = toInt(data[2])
    hour = toInt(data[3])
    minu = toInt(data[4])
    sec = toInt(data[5])
    return year + "-" + month + "-" + day + "T" + hour + ":" + minu + ":" + sec+"+01:00"


def writeToJson(inputFile):
    f = open(inputFile, "r")

    jsonData = []
    first = True
    for line in f:
        if first:
            first = False
            continue
        values = line.split(',')
        date = getDate(values)
        jsonData.append(
            {
                "date": date,
                "latitude": float(values[6]),
                "longitude": float(values[7]),
                "uAindex": float(values[8])
            }
        )
        
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(jsonData, f, ensure_ascii=False, indent=4)
