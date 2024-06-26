class GildedRose(object):
    def __init__(self, items):
        self.items = items
    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Aged Brie":
                item.quality = min(item.quality + 1, 50)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality = min(item.quality + 3, 50)
                elif item.sell_in <= 10:
                    item.quality = min(item.quality + 2, 50)
                else:
                    item.quality = min(item.quality + 1, 50)
            elif "Conjured" in item.name:
                item.quality = max(item.quality - 2, 0)
            else:
                 item.quality = max(item.quality - 1, 0)  
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1