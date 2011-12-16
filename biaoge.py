#! /usr/bin/env python

import csv

print open("biaoge-ps-header.txt").read()

for field in csv.DictReader(open("dhl.csv")):
  print "newpath (%s) %s %s %s text closepath stroke" % (field['Value'], field['X'], field['Y'], field['Font'])

print open("biaoge-ps-trailer.txt").read()

