"""
Aplikasi deteksi gempa terkini
"""

import gempaterkini

if __name__ == '__main__':
    print('Main app')
    print('\nLatest Earthquake data from BMKG | Indonesia Meteorological, Climatological, and Geophysical Agency')
    result = gempaterkini.extract_data()
    gempaterkini.show_data(result)
