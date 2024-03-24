from clases.five_minute_japanese_candle import FiveMinuteJapaneseCandle
from lib_no_more_poverty.pattern_calculator.candle_group import CandleGroup
from datetime import datetime

class TestCandleGroup:

    def test_should_return(self):
        # Suponiendo que ya tienes definida la clase FiveMinuteJapaneseCandle como antes

        # Ejemplo de cómo se usaría con datos de ejemplo
        candles_grupo1 = [FiveMinuteJapaneseCandle(100, 102, 105, 99, 500,datetime(2023, 3, 19, 10, 0)),
                          FiveMinuteJapaneseCandle(102, 101, 103, 100, 600, datetime(2023, 3, 19, 10, 5)),
                          FiveMinuteJapaneseCandle(101, 103, 104, 100, 550, datetime(2023, 3, 19, 10, 10)),
                          FiveMinuteJapaneseCandle(103, 105, 106, 102, 600, datetime(2023, 3, 19, 10, 15))
                            ]

        grupo1 = CandleGroup(candles_grupo1)

        assert grupo1.return_pattern() == [-0.00980392156862745, 0.019801980198019802,0.019417475728155338]

        # Esto imprime el patrón calculado para el grupo de velas, así como las fechas de inicio y fin
