from lib_no_more_poverty.candle_group_operations import CandleMetricsCalculator


class CandleGroup:
    def __init__(self, candles=None):
        """
        Inicializa una nueva instancia de CandleGroup.

        :param candles: Una lista de instancias de FiveMinuteJapaneseCandle que forman el grupo.
        """
        self.candles = candles if candles is not None else []
        self.rate_of_change = CandleMetricsCalculator(self).calculate_rate_of_change()

    def calculate_rate_of_change(self):
        """
        :return: Una lista de tasas de cambio de los precios de cierre.
        """
        return self.rate_of_change

    def aggregate_volume(self):
        """
        Calcula el volumen total de compra y venta agregado de todas las velas en el grupo.

        :return: Un diccionario con el volumen total de compra y venta.
        """
        total_buy_volume = sum(candle.buy_volume for candle in self.candles)
        total_sell_volume = sum(candle.sell_volume for candle in self.candles)
        return {'buy_volume': total_buy_volume, 'sell_volume': total_sell_volume}

    def __str__(self):
        """
        Devuelve una representación en string del grupo de velas, mostrando la cantidad de velas.

        :return: Un string que representa el grupo de velas.
        """
        return f"CandleGroup(candles={len(self.candles)})"
