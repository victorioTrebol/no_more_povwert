from datetime import datetime

from clases.five_minute_japanese_candle import FiveMinuteJapaneseCandle
from lib_no_more_poverty.clustering_patterns.candle_group_clusterer import  CandleGroupClusterManager
from lib_no_more_poverty.mappers.similarity_lhs_map_builder import CandleGroupClusterAggregator
from lib_no_more_poverty.pattern_calculator.candle_group import CandleGroup


class TestCandleGroupClusterer:

    def test_should_return_1_element_group_when_2_groups_are_similar(self):
        # Arrange
        candles1 = [FiveMinuteJapaneseCandle(opening_price=101, closing_price=102, hightest_price=105, lower_price=99, volume=502, datetime=datetime(2023, 3, 19, 10, 0)),
                        FiveMinuteJapaneseCandle(opening_price=102, closing_price=101, hightest_price=103, lower_price=100, volume=600, datetime=datetime(2023, 3, 19, 10, 5)),
                        FiveMinuteJapaneseCandle(opening_price=101, closing_price=103, hightest_price=104, lower_price=100, volume=550, datetime=datetime(2023, 3, 19, 10, 10)),
                        FiveMinuteJapaneseCandle(opening_price=103, closing_price=105, hightest_price=106, lower_price=102, volume=600, datetime=datetime(2023, 3, 19, 10, 15)),
                        FiveMinuteJapaneseCandle(opening_price=103, closing_price=104, hightest_price=106, lower_price=102, volume=600, datetime=datetime(2023, 3, 19, 10, 20))
                        ]

        candles2 = [FiveMinuteJapaneseCandle(opening_price=101, closing_price=102, hightest_price=105, lower_price=99, volume=502, datetime=datetime(2023, 3, 19, 10, 0)),
                        FiveMinuteJapaneseCandle(opening_price=102, closing_price=101, hightest_price=103, lower_price=100, volume=600, datetime=datetime(2023, 3, 19, 10, 5)),
                        FiveMinuteJapaneseCandle(opening_price=101, closing_price=103, hightest_price=104, lower_price=100, volume=550, datetime=datetime(2023, 3, 19, 10, 10)),
                        FiveMinuteJapaneseCandle(opening_price=103, closing_price=105, hightest_price=106, lower_price=102, volume=600, datetime=datetime(2023, 3, 19, 10, 15)),
                        FiveMinuteJapaneseCandle(opening_price=103, closing_price=104, hightest_price=106, lower_price=102, volume=600, datetime=datetime(2023, 3, 19, 10, 20))
                        ]

        candles3 = [FiveMinuteJapaneseCandle(opening_price=101, closing_price=500, hightest_price=105, lower_price=99, volume=502, datetime=datetime(2023, 3, 19, 10, 0)),
                        FiveMinuteJapaneseCandle(opening_price=102, closing_price=20, hightest_price=103, lower_price=100, volume=600, datetime=datetime(2023, 3, 19, 10, 5)),
                        FiveMinuteJapaneseCandle(opening_price=101, closing_price=25, hightest_price=104, lower_price=100, volume=550, datetime=datetime(2023, 3, 19, 10, 10)),
                        FiveMinuteJapaneseCandle(opening_price=103, closing_price=1, hightest_price=106, lower_price=102, volume=600, datetime=datetime(2023, 3, 19, 10, 15)),
                        FiveMinuteJapaneseCandle(opening_price=103, closing_price=60, hightest_price=106, lower_price=102, volume=600, datetime=datetime(2023, 3, 19, 10, 20))
                        ]

        # Ejemplo de cómo utilizar estas clases:
        groups = [CandleGroup(candles1), CandleGroup(candles2), CandleGroup(candles3)]
        manager = CandleGroupClusterAggregator(groups, 0.02)
        grouped=manager.aggregate()

        assert len(grouped) == 2