class CandleMetricsCalculator:
    def __init__(self, candle_group):
        """
        Inicializa una nueva instancia de CandleMetricsCalculator.

        :param candle_group: Una instancia de CandleGroup para calcular métricas.
        """
        self.candle_group = candle_group

    def calculate_rate_of_change(self):
        """
        Calcula la tasa de cambio de los precios de cierre de las velas en el grupo.
        La tasa de cambio se calcula como la diferencia entre precios de cierre consecutivos,
        dividida por el precio de cierre del punto inicial, para normalizarla respecto al precio.

        :return: Una lista de tasas de cambio de los precios de cierre.
        """
        rate_of_change = []
        candles = self.candle_group.candles
        for i in range(1, len(candles)):
            previous_price = candles[i-1].closing_price
            current_price = candles[i].closing_price
            if previous_price != 0:  # Evitar división por cero
                change = (current_price - previous_price) / previous_price
                rate_of_change.append(change)
            else:
                rate_of_change.append(0)  # Otra opción podría ser None o continuar sin añadir valor
        return rate_of_change

    # Aquí se pueden añadir métodos adicionales para calcular otras métricas si es necesario.
