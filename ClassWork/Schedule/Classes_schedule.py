import datetime
import random


class IncorrectInput(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return 'Incorrect input: {}'.format(self._arg)


class Route:
    """
    implementation of
    """
    def __init__(self, string):  # got string of info on the input
        self.check_input(string)
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

        self.delay = self.set_delay()  # timedelta instance with delay
        if self.delay.seconds > 0:  # correcting the schedule
            self.arrival_time = self.arrival_time + self.delay
            self.departure_time = self.departure_time + self.delay

        self.dep_time = self.departure_time.strftime('%H:%M:%S')
        self.arr_time = self.arrival_time.strftime('%H:%M:%S')

    @staticmethod
    def check_input(_input):
        """
        Checks the correctness of input data.
        :param _input: data represented by <str>
        :return: None
        """
        _input = _input.split()
        try:
            assert len(_input) == 4
            _code = _input[0]
            assert len(_code) == 4  # checking the code length
            assert _code.isupper()  # checking the code format
            _route = _input[1].split('–')
            assert len(_route) == 2  # checking the correctness of route
            _time_arr = _input[2].split(':')
            _time_dep = _input[3].split(':')
            assert len(_time_arr) == 3 and len(_time_dep) == 3  # checking if there are 3 components of time
            for i in range(3):
                assert float(_time_dep[i]) - int(_time_dep[i]) == 0  # checking if time repr. by <int>
                assert float(_time_arr[i]) - int(_time_arr[i]) == 0  # checking if time repr. by <int>
                _time_arr[i] = int(_time_arr[i])  # converting to <int>
                _time_dep[i] = int(_time_dep[i])  # converting to <int>
            _time_dep = _time_dep[0]*3600 + _time_dep[1]*60 + _time_dep[2]  # converting to seconds
            _time_arr = _time_arr[0]*3600 + _time_arr[1]*60 + _time_arr[2]  # converting to seconds
            assert _time_dep > _time_arr  # checking if departure after arrival
        except AssertionError:
            raise IncorrectInput(_input)

    def get_status(self):
        _diff_time = datetime.datetime.today() - self.arrival_time  # difference in time
        _diff_time = _diff_time.days * 86400 + _diff_time.seconds  # difference in seconds
        if _diff_time < 0:
            _status = 'Waiting for arrival'
        elif 0 <= _diff_time <= self._staying_time:
            _status = "Arrived"
        elif self._staying_time < _diff_time <= self._staying_time + 180:  # wait 3 minutes
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
    r1 = Route('PA21 Rym–Kyiv 17:11:04 17:12:34')
    print(r1)
    print(r1.delay)
