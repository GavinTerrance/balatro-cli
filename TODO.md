# Balatro CLI Game Development Todo List

## Items to be implemented
### Bugs
[x] Bug: Tarot/Spectral cards that apply an effect to a playing card bought in shop outside of a card pack should only have the option to add to consumable slots. See "testing_results/issue_7.md"
[x] Bug: "Death" Tarot card destroys the original card when it shouldn't there should be 2 copies of the original card after use. See "testing_results/issue_8.md"
[x] Bug: "Death" Tarot card should have command line instructions and not telling the user to drag items. See "testing_results/issue_8.md"
[x] Bug: "The Hermit" Tarot card is limiting the balance to $20, not the amount doubled to $20. So if the user has a $25 balance before play, after play they should have $45 dollars ($25 + $20). See "testing_results/issue_9.md"
[x] Bug: "Clearance Sale" voucher doesn't discount items in shop. See "testing_results/issue_10.md".
[x] Bug: Typing in a non-integer for a card index crashes game. See "testing_results/issue_11.md"
[ ]

### Features
[x] Implement Selling Consumable items and Jokers. (sell_cost = math.max(1, math.floor(cost/2)) + ability_extra_value) | ability extra value  (+2 if foil, +3 if holo, +5 if polychrome, +5 if negative)
 - Related Bug: Swashbucker card seems to be only using the number of jokers to the multiplier instead of sell value. 

### Minor Enhancements
[x] Game state needs to be at the bottom of round output. Score needed and current score need to be together. Hands and Discards need to be more visible. See "testing_results/enhancement_1.md"


## Items implemented 

[x] Spectral and Tarot packs show the 9 card hand available to apply card effect to
 - See cards when pack is opened, not just when card is chosen
 - Invalid selection no longer closes pack. See "testing_results/issue_1.md"
[x] implement any effect that is not yet implemented (search code base for "effect not yet implemented")
[x] Buying tarot/planet cards in the shop gives you the option to "apply now" or "put in hand"
[x] You can only have 2 consumables in your inventory unless expanded by a voucher/joker
[x] Give the user the option to exit at any point during gameplay
[x] Only cards in the hand played count in scoring (example: if user plays pair, only the cards in the pair count in scoring).
 - This can be reversed by an effect. (See Joker "Splash" as an example)
[x] Bug: Riff-Raff Joker now creates two common jokers when a blind is selected. See "testing_results/issue_3.md"
[x] Implement interest. See "data/interest.md" 
[x] Bug: Imolate Spectral card only destroys 3 cards. See "testing_results/issue_4.md"
 - Show user which cards are destroyed
[x] Rarity of item influences the chance of them showing up in shop/packs
[x] Bug: Arcana pack is only showing 4 cards after purchase in the shop. I believe this is due to cards played previously are not being put back in deck. See "testing_results/issue_5.md"
[x] Bug: Buying a pack should generate a new random set of 9 cards instead of keeping the same set in round. Could be a result of cards not being put back in deck. See "testing_results/issue_6.md"

