import json
import os
import csv
import shutil


path = 'C:\\Users\\bonma\\guru_code\\endomondo_reader\\upload_endo\\Workouts\\JSON\\'

def get_sport(file):

    try:  
        o = json.load(open(path + file))
    # except json.decoder.JSONDecodeError:
    except ValueError:
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
        print(output_list)
        return output_list

    except KeyError:
        return o[0]['sport']

    except UnboundLocalError:
        pass


def get_file_list(path):
    dir_list = os.listdir(path)
    return dir_list


def copy_file(file, out_dir):
    file = file.rstrip('.json') + '.tcx'
    src_path = 'C:\\Users\\bonma\\guru_code\\endomondo_reader\\endo_full_save\\Workouts\\' + file
    dst_path = 'C:\\Users\\bonma\\guru_code\\endomondo_reader\\' + out_dir + file
    shutil.copy(src_path, dst_path)
    print(file, 'copied')


def main():

    files = get_file_list(path)

    with open('sports_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['File', 'Start time', 'Sport', 'Distance', 'Duration'])
        for file in files:
            print(file)
            sport = get_sport(file)
            if sport != None:
                writer.writerow(sport)
                if sport[2] == 'SKATEBOARDING':
                    copy_file(file, 'strava_skate\\')
                elif sport[2] == 'OTHER':
                    copy_file(file, 'strava_other\\')




if __name__ == '__main__':
    main()
