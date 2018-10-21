# extract name and phone numbers from a vcf


import re

# todo: reformat phone number uniformally
def phone(raw):
	"""Re-format phone numbers to +1 012 345 6789."""
	lcal = r"0(\d+)-(\d+)-(\d+)"
	rplc = r"+234\1\2\3"
	
	if re.match(lcal, raw):
		return re.sub(lcal, rplc, raw)
	else:
		return raw

def group_contacts(raw_lines):
    """Return a list of lists of each contact and its
    contact fields.
    """

    contacts = []
    for line in raw_lines:
        if line.startswith('BEGIN'):
            new_contact = []
            same_contact = True
        if same_contact:
            if line.split(":")[0] not in ['BEGIN', 'VERSION', 'END']:
                new_contact.append(line.strip())
        if line.startswith('END'):
            contacts.append(new_contact)
            same_contact = False
    
    return contacts

def get_contacts(path_to_vcf):
    """Given a path to a vcf file, return a list
    of contacts in dict type.

    e.g
    [
        {
            'name': "john doe",
            'phone': ['phone-number', 'phone-number']
        },
        {
            'name': "jane doe",
            'phone': ['phone-number']
        }
    ]
    """
    
    vcf_file = open(path_to_vcf)
    batches = group_contacts(vcf_file.readlines())

    contacts = []
    for batch in batches:
        # extract: name & phone numbers
        contact = {
            'name': "",
            'phone': [],
        }

        for line in batch:
            if line.startswith('FN'):
                contact['name'] = line.split(":")[-1]
            if line.startswith('TEL'):
                contact['phone'].append(phone(line.split(":")[-1]))
        
        contacts.append(contact)
    
    return contacts
