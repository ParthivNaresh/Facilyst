import re

import numpy as np
import pandas as pd

from facilyst.mocks import MockBase


class Dates(MockBase):

    name = "Dates"

    chaos_percentage = {
        0: 0,
        1: 10,
        2: 15,
        3: 20,
        4: 25,
        5: 30,
        6: 40,
        7: 50,
        8: 60,
        9: 70,
        10: 80,
    }

    def __init__(
        self,
        num_rows=100,
        library="pandas",
        start_date="1/1/2001",
        frequency="1D",
        missing=False,
        misaligned=False,
        duplicates=False,
        chaos=1,
    ):
        """Class to manage mock data creation of datetime values.


        :param num_rows: The number of observations in the final dataset. Defaults to 100.
        :type num_rows: int, optional
        :param library: The library of which the final dataset should be, options are 'pandas' and 'numpy'. Defaults to 'pandas'.
        :type library: str, optional
        :param start_date: The start date for the datetime values. Defaults to January 1, 2001.
        :type start_date: str, optional
        :param frequency: Frequency for the datetime values. Defaults to a frequency of 1 day.
        :type frequency: str, optional
        :param missing: Flag that determines if datetime values will be randomly removed. Defaults to False. Will be set to False if chaos is 0.
        :type missing: bool, optional
        :param misaligned: Flag that determines if datetime values will be randomly misaligned. Defaults to False. Will be set to False if chaos is 0.
        :type misaligned: bool, optional
        :param duplicates: Flag that determines if duplicate datetime values will be randomly added. Defaults to False. Will be set to False if chaos is 0.
        :type duplicates: bool, optional
        :param chaos: Determines what percentage of the date range will be modified to be uninferable. Set on a scale
        of 0 (no duplicate, missing, or misaligned values in the date range, resulting in an inferable frequency) to 10.
        If parameters `duplicates`, `missing`, and `misaligned` are all set to False, then this parameter will be set to 0.
        Defaults to 1.
        :type chaos: int, optional
        :return: Mock datetime data.
        :rtype: pd.DateTimeIndex by default, can also return np.ndarray
        """
        self.num_rows = num_rows
        self.start_date = start_date
        self.frequency = frequency
        self.missing = missing
        self.misaligned = misaligned
        self.duplicates = duplicates
        self.chaos = int(chaos)

        if self.num_rows < 3:
            raise ValueError("Parameter `num_rows` must be 3 or above!")

        if not (self.duplicates or self.missing or self.misaligned):
            self.chaos = 0

        self.validate_num_rows()

        parameters = {
            "start": self.start_date,
            "freq": self.frequency,
            "missing": self.missing,
            "misaligned": self.misaligned,
            "duplicates": self.duplicates,
            "chaos": self.chaos,
        }

        super().__init__(library, num_rows, parameters)

    def create_data(self):
        data = pd.date_range(
            start=self.start_date, periods=self.num_rows, freq=self.frequency
        )
        if self.chaos:
            data = self.make_uninferrable(data)
        data = self.handle_library(data)
        return data

    def validate_num_rows(self):
        if self.chaos and (self.num_rows < 30):
            raise ValueError(
                f"The `num_rows` parameter must be a minimum of 30 if chaos is not 0."
            )

    def make_uninferrable(self, dates_):
        chaos_percent = Dates.chaos_percentage[self.chaos] / 100
        num_chaos_rows = chaos_percent * self.num_rows
        num_of_each_issue = int(
            num_chaos_rows // sum([self.missing, self.misaligned, self.duplicates])
        )
        all_indices_to_consider = np.arange(self.num_rows)
        if self.missing:
            random_missing_indices = np.random.choice(
                all_indices_to_consider, num_of_each_issue, replace=False
            )
            all_indices_to_consider = np.setdiff1d(
                all_indices_to_consider, random_missing_indices
            )
            dates_ = Dates.remove_missing(dates_, random_missing_indices)
        if self.misaligned:
            random_misaligned_indices = np.random.choice(
                all_indices_to_consider, num_of_each_issue, replace=False
            )
            all_indices_to_consider = np.setdiff1d(
                all_indices_to_consider, random_misaligned_indices
            )
            dates_ = Dates.shift_misaligned(
                dates_, random_misaligned_indices, self.frequency
            )
        if self.duplicates:
            random_duplicate_indices = np.random.choice(
                all_indices_to_consider, num_of_each_issue, replace=False
            )
            dates_ = Dates.add_duplicates(dates_, random_duplicate_indices)
        return dates_

    @staticmethod
    def remove_missing(dates_, missing_indices):
        datetime_series = pd.Series(dates_)
        datetime_series.iloc[missing_indices] = None
        return datetime_series

    @staticmethod
    def shift_misaligned(dates_, misaligned_indices, freq):
        try:
            num_freq = re.findall("\\d+", freq)[0]
        except IndexError:
            num_freq = 1
        num_freq = int(num_freq)
        str_freq = re.findall("\\D+", freq)[0]
        if str_freq == "A":
            num_freq *= 365
            str_freq = "D"
        elif str_freq == "MS":
            num_freq *= (
                28  # Because February is the shortest month, it's a limiting factor
            )
            str_freq = "D"
        current_td = pd.Timedelta(int(num_freq), str_freq)

        missing_values = []
        for missing_index in misaligned_indices:
            fraction_td = current_td / np.random.choice([2, 3, 4, 5], 1)[0]
            missing_values.append(dates_[missing_index] + fraction_td)
        datetime_series = pd.Series(dates_)
        datetime_series.iloc[misaligned_indices] = missing_values
        return datetime_series

    @staticmethod
    def add_duplicates(
        dates_, duplicate_indices
    ):  # Currently adds values to entire Series, maybe change logic so num_rows doesn't change
        datetime_series = pd.Series(dates_)
        duplicate_values = pd.Series(datetime_series.iloc[duplicate_indices].values)
        datetime_series = datetime_series.append(duplicate_values)
        sorted_datetime_series = datetime_series.sort_values().reset_index(drop=True)
        return sorted_datetime_series

    def handle_library(self, dates_):
        """
        Handles the library that was selected to determine the format in which the data will be returned.

        :return: The final data created from the appropriate library as a pd.DatetimeIndex or ndarray.
        """
        if self.library.lower() == "numpy":
            return dates_.to_numpy()
        else:
            return pd.DatetimeIndex(dates_)
