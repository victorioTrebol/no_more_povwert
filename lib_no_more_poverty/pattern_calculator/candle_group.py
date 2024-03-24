from typing import List

from clases.five_minute_japanese_candle import FiveMinuteJapaneseCandle


class CandleGroup:
    def __init__(self, candle_list:List[FiveMinuteJapaneseCandle]):
        self.candle_list = candle_list
        self.start_date = min(candle_list, key=lambda x: x.datetime)
        self.end_date = max(candle_list, key=lambda x: x.datetime)
        self.pattern = self.__calculate_pattern()

    def __calculate_pattern(self):
        precios_cierre = [candle.closing_price for candle in self.candle_list]
        cambios = [(precios_cierre[i] - precios_cierre[i-1]) / precios_cierre[i-1] for i in range(1, len(precios_cierre))]
        return cambios

    def return_pattern(self):
        return self.pattern