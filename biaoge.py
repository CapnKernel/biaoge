#! /usr/bin/env python

import csv

print open("biaoge-ps-header.txt").read()

for field in csv.DictReader(open("dhl.csv")):
  print "newpath (%s) %s %s %s text closepath stroke" % (field['Value'], int(field['X']), field['Y'], int(field['Font']))

print open("biaoge-ps-trailer.txt").read()

