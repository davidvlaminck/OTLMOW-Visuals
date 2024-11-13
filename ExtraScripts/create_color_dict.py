if __name__ == "__main__":
    aangeleverd_dict = {
        'HeeftBetrokkene': 39413,
        'VoedtAangestuurd': 8721863,
        'HeeftNetwerkProtectie': 42495,
        'IsAdmOnderdeelVan': 8421616,
        'Voedt': 255,
        'IsSWOnderdeelVan': 8388736,
        'IsSWGehostOp': 16711680,
        'Sturing': 32768,
        'IsNetwerkECC': 14822282,
        'Bevestiging': 5855577,
        'LigtOp': 3329330,
        'SluitAanOp': 16748574,
        'HeeftBeheer': 9408444,
        'HoortBij': 1463500,
        'HeeftNetwerktoegang': 15631086,
        'IsInspectieVan': 16110950,
        'RelatieObject': 39413,
        'Omhult': 128,
        'HeeftAanvullendeGeometrie': 13828244,
        'HeeftToegangsprocedure': 2763429,
        'HeeftBijlage': 16711680
    }

    for key, value in aangeleverd_dict.items():
        color = str(hex(value)).replace('0x','')
        while len(color) < 6:
            color = '0' + color
        color = color[4:6] + color[2:4] + color[0:2]
        if key == 'Bevestiging':
            color = '000000'
        print(f"'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#{key}' : '{color}',")