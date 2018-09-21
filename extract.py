# extract name and phone numbers from grouped_contacts.vcf

# todo: reformat phone number uniformally

import os

class FileError(Exception):
    pass

def group_contacts(raw_text):
    """Given raw text froma vcf file, return a list of lists.
    Inner list of items belonging to a single contact.
    """

    grouped_contacts = []
    for line in raw_text:
        if line.startswith('BEGIN'):
            new_contact = []
            same_contact = True
        if same_contact:
            if line.split(":")[0] not in ['BEGIN', 'VERSION', 'END']:
                new_contact.append(line.strip())
        if line.startswith('END'):
            grouped_contacts.append(new_contact)
            same_contact = False
    
    return grouped_contacts

def get_contacts(vcf_file):
    """Given a path to a vcf file, return a list
    of dictionaries of attributes assignable to a contact.

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

    pass
    if not os.path.exists(vcf_file):
        raise FileError(f"VCF File does not exist at {vcf_file}.")
    
    raw_text = open(vcf_file, "r").readlines()
    grouped = group_contacts(raw_text)

    contacts = []
    for group in grouped:
        # keeping it simple now, i'm only extracting
        # names and phone numbers
        contact = {
            'name': "",
            'phone': []
        }

        for line in group:
            if line.startswith('FN'):
                contact['name'] = line.split(":")[-1]
            if line.startswith('TEL'):
                contact['phone'].append(line.split(":")[-1])
        
        contacts.append(contact)
    
    return contacts

c = get_contacts("contact_list.vcf")
