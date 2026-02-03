#!/usr/bin/env python3

class GardenManager():
    class GardenStats():
        @staticmethod
        def calculate_growth_length(plants_added):
            return plants_added * 1
    total_gardens = 0

    def __init__(self, owner):
        self.owner = owner
