#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

from xml.etree import ElementTree

def xmlToCSV(xmlPath, csvPath):
	xml = open(xmlPath, 'r')
	tree = ElementTree.parse(xml)
	root = tree.getroot()
	with open(csvPath, 'w', newline='') as csvfile:
		csvwriter = csv.DictWriter(csvfile, fieldnames=['First Name', 'Last Name', 'Email', 'UID'], delimiter=',', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writeheader()
		for victims in root.findall('victims'):
			for victim in victims:
				csvwriter.writerow({"First Name": victim.find('firstname').text, "Last Name": victim.find('lastname').text, "Email": victim.find('email-address').text, "UID": victim.find('uid').text})

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument(metavar="xml_file", dest="xml", help="XML file from PhishingFrenzy that is usually called download_stats.xml.", type=str)
	parser.add_argument(metavar="csv_file", dest="csv", help="Write to CSV file.", type=str)
	args = parser.parse_args()

	xmlToCSV(args.xml, args.csv)