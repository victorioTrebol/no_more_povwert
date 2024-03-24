from lib_no_more_poverty.pattern_calculator.candle_group import CandleGroup


class CandleGroupMapper:
    def __init__(self, candles, group_size):
        self.candles = candles
        self.group_size = group_size
        self.groups = self.map_candles_to_groups()

    def map_candles_to_groups(self):
        groups = []

        for i in range(0, len(self.candles), self.group_size):
            group = CandleGroup(self.candles[i:i + self.group_size])
            groups.append(group)

        sorted(groups, key=lambda x: x.pattern)
        return groups

