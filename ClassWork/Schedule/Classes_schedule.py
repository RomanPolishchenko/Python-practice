import datetime
import random


class Race:
    def __init__(self, string):  # got string of info on the input
        _today = datetime.datetime.today()
        self.info = string
        self._info = string.split()
        self.code = self._info[0]
        self.route = self._info[1]
        self._arrival_time = list(map(int, self._info[2].split(':')))
        self.arrival_time = datetime.datetime(_today.year,
                                              _today.month,
                                              _today.day,
                                              self._arrival_time[0],
                                              self._arrival_time[1],
                                              self._arrival_time[2])
        self._departure_time = list(map(int, self._info[3].split(':')))
        self.departure_time = datetime.datetime(_today.year,
                                                _today.month,
                                                _today.day,
                                                self._departure_time[0],
                                                self._departure_time[1],
                                                self._departure_time[2])
        # got time with current date
        self._staying_time = (self.departure_time - self.arrival_time).days * 86400 +\
                             (self.departure_time - self.arrival_time).seconds  # staying time in seconds

        self.delay = Race.set_delay()  # timedelta instance with delay
        if self.delay.seconds > 0:  # correcting the schedule
            self.arrival_time = self.arrival_time + self.delay
            self.departure_time = self.departure_time + self.delay

        self.dep_time = self.departure_time.strftime('%H:%M:%S')
        self.arr_time = self.arrival_time.strftime('%H:%M:%S')

    def get_status(self):
        _diff_time = datetime.datetime.today() - self.arrival_time  # difference in time
        _diff_time = _diff_time.days * 86400 + _diff_time.seconds  # difference in seconds
        if _diff_time < 0:
            _status = 'Waiting for arrival'
        elif 0 < _diff_time < self._staying_time:
            _status = "Arrived"
        elif self._staying_time < _diff_time < self._staying_time + 180:  # wait 3 minutes
            _status = 'Departed'
        else:
            _status = "Gone"

        return _status

    def __repr__(self):
        return self.info

    @staticmethod
    def set_delay():
        """
        Delay is determined randomly. 1/10 that it happens.
        """
        _delay = datetime.timedelta(0, 0)  # no delay by default
        _choice = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]  # 1/10 chance
        if random.choice(_choice):
            _ds = random.randint(1, 120)  # delay is up to 2 minutes
            _delay = datetime.timedelta(0, _ds)
        return _delay


if __name__ == '__main__':
    r1 = Race('PA21 Rym-Kyiv 17:11:04 17:12:34')
    print(r1)
    print(r1.delay)
