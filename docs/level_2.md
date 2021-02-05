---
id: level_2
title: Level 2 - Novice
---

- Level 2 strategies should only be learned if you have played with the group a few times and have got the basics down (5-10 games of experience).
- This level builds the strategies in level 1, outlining what to do in more specific situations.
- Level 2 subsections:
  - [Conventions & Special Moves](#conventions--special-moves)
  - [General Principles](#general-principles)
  - [Common Mistakes](#common-mistakes)

<br />

## Conventions & Special Moves

### Playing Multiple 1's - Play Order Inversion in the Starting Hand (Part 1)

- If one or more 1's in your hand are clued, **you should assume that they are all playable**. (This only applies to 1's, and follows from *Good Touch Principle*.)
- We agree that playing 1's at the beginning of the game is a special case - you should always **play the 1's in your starting hand from oldest to newest**. (This is a special case because normally, *Play Clues* mean to play the left-most card.)

<img src="img/intermediate/playing_multiple_1s.png" height="150" />

- In the above screenshot, on the first turn of the game, Alice clues number 1 to Bob, which touches three 1s on slot 2, slot 3, and slot 4.
- From *Good Touch Principle*, Bob knows that he can now play all 3 of these cards.
- Bob should play the slot 4 card first, and then the slot 3 card, and then the slot 2 card.
- The logic behind this convention is explained [here](https://github.com/Zamiell/hanabi-conventions/blob/master/misc/Convention_Reasons.md#play-order-of-multiple-1s).

### The Double Prompt / Triple Prompt / etc.

- Sometimes, someone can give a *Prompt* that is prompting **two** (or more) cards with one clue, which is pretty good.
- For example, in a 3-player game:
  - A red 1 is played on the stacks.
  - Alice clues Cathy red, which touches a red 4. This must be a *Play Clue*, because the red 4 is not on chop.
  - Bob has two clued red cards in his hand. Since Alice has indicated that the red 4 must be playable right now, he knows that his two red cards must be a red 2 and a red 3 (in order from left-to-right).
  - Bob plays the left-most card as the red 2. On Bob's next turn, he plays the other red card as the red 3.

### The Double Finesse / Triple Finesse / etc.

- Typically, *Finesses* are performed by cluing a *one-away-from-playable* card. However, it is possible to get two different people to blind-play their cards in a row if you give a clue to a *two-away-from-playable* card. This is very efficient, as it is a 3-for-1 clue.
- For example, in a 4-player game:
  - A red 1 is played on the stacks.
  - Alice clues Donald red, which touches a red 4.
  - Bob plays red 2 from his *Finesse Position*.
  - Cathy plays red 3 from her *Finesse Position*.
  - Donald plays red 4.
- Similarly, it is possible to get a single player to blind-play 2 cards in a row. In this situation, since they see that the blind cards are not in anyone else's hands, they will blind-play two turns in a row, playing from left to right.
- For example, in a 3-player game:
  - It is the first turn and nothing is played on the stacks.
  - Alice clues red to Cathy, touching a red 3.
  - Bob blind-plays red 1 from slot 1.
  - Cathy would normally think that she has red 2, which would match the red 1 that was just played. However, she sees that when the clue happened, there was a red 2 next to the red 1.
  - Thus, Cathy discards, giving Bob a chance to blind-play the red 2. If he does not blind-play it, then it was a normal *Finesse* and she has red 2. If he does blind-play it, then it was a *Double Finesse* and she has red 3.
  - On his next turn, Bob blind-plays red 2 from slot 2. Cathy now knows that she has the red 3.

### The Prompt + Finesse

- In general, remember that players will always assume *Prompts* over *Finesses*. Thus, is it possible to do a clue that *Prompts* a card from a player's hand **and then** gets them to blind-play their *Finesse Position* card on the next turn.
- For example, in a 3-player game:
  - Red 1 is played on the stacks.
  - Bob has a clued red card in his hand on slot 4.
  - Alice clues Cathy red, which touches a red 4 as a *Play Clue*.
  - Bob knows he must have both red 2 and red 3 (in order to make the red 4 playable), but he only has one clued red card in his hand. So this must be both a *Prompt* on him and a *Finesse* on him at the same time.
  - Since *Prompts* take precedence over *Finesses*, he plays the clued red card first from slot 4. It is red 2 and it successfully plays.
  - On his next turn, Bob blind-plays slot 2 as red 3. (His *Finesse Position* at the time of the clue was slot 1, but he drew a card, and now it slid down to slot 2.)

### The Reverse Finesse

- In a normal *Finesse*, you would give a clue to a player who comes after the player blind-playing a card. (e.g. clue --> blind-play --> clued-card plays)
- If you give a *Finesse* clue to someone who gets to have a turn **before** the blind-play occurs, it is called a *Reverse Finesse*. This is more complicated than a normal *Finesse* and is harder to see. (e.g. clue --> clued player does unrelated action --> blind-play --> clued-card plays)
- Because *Reverse Finesses* exist as a strategy, before playing any cards, players should always check out everyone's *Finesse Position*. If a card in someone's *Finesse Position* is playable and "matches" the clue, then **they need to defer playing the clued card** for at least one go-around and wait to see what happens.
- If the player with the "matching" card blind-plays it, then it means that the clued card is the next card in the chain. For example, in a 3-player game:
  - It is the first turn and nothing is played on the stacks.
  - Alice clues Bob red, which touches his red 2.
  - Next, it is Bob's turn. Normally, Bob would think that he had the red 1, and play it immediately.
  - However, Bob also notices that on Cathy has a red 1 on her slot 1 position. Thus, he has to give a chance for Cathy to prove whether or not a *Reverse Finesse* is happening. If Cathy does not blind-play anything, then Bob should have the red 1, and he can play it on his next turn.
  - Bob discards.
  - Cathy blind-plays red 1. Bob now knows that he has the red 2.
- If the player with the "matching card" **does not** blind-play, then the clued card is probably the other copy, and can be played on the next turn. For example, in a 3-player game:
  - The setup is the same as the last example. Bob is clued red, so he suspects a *Reverse Finesse* is occurring and discards.
  - Cathy discards.
  - Now Bob knows that the red card in his hand is actually the red 1.

### The Self-Finesse

- It is also possible to perform a *Finesse* on a player by giving **them** a clue.
- For example, in a 3-player game:
  - All of the 1's are played on the stacks.
  - Alice clues number 3 to Cathy, touching one 3 on slot 2.
  - Bob discards.
  - Cathy knows that this was a *Play Clue* on the 3, but there are no 3's that are directly playable. Thus, someone must have the matching 2. Since Bob discarded, Cathy must be the one who has the matching 2.
  - Thus, Cathy plays her *Finesse Position* card as **any** 2. It is red 2 and successfully plays.
  - Cathy now knows that her 3 must match the 2, so she marks her 3 as red 3.
- Note that *Self-Finesses* can be difficult to perform because the player receiving the clue will **only** consider the possibility of a *Self-Finesse* **if there are no other possibilities** for the clue. For example:
  - If the clue looks like it *could* just be a normal/direct *Play Clue* on a card, then the clue receiver will not blind-play anything - they will just play the card that was clued.
  - If the clue looks like it *could* be a *Prompt*, then the clue receiver will not play anything and assume that it is a *Prompt*. (At least, until the other player has had a chance to play the *Prompted* card.)
  - If the clue looks like it *could* be a *Reverse Finesse*, then the clue receiver will not play anything and assume that it is a *Reverse Finesse*. (At least, until the other player has had a chance to blind-play the card.)

### Fix Clues

- Nearly every clue that is given is either a *Save Clue* or *Play Clue*. One small exception to this is a *Fix Clue*, which is an attempt to "fix" an impending misplay.
- *Fix Clues* are often needed when a duplicate card is touched. Cards are not normally duplicated (which follows from *Good Touch Principle*), but sometimes someone makes a mistake, or a sequence of particular cards makes duplicating necessary. Duplicate cards will lead to misplays, so it is the team's responsibility to fix the problem and intervene before this happens.

<img src="img/intermediate/fix_clue.png" height="300" />

- In the above screenshot:
  - Before the clue was given, Alice had an unknown purple card in her hand.
  - From *Good Touch Principle*, Alice concluded that her card must be purple 5, and had planned to play it as soon as possible.
  - Bob clues number 3 to Alice, which "fills in" the purple card and reveals that it is purple 3.
  - Since Alice was just about to play this card, Alice knows that this was a *Fix Clue* and that she can now safely discard the purple 3.

<img src="img/intermediate/fix_clue2.png" height="300" />

- **A clue cannot be a *Play Clue* and a *Fix Clue* at the same time.** If you receive a *Fix Clue* and it touches other ancillary cards, none of them are necessarily playable; the primary point of the clue is to fix the impending misplay.
- In the above screenshot:
  - Before the clue was given, Alice has an unknown 1 in her hand.
  - From *Good Touch Principle*, Alice concluded that her 1 must be green 1, and had planned to play it as soon as possible.
  - Bob clues blue to Alice, which "fills in" the 1 and reveals that it is blue 1. The blue clue also touches a blue card on slot 1.
  - In this situation, Alice might be tempted to think that this is a *Play Clue* on a blue 2 in slot 1, especially considering that the slot 1 card was the only brand new card introduced in the clue (and that the focus of a clue should always be on the brand new card introduced).
  - However, the fact that the blue clue "fixed" an impending misplay means that Bob may have had no choice but to clue blue, and he may not necessarily be trying to give a *Play Clue*.
  - Alice marks the blue card as either blue 2, blue 3, blue 4, or blue 5, and discards the blue 1.

### Fix Clues (That Give No Additional Information)

- Usually a *Fix Clue* will "fill in" the card to explicitly make it known that the card is unplayable or duplicated. However, it is also possible to perform a *Fix Clue* just by cluing the card again. For example:
  - Alice clues Bob number 1 and it touches three 1's.
  - Bob successfully plays two 1's.
  - Before Bob can play the 3rd 1, Alice clues Bob number 1 again, and all the clue does is re-touch the remaining 1.
  - Now it is Bob's turn. Since he was going to play the 1 already without Alice doing anything, the clue must have some other meaning. Thus, it is a *Fix Clue*: the remaining 1 is bad, and Bob can safely discard it.
- Note that in general, giving a *Fix Clue* should wait until the card is actually in danger of being misplayed (like in the previous example). If a duplicated card is not in danger of being misplayed anytime soon, then players should defer giving the *Fix Clue* until later. This way, it gives the player a chance to figure out the duplication on their own, which can happen from time to time.
- *Fix Clues* that give no additional information only "fix" one card. For example:
  - Alice clues Bob number 1 and it touches three 1's.
  - Bob successfully plays one 1.
  - Before Bob can play the 2nd 1, Alice clues Bob number 1 again, and all the clue does is re-touch the two remaining 1's.
  - Now it is Bob's turn. Since he was going to play both of these 1's already without Alice doing anything, the clue must have some other meaning. Thus, it is a *Fix Clue*: the 1 that Bob was about to play is bad, and Bob can safely discard it. Bob skips over the 1 that he was about to play and plays the other one.

<br />

## General Principles

### Trash

- *Trash* cards are defined as cards that have already been played. Thus, they are useless to the team.
- Players should generally avoid "touching" trash cards with a clue, as doing so would violate *Good Touch Principle*.
  - Rarely, it can be useful to deliberately clue a trash card and violate *Good Touch Principle* in order to perform a special move. Several such moves are covered later on in this document.
- In the case where a suit is partially "dead", the unneeded cards are also considered trash. For example, if both copies of the red 3 have been discarded, then the red 4 and the red 5 are both considered trash.

<br />

## Common Mistakes

### Stomping on a Finesse

- This is the term used for when a player clues a card directly that was going to be blind-played from a *Finesse*. Typically, this means that the player who gave the clue was not paying attention and failed to see that a *Finesse* happened at all.
- *Stomping* on a *Finesse* essentially wastes a clue for the team.

### What to Do After a Strike / Bomb

- When a card is misplayed and goes to the discard pile, the team accumulates a *strike* (which is also referred to as a *bomb*).
- If three strikes are accumulated, the team will get a score of 0. This is to be **avoided at all costs** and players should play relatively conservatively when the team is at two strikes. (One exception is when players are explicitly going for a perfect score in a really tough variant, but this is less common.)
- Building on this concept, it can also be **very bad** to get **two strikes in a row**. For example, say that Alice performs a bad clue and Bob misplays, causing a strike. And then Cathy "still believes" the original clue (thinking that Bob was the one who made the mistake instead of Alice), and Cathy goes on to misplay, causing yet another strike.
- So, in general, we want to **isolate one mistake to one strike**. Why? Since Hanabi is so difficult, mistakes are common, and we don't want to push the team to the precipice of failure after one tiny mistake. That kind of thing is not very good for the overall win-rate.
- This means that when a strike happens, **the state of information should "reset"** back to what it was before the mistake happened, at least most of the time.
- For example, if Alice clues red to Cathy, and Bob misplays a card, then Cathy should **not** go on to play any of her red cards, and Cathy should **not** make any assumptions about what her red cards could be. Obviously, some kind of mistake happened, and Cathy should sit and wait patiently for further instructions.
