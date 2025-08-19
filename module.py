import datetime
import time
import winsound

class Alarm:

    def get_user_time(self, hour_input, minute_input):
        hour = int(hour_input)
        minute = int(minute_input)

        user_time = f'{hour:02d}:{minute:02d}'
        return user_time
    
    def set_alarm(self, user_time):
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            print(now, user_time)
            if now >= user_time:
                winsound.PlaySound('alarm_beep.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                print('Time to wake up!')
                break
            time.sleep(30)
        

def main():
    alarm = Alarm()

    user_time = alarm.get_user_time(22, 24)
    alarm.set_alarm(user_time)

if __name__ == "__main__":
    main()
