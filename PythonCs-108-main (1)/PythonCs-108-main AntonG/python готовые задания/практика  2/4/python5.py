def reverse_lookup(Phonebook, name):
    for phone, person_name in Phonebook.items():
        if person_name == name:
            return phone
    return "Not found"
phonebook = {
    '123-456-7890': 'Anton',
    '999-666-1010': 'Dasha',
    '555-666-7878': 'Artur'
}
phone_number = reverse_lookup(phonebook, 'Islam')
print("Номер телефона для Islam:", phone_number)
