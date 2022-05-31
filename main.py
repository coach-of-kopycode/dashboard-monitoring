"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION & PACKAGE
"""

import gempaterkini

if __name__ == '__main__':
    print('Aplikasi Utama')
    print('\nGempa terkini berdasarkan BMKG')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)
