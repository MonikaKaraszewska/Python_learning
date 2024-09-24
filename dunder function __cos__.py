class ASAPMob:
    def __init__(self):
        self._members =  [
        "Jan Kowalski",
        "Anna Nowak",
        "Piotr Wiśniewski",
        "Katarzyna Dąbrowska",
        "Andrzej Lewandowski",
        "Magdalena Wójcik",
        "Michał Kamiński",
        "Joanna Kowalczyk",
        "Tomasz Zieliński",
        "Małgorzata Szymańska",
        "Paweł Woźniak",
        "Agnieszka Kozłowska",
        "Marcin Jankowski",
        "Dorota Włodarczyk",
        "Krzysztof Wojciechowski",
        "Ewa Adamczyk",
        "Bartosz Nowicki",
        "Aleksandra Jóźwiak",
        "Łukasz Grabowski",
        "Monika Pawłowska"
    ]
    def __len__(self):
        return len(self._members)

    def __getitem__(self, key):

        if isinstance(key, int):
            return self._members.pop(key)
        raise TypeError('not a number')

    # def __contains__(self, member):
    #     return member in self._members



asap_mob = ASAPMob()
print(len(asap_mob))
print("goes solo: ", asap_mob[4])
print(len(asap_mob))
print("Monika" in asap_mob)
