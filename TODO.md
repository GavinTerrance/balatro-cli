# Balatro CLI Game Development Todo List

[x] Spectral and Tarot packs show the 9 card hand available to apply card effect to
 - See cards when pack is opened, not just when card is chosen
 - Invalid selection no longer closes pack. See "testing_results/issue_1.md"
[x] implement any effect that is not yet implemented (search code base for "effect not yet implemented")
[x] Buying tarot/planet cards in the shop gives you the option to "apply now" or "put in hand"
[x] You can only have 2 consumables in your inventory unless expanded by a voucher/joker
[x] Give the user the option to exit at any point during gameplay
[ ] Only cards in the hand played count in scoring (example: if user plays pair, only the cards in the pair count in scoring).
 - This can be reversed by an effect. (See Joker "Splash" as an example)
[x] Bug: Tarot/Spectral cards that apply an effect to a playing card bought in shop outside of a card pack now show playing cards available to apply to. See "testing_results/issue_2.md"
[x] Bug: Riff-Raff Joker now creates two common jokers when a blind is selected. See "testing_results/issue_3.md"
[ ] Implement interest. See "data/interest.md" 
