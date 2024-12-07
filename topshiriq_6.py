sozlar = ["olma", "anjir", "behi", "gilos", "anor", "uzum", "nok"]

def saralash_yoli(soz):
    return soz[0], len(soz)

sozlar.sort(key=saralash_yoli)

print("Saralangan ro'yxat:", sozlar)