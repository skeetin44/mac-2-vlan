import glob
import re
import csv


for file in glob.glob('*.txt'):
  with open(file,'r') as infile:
      for line in infile:
        if "gi" in line:
            first = line[3:8]
            second = line [9:32]
            interface = (line.split("gi",1))[1]
            int_split = (interface.split())
            print ("int g1/0/"+(int_split[0]))
            print ("desc mac address "+(second)+" was on vlan "+(first))
            print ("swtichport access vlan"+(first))
            print ("spanning-tree portfast")
            print ("")