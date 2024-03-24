
class PatternComparator:
    def __init__(self, tolerance):
        self.tolerance = tolerance

    def are_similar(self, pattern1, pattern2):
        if len(pattern1) != len(pattern2):
            return False
        return all(abs(v1 - v2) <= self.tolerance for v1, v2 in zip(pattern1, pattern2))

