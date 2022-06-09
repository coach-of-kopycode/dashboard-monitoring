"""
Aplikasi deteksi gempa terkini
"""

from gempaterkini import GempaTerkini

if __name__ == '__main__':
    print('Dashboard monitoring')
    gempa = GempaTerkini('https://www.bmkg.go.id/')
    gempa.show_description()
    gempa.run()

