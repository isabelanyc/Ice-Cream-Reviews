import numpy as np
import pandas as pd

from scattertext.termscoring.CorpusBasedTermScorer import CorpusBasedTermScorer


class CliffsDelta(CorpusBasedTermScorer):
    """
    Cliff's Delta from Cliff (1993).


    Cliff, N. (1993). Dominance statistics: Ordinal analyses to answer ordinal questions.
    Psychological Bulletin, 114(3), 494–509.

    Not Yet Implemented
    """

    def _set_scorer_args(self, **kwargs):
        pass

    def get_scores(self, *args) -> pd.Series:
        '''
        In this case, args aren't used, since this information is taken
        directly from the corpus categories.

        Returns
        -------
        np.array, scores
        '''
        cat_X, ncat_X = self._get_cat_and_ncat(self._get_X())
        resd = []

        #for termi, term in enumerate(self.get_terms()):
        #    cat_X[,:termi]

    def get_name(self):
        return "Cliff's Delta"
