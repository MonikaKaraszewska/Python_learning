# class Portishead:
#     def __init__(self):
#         print("Portishead")
#
# class KanyeWest(Portishead):
#     def __init__(self):
#         print("Keanye West")
#
#         Portishead.__init__(self)
#         # super().__init__()
#
# class ASAPRocky(Portishead):
#     def __init__(self):
#         print("ASAP Rocky")
#         Portishead.__init__(self)
#
# class ASAPSebbie(ASAPRocky, KanyeWest):
#     def __init__(self):
#         print("ASAP Sebbie")
#         ASAPRocky.__init__(self)
#         KanyeWest.__init__(self)
#
#
# asap_sebbie = ASAPSebbie()

print(".............................................a to z super().......")
#
class Portishead:
    def __init__(self):
        print("Portishead")

class KanyeWest(Portishead):
    def __init__(self):
        print("Keanye West")

        super().__init__()

class ASAPRocky(Portishead):
    def __init__(self):
        print("ASAP Rocky")
        super().__init__()

class ASAPSebbie(ASAPRocky, KanyeWest):
    def __init__(self):
        print("ASAP Sebbie")
        super().__init__()


asap_sebbie = ASAPSebbie()
