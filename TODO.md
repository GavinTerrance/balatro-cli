# Balatro CLI Game Development Todo List

[x] Spectral and Tarot packs show the 9 card hand available to apply card effect to
 - See cards when pack is opened, not just when card is chosen
 - Invalid selection no longer closes pack. See "testing_results/issue_1.md"
[x] implement any effect that is not yet implemented (search code base for "effect not yet implemented")
[x] Buying tarot/planet cards in the shop gives you the option to "apply now" or "put in hand"
[x] You can only have 2 consumables in your inventory unless expanded by a voucher/joker
[x] Give the user the option to exit at any point during gameplay
[x] Only cards in the hand played count in scoring (example: if user plays pair, only the cards in the pair count in scoring).
 - This can be reversed by an effect. (See Joker "Splash" as an example)
[x] Bug: Tarot/Spectral cards that apply an effect to a playing card bought in shop outside of a card pack now show playing cards available to apply to. See "testing_results/issue_2.md"
[x] Bug: Riff-Raff Joker now creates two common jokers when a blind is selected. See "testing_results/issue_3.md"
[x] Implement interest. See "data/interest.md" 
[x] Bug: Imolate Spectral card only destroys 3 cards. See "testing_results/issue_4.md"
 - Show user which cards are destroyed
[x] Rarity of item influences the chance of them showing up in shop/packs
[ ] Implement Selling Consumable items and Jokers. (sell_cost = math.max(1, math.floor(cost/2)) + ability_extra_value) | ability extra value  (+2 if foil, +3 if holo, +5 if polychrome, +5 if negative)
 - Swashbucker card seems to be only using the number of jokers to the multiplier
[ ] Bug: Arcana pack is only showing 4 cards after purchase in the shop. I believe this is due to cards played previously are not being put back in deck. See "testing_results/issue_5.md"
[ ] Bug: Buying a pack should generate a new random set of 9 cards instead of keeping the same set in round. Could be a result of cards not being put back in deck. See "testing_results/issue_6.md"