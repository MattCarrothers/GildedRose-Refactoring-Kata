from observer import Observer


class GildedRose(Observer):

    def __init__(self, items):
        self.items = items
        self.string_to_return = "OMGHAI!\n"
        self.update_output_string(0)

    def update_quality(self):
        [item.update_item() for item in self.items]

    def update_output_string(self, day):
        self.string_to_return += f"-------- day {day} --------\nname, sellIn, quality\n"
        for item in self.items:
            self.string_to_return += str(item)
            self.string_to_return += "\n"
        self.string_to_return += "\n"
