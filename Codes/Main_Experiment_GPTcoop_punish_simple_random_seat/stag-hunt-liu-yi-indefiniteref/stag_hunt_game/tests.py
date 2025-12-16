from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    cases = ['both_stag','h_1_stag','h_2_stag', 'both_hare']

    def play_round(self):
        yield (pages.Introduction)

        if self.case == 'both_stag':
            yield (pages.Decide, {"decision": 'stag'})
            if self.player.role() == 'h_1':
                assert self.player.payoff == Constants.stag_match_payoff
            else:
                assert self.player.payoff == Constants.stag_match_payoff

        if self.case == 'h_1_stag':
            if self.player.role() == 'h_1':
                yield (pages.Decide, {"decision": 'stag'})
                assert self.player.payoff == Constants.stag_mismatch_payoff
            else:
                yield (pages.Decide, {"decision": 'hare'})
                assert self.player.payoff == self.group.h_2_hare_payoff()

        if self.case == 'h_2_stag':
            if self.player.role() == 'h_1':
                yield (pages.Decide, {"decision": 'hare'})
                assert self.player.payoff == Constants.h_1_hare_payoff
            else:
                yield (pages.Decide, {"decision": 'stag'})
                assert self.player.payoff == Constants.stag_mismatch_payoff

        if self.case == 'both_stag':
            yield (pages.Decide, {"decision": 'hare'})
            if self.player.role() == 'h_1':
                assert self.player.payoff == Constants.h_1_hare_payoff
            else:
                assert self.player.payoff == self.group.h_2_hare_payoff()

        yield (pages.Results)
