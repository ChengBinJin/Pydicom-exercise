# import os
import pydicom
from pydicom.data import get_testdata_files

filename = get_testdata_files("rtplan.dcm")[0]
ds = pydicom.dcmread(filename)  # plan dataset
print('PatientName: {}'.format(ds.PatientName))

print('setup: {}'.format(ds.dir('setup')) ) # get a list of tags with "setup" somewhere in the name

print('Before:')
print('PatientSetupSequence[0]: {}'.format(ds.PatientSetupSequence[0]))
ds.PatientSetupSequence[0].PatientPosition = 'HFP'

print('After:')
print('PatientSetupSequence[0]: {}'.format(ds.PatientSetupSequence[0]))

ds.save_as('rtplan2.dcom')
