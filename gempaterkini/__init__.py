def ekstraksi_data():
    """
    Tanggal: 30 Mei 2022
    Waktu: 13:42:40 WIB
    Magnitudo: 4.1
    Kedalaman:23 km
    Lokasi: 1.75 LS - 100.29 BT
    Pusat Gempa: Pusat gempa berada di laut 55 km BaratDaya Painan-Pesisir Selatan
    Dirasakan: Dirasakan (Skala MMI): I - II Painan, I - II Padang
    :return:
    """

    hasil = dict()
    hasil['tanggal'] = '30 Mei 2022'
    hasil['waktu'] = '13:42:40 WIB'
    hasil['magnitudo'] = 4.1
    hasil['kedalaman'] = '2.3 km'
    hasil['lokasi'] = {'ls': 1.75, 'bt': 100.29}
    hasil['pusat'] = 'Pusat gempa berada di laut 55 km BaratDaya Painan-Pesisir Selatan'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): I - II Painan, I - II Padang'

    return hasil


def tampilkan_data(result):
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Lokasi : LS= {result['lokasi']['ls']}, BT= {result['lokasi']['bt']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Pusat Gempa : {result['pusat']}")
    print(f"Dirasakan : {result['dirasakan']}")
