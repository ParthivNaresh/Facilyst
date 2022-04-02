import numpy as np
import pandas as pd

from facilyst.mocks import MockBase


class Wave(MockBase):

    name = "Wave"

    def __init__(
        self,
        library="numpy",
        num_rows=100,
        wave_type="sine",
        amplitude=1,
        frequency=1,
        random_amplitudes=False,
        random_frequency=False,
        trend=None,
    ):
        if wave_type.lower() in ["sin", "sine"]:
            wave_type = "sine"
        elif wave_type.lower() in ["cos", "cosine"]:
            wave_type = "cosine"
        else:
            wave_type = "sine"
        self.wave_type = wave_type
        self.amplitude = amplitude
        self.frequency = frequency
        self.random_amplitudes = random_amplitudes
        self.random_frequency = random_frequency
        self.trend = trend

        parameters = {
            "wave_type": wave_type,
            "amplitude": amplitude,
            "frequency": frequency,
            "random_amplitudes": random_amplitudes,
            "random_frequency": random_frequency,
            "trend": trend,
        }

        super().__init__(library, num_rows, parameters)

    def create_data(self):
        data = self.generate_wave()
        data = self.handle_library(data)
        return data

    def generate_wave(self):
        if not (self.random_frequency or self.random_amplitudes):
            samples = np.arange(self.num_rows) / self.num_rows
            if self.wave_type == "sine":
                signal = self.amplitude * np.sin(2 * np.pi * self.frequency * samples)
            elif self.wave_type == "cosine":
                signal = self.amplitude * np.cos(2 * np.pi * self.frequency * samples)
        else:
            length_of_each_wave = self.num_rows // self.frequency
            split_indices = []
            start = 0
            for split in range(self.frequency):
                if split == self.frequency - 1:
                    end = self.num_rows
                else:
                    end = start + length_of_each_wave
                split_indices.append((start, end))
                start = end
            split_signals = []
            for interval in split_indices:
                samples = np.arange(interval[1] - interval[0]) / (
                    interval[1] - interval[0]
                )
                amplitude = (
                    self.amplitude
                    if not self.random_amplitudes
                    else np.random.choice([1, 2, 3], 1)[0]
                )
                frequency = (
                    1
                    if not self.random_frequency
                    else np.random.choice([1, 2, 3], 1)[0]
                )
                if self.wave_type == "sine":
                    signal = amplitude * np.sin(2 * np.pi * frequency * samples)
                elif self.wave_type == "cosine":
                    signal = amplitude * np.cos(2 * np.pi * frequency * samples)
                split_signals.extend(signal)
            signal = split_signals
        return signal

    def handle_library(self, data):
        """
        Handles the library that was selected to determine the format in which the data will be returned, and then
        returns the data based on the dtype specified during class instantiation.

        :return: The final data created from the appropriate library as a pd.Series or ndarray.
        """
        if self.library.lower() == "pandas":
            return pd.Series(data)
        elif self.library.lower() == "numpy":
            return data
        return data
