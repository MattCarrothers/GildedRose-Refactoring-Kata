class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.adjust_quality()
            item.advance_day()
            item.check_out_of_date()

