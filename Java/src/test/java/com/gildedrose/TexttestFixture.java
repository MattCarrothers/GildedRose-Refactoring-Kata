package com.gildedrose;

public class TexttestFixture {
    public String golden_master(String[] args) {
        System.out.println("OMGHAI!");

        Item[] items = new Item[]{
            new Item("+5 Dexterity Vest", 10, 20), //
            new Item("Aged Brie", 2, 0), //
            new Item("Elixir of the Mongoose", 5, 7), //
            new Item("Sulfuras, Hand of Ragnaros", 0, 80), //
            new Item("Sulfuras, Hand of Ragnaros", -1, 80),
            new Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            new Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            new Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            // this conjured item does not work properly yet
            new Item("Conjured Mana Cake", 3, 6)};

        StringBuilder string_to_return = new StringBuilder();

        GildedRose app = new GildedRose(items);

        int days = 2;
        if (args.length > 0) {
            days = Integer.parseInt(args[0]) + 1;
        }

        for (int i = 0; i < days; i++) {
            string_to_return.append("-------- day ").append(i).append(" --------\n");
            string_to_return.append("name, sellIn, quality");
            for (Item item : items) {
                string_to_return.append(item);
            }
            string_to_return.append("\n");
            app.updateQuality();
        }
        string_to_return.toString();
        return string_to_return;
    }
}
