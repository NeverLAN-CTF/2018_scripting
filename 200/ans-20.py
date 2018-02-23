#!/usr/bin/python2.7

import json

with open('file-20171020T1500', 'r') as infile:
	engines = {}
	for sample in infile:
		sample = json.loads(sample)
		for engine in sample["scans"]:
			if engine not in engines:
				engines[engine] = {"hit": 0, "miss": 0}
			if sample["scans"][engine]["detected"]:
				engines[engine]["hit"] += 1
			else:
				engines[engine]["miss"] += 1

	engine_ratios = {}

	for engine in engines:
		engine_ratios[engine] = {"ratio": float(engines[engine]["hit"]) / (float(engines[engine]["miss"]) + float(engines[engine]["hit"]))}

	d_view = [ (v,k) for k,v in engine_ratios.iteritems() ]
	d_view.sort(reverse=True)

	ans = []

	for item in d_view:
		ans.append(item[1])

	ans_string = ""

	for x in range(0,5):
		ans_string = ans_string +  ans[x]
	
		if x < 4:
			ans_string = ans_string + ","

	print ans_string
