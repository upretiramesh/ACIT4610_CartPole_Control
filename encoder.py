import random
import config


class Encoder:
    def __init__(self, obs, method=None, cp_high=0.2, cv_high=0.2, pa_high=0.04, pv_high=0.2):
        self.obs = obs
        self.method = method
        self.obs_limit = [cp_high, cv_high, pa_high, pv_high]
        self.prob = self.convert_int_probability()
        self.cells = []

        if self.method == 'prob_base':
            self.probability_encoder(config.PROB_ITERATION)
        elif self.method == 'mix':
            self.mix_encoder(config.PROB_ITERATION, config.VALUE_ENCODE_LIMIT)
        else:
            self.value_encoder(config.VALUE_ENCODE_LIMIT)

    def convert_int_probability(self):
        lst = []
        for obs_limit, obs_value in zip(self.obs_limit, self.obs):
            lst.append(1 if abs(obs_value) > obs_limit else round(abs(obs_value) / obs_limit, 2))
        return lst

    def probability_encoder(self, n):
        action = [0, 1]
        for _ in range(n):
            for v, p in zip(self.obs, self.prob):
                self.cells.append(
                    random.choices(action, [p, 1 - p])[0] if v > 0 else random.choices(action, [1 - p, p])[0])

    def value_encoder(self, limits):
        self.cells.extend([1 if ob > 0 else 0 for ob in self.obs])
        for limit in limits:
            for ob in self.obs:
                if ob > 0:
                    self.cells.append(0 if ob > limit else 1)
                else:
                    self.cells.append(1 if ob < -limit else 0)

    def mix_encoder(self, n, limits):
        self.probability_encoder(n)
        self.value_encoder(limits)
