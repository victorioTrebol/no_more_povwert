
import csv

from lib_no_more_poverty.mappers.map_five_minute_candle import MapperFiveMinuteCandle


class RepoEth:

    def __init__(self,data_path: str):
        self.data_path = data_path

    def get_data_from_csv(self):
        FiveMinutejapaneseCandleList = []
        mapper=MapperFiveMinuteCandle()

        with open(self.data_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                FiveMinutejapaneseCandleList.append(mapper.map(row))

        return FiveMinutejapaneseCandleList