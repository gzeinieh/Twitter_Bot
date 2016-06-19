from unidecode import decode


with open( "/Users/George/PycharmProjects/Twitter_Bot/twitter/data/update_status_2016-06-14 18:20:15.247625.txt"
        ,mode ='r', encoding='utf-8') as f:
    print(f.read().decode('unicode_escape'))
