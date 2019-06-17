import json

class Judgement:
	def __init__(self, src, id, text, updoots, updoot_pct):
		self.src = src
		self.id = id
		self.text = text
		self.updoots = updoots
		self.updoot_pct = updoot_pct
	
	def toJson(self):
		j = {
		"src":self.src,
		"id": self.id,
		"text": self.text,
		"updoots": self.updoots,
		"updoot_pct": self.updoot_pct
		}
		return json.dumps(j);