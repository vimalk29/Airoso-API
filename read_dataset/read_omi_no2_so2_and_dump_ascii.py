#!/usr/bin/python
import h5py
import numpy as np
import sys
import time
import calendar
import create_json as CJ

# read_omi_no2_so2_and_dump_ascii.py

# This finds the user's current path so that all hdf4 files can be found
try:
    fileList = open('fileList.txt', 'r')
except:
    print('Did not find a text file containing file names (perhaps name does not match)')
    sys.exit()

# loops through all files listed in the text file
for FILE_NAME in fileList:

    # 'r' means that hdf5 file is open in read-only mode
    file = h5py.File(FILE_NAME, 'r')
    # checks if the file contains NO2 or SO2 data, and reacts accordingly

    geolocation = file['GEOLOCATION_DATA']
    sciencedata = file['SCIENCE_DATA']

    # get lat and lon info as vectors
    lat = geolocation['Latitude'][:].ravel()
    lon = geolocation['Longitude'][:].ravel()
    sci = sciencedata['UVAerosolIndex354and388'][:].ravel()

    # get scan time and turn it into a vector
    scan_time = geolocation['TimeTAI93'][:].ravel()

    # creates arrays the same size as scan time to receive time attributes
    year = np.zeros(scan_time.shape[0])
    month = np.zeros(scan_time.shape[0])
    day = np.zeros(scan_time.shape[0])
    hour = np.zeros(scan_time.shape[0])
    min = np.zeros(scan_time.shape[0])
    sec = np.zeros(scan_time.shape[0])

    # gets date info for each pixel to be saved later
    for i in range(scan_time.shape[0]):
        temp = time.gmtime(scan_time[i-1]+calendar.timegm(time.strptime(
            'Dec 31, 1992 @ 23:59:59 UTC', '%b %d, %Y @ %H:%M:%S UTC')))
        year[i-1] = temp[0]
        month[i-1] = temp[1]
        day[i-1] = temp[2]
        hour[i-1] = temp[3]
        min[i-1] = temp[4]
        sec[i-1] = temp[5]

    # Begin saving to an output array
    output = np.array(np.zeros((year.shape[0]*60, 9
                                )))
    output[0:, 0] = year[:].repeat(60)
    output[0:, 1] = month[:].repeat(60)
    output[0:, 2] = day[:].repeat(60)
    output[0:, 3] = hour[:].repeat(60)
    output[0:, 4] = min[:].repeat(60)
    output[0:, 5] = sec[:].repeat(60)
    output[0:, 6] = lat[:]
    output[0:, 7] = lon[:]
    output[0:, 8] = sci[:]

    # list for the column titles (because you can't combine string values and float values into a single array)
    tempOutput = []
    tempOutput.append('year')
    tempOutput.append('month')
    tempOutput.append('day')
    tempOutput.append('hour')
    tempOutput.append('minute')
    tempOutput.append('second')
    tempOutput.append('Latitude')
    tempOutput.append('Longitude')
    tempOutput.append('UAindix')

    # changes list to an array so it can be stacked
    tempOutput = np.asarray(tempOutput)
    # This stacks the titles on top of the data
    output = np.row_stack((tempOutput, output))
    # save the new array to a text file, which is the name of the HDF4 file .txt instead of .hdf
    np.savetxt('{0}.txt'.format(
        FILE_NAME[:-4]), output, fmt='%s', delimiter=',')
    CJ.writeToJson('{0}.txt'.format(FILE_NAME[:-4]))

    file.close()
print('\nAll files have been saved successfully.')
