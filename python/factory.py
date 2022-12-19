from context_class import *


class Factory:
    def build_item(self, entry):
        if entry[0] == "Aged Brie":
            context = Context(BrieStrategy())
            item = context.build_item(entry)
        elif entry[0] == "Backstage passes to a TAFKAL80ETC concert":
            context = Context(BackstageStrategy())
            item = context.build_item(entry)
        elif entry[0] == "Sulfuras, Hand of Ragnaros":
            context = Context(LegendaryStrategy())
            item = context.build_item(entry)
        else:
            context = Context(BasicStrategy())
            item = context.build_item(entry)
        return item

        # if 'else' in build_item:
        #     print("Sorry Alan.")
