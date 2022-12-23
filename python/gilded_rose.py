from observer import Observer


class GildedRose(Observer):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        [item.update_item() for item in self.items]
