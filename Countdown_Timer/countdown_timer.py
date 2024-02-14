import time

class CountdownTimer:
    def __init__(self, user_time):
        """
        Initialize the CountdownTimer.
        Parameters: user_time (int): Time in seconds to countdown.
        """
        self.user_time = user_time

    def countdown(self):
        """
        Start the countdown timer.
        Returns: None
        """
        while self.user_time >= 0:
            mins, secs = divmod(self.user_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            self.user_time -= 1
        print('Lift off!')

if __name__ == '__main__':
    user_time = int(input("Enter a time in seconds: "))
    timer = CountdownTimer(user_time)
    timer.countdown()
