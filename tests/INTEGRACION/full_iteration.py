import datetime

from lib_no_more_poverty.clustering_patterns.candle_group_clusterer import CandleGroupClusterManager
from lib_no_more_poverty.mappers.candle_group_mapper import CandleGroupMapper
from lib_no_more_poverty.repository.data_eth_repository import RepoEth


class TestFull_:

    def _test_full_(self):
        repo_eth = RepoEth(data_path='../../data_eth.csv')
        start_datetime=datetime.datetime.now()
        data = repo_eth.get_data_from_csv()


        data=data[:100_000]
        grouper=CandleGroupMapper(data, 4)

        groups=grouper.map_candles_to_groups()

        manager=CandleGroupClusterManager(groups, 0.02)
        manager.group_clusters()

        end_datetime=datetime.datetime.now()


        assert len(groups) == 2


TestFull_()._test_full_()