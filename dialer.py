
import re
import sys
from itertools import permutations as perm

import parser

keypad = {
1: "",
2: "abc",
3: "def",
4: "ghi",
5: "jkl",
6: "mno",
7: "pqrs",
8: "tuv",
9: "wxyz",
0: "+ "
}

contacts = parser.get_contacts("contacts.vcf")

def wrap(pkg):
	return "[" + pkg + pkg.upper() + "]"

def make_block(query):
	return "".join([wrap(keypad[int(i)]) for i in str(query)])

def find_block(block, contacts):
	found = []
	
	for contact in contacts:
		mo = re.search(re.compile(block), contact['name'])
		if mo:
			contact['pos'] = (mo.start(), mo.end())
			if contact not in found:
				found.append(contact)
	
	return found

def proceed(query):
	int(query) # for now, query should be numbers
	q = str(query)
	
	blk = make_block(q)
	hits = find_block(blk, contacts)
	
	if not hits:
		print("No contacts matched query.")
		return
	
	sort_key = lambda c: c['pos'][0]
	hits = sorted(hits, key=sort_key)
	
	return hits
	
def paint(hits):
	print("")
	for hit in hits:
		n = hit['name']; s, e = hit['pos']
		n = n[:s] + "'" + n[s:e] + "'" + n[e:]
		p = "No phone." if not hit['phone'] else ", ".join(hit['phone'])
		
		print(n, p, "", sep="\n")
 

if __name__ == "__main__":
	args = sys.argv
	q = args[1]
	color = proceed(q)
	paint(color)