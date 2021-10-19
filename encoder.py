import random
import config
import pandas as pd


class Encoder:
    def __init__(self, obs, method=None, cp_high=0.2, cv_high=0.2, pa_high=0.04, pv_high=0.2):
        self.obs = obs
        self.method = method
        self.obs_limit = [cp_high, cv_high, pa_high, pv_high]
        self.prob = self.convert_into_probability()
        self.cells = []

        if self.method == 'prob_base':
            self.probability_encoder(config.PROB_ITERATION)
        elif self.method == 'mix':
            self.mix_encoder(config.PROB_ITERATION, config.VALUE_ENCODE_LIMIT)
        elif self.method == 'pole_angle_velocity':
            self.encoder_only_poleAngle_poleVelocity()
        elif self.method == 'cart_position_velocity':
            self.encoder_only_cartPosition_cartVelocity()
        elif self.method == 'cart_pole':
            self.encode_both_cart_and_pole()
        else:
            self.value_encoder(config.VALUE_ENCODE_LIMIT)

    def convert_into_probability(self):
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
        for i in range(config.REPEAT):
            self.cells.extend([1 if ob > 0 else 0 for ob in self.obs])
            for limit in limits:
                for ob in self.obs:
                    if ob > 0:
                        self.cells.append(0 if ob > limit else 1)
                    else:
                        self.cells.append(1 if ob < -limit else 0)

    def encoder_only_poleAngle_poleVelocity(self):
        bins = config.BINS
        # encode base on pole angle
        pole_angle = config.POLE_ANGLE
        if self.obs[2] > 0:
            for val in pd.cut([0, pole_angle], bins=bins, retbins=True)[1][1:]:
                self.cells.append(1 if self.obs[2] > val else 0)
        else:
            for val in pd.cut([0, pole_angle], bins=bins, retbins=True)[1][1:]:
                self.cells.append(0 if self.obs[2] < -val else 1)

        # encode base on pole velocity
        pole_velocity = config.POLE_VELOCITY
        if self.obs[3] > 0:
            for val in pd.cut([0, pole_velocity], bins=bins, retbins=True)[1][1:]:
                self.cells.append(1 if self.obs[3] > val else 0)
        else:
            for val in pd.cut([0, pole_velocity], bins=bins, retbins=True)[1][1:]:
                self.cells.append(0 if self.obs[3] < -val else 1)

    def encoder_only_cartPosition_cartVelocity(self):
        bins = config.BINS
        # encode base on pole angle
        card_position = config.CART_POSITION
        if self.obs[0] > 0:
            for val in pd.cut([0, card_position], bins=bins, retbins=True)[1][1:]:
                self.cells.append(0 if self.obs[0] > val else 1)
        else:
            for val in pd.cut([0, card_position], bins=bins, retbins=True)[1][1:]:
                self.cells.append(1 if self.obs[0] < -val else 0)

        # encode base on pole velocity
        cart_velocity = config.CART_VELOCITY
        if self.obs[1] > 0:
            for val in pd.cut([0, cart_velocity], bins=bins, retbins=True)[1][1:]:
                self.cells.append(0 if self.obs[1] > val else 1)
        else:
            for val in pd.cut([0, cart_velocity], bins=bins, retbins=True)[1][1:]:
                self.cells.append(1 if self.obs[1] < -val else 0)

    def encode_both_cart_and_pole(self):
        self.encoder_only_cartPosition_cartVelocity()
        self.encoder_only_poleAngle_poleVelocity()

    def mix_encoder(self, n, limits):
        self.probability_encoder(n)
        self.value_encoder(limits)