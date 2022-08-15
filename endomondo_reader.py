import json
import os
import csv


path = 'C:\\Users\\bonma\\Desktop\\upload_endo\\Workouts\\JSON\\'

def get_sport(file):

    try:  
        o = json.load(open(path + file))
    except json.decoder.JSONDecodeError:
        print("Can't process", file)

    try:
        sport_dic = {}
        for entry in o:
            sport_dic = sport_dic | entry

        output_list = [
            file,
            sport_dic['start_time'],
            sport_dic['sport'],
            round(sport_dic['distance_km'], 2),
            str(round(sport_dic['duration_s'] / 60)) + 'min'
            ]

        return output_list

    except KeyError:
        return o[0]['sport']

    except UnboundLocalError:
        pass


def get_file_list(path):
    dir_list = os.listdir(path)
    return dir_list


def main():

    files = get_file_list(path)

    with open('sports_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['File', 'Start time', 'Sport', 'Distance', 'Duration'])
        for file in files:
            sport = get_sport(file)
            if sport != None:
                writer.writerow(sport)


if __name__ == '__main__':
    main()