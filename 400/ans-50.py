#!/usr/bin/python2.7

import json
import ssdeep

with open('file-20171020T1500', 'r') as infile:
	hashes = {}
	positives = {}

	for sample in infile:
		sample = json.loads(sample)

	 	positives[sample["md5"]] = sample["positives"]
		hashes[sample["md5"]] = sample["ssdeep"]

	d_view = [ (v,k) for k,v in positives.iteritems() ]
	d_view.sort(reverse=True)

	matches = {}

	for sample in hashes:
		try:
			matches[sample] = ssdeep.compare(hashes[d_view[3][1]], hashes[sample])
		except:
			pass

	d_view = [ (v,k) for k,v in matches.iteritems() ]
	d_view.sort(reverse=True)

	ans_text = d_view[1]

	print str(ans_text[0]) + ":" + str(ans_text[1])
