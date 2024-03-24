from datetime import datetime

from clases.five_minute_japanese_candle import FiveMinuteJapaneseCandle
from lib_no_more_poverty.mappers.candle_group_mapper import CandleGroupMapper


class TestMapEvery4:

    def test_should_return_2_elements(self):
        candles_test = [FiveMinuteJapaneseCandle(100, 102, 105, 99, 500, datetime(2023, 3, 19, 10, 0)),
                        FiveMinuteJapaneseCandle(102, 101, 103, 100, 600, datetime(2023, 3, 19, 10, 5)),
                        FiveMinuteJapaneseCandle(101, 103, 104, 100, 550, datetime(2023, 3, 19, 10, 10)),
                        FiveMinuteJapaneseCandle(103, 105, 106, 102, 600, datetime(2023, 3, 19, 10, 15)),
                        FiveMinuteJapaneseCandle(103, 105, 106, 102, 600, datetime(2023, 3, 19, 10, 15))
                        ]

        # Crear el mapper con un tamaño de grupo de 4
        mapper_test = CandleGroupMapper(candles_test, 4)

        mapped=mapper_test.map_candles_to_groups()

        assert len(mapped) == 2