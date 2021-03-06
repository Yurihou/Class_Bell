# coding=utf-8

import time
import os

timetable = [
    '8:00', '8:45', '8:50', '9:35', '9:50', '10:35', '10:40', '11:25', '11:30',
    '12:15', '13:30', '14:15', '14:20', '15:05', '15:20', '16:05', '16:10',
    '16:55', '17:05', '17:50', '17:55', '18:40', '19:20', '20:05', '20:10',
    '20:55', '21:00', '21:45'
]
bell_cmd = 'mpg123 /home/pi/Bell/skl.mp3'


def rest(t):
    h, m = time.localtime()[3:5]
    x, y = t.split(':')
    return 60 * ((int(x) - h) % 24) + (int(y) - m)


def look():
    while (1):
        for timepoint in timetable:
            if rest(timepoint) == 0:
                os.system(bell_cmd)
                time.sleep(60)
        else:
            time.sleep(2)


def main():
    print('Bell is running.:)')
    look()


if __name__ == '__main__':
    main()
