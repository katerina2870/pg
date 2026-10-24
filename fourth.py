def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]
    
    r, c = cilova_pozice
    if not (1 <= r <= 8 and 1 <= c <= 8):
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False
    
    dr = abs(r - aktualni_pozice[0])
    dc = abs(c - aktualni_pozice[1])
    
    if typ == "král":
        if dr <= 1 and dc <= 1 and (dr > 0 or dc > 0):
            return True
        
    elif typ == "jezdec":
        if (dr == 2 and dc == 1) or (dr == 1 and dc == 2):
            return True
        
    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True (o 1 pole dolů)
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False (příliš daleko - o 2 pole)
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False (mimo šachovnici)

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True (tvar L: 2 nahoru, 1 doprava)
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # True (tvar L)
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False (mimo šachovnici)
