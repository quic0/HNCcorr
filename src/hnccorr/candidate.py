from hnccorr.segmentation import Segmentation


class Candidate:
    def __init__(self, center_seed, hnccorr):
        self._center_seed = center_seed
        self._hnccorr = hnccorr
        self.segmentations = None
        self.best_segmentation = None

    def __eq__(self, other):
        return (self._center_seed == other._center_seed) and (
            self._hnccorr == other._hnccorr
        )

    def segment(self):
        pos_seeds = self._hnccorr.positive_seed_selector.select(self._center_seed)
        neg_seeds = self._hnccorr.negative_seed_selector.select(self._center_seed)
        patch = "patch"
        embedding = "embedding"
        graph = self._hnccorr.graph_constructor.construct(patch, embedding)
        self.segmentations = self._hnccorr.segmentor.solve(graph, pos_seeds, neg_seeds)

        self.best_segmentation = self._hnccorr.postprocessor.select(self.segmentations)
        return self.best_segmentation
