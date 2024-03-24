

from typing import List, Dict
import datetime
from clases.five_minute_japanese_candle import FiveMinuteJapaneseCandle


class MapperFiveMinuteCandle:

    def map(self,row:Dict[str,str])->FiveMinuteJapaneseCandle:
        five_minute_japanese_candle = FiveMinuteJapaneseCandle(opening_price=float(row['open']),
                                                                closing_price=float(row['close']),
                                                                hightest_price=float(row['high']),
                                                                lower_price=float(row['low']),
                                                                volume=float(row['volume']),
                                                                datetime=datetime.datetime.strptime(row['datetime'], '%Y-%m-%d %H:%M:%S'))

        return five_minute_japanese_candle