# extract name and phone numbers from contact_list.vcf

contact_list_file = open("contact_list.vcf", "r")
contact_list_vcf = contact_list_file.readlines()


contact_list = []
for line in contact_list_vcf:
    if line.startswith('BEGIN'):
        new_contact = []
        same_contact = True
    if same_contact:
        new_contact.append(line)
    if line.startswith('END'):
        contact_list.append(new_contact)
        same_contact = False

raw_format = []
for contact in contact_list:
    contact_dict = {
        'name': "",
        'phone': []
    }
    for line in contact:
        if line.startswith('FN'):
            tag, value = line.strip().split(":")
            contact_dict['name'] = value
        if line.startswith("TEL"):
            tag, *value = line.strip().split(";")
            if len(value) > 1: value = [value[1]] # patch work to handle off cases
            contact_dict['phone'] = value
    raw_format.append(contact_dict)

# i guess the whole script
# i'll spend time later reformatting the whole thing vcf file

contacts ={}
for contact in raw_format:
    try:
        phones = [p.split(":")[1] for p in contact['phone']]
        contacts['contact'] = phones
    except:
        print(contact)
        raise

# import pprint
# pprint.pprint(raw_format[:15])