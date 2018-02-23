#!/usr/bin/python2.7

import json

with open('file-20171020T1500', 'r') as infile:
	resources = {}
	for sample in infile:
		sample = json.loads(sample)

		if sample["unique_sources"] > 1:

			try:
				for resource in sample["additional_info"]["pe-resource-list"]:
					if resource in resources:
						resources[resource] += 1
					else:
						resources[resource] = 1
			except:
				pass

	d_view = [ (v,k) for k,v in resources.iteritems() ]
	d_view.sort(reverse=True)

	for resource in d_view:
		if resource[0] == 7:
			print resource[1]
