from tqdm import tqdm

class SimilarityMapBuilder:
    def __init__(self, groups, comparator):
        self.groups = groups
        self.comparator = comparator

    def build(self):

        similarity_map = {}
        list(map(lambda group_i: self.compare_group_with_others(group_i[0], group_i[1], similarity_map),
                 tqdm(enumerate(self.groups))))
        return similarity_map

    def compare_group_with_others(self, current_index, current_group, similarity_map):
        """
        Compara un grupo de velas con todos los demás grupos siguientes en la lista para encontrar similitudes.
        """
        for next_index in range(current_index + 1, len(self.groups)):
            self.evaluate_and_record_similarity(current_index, next_index, current_group, self.groups[next_index], similarity_map)

    def evaluate_and_record_similarity(self, index_a, index_b, group_a, group_b, similarity_map):
        """
        Evalúa si dos grupos de velas son similares y, en caso afirmativo, registra esta similitud en el mapa.
        """
        if self.comparator.are_similar(group_a.pattern, group_b.pattern):
            similarity_map.setdefault(index_a, []).append(index_b)
            similarity_map.setdefault(index_b, []).append(index_a)
