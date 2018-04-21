import datetime
import random


class Race:
    def __init__(self, string):  # got string of info on the input
        _today = datetime.datetime.today()
        self.info = string
        self._info = string.split()
        self.code = self._info[0]
        self.route = self._info[1]
        self.arr_time = self._info[2]
        self._arrival_time = list(map(int, self._info[2].split(':')))
        self.arrival_time = datetime.datetime(_today.year,
                                              _today.month,
                                              _today.day,
                                              self._arrival_time[0],
                                              self._arrival_time[1],
                                              self._arrival_time[2])
        self.dep_time = self._info[3]
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
        self.delay = Race.set_delay()  # False or datetime instance

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
        _today = datetime.datetime.today()
        _delay = False  # no delay by default
        _choice = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]  # 1/10 chance
        if random.choice(_choice):
            _dm = random.randint(0, 1)
            _ds = random.randint(0, 59)
            _delay = datetime.datetime(_today.year,
                                       _today.month,
                                       _today.day,
                                       0,
                                       _dm,
                                       _ds)
        return _delay


if __name__ == '__main__':
    r1 = Race('PA21 Rym-Kyiv 15:31:04 15:32:34')
    print(r1.get_status())
