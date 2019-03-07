# Strategy Reference

Our group has come up with many different strategies. It is helpful to give specific names to each strategy to aid in both discussion and comprehension. If you know the general way we play but don't know about a specific kind of move, then you can look it up in this document.

If you are a new player, do not bother reading this document. It is much better to simply read the [introductory document](https://github.com/Zamiell/hanabi-conventions/blob/master/Beginners.md) and then start playing games with the group. This document can be used as a reference as you continue to naturally improve at the game.

Note that convention updates for the group are listed in the `#announcements` channel on the [Hanabi Discord server](https://discord.gg/FADvkJp). (You can also review the [commit history](https://github.com/Zamiell/hanabi-conventions/commits/master) of this repository.)

<br />

## Table of Contents

1. [First Principles](#first-principles)
2. [Examples](#examples)
3. [Level 2 - Intermediate Strategies](#level-2---intermediate-strategies)
4. [Level 2 - General Principles](#level-2---general-principles)
5. [Level 3 - Advanced Strategies](#level-3---advanced-strategies)
6. [Level 4 - Expert Strategies](#level-4---expert-strategies)
7. [Level 3 - Variant-Specific Strategies](#level-3---variant-specific-strategies)
8. [Level 3 - Rarely Used Advanced Strategies](#level-3---rarely-used-advanced-strategies)
9. [Level 4 - Rarely Used Expert Strategies](#level-4---rarely-used-expert-strategies)
10. [Convention Attribution](#convention-attribution)

<br />

## First Principles

In general, we want all of our strategies to flow from some basic principles. That way, new players can just learn the first principles, and then use logic and reasoning to find out the resulting strategy that their teammate is intending. However, there are a few wrinkles with this:

1) Some of our strategies are arbitrary and do not flow from the first principles, such as [The 3 Bluff](#the-3-bluff). So take the phrase "First Principles" with a grain of salt.
2) Since the principles are a little abstract, they are more useful as a reference than as an actual guide on how to play Hanabi with our group - this is what the [introductory document](https://github.com/Zamiell/hanabi-conventions/blob/master/Beginners.md) is for.

<br />

### 1. Chop Principle

* The "chop" is the right-most unclued card.
* When a player needs to discard and has no known safe discards, they should discard the chop card.

### 2. Minimum Clue Value Principle

* A given clue must either:
  * indicate sufficient information for **one or more previously unclued** cards to be played
  * prevent the possible discard of a card that needs to be saved

### 3. Save Principle

* Cards that meet the following criteria must not be discarded:
  * only one copy remains (e.g. 5's or unplayed cards in the discard pile)
  * it is a 2 and not visible elsewhere in players' hands
  * it is currently playable and not visible elsewhere in players' hands
* When a card that needs to be saved is at immediate risk of being discarded, it must be indicated with a *Save Clue*.
* A player receiving a clue should give precedence to a *Save Clue* interpretation over a *Play Clue* interpretation.

### 4. Good Touch Principle

* A safe discard is defined as:
  * a copy of a card that has already been played
  * a copy of a card that is in someone's hand and has been clued
* Safe discards should **not** be clued (unless there's an important reason to).
* Players should generally assume that any clued card in their hand will be eventually be played.

### 5. Play Order Principle

* When a *Play Clue* touches multiple cards, if it includes the chop, it's focused on the chop.
* Otherwise it's focused on the newest of the freshly-introduced cards.
* The non-focused cards may or may not be playable.

### 6. Left-Most Playable Principle

* When a player is expected to play a card (or know a card is playable) in a situation not covered by the *Play Order Principle*, the card to be played is the left-most of the various cards that are most likely to be it.

### 7. Information Lock Principle

* What is indicated by a clue is determined by the known information at the time the clue is given. Subsequent clues may build upon that information, but do not override it unless a direct conflict is evident.

### 8. Good Lie Principle

* When a *Play Clue* is given, it's a message that says the card is playable. Sometimes this message can be a lie, in order to usefully manipulate other players.
* Valid lies must not allow for the possibility of any misinformed player to give a conflicting clue or misplay. In simpler terms, this means that good lies almost always reveal themselves on the very next turn.

### 9. High Value Principle

* The highest value clue is expected. If a clue is given, it should be interpreted to be the highest value move available to that player.
* In other words, you can draw many important conclusions from the fact that a player did not do some other (potentially higher-value) move.

<br />

## Examples

Throughout this document, there will be a mix of both text-based examples and graphical screenshots.

In a text-based example:
* The player who goes first will always be Alice.
* The second player will always be Bob.
* The third player will always be Cathy.
* The forth player will always be Donald.
* The fifth player will always be Emily.

(This is a historical convention created by [Keldon Jones](http://keldon.net/) and follows loosely from [cryptography](https://en.wikipedia.org/wiki/Alice_and_Bob).)

A screenshot will look like the following:

![Example Screenshot](img/example.png)

Note that in this user interface, players are holding their hands like they would be if they were playing in real life. For example, in this screenshot, Donald's chop card / right-most card / slot 4 card is the green 5, and Alice's chop card / right-most card / slot 4 card is the yellow 1.

<br />

## Level 2 - Intermediate Strategies

### 2 Saves

* As explained in the beginners guide, *2 Saves* must be given with a number 2 clue.
* Players are not allowed to perform a *2 Save* on a 2 if that same 2 is visible in someone else's hand.
  * The exception to this rule is when the same 2 is on two people's chops at the same time. In that situation, players are allowed to *2 Save* whichever one they want.

### The Fresh 1's Rule

* Sometimes, a player will get clued about a bunch of 1's. As explained in the beginners guide, freshly drawn 1's should always be played before any 1's that were present in the starting hand.
* However, as an important exception, *Chop Focus* overrides the *Fresh 1's Rule*.
* For example, in a 3-player game:
  * No cards are played on the stacks.
  * Alice discards a red 4.
  * Alice gets clued about four 1's on slots 1, 2, 3, and 5.
  * Alice knows that the correct order to play all of the 1's in is 5, 1, 3, 2:
    * Alice knows that normally, you are supposed to play freshly-drawn 1's because playing the 1's that were present in your starting hand. However, *Chop Focus* overrides this rule, so she knows that when the time comes, the slot 5 card (her chop) should play first.
    * After that, she uses the *Fresh 1's Rule*, and play the 1 in slot 1 next.
     * After that, she will play the rest of the 1's from oldest to newest, so she will play slot 3 and then slot 2.

### Prompts in Multi-Color Variants

* In multi-color variants, *Prompts* apply to the card with the most positive information.
* For example, in a 3-player game:
  * Bob is *Prompted* for a red 3.
  * In slot 1, Bob has a card with only a red clue on it.
  * In slot 2, Bob has a card with a red clue and a 3 clue on it.
  * Since slot 2 has more positive information, Bob should choose to play slot 2 as red 3.

### Finesse Position

* As covered in the beginner's guide, a player's *Finesse Position* refers to the slot that their left-most unclued card is in.

### The Prompt + Finesse

* In general, remember that players will always assume *Prompts* over *Finesses*. Thus, is it possible to do a clue that *Prompts* a card from a player's hand **and then** gets them to blind-play their *Finesse Position* card on the next turn.
* For example, in a 3-player game:
  * Red 1 is played on the stacks.
  * Bob has a clued red card in his hand on slot 4.
  * Alice clues Cathy red, which touches a red 4.
  * Bob knows he must have both red 2 and red 3, but he only has one clued red card in his hand. So this must be both a *Prompt* on him and a *Finesse* on him at the same time.
  * Since *Prompts* take precedence over *Finesses*, he plays the clued red card first from slot 4 as red 2.
  * On his next turn, he blind-plays slot 2 as red 3. (His *Finesse Position* at the time of the clue was slot 1, but he drew a card, and now the red 3 slid down to slot 2.)

### The Reverse Finesse

* In a normal *Finesse*, you would give a clue to a player who comes after the player blind-playing a card. If you give a *Finesse* clue to someone who gets to have a turn **before** the blind-play occurs, it is called a *Reverse Finesse*. This is more complicated than a normal *Finesse* and is harder to see.
* Because *Reverse Finesses* exist as a strategy, before playing any cards, players should always check out everyone's *Finesse Position*. If a card in someone's *Finesse Position* is playable and "matches" the clue, then **they need to defer playing the clued card** for at least one go-around and wait to see what happens.
* If the player with the "matching" card blind-plays it, then it means that the clued card is the next card in the chain. For example, on the first turn of a 3-player game:
  * Alice clues Bob red, which touches his red 2.
  * Next, it is Bob's turn. Normally, Bob would think that he had the red 1, and play it immediately.
  * However, Bob also notices that on Cathy has a red 1 on her slot 1 position. Thus, he has to give a chance for Cathy to prove whether or not a *Reverse Finesse* is happening. If Cathy does not blind-play anything, then Bob should have the red 1, and he can play it on his next turn.
  * Bob discards.
  * Cathy blind-plays red 1. Bob now knows that he has the red 2.
* If the player with the "matching card" **does not** blind-play, then the clued card is probably the other copy, and can be played on the next turn. For example, in a 3-player game:
  * The setup is the same as the last example. Bob is clued red, so he suspects a *Reverse Finesse* is occurring and discards.
  * Cathy discards.
  * Now Bob knows that the red card in his hand is actually the red 1.

### Bluffs

* *Finesses* are quite efficient. So, when you see a playable card in someone's *Finesse Position* slot, you will often want to "get" the card with a *Finesse* (instead of cluing it directly). However, often times, the proper "connecting" card is not on the table.
* In this situation, you can perform an alternate strategy by lying to the next player. By cluing an unrelated, one-away from playable card, the next player will think that it is a *Finesse* and that they have the matching card, so they will blind-play their *Finesse Position* card. This is called a *Bluff*.
* After the card is blind-played, the player who received the clue will realize that something strange has happened - the type of clue **did not match** the card that was blind-played. Thus, the clued card is not currently playable and must be a one-away from playable card.
* For example, in a 3-player game:
  * All the 2's are played on the stacks.
  * Alice clues Cathy red, which touches a red 4 as a *Play Clue*.
  * Next, it is Bob's turn. Bob sees that, with this red clue, Cathy has just been signaled that she has the red 3.
  * From Bob's perspective, this looks like a *Finesse* - if Bob does not blind-play the red 3 right now, Cathy will go on to misplay the red 4 as the red 3.
  * Bob blind-plays his slot 1 card. However, it is not the red 3, it was the blue 3! Now Bob knows that he has been *Bluffed* by Alice.
  * Next, Cathy sees that Bob just blind-played a blue 3 immediately after this red clue, so she knows that she must have a one-away from playable red card - the red 4. Cathy holds on to the red 4 for later and discards.
* Except in rare circumstances, ***Bluffing* is only permissible when you are the person directly before the player who is blind-playing a card**. This is called being in *Bluff Seat*. Do not *Bluff* unless you are in *Bluff Seat*! (This follows from *Good Lie Principle*.)

### Bluffs Through Already-Clued Cards

* It is also permissible to *Bluff* "through" cards that are already clued. This is better than a normal *Bluff* because in addition to getting the blind-play, it also gives information to the player with the in-between card.
* For example, in a 4-player game:
  * All the 1's are played on the stacks.
  * Bob has nothing clued in his hand.
  * Cathy has a red 3 clued in her hand with just a number 3 (she does not know what color it is).
  * Alice clues Donald red, which touches one red 4.
  * Bob knows that he must have the red 2. If he plays the red 2, then Cathy will play the red 3, and Donald will play the red 4.
  * Bob plays his *Finesse Position* card and it is instead the blue 2.
  * From Donald's perspective, since blue does not match red, he knows that this is a *Bluff*. Normally, he would think he has the one-away from playable red card, but that would be red 3, and Cathy already has that clued. If he had red 3, then the clue would be violating *Good Touch Principle*. Thus, he must have the red 4 instead.
  * From Cathy's perspective, she knows that the red 4 is two-away instead of one-away. *Bluffs* on two-away cards are normally illegal, so her mystery 3 must be exactly red 3, making the red 4 one-away after all.
* Sometimes, the player who has the in-between card might have more than one "matching" clued card. In this situation, the player is promised that they have the in-between card, but they are not promised the position - it can be any of the matching clued cards.

### Telling the Difference Between a Finesse and a Bluff - Part 1

* Sometimes, a player will give a clue that looks like it could be either a *Finesse* or a *Bluff*. Between these two moves, which should have precedence?
* For example, in a 4-player game:
  * All of the 1's are played on the stacks.
  * Cathy has a blue 2 on her *Finesse Position*.
  * Alice clues blues to Donald, highlighting a blue 3 as a *Play Clue*.
  * Now, it is Bob's turn.
* What to think **depends** on whether you are Bob or whether you are someone else on the team.
* First, let's consider the case of Bob, the very next player. Bob should **always assume a *Finesse* over a *Bluff***. From his perspective:
  * Bob knows that if this is a *Finesse*, then Cathy will blind-play the blue 2, and then Donald will know that he has the blue 3. If this is the case, Bob should not do anything special.
  * Bob also knows that if this is a *Bluff*, then Bob should blind-play his *Finesse Position* card immediately.
  * Bob knows that if there is any way that this could be a *Finesse* (the truth), he should **assume that the truth is being told**. Thus, Bob knows that it must be a *Finesse* on Cathy and should not blind-play anything.

### Telling the Difference Between a Finesse and a Bluff - Part 2

* Let's switch examples and assume that Alice did a clue and then Bob blind-played a card.
* So secondly, we can consider the case of Bob **after** he has blind-played a card, which also extends to the rest of the team. How does everyone know whether Alice did a *Finesse* or a *Bluff* on Bob?
* The way to find out is to look at **whether the card that blind-played "matches" the clue that was given**. If the clue matches, then it is a *Finesse*. If the clue did not match, then it is a *Bluff*.
* If it is ambiguous whether or not the card matches, then the team should **always assume a *Bluff* over a *Finesse***. (Note that this is the opposite of the precedence in step 1!)
* Some common examples:
  * Blue 1 is played on the stacks. Alice clues Cathy about a blue card. Bob blind-plays a blue 2. This must be a *Finesse*, because **blue matches blue**. So Cathy should think that she has the blue 3.
  * Blue 1 is played on the stacks. Alice clues Cathy about a blue card. Bob blind-plays a red 1. This must be a *Bluff*, because **red does not match blue**. So Cathy should think that she has the one-away from playable blue card, blue 3.
  * Rainbow 1 is played on the stacks. Alice clues Cathy about a blue card. Bob blind-plays a rainbow 2. This must be a *Finesse*, because **blue matches blue**. So Cathy should think that she has the rainbow 3.
  * Blue 2 is played on the stacks. Alice clues Cathy about a 4. Bob blind-plays the blue 3. This must be a *Finesse*, because **3 matches 4**. So Cathy should think that she has the blue 4.
  * Blue 2 is played on the stacks. Alice clues Cathy about a 4. Bob blind-plays the red 1. This must be a *Bluff*, because **1 does not match 4**. So Cathy should think that she has the one-away from playable 4, the blue 4. (This is an example of a *Hard Bluff*, which is covered in more detail later.)
* And a final example that is slightly more complicated:
  * Nothing is played on the stacks.
  * Alice clues Cathy about a 4.
  * Bob blind-plays the red 1.
  * This **cannot** be a *Bluff*, because there are no one-away from playable 4's. So even though 1 does not match 4, this must be a *Finesse*, because Alice is not allowed to perform a *Bluff* with any old card that she wants.
  * Cathy does not see any other red cards in Bob's hand. So Cathy should think that she has the red 4, because that would match the blind-play of a red 1. Subsequently, Cathy must have red 2 on her *Finesse Position* and red 3 on her *Second Finesse Position*.

### The Urgency Principle (e.g. How to Tell If Someone Is Finessed)

* Normally, when a *Finesse* or *Bluff* occurs, someone blind-plays right away. This is extremely important, because it resynchronizes the information amongst the team. So, as a group, we always agree to blind-play our cards are soon as reasonably possible. This is called *The Urgency Principle*.
* Thus, if you see that a player does **not** blind-play into the *Finesse* or *Bluff*, then you know that the *Finesse* must be **on you**.
* However, there are some important exceptions:
  1) Players are allowed to **defer** playing into a *Finesse* or *Bluff* if they are doing a *Finesse* or *Bluff* of their own (and no-one else on the team could have done it).
  2) Players are allowed to **defer** playing into a *Finesse* or *Bluff* if they are doing something really important, like saving a 5 on chop, giving a *Play Clue* to a card that is about to be discarded*, or something along those lines.
* So, if any of the above two conditions apply, then you have to **wait** and give the player yet another turn to demonstrate whether or not they will blind-play.

### The Early Game (Intermediate Section)

* The *Early Game* is introduced in the beginner's document. In short:
  * The *Early Game* is defined as the period of time before the first discard happens.
  * Players **must** "extinguish" all of the available *Play Clues* and *Save Clues* on the board before ending the *Early Game*.
* As an intermediate player, you should note that:
  * Misplaying a card **does not count** as ending the *Early Game*.
  * Discarding known trash **does not count** as ending the *Early Game*.
  * Doing special discards that "transfer" cards to other players **does not count** as ending the *Early Game*.
* In order to squeeze as much value out of the conventions as possible, we have some extra rules about "extinguishing" every possible clue:
  * Extinguishing every clue **does** include *5 Stalling*, but it is only mandatory for the team to collectively perform one *5 Stall*. If one *5 Stall* clue has already been given and there is another *5 Stall* clue available, players are allowed (but not required) to clue it.
  * Extinguishing every clue **does not** include cluing something in the hand of the player who came directly before. This is because the player who came before did not see anything for the next player to do, and is therefore giving them "permission" to discard. In this situation, cluing is optional; players can choose to either clue the previous hand or discard at their discretion.
  * Extinguishing every clue **does not** include cluing cards that will be almost certainly be *Order Chop Moved* by an upcoming player who already has two or more 1's clued in their hand. (*Order Chop Moves* are an advanced move that is covered later.)

### 5 Stalls (Intermediate Section)

* As mentioned in the beginner document, *5 Stalls* are when a player clues an off-chop 5 purely because they want (or need) to give a stall clue.
* *5 Stalls* are usually done in the *Early Game*, but they can also be done in the *Mid-Game* if a player is in a special situation where they are not allowed to discard.
* *5 Stalls* are only allowed if there is nothing else to do. (If a player does have something else to do, then it is not a *5 Stall* at all, and is either a *5's Chop Move* or a *5 Pull*, which are advanced moves that are covered later.)
  * However, as an exception, you are also allowed to *5 Stall* if there is **only one** *Play Clue* remaining and it would touch a card on *Finesse Position*. (We refer to this as the *Finesse Position Exception*.)
  * The *Finesse Position Exception* also applies if the same card is in multiple *Finesse Positions* and there is nothing else to do.
* *5 Stalls* **must** be given to the 5 that is closest to chop. For example, in a 3-player game:
  * It is the *Early Game*. The only thing left for Alice to do is to clue an off-chop 5.
  * Bob has two playable 1's on slots 1 and 2. He has a 5 on slot 4. Bob's 5 is therefore one-away from chop.
  * Cathy has nothing clued in her hand. She has a 5 on slot 3. Cathy's 5 is therefore two-away from chop.
  * Alice must clue number 5 to Bob as a *5 Stall* since his 5 is closer to chop (even though Bob has two playable cards).

### The Priority Prompt & The Priority Finesse

* When a player has two or more playable cards to play **and** those cards are different in some way (e.g. not two unknown 1's), everyone agrees that they should be played in a specific order. We refer to this as *Priority*. The agreed *Priority* is as follows:

| Priority | Category of card                                                   | Reason
| -------- | ------------------------------------------------------------------ | ------
| 1        | Blind-plays                                                        | Demonstrating that a *Finesse* or *Bluff* occurred is very important.
| 2        | Cards that *for sure* lead into clued cards in someone else's hand | Otherwise, the team would lose *Tempo*.
| 3        | Cards that *could* lead into cards the player's own hand           | It is bad for a suit to be "held up" on one player.
| 4        | 5's                                                                | Playing a 5 gets the team a free clue.
| 5        | The lower rank card                                                | The smaller stacks are more important to fill up.
| 6        | The left-most card                                                 | The left-most card is more likely to be good.

* When a player does not play the card with *Priority*, they must be trying to send a special message.
* Based on what card they did play, if you have any clued cards in your hand that match the next "connecting" card, it is a message that you can play it right now, similar to a *Prompt*. (The difference is that instead of initiating the *Prompt* with a clue, they initiated it with the order that they played cards.)
* Alternatively, if you do not have any clued cards in your hand that matches the card that they played, then you you should play your *Finesse Position* card as a *Priority Finesse*.
* For example, this would be a *Priority Finesse*:
  * Alice has a known playable red 1 and a known playable blue 2 in her hand.
  * Alice plays blue 2.
  * Bob comes next. Bob does not see any red 2's. He does not see any blue 3's either. Thus, Alice was supposed to play the red 1 first, since red 1 is a lower rank than blue 2. Alice **did not** play the card with *Priority*.
  * This means that Bob must have blue 3. Bob does not have any clued cards in his hand, so he blind-plays his *Finesse Position* card.
* Sometimes, players do not play cards with *Priority* purely in order to give someone else on the team something to do on their turn. For example, this **is not** a *Priority Finesse*:
  * Alice has a known playable red 1 and a known playable blue 2 in her hand.
  * Alice plays blue 2.
  * Bob comes next. Bob does not see any red 2's. Bob does see blue 3 on the chop of Cathy. Thus, even though the red 1 was supposed to have *Priority*, Alice played the blue 2 to give Cathy something to do.
  * Bob clues blue to Cathy as a chop-focus *Play Clue*.
* Similar to a normal *Prompt*, if a *Priority Prompt* could apply to two or more clued cards, then you should play the left-most one.
* Similar to a normal *Prompt*, if a *Priority Prompt* made you play the left-most card and it was not the matching card, then you should continuing playing clued cards until you find the matching card.
* Note that the "left-most" *Priority* is contextual and does not always apply. For example, in the middle of a 3-player game:
  * Blue 1 and blue 2 are played on the stacks.
  * Bob has a red 2 on his chop and is about to discard it. Bob also has a blue 2 in his hand.
  * Alice is forced to clue number 2 to *2 Save* the red 2 in Bob's hand, even though it "picks up" a duplicate blue 2. Alice has no choice, because if she clues reds, Bob will misplay the red 2 as red 1. And she certainly cannot let the red 2 get discarded, because everyone on the team agrees to save all the 2's in a manner similar to 5's.
  * Later on in the game, all of the 1's get played. It is now Bob's turn, and the time has come to play both of the 2's in his hand.
  * From *Good Touch Principle*, Bob knows that both of the 2's in his hand are "good". Since both are the same rank, the left-most 2 should have *Priority*.
  * However, Bob knows that Alice might have been forced to pick up a duplicate 2 in order to save the 2 that was on his chop. Therefore, the chop 2 is certainly good, but the other 2 may or may not be good.
  * Thus, Bob disregards the "left-most" *Priority* and just plays the chop 2 first.
* Normally, blind-playing cards has *Priority* over playing clued cards that lead into other people's hands. However, in some advanced cases, the blind-play does not need to be demonstrated to the team - everyone already has full knowledge of what is going on. In this case, players are supposed to treat the cards as clued for the purposes of finding the *Priority*. (The *Gentleman's Discards* is the main move that this applies to, which is a special move that is covered later.)

### A Priority Flowchart (For Choosing Between 2+ Playable Cards)

*Priority* can sometimes be confusing. [Here is a handy flowchart](https://raw.githubusercontent.com/Zamiell/hanabi-conventions/master/flowcharts/priority_flowchart.png) that shows, in general, which card should be played when there is a choice between two cards.

### The Load Clue

* Players will generally play cards without *Priority* if they see the next card in someone else's *Finesse Position*, because this will get the card for "free" as a *Priority Finesse*.
* Less commonly, players will see the next card in someone else's hand, but it will not be in *Finesse Position*. In these cases, it might still be good to play the card without *Priority*, just so that the player with the next card will have something to do on their turn.
* However, if they do play the card without *Priority*, it will cause an impending misplay because the target player will think the card is actually on their *Finesse Position*. Thus, doing this **forces** someone to give a clue to the card directly in order to stop the misplay.
* This clue is similar to a *Fix Clue*, since it fixes an impending misplay. But we specifically call this kind of clue a *Load Clue* to differentiate it from a *Fix Clue* that fixes a lie or mistake. It is a *Load Clue* because it is loading the player up with something to do on their turn.
* If you receive a *Load Clue*, you should suspect that you might have something valuable on your chop, as this would be an excellent reason to commit the team to giving the *Load Clue* in the first place.
* If a player has a choice between playing one card that leads nowhere and playing one card that commits the team to giving a *Load Clue*, then they are not obligated to choose one or the other - they can choose whichever one is best for the situation.
* When a player receives a *Load Clue*, they are to interpret it as a normal *Play Clue* instead of a *Fix Clue*. For example, in a 3-player game:
  * Blue 1 and red 1 are played on the stacks.
  * Alice has a choice between playing a known blue 2 and a known red 2. The blue 2 has *Priority* because it is the left-most card.
  * Alice plays the red 2.
  * Bob sees that Cathy has the red 3, but it is on her chop instead of on her *Finesse Position*. Thus, Bob must now give a *Load Clue* to stop the impending misplay.
  * Cathy's hand is, from newest to oldest: yellow 4, yellow 3, yellow 4, blue 1, red 3.
  * Bob clues number 3 to Cathy.
  * Cathy is surprised - she was about to play her *Finesse Position* card as red 3, but she now knows that it can't be a red 3.
  * If this was a *Fix Clue*, Cathy might be inclined to play the card that was closest to her slot 1 (which would be the 3 on slot 2).
  * However, Cathy knows that *Load Clues* are to be interpreted as normal *Play Clues* instead of *Fix Clues*, so she interprets this as a normal *Chop Focus Play Clue* and plays red 3 from slot 5.

### Priority in Multi-Color Variants

* Multi-color variants can make finding out which card has *Priority* a little tricky, because sometimes players will know that a card is playable, but not know its exact identity.
* In these situations, players should always assume that the suit of their playable card is the left-most of the possible suits.
* For example:
  * Alice has a known playable red 2 and a known playable blue card that is either blue 1 or rainbow 3.
  * If the blue card is blue 1, then the blue card would have *Priority*, since it would be the lowest rank. But if the blue card is rainbow 3, then the red 2 would have *Priority*, since that would be the lowest rank.
  * However, since the blue stack is the to the left of the rainbow stack, Alice knows that for the purposes of calculating *Priority*, she has to assume that her blue card is the blue 1.
  * Thus, even if Alice really does have the rainbow 3, playing the red 2 will still cause a *Priority Finesse* to occur on the red 3.

### The Trash Chop Move

* In the middle of a game, if all of the 1's have been played already, and someone clues a 1, it is quite strange - from *Good Touch Principle*, players are not supposed to touch cards that have already been played. In this situation, the 1 is considered "trash".
* Thus, the clue must have some deeper meaning. We agree that it means that the cards to the right of the trash are important. The point of the clue was to give the player a known-safe discard.
* However, not only does it give a known-safe discard, but it also *Chop Moves* **all** of the cards to the right of the trash. This means that the player should consider the cards to be touched with an "invisible" clue, and never discard them for the rest of the game.
* Most of the time, the *Trash Chop Move* is done to *Chop Move* a single card (meaning that the clued trash card was one-away from chop). However, you can also use the *Trash Chop Move* to *Chop Move* multiple cards. For example, in a 3-player game:
  * All of the 1's have been played on the stacks.
  * Bob has a completely unclued hand.
  * Alice clues 1's to Bob, which touches a 1 in his slot 1.
  * Bob *Chop Moves* his slot 2, his slot 3, his slot 4, and his slot 5 (a quadruple *Chop Move*).
  * Bob discards the 1.
  * Bob's chop is now his slot 1.
* Once a card has been *Chop Moved* and is no longer in danger of being discarded, it is treated as an already-clued card with regards to new clues given to that hand. For example, in a 3-player game:
  * All of the 1's have been played on the stacks.
  * Bob has a completely unclued hand.
  * Alice clues 1's to Bob, which touches a 1 in his slot 4.
  * Bob *Chop Moves* his slot 5.
  * Bob discards the 1.
  * Bob's chop is now his slot 4.
  * Cathy clues blue to Bob, which touches his slot 1 (the card he just drew) and his slot 5 (the card that was just chop moved).
  * Bob knows that the focus of the clue is always on the brand-new card introduced, so this is **not** chop-focus, and the focus of the clue is on slot 1.
  * Thus, Bob will play blue 2 from slot 1 on his next turn.
* This move is most commonly done with a number 1 clue because it is likely that in the middle of a game, all of the 1's will be already played. But it could also be done with a number two 2 clue if all the 2's are already played / accounted for. Or, it could be done with a red clue if all of the red cards are already played / accounted for. And so forth.
* Strategy wise, the *Trash Chop Move* is used for two main reasons:
  1) Sometimes there are multiple critical cards in a row on chop and it falls to one player to save all of them. In this situation, a multiple-card *Chop Move* could be the only way to do it.
  2) Some cards (e.g. a one-away from playable 3) are quite useful to the team, but illegal to touch directly (as touching them directly with a clue would imply that they are playable right now). If the game is going well, then it can be useful to "waste" a clue in order to have the card saved permanently.
* Note that you are **not** allowed to *Chop Move* a card that you can just clue directly with a *Save Clue* (unless there are multiple critical cards in a row on chop and you have no other choice). This is because having some positive information is always better than having the card be a complete mystery.
* If a *Trash Chop Move* touches **multiple** trash cards, then it only *Chop Moves* the cards to the right of the right-most trash card. For example, in a 3-player game:
  * All the 1's are played on the stacks.
  * Bob has a completely unclued hand.
  * Alice clues 1's to Bob, which touches a 1 in slot 2 and a 1 in slot 4.
  * Bob **only** *Chop Moves* his slot 5 card.

### Chop Moves & Prompts

* There are many different kinds of *Chop Moves*. The most common is the *Trash Chop Move*, but there are others, which are covered later.
* *Chop Moves* interact with *Prompts* & *Finesses* in a potentially confusing way. *Chop Moved* cards should **not** be played into *Prompts*, even though they are imagined to have an "invisible" clue on them. For example:
  * All the 1's are played on the stacks.
  * Bob has no cards clued in his hand, but he is *Chop Moved* for a mystery card on his slot 5.
  * Alice clues Cathy red, which touches a red 3.
  * Bob knows that he is promised the red 2. If this is a *Finesse*, then he has the red 2 on his *Finesse Position* (slot 1).
  * However, Bob is also *Chop Moved* for a card. Bob knows that *Chop Moved* cards have an "invisible" clue around them, and Bob also knows that *Prompts* are said to take precedence over *Finesses*.
  * So should he play his slot 1 as a *Finesse* or his slot 5 as a *Prompt*? In this situation, Bob knows that *Prompts* do not apply to *Chop Moved* cards, so Bob should play his slot 1.

### The 5's Chop Move

* See the *Trash Chop Move* section above for an explanation on what a *Chop Move* is.
* Normally, we are only allowed to save 5's on chop (unless it is the *Early Game* and there is nothing else to do).
* So, in the *Mid-Game*, if a 5 is clued that is not on chop, it will normally look like a *Play Clue* on that 5.
* However, if the 5 is **one-away** from chop (or, if two or more 5's are clued and the right-most 5 is one-away from chop), then we agree that it has a special meaning, and that the clue is **not** a *Play Clue* at all.
* Instead, it is understood that the clue is a *5's Chop Move*, and the player should *Chop Move* in a manner similar to the *Trash Chop Move*.
* Note that the *5's Chop Move* is different than the *Trash Chop Move* in that you can only chop move **one** card with it. Thus, if you clue a 5 and it is **two** (or more) slots away from the chop, then it is to be assumed to be a *Play Clue* on the 5.
* Similar to the *Trash Chop Move*, if a *5's Chop Move* touches **multiple** 5's, then it only *Chop Moves* the cards to the right of the right-most 5. For example, in a 3-player game:
  * All the 1's are played on the stacks.
  * Bob has a completely unclued hand.
  * Alice clues 5's to Bob, which touches a 5 in slot 2 and a 5 in slot 4.
  * Bob **only** *Chop Moves* his slot 5 card.

### The Scream Discard Chop Move (Deliberately Discarding Instead of Playing)

* See the *Trash Chop Move* section above for an explanation on what a *Chop Move* is.
* The *Chop Move* outlined above is a tool to save multiple cards with one clue. However, sometimes you may not have a clue at all. One way to solve this situation is with a special kind of discard.
* Typically, discarding is a last resort. So, if you have a known playable card in your hand, you can send a powerful message to your teammate by discarding instead. This is called a *Scream Discard*. Since your teammate expected you to play the card, it is like screaming at them to let them know that things are very bad.
* The player being "screamed at" should permanently move their chop by one position.
* Furthermore, the player being "screamed at" is not allowed to discard on this turn. They must make some clue. Clues in this situation are treated the same as a *Double Discard Situation* (see *Avoiding Double Discards* below). In short, this means that they are allowed to give "stall" clues, if necessary.
* Players are only allowed to *Scream Discard* for **cards that are playable or critical** (or a needed 2 that isn't seen anywhere else). (This follows from *Save Principle*.)
* Players are **not** allowed to *Scream Discard* for cards that are one-away from being playable.
* Sometimes, a player will discard with a known-playable card in their hand, but they are **not** intending a *Scream Discard* - it is some other special situation:
  1) It is not a *Scream Discard* if the next player **has** to generate a clue for cluing the next player after that. This is called a *Generation Discard*; see below.
  2) It is not a *Scream Discard* when the card that the player did not play was a "blind" card from a *Finesse* **and** the blind card could also be in the next player's *Finesse Position*. When this happens, the next player will usually want to blind-play their *Finesse Position* card, since this sequence of events indicates either an *Ambiguous Finesse* or a *Pass Bluff* (which are both covered later on).

### The Generation Discard

* Usually, if someone has a known playable card and they discard instead of playing that card, this would indicate a *Scream Discard Chop Move*.
* However, if playing the card (player 1) would cause the next player to discard (player 2) and the next player after that (player 3) to have a critical and/or playable card "ride" on chop, it is a very bad situation. Thus, the discard is **just** for the purposes of generating a clue so that player 2 can clue player 3.
* The *Generation Discard* is **only** to be used as a last resort. If player 3 has something else to do (like play a card or give some obvious clue), then player 1 should just play their card and let the card "ride" on chop.

### A Scream Discard Flowchart

[Here is a handy flowchart](https://raw.githubusercontent.com/Zamiell/hanabi-conventions/master/flowcharts/scream_discard_flowchart.png) for determining whether something is a *Scream Discard Chop Move* or a *Generation Discard*. (It also covers some more rare types of discards that are covered later on in this document.)

### Tempo Clues (Re-cluing a Card)

* *Tempo Clues* are defined as clues that touch no new cards. Their purpose is to get 1 or more cards played that already had a clue.
* Note that *Tempo Clues* do not meet *Minimum Clue Value Principle*. They are inefficient, and in Hanabi you want to be as efficient as possible. Thus, we agree that *Tempo Clues* are only allowed in the following special circumstances:
  1. When the tempo clue gets 2 or more cards played
  2. When the card is "out of order" (meaning that it is impossible for a *Prompt* to get the cards played)
  3. When the card was *Chop Moved* and it is now playable
  4. When the clue giver has a fully clued hand
  5. When the clue giver has been *Screamed* at
  6. When the clue giver is in a *Double Discard* situation (see *Avoiding Double Discards* below)
  7. When the clue receiver has a fully clued hand
  8. When the clue receiver is receiving a tempo clue on a card that unlocks someone else's hand
  9. When there are 8 clues in the bank (a forced clue)
  10. When there are 7 clues in the bank (since discarding would take the team to 8 clues, which is generally bad)
  11. When in the *End-Game* / when pace is low
* Since they are so inefficient, *Tempo Clues* that are done outside of these special circumstances are assigned a special meaning. See the *Tempo Clue Chop Moves* section below.
* Sometimes, a *Tempo Clue* can touch multiple cards, which typically means that all of the cards touched are playable. See *The Double Tempo Clue* section below.

### The Tempo Clue Chop Move

* See the *Trash Chop Move* section above for an explanation on what a *Chop Move* is.
* In general, *Tempo Clues* do not follow from *Minimum Clue Value Principle*, which states that a clue must get at least 1 new card played or save at least 1 new card from being discarded.
* Thus, a *Tempo Clue* with no other purpose **must** save at least 1 new card, and the player should *Chop Move* their chop card.
* For example, on the first turn of a 3-player game:
  * Alice clues red to Bob, which touches two cards on slot 1 and slot 2.
  * Bob plays red 1 from slot 1. The red card in slot 2 could be red 2, red 3, red 4, or red 5.
  * Cathy clues number 2 to Bob, which does not introduce any new cards, but it does "fill in" his slot 2 card.
  * Bob now knows that he has exactly red 2 on slot 2 and that this was a *Tempo Clue*. Since it does not get any new cards and only get tempo on one card in total, he knows that he should also *Chop Move* his slot 5 card.
* Naturally, *Tempo Clue Chop Moves* **do not** apply in the special situations listed above where natural *Tempo Clues* are allowed.

### The Double Tempo Clue (Re-cluing 2+ Cards)

* Typically, when a *Tempo Clue* is given that touches two or more cards, it means that **all** of the cards touched are playable in order from left to right.
* For example, on the first turn of a 3-player game:
  * Alice clues red to Bob, which touches slot 1, slot 2, and slot 3.
  * Bob plays red 1 from slot 1. The other two red cards in his hand could be nearly anything.
  * Cathy clues red to Bob, which does not introduce any new cards, but it does re-touch slot 2 and slot 3.
  * Bob knows that this is a *Double Tempo* clue. Both must be playable in order, so he must have red 2 in slot 2, and red 3 in slot 3.
* Note that the normal "play all the cards" interpretation does not apply in some special situations:
  * when the clue unlocks a player's hand
  * when the clue got 2+ cards played in total (using cards in someone else's hand)
  * when the clue touched a *Chop Moved* card; in this situation, **only** the *Chop Moved* card is playable
* As another special exception, the "play all the cards" interpretation does not apply when the second card is strictly not playable. In this situation, all players can see that since only one card is getting tempo, the interpretation of the clue should be a *Tempo Clue Chop Move*. For example, in a 3-player game:
  * Red 1 is played on the stacks.
  * Green 4 is in the trash.
  * Bob has:
    * a red 2 on slot 2 with a red clue on it
    * a red 5 on slot 4 with a 5 clue on it
    * a green 4 on slot 5 with no clues on it yet (on chop and critical)
  * Alice clues red to Bob, which re-touches his slot 2 card and "fills in" his red 5.
  * Bob knows that this is a *Tempo Clue*, and plays red 2.
  * In most cases, since two cards were re-touched, they should both be playable. However, Bob knows that the red 5 is strictly not playable right now. Thus, since the clue did not get any new cards and only got tempo on one card in total, he knows that he should also *Chop Move* his slot 5 card.
* Building on the previous example, if the other players can see that the card being *Chop Moved* is useless (or not very good), it implies a *Finesse* on the touched cards that are not strictly playable right now. For example, in a 3-player game:
  * Red 1 and blue 1 are played on the stacks.
  * Bob has:
    * a red 2 on slot 2 with a red clue on it
    * a red 5 on slot 4 with a 5 clue on it
    * a blue 1 on slot 5 with no clues on it yet (on chop)
  * Alice clues red to Bob, which re-touches his slot 2 card and "fills in" his red 5.
  * Bob knows that this is a *Tempo Clue*, and plays red 2.
  * Cathy sees that if this was a *Tempo Clue Chop Move*, it would be saving the blue 1, which is useless. Thus, for both the red 2 and the red 5 to be playable, Cathy must have both the red 3 and the red 4 on *Finesse Position*.
  * Cathy blind-plays red 3.

### Avoiding Double Discards (Level 2 Stalling)

* If the player before you just discarded a card (say the red 4), and you don't see that card in anyone else's hand, there is a possibility that you could have that same card on your chop. In this example, if you discarded, both red 4's could be lost and your team would not be able to get a perfect score. This is called *Double Discarding*.
* Since *Double Discarding* can "lose" the game, you should never *Double Discard* and give a clue instead! In this situation, if there are no normal clues to give, you are allowed to give "stall" clues; see below.
* Because of this convention, players do not have to be worried about the same card being on two chops in a row.
* Normally, players in *Double Discard* situations are not able to give tricky-looking *Finesses*, because they will be interpreted as a stall instead. However, from *High Value Principle*, you can know that a player in a *Double Discard* situation is **not** giving a "stall" clue if there is some other better clue available for them to give. Thus, players in *Double Discard* situations are still often able to make *Finesses* happen. See the priority column of the below table for an explicit ranking of what constitutes a "better" clue.
* One common way of stalling in a *Double Discard* situation is to do a *5 Stall*. Note that the *Finesse Position Exception* applies to both *5 Stalls* in the *Early Game* and *5 Stalls* in *Double Discard* situations.

### Allowable Stall Clues

* In certain special situations, everyone understands that a player might be giving a "stall" clue. However, there are limits - they are not allowed to just clue anything they want. These are the specific clues that they are allowed to give along with the priority of each clue:

| Priority | Type of Clue | Early Game (Level 1) | Double Discard (Level 2) | Locked Hand (Level 3) | 8 Clues (Level 4)
| -------- | ------------ | -------------------- | ------------------------ | --------------------- | -----------------
| 1        | Normal *Play Clues* or *Save Clues*                                                  | ✔ | ✔ | ✔ | ✔
| 2        | *5 Stall* (cluing off-chop 5's)                                                      | ✔ | ✔ | ✔ | ✔
| 3        | Early *Fix Clue* (fixing a duplicate before it is in danger of misplaying)           | ❌ | ✔ | ✔ | ✔
| 4        | *Tempo Clue* (re-cluing a card to make it play)                                      | ❌ | ✔ | ✔ | ✔
| 5        | *Locked Hand Save* (saving any card on chop)                                         | ❌ | ❌ | ✔ | ✔
| 6        | *8 Clue Save* (saving any card off chop)                                             | ❌ | ❌ | ❌ | ✔
| 7        | Filling in extra info on unplayable "mystery" cards                                  | ❌ | ✔ | ✔ | ✔
| 8        | *Hard Burn* (re-cluing an unplayable card that gives no new information, usually a 5) | ❌ | ✔ | ✔ | ✔

### Locked Hands & The Locked Hand Save (L.H.S. / LHS) (Level 3 Stalling)

* Generally speaking, it is a bad situation when someone's hand gets fully clued. This is also known as being *Locked*, and it should be avoided if possible. However, sometimes it cannot be helped, like when a player draws three 5's in a row.
* A player with a fully clued hand may give a low-value clue because they are not sure that they can play anything (and they can't discard because their hand is fully clued). Similar to a *Double Discard* situation, players should not read too closely into any clues given during this state.
* If the team is out of clues and someone's hand is fully clued, then you **have** to discard to generate a clue for them. Similarly, if there is only 1 clue left, you cannot steal it from them.
* Players with a *Locked Hand* gain the special ability to save any card on chop. This is called a *Locked Hand Save* if it saves a card that would otherwise not be legal to save (like some one-away from playable card that is not in the discard pile yet). However, players can only do *Locked Hand Saves* if there are no higher priority clues available. See the "Allowable Stall Clues" section above.

### The Anxiety Play (Forcing a Locked Player to Play)

* Sometimes, someone with a *Locked Hand* has a playable card, but they do not know that they can play it yet. Re-cluing the card would signal this, but that would waste a clue and not be very efficient.
* A better way to signal this information is to deliberately leave them at 0 clues. By convention, this means that one of their cards is actually playable. If there is more than one option, then they should know that the left-most is playable. (This follows from *Left-Most Playable Principle*.)
* This is called an *Anxiety Play* because you are putting the *Locked* player in a "do or die" situation.

### Clues Given While at 8 Clues & The 8 Clue Save (Level 4 Stalling)

* At the beginning of the game, you start with 8 clues. This section only applies to situations where you climb to 8 clues in the middle of the game.
* A player who has a turn with 8 clues in the bank may give a low-value clue because they are not sure that they can play anything (and they can't discard because the game does not allow you to discard while at 8 clues). Similar to a *Double Discard* or a *Locked Hand* situation, players should not read too closely into any clues given during this state.
* Players at 8 clues gain the special ability to save any card that they want, on **or** off chop, as long as the card is not freshly drawn. This is called an *8 Clue Save*. However, similar to a *Locked Hand Save*, they can only do this if there are no higher priority clues available. See the "Allowable Stall Clues" section above.

<br />

## Level 2 - General Principles

This section is unique in that it contains things that are separate from actual moves and strategies. We refer to them in post-game reviews when thinking about the game.

### Misplay Cost Principle

* On a turn where a player misplays and accumulates a strike for the team, they could have discarded instead and generated a clue.
* So, if you can spend one clue to stop one misplay, the value comes out even.
* Thus, since there are only 2 strikes allowed and accumulating strikes limits flexibility, it is almost always worth it to spend one clue to stop one strike.
* If it would require two clues to stop an impending misplay, then as long as the strike would not lose the game, it is usually best to let the player misplay the card and get a strike.

### Stomping on a Finesse

* This is when a player clues a card directly that was going to be blind-played from a *Finesse*. Typically, this is a mistake, and it means that the player who gave the clue was not paying attention and failed to see that a *Finesse* happened at all.

### Lines

* During your turn, part of figuring out the best move involves looking into the future to see what the next player will do. If they discard, will it be okay? Is there some obvious clue that they will do? And so on.
* As you get better at Hanabi, you will need to do this prediction not just for the next player, but for an entire go-around of the table. And as you really get good at Hanabi, you will need to do this for as far in the future as you can reasonable predict. (Sometimes, this means 15 moves or more in the future.)
* Similar to chess, initiating a move in which you can predict the next sequence of moves is called initiating a "line".
* In post-game reviews, we will often compare and hypothetically "play through" two different lines to see which one is better.

### Bluff Seat and the Pang of Guilt

* As mentioned in the section on *Bluffs*, you are in *Bluff Seat* for a certain player if you are immediately before them.
* Before cluing a card directly, you should first consider if it is on *Finesse Position*. If it is, and you clue it directly, you may be "stealing" someone's *Finesse* or *Bluff*.
* Thus, in this situation, it may be better to discard and let the player in *Bluff Seat* get the card. If you do decide to clue the card directly, you should always feel a *Pang of Guilt*.

### Discard Modulation

* Often times, either you or the player who comes after you can perform a clue. And the clue would have the same result if done by either player. So who should do it?
* One way to decide is to look at the next player's chop. Is their chop high-value, low-value, or useless? If it is high-value, then you should discard and let them give the clue. If it is low-value or useless, then you should give the clue and let them discard.
* "Stealing" clues in this way is called *Discard Modulation*. If other players are discarding to let you give all of the clues, you probably have a high-value chop.

### One-Away From Playable

* In general, 3's are pretty high value, and 4's are pretty low value.
* But combined with this, cards that are one-away from playable are pretty high value, and cards that are two-away (or more) are pretty low value.
* Thus, in some situations, a one-away 4 may be more valuable than a two-away 3.
* According to our conventions, it is illegal to clue a one-away card directly without it being some kind of special move like a *Finesse* or *Bluff*. However, sometimes we still want to "save" these cards. Thus, they are prime targets for indirect saves like the *Trash Chop Move* or the *5's Chop Move*.
* However, in most cases, *Chop Moving* the valuable card just won't be possible. So in general, you should try to construct lines that protect high-value cards from being discarded for as long as possible.

### The All 4's Test

* According to *Save Principle*, the team must not let any critical and/or playable cards be discarded. So part of constructing a line is figuring out whether this might happen.
* When considering a line, it is not safe to assume that a player will clue anything in your hand. You should perform the *All 4's Test*: what would everyone do if I have all useless 4's in my hand? If a critical and/or playable card would get discarded, then the line has failed the test, and it is probably a bad idea.

### Schrödinger's Cat Principle

* Often times when you are given a clue, the card could be two or more things. For example:
  * In a no-variant game, a red *Play Clue* might indicate a red 2 or a red 3 depending on whether or not red 2 will blind-play from someone else's hand.
  * In a rainbow-game, a red clue might indicate either a *Play Clue* on a red 1 or a *Delayed Play Clue* on a rainbow 2 through another player's yet-to-be-played rainbow 1.
* After getting a clue, you should immediately mark all of the possibilities down on the card as a note.
* For all of your subsequent turns, you have to treat that card like it is **all of the possibilities** at the same time. This is a lot like the *Schrödinger's Cat* quantum physics analogy, which states a cat is both alive and dead at the same time, and you won't know until you actually open the box and look. Similarly, treat the unknown card as all the possibilities, and you won't actually know until the card is played.
* The implications of *Schrödinger's Cat Principle* is that players must be very careful - before playing a card, they will often have to wait for everyone else to have a turn to allow for the possibility of a *Prompt*, *Reverse Finesse*, and so forth.

### Clue Interpretation Priority & Occam's Razor

* When a clue could have multiple interpretations, usually *Schrödinger's Cat Principle* is involved - players must wait a round and see what their teammates do in order to find out the true meaning of the clue. But what if a clue could have multiple interpretations and a player does **not** have to wait for information from anyone else?
* In this situation, players should use *Occam's Razor* - always assume the simplest possible interpretation:
  * First, assume a *Play Clue* or a *Delayed Play Clue*.
  * If that is impossible, assume a *Prompt*.
  * If that is impossible, assume a *Finesse*.
  * If that is impossible, assume a *Bluff*.

### Team Distribution Principle

* In general, it is better for useful cards to be distributed **evenly** throughout the team. This is especially important in 5-player games.
* Thus, if one of your teammates has 3 out of 4 cards clued, it may be better for **them** to be the one giving the clues, and you to be the one discarding - even if their chop is known trash.
* There are multiple reasons for this. First, you don't want them to get a *Locked Hand*, which is generally bad. Second, if they continue to draw playable cards, the game may end before they get a chance to play them all.

### End-Game Threshold (End Game)

* Towards the end of the game, the strategy of the team will change. In most games, you stop becoming concerned with efficiency and become more concerned with tempo - every card needs to play **right now** before the game ends!
* Thus, since clues can mean different things depending on whether you are in the *Mid-Game* or the *End-Game*, you need to be able to keep track of when the *End-Game* has arrived.
* A value called *Pace* is used to determine *End-Game* status. *Pace* is calculated by the following formula: `current score + cards in deck + number of players - maximum score`
  * On [Hanabi Live](https://hanabi.live), the user interface will calculate this for you on the right side of the screen.
* Pace is essentially the maximum amount of discards that can happen while still having a chance to get the maximum score.
* If pace is **less than the number of players**, the *End-Game* has arrived.
  * On [Hanabi Live](https://hanabi.live), pace will turn yellow when this occurs.
* If pace is **less than the number of players / 2**, you should be very careful with discarding. It might still be the best thing to do, but if there are enough clues in the bank, it is usually better to *Burn* a clue (meaning to deliberately waste a clue).
* If pace is 0, no more discards can happen in order to get the maximum score.
* If pace is below 0, it is impossible to get the maximum score.

### The Pace +1 Rule

* Players can use *Pace* to determine if it is safe to discard. In general, a group can discard down to pace 0 and still get a perfect score.
* However, as a rule, if pace is +1 and one of the players on your team **does not** have any playable cards, then you cannot discard - **you must let them perform the final discard**.
* If both you and another player do not have any playable cards, then you can do the final discard - the team won't be able to get a perfect score anyway. But if you you **could** have an unknown useful/playable card in your hand, then you should be very careful about discarding, because it could ruin a perfect score.

<br />

## Level 3 - Advanced Strategies

### The Double/Triple/Quadruple Prompt

* Sometimes, someone can give a *Prompt* that is prompting **two** (or more) cards with one clue, which is pretty efficient.
* For example, in a 3-player game:
  * A red 1 is played on the stacks.
  * Alice clues Cathy red, which touches a red 4.
  * Bob has two clued red cards in his hand. Since the red 4 is playable right now, he knows that his two red cards must be a red 2 and a red 3 (in order from left-to-right).
  * Bob plays both of them.

### The Double/Triple/Quadruple Finesse

* Typically, *Finesses* are performed by cluing a one-away from playablecard. However, it is possible to get two different people to blind-play their cards in a row if you give a clue to a card that is two-away from being playable. This is very efficient, as it is a 3-for-1 clue.
* For example, in a 4-player game:
  * A red 1 is played on the stacks.
  * Alice clues Donald red, which touches a red 4.
  * Bob plays red 2 from his *Finesse Position*.
  * Cathy plays red 3 from her *Finesse Position*.
  * Donald plays red 4.
* Similarly, it is possible to get a single player to blind-play 2 cards in a row. In this situation, since they see that the blind cards are not in anyone else's hands, they will blind-play two turns in a row, playing from left to right.
* For example, on the first turn of a 3-player game:
  * Alice clues red to Cathy, touching a red 3.
  * Bob blind-plays red 1 from slot 1.
  * Cathy would normally think that she has red 2, which would match the red 1 that was just played. However, she sees that when the clue happened, there was a red 2 next to the red 1.
  * Thus, Cathy discards, giving Bob the chance to blind the play the red 2. If he does not blind-play it, then it was a normal *Finesse* and she has red 2. If he does blind-play it, then it was a *Double Finesse* and she has red 3.
  * On his next turn, Bob blind-plays red 2 from slot 2. Cathy now knows she has the red 3.

### The Ambiguous Finesse

* Sometimes, the player that is supposed to blind-play a card into a *Finesse* is ambiguous. For example, in a 4-player game:
  * Nothing is played on the stacks.
  * Alice clues Donald about a red 2 as a *Play Clue*.
  * Both Bob **and** Cathy have red 1 on their *Finesse Position*.
  * Bob will think that it is a *Reverse Finesse* directed at Cathy, and he will discard.
  * Next, Cathy thinks that Bob made a mistake and "missed" the *Finesse*. Cathy discards.
* Here, Cathy is actually the one making the mistake. It follows from *High-Value Principle* that you should never assume that your teammates are making a mistake. If Bob is discarding, then it means that Cathy also has the exact same copy of the card, and Cathy should immediately blind-play.
* From Cathy's perspective, it is also possible that Bob is performing a special move called a *Pass Bluff* (which is covered later on in the document).

### The Ambiguous Finesse Pass-Back

* When an *Ambiguous Finesse* occurs, one person will hesitate, not playing into the *Finesse*. Once that happens, it is usually clear that someone else on the team also has the matching card. Next, the other person should **immediately blind-play**, resolving the *Ambiguous Finesse* as fast as possible.
* However, in some specific situations, the next person **cannot** blind-play the card, or else a misplay would occur. In these situations, the second person has to **also** hesitate, "passing" the blind-play back to the first person again.
* For example, in a 4-player game:
  * Blue 1 is played on the stacks.
  * Alice clues blue to Donald, touching a blue 4 as a *Play Clue*.
  * Bob sees that Cathy has the blue 2 on her *Finesse Position*. From his position, this must be a *Double Finesse*, with Cathy blind-playing the blue 2, and Bob blind-playing the blue 3 from his own *Finesse Position*. Bob discards.
  * Cathy sees that Bob has the blue 2 on his *Finesse Position* and the blue 3 on his *Second Finesse Position*.
  * Cathy also knows that the only reason that Bob would discard is if Cathy **also** had the blue 2 on her *Finesse Position*. Thus, Bob expects her to blind-play on this turn, and this is an *Ambiguous Finesse*.
  * Normally, Cathy would blind-play the blue 2 herself. However, in this situation, if she blind-plays the blue 2, then Bob would go on to misplay the other blue 2, thinking that it is blue 3.
  * Thus, Cathy must pretend like the *Finesse* is not on her all, and force Bob to be the one to blind-play first. Cathy discards, passing the *Finesse* back to Bob.
  * Donald and Alice discard.
  * Bob knows that Cathy was supposed to blind-play the blue 2, but she didn't. He must also have the blue 2. Furthermore, he must also have the blue 3, as that would be an excellent reason for Cathy to pass the *Finesse* back to him. Bob will now blind-play blue 2 and blue 3.

### The Positional Discard (Indicating a Play with a Discard)

* Near the end of the game, if you have no clues left and no cards to play, you can transmit information based on which card you discard.
* Thus, you can discard the slot in your hand that matches the slot in someone else's hand that they are supposed to play.
* Usually, players will only do this if they can see all of the remaining useful cards. Since they see everything, they know that they cannot be discarding anything important.

### The Positional Misplay (Indicating a Play with a Misplay)

* On the final round of the game, if a player has no cards in their hand to play, a *Positional Discard* from **any** slot will work, because it is globally known that every card is visible.
* However, sometimes *Positional Discards* are done before the final round while there are still some cards left in the deck. In this situation, if a player discarded their chop card as a *Positional Discard*, this would not work, because discarding chop is the normal action that the rest of the team is expecting.
* Thus, in order to more strongly communicate the "play this slot" message, they can instead misplay their chop card. Since the rest of the team can see that the card misplayed for "no reason", they can deduce that it was a *Positional Misplay*.

### The Double Positional Misplay (Indicating Two Plays with a Misplay)

* Normally, the *Positional Misplay* is only used as a last-resort when a *Positional Discard* would not work. But what if a player does a *Positional Misplay* when a normal *Positional Discard* would have gotten the job done?
* *Positional Discards* and *Positional Misplays* promise that only one card in the specified slot is playable. So, if there are **two** people with a play on the same slot, then it will be ambiguous, because each of them will think that the other person is supposed to play.
* Thus, a *Positional Misplay* that is unnecessary transforms into a *Double Positional Misplay*, indicating to the team that **two** cards on that exact slot are playable.

### The Hidden Finesse

* Sometimes, you want to *Finesse* someone with a clued card already in their hand. However, if you try to *Finesse* them, they will assume it is a *Prompt* and will misplay their clued card, so it doesn't work out.
* However, what if the clued card actually is playable? That means you can still do the *Finesse* - they will play the *Prompted* card, see that it wasn't the card you had intended, and then blind-play their 2nd newest card on the next turn. This is called a *Hidden Finesse* because the *Finesse* was temporarily hidden by the presence of clued card.
* For example, in a 3-player game:
    * Red 1 and rainbow 2 are played on the stacks.
    * Alice clues red to Cathy, which touches her red 3.
    * Bob has a rainbow 3 clued as red in his hand and he has no idea what it is.
    * Bob sees that Alice's clue must be a *Prompt*, so he plays his red card as red 2. He is surprised to see that it is actually rainbow 3.
    * Bob knows that he really must have the red 2, and it must have been on *Finesse Position* when Alice originally gave the clue. Since he just drew a card after he played the rainbow 3, he now knows that the red 2 is on his slot 2 (the second-newest card).
    * On Bob's next turn, he blind-plays his the red 2 from slot 2.
    * In this example, the red 2 was "hidden" by the rainbow 3.

### The Layered Finesse

* Normally, if a red card is clued and someone blind-plays a blue card, it would be some kind of *Bluff*. However, we only allow players to perform a *Bluff* on the very next player. (This is referred to as sitting in *Bluff Seat*.)
* It follows from this that if an unrelated card is blind-played, and it cannot be a *Bluff*, then it must be a special kind of *Finesse*.
* Normally, a *Finesse* promises the exact copy of the card on *Finesse Position*. However, as long as all of the cards leading to the card are playable, you can still promise the exact copy of the card. With respect to *Good Lie Principle*, we don't count this as a "lie", since the blind-playing player does indeed have the true copy of the card.
* We call this a *Layered Finesse* because the intended *Finesse* blind-play target is "layered" behind other playable cards.
* For example, in the following screenshot:
  * SedNegi clues yellow 3, which is a signal that it is playable right now.
  * 910dan comes next. At first glance, this might be a *3 Bluff*, since SedNegi used number 3. However, *Finesses* take priority over *Bluffs*, and since it could be a *Layered Finesse* on Zamiel, then it cannot be a *3 Bluff*.
  * 910dan therefore assumes that it is a *Layered Finesse* on Zamiel and clues blues to SedNegi, which is a *Play Clue* on blue 1.
  * Zamiel sees the yellow 2 on 910dan's *Finesse Position*. Thus, it would make the most sense for SedNegi's clue to be a *Double Finesse* on yellow 1 and yellow 2. Zamiel blind-plays his *Finesse Position* card, expecting it to be yellow 1. Instead, it is purple 1. Zamiel now thinks that SedNegi's initial clue was touching a purple 3 to initiate a *Double Self-Finesse* on purple 1 and purple 2.
  * SedNegi plays blue 1.
  * 910dan now knows that it was indeed a *Layered Finesse*, and that he has the yellow 2 on his *Finesse Position*. But he has to wait for the yellow 1 to come down first before he can play it. So, he clues purple to Zamiel, which is a *Play Clue* on purple 2.
  * Zamiel now has negative purple on his 3, which means that it must be yellow 3 after all. He now understands that SedNegi's original clue was a *Layered Finesse*. Zamiel blind-plays yellow 1 from slot 2.
  * SedNegi clues 1's to 910dan, which touches two 1's.
  * 910dan blind-plays yellow 2 from slot 1.
  * Zamiel plays yellow 3.

![Layered Finesse](img/layered_finesse.png)

### The Paused Priority Finesse

* For the purposes of *Priority*, blind-playing a card is the most important thing to do. When players are supposed to be blind-playing a card, they are usually **not** allowed to perform a *Priority Finesse* - they must stick to playing the blind card.
* One exception to this is if a player is in the middle of unraveling the layer of a *Layered Finesse*. Since they have already blind-played their first card in the layer, they have demonstrated that the *Finesse* was on them, and now everyone on the team knows that the rest of the cards inside of the layer are "gotten" for sure.
* Thus, in this situation, a player can "pause" finishing up the *Layered Finesse* and play some other clued card to perform a *Paused Priority Finesse*.

### The Sarcastic Discard

* Occasionally, through a mistake (or complicated situation), the same card will be clued in two different people's hands. Generally, this is to be avoided, but sometimes it happens. Handling this can be tricky.
* Generally, the **first** player who fully realizes that they have the duplicate card should discard it (as opposed to playing it or holding on to it). This is called a *Sarcastic Discard*, and it communicates to the other player that they 100% have the discarded card.
* For example, in a 3-player game:
  * On the stacks, red 2 is played.
  * Alice has one red 3 clued in his hand with just number 3.
  * Alice clues number 3 to Bob, which touches one 3. (This is a mistake, because it might be violating *Good Touch Principle*.)
  * Bob knows that the only playable 3 is red 3. He also knows that Alice has a clued red 3 already in her hand. Thus, he knows that he has the red 3 and that Alice made a mistake.
  * Bob performs a *Sarcastic Discard* to pass the red 3 back to Alice.
* The *Sarcastic Discard* is similar to the *Prompt*, except that it is initiated by a discard instead of a clue.
* However, unlike a *Prompt*, if there are multiple cards that a *Sarcastic Discard* could apply to, then it does **not** promise that it is the left-most card. It only promises that they have the card somewhere. For example:
  * Alice *Sarcastic Discards* a red 3.
  * Bob has two cards clued with number 3 in his hand. He doesn't have any color information on either 3.
  * Bob can be certain that one of the two 3's is red 3, but he does not know which one it is yet.

### The Sarcastic Finesse

* Imagine that in a 3-player game:
  * Nothing is played on the stacks.
  * Alice has an already-clued 2 in her hand. She has no idea what color 2 it is.
  * Alice performs a *Finesse* by giving a red color *Play Clue* to a red 2 in Cathy's hand.
  * Bob blind-plays red 1 from his *Finesse Position*.
  * Normally, Cathy would think that she has the next red card, which is red 2, and play it.
  * However, what if Alice actually has the red 2? In this situation, Cathy is expected to perform a *Sarcastic Discard*.
* Doing a *Finesse* that potentially duplicates a card in this way is called a *Sarcastic Finesse*. Normally, potentially duplicating a card is bad - it violates *Good Touch Principle* and could lead to a clue being wasted. However, potentially duplicating a card with the *Sarcastic Finesse* is not bad because:
  * In the best case, you get a "true" *Finesse* (a 2-for-1 or better).
  * In the worst case, you get a 1-for-1 and full knowledge on a clued card in your own hand that was previously a mystery.

### The Gentleman's Discard

* The *Sarcastic Discard* is very similar to the *Prompt*, because it gets someone to play a card that already had a clue on it. It is also possible to intentionally discard a known card in order to get someone to blind-play a card, similar to a *Finesse*. 
* When this occurs, it is called a *Gentleman's Discard* to signify that the card played was completely blind as opposed to having a clue on it already.
* For example, on the first turn of a 3-player game:
  * Alice clues number 1 to Cathy, touching one 1.
  * Bob clues red to Cathy, filling in the already-touched 1 as red 1, as well as touching a new card, which must be red 2.
  * Cathy discards the known red 1 as a *Gentleman's Discard*.
  * Alice blind-plays her *Finesse Position* card as red 1.
* The *Gentleman's Discard* essentially transfers a card to another player on the team. However, often times, doing this will delay things and cost the team *Tempo*. Thus, a *Gentleman's Discard* that slows things down is only good if there is some other side benefit to offset the lost *Tempo* (such as delaying the discard of a valuable card, for example).
* For the purposes of *Priority*, *Gentleman's Discards* do not count as a blind-play. This means that if there is a playable clued card that leads into someone else's hand, then it should have priority over the blind-play from the *Gentleman's Discard*. (This is because the *Gentleman's Discard* is an information-symmetric move and nothing needs to be "proven" to other members of the team.)

### The Baton Discard

* Usually, when a *Gentleman's Discard* happens, it is for a playable card. But it is also possible to do a *Gentleman's Discard* to transfer a card to another player that is just completely unplayable at the current time.
* In order to disambiguate this from the more ordinary type of *Gentleman's Discard*, we call this a *Baton Discard*.
* *Baton Discards* are mostly useful for two main reasons:
  1) To better satisfy *Team Distribution Principle*. It makes sense to transfer a card out of a locked / almost locked hand to a player with an "empty" hand or a hand that only has one card clued in it.
  2) You want to protect your own chop. If you discard your chop, the team could be losing some high-value one-away from playable card. But if you transfer a card to someone else, it gives you something "safe" to do.

### The Certain Finesse / The Certain Discard

* Imagine that in a 3-player game:
  * Red 2 is played on the stacks.
  * Alice has an already-clued red card in her hand. It has a negative 4 clue on it, so from *Good Touch Principle* Alice knows that it is either red 3 or red 5.
  * Alice performs a *Reverse Finesse* by giving a red color *Play Clue* to a red 4 in Bob's hand.
  * Bob discards.
  * Cathy knows that she is promised the red 3 in her *Finesse Position*.
* This is an example of a *Certain Finesse* - it is similar to the *Sarcastic Finesse* above, but the "blind" card was potentially duplicated instead of the clued card.
* In this situation, if Alice really has the red 3, Cathy is allowed to blind-discard their *Finesse Position* card. This is called a *Certain Discard*, because Cathy can be certain that it is exactly red 3.
* A separate way to explain this convention is that everyone agrees that performing a *Layered Finesse* on a card that could potentially be clued in your own hand is illegal. So, everyone can be certain that they can safely blind discard a card to pass it back to someone who potentially duplicated. (*Layered Finesses* are an advanced type of *Finesse* that was explained above.)
* Note that players are **only allowed** to do a *Certain Discard* if they know they have not been *Bluffed*. This means that *Certain Finesses* **cannot be performed** from *Bluff Seat*.
* For example, in a 3-player game:
  * Red 2 and blue 3 are played on the stacks. Blue 4 is in the discard pile.
  * Alice has an unknown 3 in her hand that happens to be the red 3.
  * Alice clues number 4 to Cathy, touching a red 4 as a *Play Clue*.
  * Bob knows that Alice could be trying to perform a *Finesse* on a red 3. Normally, he would blind-discard his *Finesse Position* card as a *Certain Discard* in order to pass this card back to Alice.
  * However, Bob **also** knows that you are not allowed to perform a *Certain Discard* from *Bluff Seat*. In other words, there are other possibilities for this move - it could also be a *Bluff* on the blue 4. If he blind-discarded, that could "kill" the blue stack, since the other copy of blue 4 is already discarded.
  * Bob blind-plays his *Finesse Position* card and it is the blue 4. Good thing he did not discard the card!

### The Early Fix Clue Chop Move

* As noted in the *Fix Clues* section, a *Fix Clue* is required before a misplay occurs on duplicated cards. But usually, the misplay will not occur until late in the game, because there is always some other extra card (that is not currently playable) that it could be.
* Thus, if other urgent things are at hand, you can usually defer giving some *Fix Clue* for a long time and hope that through ancillary information and the context of the game, the player will "naturally" figure out that the card is duplicated.
* So if a *Fix Clue* is given early to you, it can be strange. You were happily discarding, and now all of a sudden you are being fixed on a card that was just sitting in your hand and was not in danger of being misplayed.
* This usually means that your chop suddenly became important, so the *Fix Clue* was given early to give you a good discard and keep you occupied. Thus, you should permanently chop move one card.

### The Order Chop Move & The Skipped Order Chop Move

* Normally, at the beginning of the game, players are expected to play their 1's from right to left.
* If a player skips over their right-most 1, and there is nothing else special going on, it means that the next player should *Chop Move* one card.
* If a player skips over **two** of their right-most 1's, the message skips over the next player, and the player after that should *Chop Move* one card. (And a skip of three 1's means that the player three seats away should *Chop Move*.)
* For example, in a 3-player game:
  * It is the first turn of the game.
  * Alice clues Bob number 1, which touches three 1's. They are in slots 1, 2, and 3.
  * Bob is expected to play slot 3 (which is the oldest 1). If he plays slot 3, nothing special happens.
  * If Bob plays slot 2, he is performing an *Order Chop Move*, and Cathy should chop move one card (her slot 5).
  * If Bob plays slot 1, he is performing a *Skipped Order Chop Move*, and Alice should chop move one card (her slot 5).
* There are some common special situations that do **not** imply an *Order Chop Move*:
  * The 1 had priority from the *Fresh 1's Rule*.
  * The 1 that was played was originally *Finessed* from a clue that happened **before** the number 1 clue.
  * The 1 that was played was not **exactly** the same as the other 1's. Any positive or negative information "turns off" *Order Chop Moves*.
  * The 1 that was skipped over is known to be bad from contextual information. (See *The Stale 1's Clue* section.)

### Double Order Chop Move (for 3-Player Games)

* This convention only applies to 3-player games.
* In the *Order Chop Move* and the *Skipped Order Chop Move*, players can play 1's in a certain order to *Chop Move* a specific player of their choosing.
* In a 4 or 5-player game, skipping over three 1's would *Chop Move* the player three seats away. However, in a 3-player game, this would be nonsensical, since there are only 3 players in total.
* Thus, in a 3-player game, skipping over three 1's should *Double Chop Move* the very next player.
* In the rare case where four things are skipped over, it should skip over the next player and *Double Chop Move* the player after that.

### Trash Order Chop Move

* Sometimes, a player will have two known trash cards in their hand (and these cards are explicitly known trash, meaning that everyone on the team can equally see that they are known trash).
* In this situation, the player is expected to discard the newest (left-most) trash card.
* Thus, if a player skips over their newest trash card and instead discards the second newest trash card, they must be trying to communicate something extra.
* This means that the next player should *Chop Move* (in a manner similar to a *Order Chop Move*).
* Note that a player is not necessarily trying to perform a *Trash Order Chop Move* if the two trash cards have different kinds of clues on them. For example, by discarding specific trash cards, it can communicate that the player "sees" all of the non-trash possibilities of that card.

### The Misplay Chop Move

* Sometimes, a desirable card is on the next player's chop and it is not directly cluable. In this situation, players can cleverly use the various kinds of chop moves in order to save the card (e.g. *Trash Chop Move*, *5's Chop Move*, *Tempo Clue Chop Move*, and so forth).
* However, none of these chop moves may be available to perform. In such a situation, you can revert to the final type of chop move - the *Misplay Chop Move*. This is done by intentionally touching a card in the next player's hand that signifies that it is currently playable. The next player will misplay, and then they will know that every card to the right of the misplayed card is valuable and is now permanently chop moved.

### The 3 Bluff

* Typically, the player who receives a clue that causes a *Bluff* blind-play knows that the card that was clued is one away from being playable.
* Our group plays with an artificial *3 Bluffs* convention. This means that in addition to being one away from being playable, we agree that the touched card can also be any 3 that will be useful in the future.
* Here are some examples that cover the four most common *3 Bluff* situations:
    * **Color mismatch (valid):**
      * On the first turn of the game, Alice clues Cathy red, which touches a red 3.
      * Bob blind-plays blue 1.
      * Cathy knows that it is either a red 2 (if it was a normal *Bluff*) or a red 3 (if it was a *3 Bluff*). She marks down both of the possibilities for later.
    * **Number 3 with suit mismatch (valid):**
      * On the first turn of the game, Alice clues Cathy number 3, which touches a red 3.
      * Bob blind-plays blue 1.
      * Cathy knows that it was a *3 Bluff*, because a played 1 does not "match" number 3.
      * Beyond that, Cathy knows nothing about the card, besides that it is a 3 (since it has a number 3 clue on it).
    * **Color match (NOT valid; looks like a Double Finesse):**
      * On the first turn of the game, Alice clues Cathy red, which touches a red 3.
      * Bob blind-plays red 1.
      * Cathy sees that Bob does not have red 2. Since red matches red, Cathy assumes that she has the red 2.
      * Cathy misplays red 3 as red 2.
      * Alternatively, if Cathy saw that Bob had both red 1 and red 2 on *Finesse Position* at the time the clue was given, she would know that she has the red 2 **or** the red 3. Subsequently, Bob is promised a red 2, since if he does not blind-play a card, Cathy will go on to misplay the red 3 as red 2.
    * **Number 3 with suit match (valid):**
      * On the first turn of the game, Alice clues Cathy number 3, which touches a red 3.
      * Bob blind-plays red 1.
      * Cathy knows that it was a *3 Bluff*, because a played 1 does not "match" number 3.
      * Beyond that, Cathy knows nothing about the card, besides that it is a 3 (since it has a number 3 clue on it).
      * Even though red 1 and red 3 are the same suit, Bob is not promised a red 2, because if he does nothing, Cathy will not go on to misplay the red 3.
* The priority of *3 Bluffs* can be confusing. If you don't want to memorize the four examples above, you can simply ask the following questions:
  1) Does the clue "match" the blind-play? If it matches, then it is a *Finesse*. If it doesn't match, then it is a *Bluff*. Red matches red, but red does **not** match blue. 2 matches 3, but 1 does **not** match 3.
  2) Will the player who received the clue go on to misplay if nothing else is blind-played? If yes, then it is a *Finesse*. If no, then it is a *Bluff*.

### Discard Elimination & The Elimination Blind-Play

* Normally, your teammates would never let you discard anything important. So when you discard some playable card (or a needed 2) **and** that card is not in anyone else's hand, you might think that the team make a mistake.
* From *High Value Principle*, you should never assume your teammates are making a mistake. One excellent reason that they would let you discard an important card is that you have the other copy in your hand. (In order to satisfy *Good Touch Principle*, they had to wait for you to discard it so that they would not duplicate the card.)
* Thus, when you get a follow-up clue, you will know exactly what card it is.
* For example, in a 4-player game:
  * Red 3 is played on the stacks.
  * Alice has a completely unclued hand.
  * Alice discards her chop (slot 5). It is a (playable) red 4.
  * Alice knows that the team was not busy, so she must have the other copy of red 4.
  * Alice writes *Elimination Notes* on slots 2, 3, 4, and 5. (It can't be on slot 1, since that is the card she just drew.)
  * Bob clues Alice red, which touches a card on slot 1 and slot 2.
  * Normally, Alice would play the left-most card (slot 1) as red 4. However, because of the *Elimination Notes*, she knows that the red 4 must be on slot 2.
  * However, the focus of the clue is on slot 1, so slot 1 must also be playable.
  * Alice plays red 4 first from slot 2. Since the red 5 is the only good red card left, Alice can assume that her other red card is red 5, and can play it on the next turn.
* In other situations, your teammates will choose to **not** to clue the card directly. But once the *Elimination Notes* are whittled down, you should be able to blind-play it.
* For example, in a 4-player game:
  * Red 3 is played on the stacks.
  * Alice has a completely unclued hand.
  * Alice discards her chop (slot 5). It is a (playable) red 4.
  * Alice knows that the team was not busy, so she must have the other copy of red 4.
  * Alice writes *Elimination Notes* on slots 2, 3, 4, and 5. (It can't be on slot 1, since that is the card she just drew.)
  * Bob clues Alice blue, which touches slots 1, 2, 3, and 4. (This is a *Play Clue* on slot 1.)
  * Alice erases her *Elimination Notes* from slots 2, 3, and 4.
  * The only card left with an *Elimination Note* is slot 5.
  * Alice blind-plays red 4 from slot 5 on her next turn.
* One last thing to note is that players should not always make *Elimination Notes* when they discard a playable card. In rare cases, games can be extremely busy, leaving no reasonable way to get the playable card, so you always have to keep that in mind.

### The Elimination Play Clue

* A clue that touches multiple cards only has one focus. As you probably know by now, if the chop card was not touched, then the focus is the left-most card.
* However, this rule does not apply if a clue singles out a playable card from *Elimination*. In this case, the card is only focused on the *Elimination* card, and any other cards touched are not necessarily playable right now.
* For example, in a 3-player game:
  * Red 1 and blue 1 are played on the stacks.
  * Alice has both red 2's in her hand on slot 3 and slot 5. (Alice's chop is her slot 5.)
  * Alice discards her chop, and it is revealed to be the red 2.
  * Alice is surprised, and writes *Discard Elimination Notes* for red 2 on slots 2, 3, 4, and 5.
  * Bob gives a number 2 clue to Alice that touches a card in slot 1 and slot 4.
  * Normally, Alice would treat this as a *Play Clue* on the 2 in her slot 1. However, she now knows that her slot 4 card is exactly red 2 (and that she can play it right now).
  * Thus, Alice knows that the point of the clue was only to get the red 2. The 2 in her slot 1 can be any 2 in the game and is not necessarily playable right now.

### The Elimination Riding Deduction

* If there are only two cards left in your hand with *Elimination Notes* on them **and** the players before you let your chop card ride **and** the players before you were not busy, then the playable card cannot be on your chop.
* This means you can "jump ahead" and immediately blind-play the newest of the two cards with the note.
* For example, in a 3-player game:
  * Red 1 has been played on the red stack.
  * Alice has a completely unclued hand.
  * Alice discards her chop (slot 5). It is a (playable) red 2.
  * Alice knows that the team was not busy, so she must have the other copy of red 2.
  * Alice writes *Elimination Notes* on slots 2, 3, 4, and 5.
  * Alice receives no clues on the next go-around of the table. She discards, and now has *Elimination Notes* on slots 3, 4, and 5.
  * Alice receives no clues on the next go-around of the table. She discards, and now has *Elimination Notes* on slots 4 and 5.
  * Alice receives no clues on the next go-around of the table. Her teammates would not let the other copy of red 2 be discarded, so it must be on slot 4. Alice blind-plays red 2 from slot 4.

### The Elimination Self-Chop Move

* Sometimes, you will have narrowed down your *Elimination Notes* to one specific card. Thus, even though the card has no positive clues on it, you know the exact identity of the card.
* If the card in question is on your chop **and** the card is not yet playable **and** you need to discard, you should obviously not discard the important elimination card. You should instead self-chop move and discard the next thing.

### Play Elimination

* When you discard something important, that triggers the writing of *Elimination Notes* on your own hand. This is *Discard Elimination* and is described above. But there are other ways that *Elimination Notes* are triggered.
* When another player plays a clued card in their hand that they should not have known was playable yet, it implies that they saw the other possibilities in someone else's hand. Thus, this should trigger you to write *Elimination Notes* on your hand.

### Double Discard Elimination

* When a player who is in a *Double Discard* situation discards anyway with an obvious clue to give (such as an off-chop 5), it implies that they **see** the other copy of the card, and were not *Double Discarding* at all.
* Thus, when this occurs, you should write *Elimination Notes* on your entire hand for that card.

### The Early 5's Chop Move & The 5 Pull

* In the *Early Game*, players are only allowed to clue an off-chop 5 if there is nothing left to do. (Or, as a special exception, if there is only one *Play Clue* to give to a card that happens to be on *Finesse Position*.)
* Thus, if someone clues a 5 and there **is** something else to do, they are performing a special move.
* If the 5 is one-away from chop, then they are performing an *Early 5's Chop Move*. This functions in the same way a normal *5's Chop Move* does (except it was done in the *Early Game*, which isn't normally possible).
* If the 5 is two or more away from chop, then they are performing a *5 Pull*. A *5 Pull* causes the player to blind-play the card to the right of the 5. For the player receiving the clue, it is understood that the 5 is not actually related to the blind-play. This is why it is called a *Pull* instead of a *Finesse* or a *Bluff*.
* *5 Pulls* are typically done to 5's that are in slot 1. But, for example, you can also clue a 5 in slot 2 in order to get a blind-play on slot 3.
* Even though they involve playing a blind card, a *5 Pull* should be treated as a *Delayed Play Clue*. This means that the blind card could play through any existing touched cards.
* *5 Pulls* also take precedence over *Finesses* and *Bluffs*. For example:
  * It is the *Early Game*.
  * On the stacks, red 3 is played.
  * A red 5 is clued with number 5 on slot 1. (There are other *Play Clues* to give, so this is **not** an off-chop 5's stall clue.)
  * Normally, this would imply a *Finesse* on a red 4.
  * However, since *5 Pulls* override *Finesses*, as long as there is a playable card to the right of the 5, then NO-ONE is promised the red 4.
* Normal *Play Clues* and *Delayed Play Clues* take priority over *Early 5's Chop Moves* and *5 Pulls* (as long as they don't cause any blind cards to play). For example:
  * It is the *Early Game*.
  * On the stacks, red 4 is played.
  * A blue 1 is available to clue in Bob's hand.
  * Instead, Alice clues an off-chop 5 in Cathy's hand (as number 5).
  * This is to be interpreted as a *Play Clue* on the red 5 (as opposed to a *5 Pull* on some other card).
* When a player is *Finessed* or *Bluffed*, they are allowed to defer playing the blind card in order to do a *Finesse* or *Bluff* of their own. However, if they could be *Bluffed*, they are **not** allowed to initiate a *5 Pull*. (Players are still allowed to defer playing into a *Finesse* in order to initiate a *5 Pull*.)
* In the rare case where a *5 Pull* is performed in a 3-player game by touching two 5's in slot 1 and slot 3, then the *5 Pulled* card is slot 2.

### A Flowchart for Cluing 5's in the Early Game

* Differentiating between a *5 Stall* and a *5 Pull* can sometimes be confusing. [Here is a handy flowchart](https://raw.githubusercontent.com/Zamiell/hanabi-conventions/master/flowcharts/early-game-5-flowchart.png) that steps you through how you can tell the difference.

### The 5 Pull Prompt & The 5 Pull Finesse

* *5 Pulls* are also allowed to initiate a *Prompt* or *Finesse*.
* However, *5 Pulls* are **not** allowed to initiate a *Reverse Finesse*.
* With that said, players **do** have to respect that forward *5 Pull Finesses* could be *Layered*/*Clandestine*. ("Clandestine" is terminology is covered later on.)

### The 5 Pull Promise (A Follow-up Play Clue After a 5 Pull)

* Normally, *5 Pulls* have to be treated as *Delayed Play Clues*. This means that sometimes, it can take a long time for the pulled card to blind-play.
* From the perspective of the player who is *5 Pulled*, if a follow up *Play Clue* is given to a currently unplayable card, then they can disregard the *Delayed Play Clue* interpretation - the *5 Pulled* player is **promised** the card that makes the unplayable card playable.
* For example, in a 4-player game:
  * Alice has two clued 1's in her hand - red 1 and blue 1.
  * Bob does a *5 Pull* on Donald. Donald knows that the *5 Pulled* card could be either red 2 or blue 2 (if it is a *Delayed Play Clue*).
  * Cathy clues Alice about a red 3. Now, Donald knows that he is **promised** the red 2 as his *5 Pulled* card (and he no longer has to wait for the blue 1 to come down before blind-playing).

### Finesses While 5 Pulled

* Sometimes, a *5 Pulled* player may not play their pulled card right away. Maybe they have to wait for existing cards to play first, or maybe they want to capitalize on a *Finesse* while it is still available.
* Any *Finesse* that a *5 Pulled* player performs is to be treated as a *Certain Finesse*.
* Any *Certain Discard* that is performed in response to a *Finesse* that a *5 Pulled* player did applies to the *5 Pulled* card.

### The Weak Prompt

* If a teammate performs a *Prompt* on you, and you have multiple cards in your hand that match the connecting card, normally you would be promised that the left-most (newest) is playable.
* However, if the card that initiated the prompt was **on chop** when it was touched **and** it was in danger of being discarded, the left-most rule no longer applies, since your teammate had to take drastic measures to prevent the discard of that card.
* So instead, you are promised that you have the connecting card somewhere in your hand, but it could be any of the cards, and not strictly the left-most.

### The Wrong Prompt (Mistake)

* A common mistake in Hanabi is to attempt to perform a *Finesse* when there is a "matching" card in that player's hand. Since *Prompts* take precedence over *Finesses*, the player will always play their matching clued cards first.
* When a card is *Prompted* and it misplays, everyone can read into this mistake - it was almost certainly a *Wrong Prompt*, meaning that the player who gave the clue probably intended for the *Finesse Position* card to play instead.
* Thus, if there is nothing else special about the situation, the player who misplayed should go on to play their *Finesse Position* card on the next turn.

### Critical Discards after a Chop Move (Mistake)

* If a player chop moves, and then the next time they discard, they discard a critical card, then obviously some kind of mistake occurred.
* The best explanation is that the chop move was never intended in the first place.
* Thus, when this happens, the player should "undo" the chop move.

### Duplication Responsibility

* Usually, if a 2 needs to be saved, it is not the responsibility of a player with already-clued 2's in his hand, because they could potentially violate *Good Touch Principle* by cluing it, so they should defer and let someone else on the team do it. (The same general concept also applies to cluing playable cards on chop, for example.)
* However, if all players have a clued 2 in their hand, then someone has to take a risk of violating *Good Touch Principle* in order to satisfy *Save Principle*. Who should do it?
* In this situation, the player who has the least number of matching clued cards should take responsibility. If 2+ players are tied, then the player with the more specific type of clue on their card(s) should take responsibility.
* If 2+ players have the exact same number of clued cards and type of clued cards, then either player should save the card.
* Example 1:
  * In a 3 player game, Alice has a blue 2 on chop that needs to be saved.
  * Bob has 2 unknown 2's.
  * Cathy has 1 unknown 2.
  * Bob should let Cathy perform the save, since 1 matching card is less than 2 matching cards.
* Example 2:
  * In a 3 player game, Alice has a blue 2 on chop that needs to be saved.
  * Bob has 2 unknown 2's.
  * Cathy has 2 unknown 2's.
  * The responsibility is shared, so Bob should perform the clue if Cathy has a good discard, or he can discard and let Cathy do it.
* Example 3:
  * In a 3 player game, Alice has a blue 2 on chop that needs to be saved.
  * Bob has 2 unknown blue cards.
  * Cathy has 1 unknown 2's.
  * Bob should let Cathy perform the save, since 1 matching card is less than 2 matching cards.
* Example 4:
  * In a 3 player game, Alice has a blue 2 on chop that needs to be saved.
  * Bob has 2 unknown blue cards. No blue cards have been played yet, so from Bob's perspective, each blue card has a 1/5 chance of being the blue 2.
  * Cathy has 2 unknown 2's. No 2's have been played yet, so from Cathy's perspective, each 2 has a 1/5 chance of being the blue 2.
  * The responsibility is shared, so Bob should perform the clue if Cathy has a good discard, or he can discard and let Cathy do it.
* Example 5:
  * In a 3 player game, Alice has a blue 2 on chop that needs to be saved.
  * Bob has 2 unknown blue cards. No blue cards have been played yet, so from Bob's perspective, each blue card has a 1/5 chance of being the blue 2.
  * Cathy has 2 unknown 2's. One 2 has been played already, so from Cathy's perspective, each 2 has a 1/4 chance of being the blue 2.
  * Thus, it is Cathy's responsibility to save the blue 2.

### Context Clues & The Stale 1's Clue

* Based on the *First Principles*, we have conventions that define what a clue means. But combined with this, we are always expected to look at the context of the game.
* For example, sometimes players will receive a clue that just feels strange. If this good clue could have been given a bunch of turns ago, why is it only being given now? Were the other players not paying close enough attention, and are only getting around to cluing this card now?
* In these types of situations, from *High Value Principle*, you can assume that the team is not making any mistakes, which means that the meaning of the clue should be altered from the "textbook" definition. We call these types of clues *Context Clues* because they rely on contextual reading of the game state.
* The most common *Context Clue* is given to "stale" 1's towards the beginning of the game. For example, in a 3-player game:
  * After a few ordinary clues happen, Alice discards, which ends the *Early Game* and initiates the *Mid-Game*. By doing this, she implies that there is nothing to do (because players are mandated to "extinguish" all of the available *Play Clues* and *Save Clues* in the *Early Game*).
  * Bob then immediately clues Cathy about two 1's.
  * Normally, from *Good Touch Principle*, Cathy would assume that both of the 1's were "good" and play both.
  * However, Cathy also knows that if both of these 1's were good, then Alice was required to clue them before discarding.
  * Thus, Cathy can reason that one of the 1's are bad. Furthermore, by convention, she knows that the oldest (right-most) 1 is bad, because that would be the one that she would ordinarily play first.
  * So, Cathy should skip over the oldest (right-most) 1, and play the other 1. Cathy should also treat the other 1 as known-trash.
* The *Stale 1's Clue* is specific example of a more general concept called *Focus Inversion*, which is covered later.

### Focus Inversion

* Sometimes, a *Play Clue* is given that both touches the chop card and one or more other card. The normal interpretation of this is to treat it as a chop-focus *Play Clue*, and play the chop. However, sometimes a player can know that the chop is not actually playable. This can be determined through:
  * explicit information - negative clues present on the card
  * implicit information - historical / contextual information about the card derived from moves that teammates performed earlier on in the game
* When this occurs, the clue is meant to be a *Play Clue* on the left-most card **instead** of the chop card.
* Just like a "normal" *Play Clue* that touches multiple new cards, the chop card (and other other new cards introduced) are not necessarily playable right now.
* For example, in a 3-player game:
  * Alice clues 1's to Bob, which introduces one card on slot 1.
  * Bob plays the 1 and it is red 1.
  * Cathy clues blue to Bob, which introduces two cards on slot 1 and slot 5.
  * Normally, Bob would think that this is a *Chop Focus* clue, and play the blue 1 from slot 5.
  * However, his slot 5 card has a negative 1 clue on it (from Alice's number 1 clue), so it explicitly cannot be the blue 1.
  * Thus, this must be *Focus Inversion* and blue 1 must be on slot 1. The blue card on slot 5 can be either blue 2, blue 3, blue 4, or blue 5.
* Note that ***Self-Finesses* always take precedence over *Focus Inversion***.

### Burning (End-Game Stalling) & Same-Suit Principle

* In the *End-Game*, often times there are still a lot of cards yet to be played. Thus, you need to be very careful when discarding, since by drawing a card you can make the game end before everyone has a chance to play all of the cards.
* If there are enough of clues available, you can choose to stall, by giving a low-value (or even a completely useless) clue. This is referred to as *Burning* a clue.
* The best way to give a useless clue is to re-clue cards which are already known to be playable.
* Give a *Burn Clue* if:
  * There is a possibility that the game can be completed without anyone discarding from now on.
  * You have two or more useful cards in your hand, and you want to follow *Team Distribution Principle*.
* Do not give a *Burn Clue* if:
  * The end-game has not started yet (see the *End-Game Threshold*).
  * You know that someone else will have to discard in the future.
  * There is only one more useful card in the deck and all of the useful cards in your hand are of the same suit as that card. This is known as *Same-Suit Principle*. For example:
    * You have two cards clued in your hand that you know to be red 3 and red 5.
    * The only useful cards left in the deck are two red 2's.
    * Here, there is no reason for you to stall, since the red 3 will **not** be played sooner if you stall.

### The Distribution Clue

* In the *End-Game*, when a player has many playable cards, there is the risk that they will not be able to play all cards before the end of the game.
* Thus, it might make sense to spend a clue to duplicate one of their playable cards in someone else's hand. This would violate *Good Touch Principle*, but it would relieve the player with the loaded hand from some of the card-playing burden.
* Since it distributes plays more evenly throughout the team, this is called a *Distribution Clue*. *Distribution Clues* better satisfy *Team Distribution Principle*.

<br />

## Level 4 - Expert Strategies

### The Occupied Play Clue & The Occupied Finesse (O.P.C. / OPC)

* If a clue could be given by multiple players, who should give the clue? Usually, it makes the most sense for the players with playable cards to play those cards, and the players with nothing to do to give the clue.
* If someone gives a clue with a playable card in their hand and forces the next player to have nothing to do, this is bad teamwork - unless there was a reason!
* When this occurs, even if the clue looks like an ordinary *Save Clue*, it **must** be a *Play Clue*, since the player who was doing it was occupied.
* Furthermore, if an *Occupied Play Clue* is given to a card that is not directly playable right now, it must be an *Occupied Finesse*!
* The concept of an *Occupied Finesse* generalizes to lots of different kind of moves. For example, when an occupied player clues an off-chop 5, it is certainly not a *5 Stall* - it must be an *Occupied 5 Pull*!

### The Clandestine Finesse

* To the player who receives a clue that initiates a *Layered Finesse*, it is usually obvious what is going on. For example, in a 4-player game:
  * Alice clues Donald about one blue card.
  * Bob discards.
  * Cathy blind-plays a green 1.
  * Donald clearly knows that this is a *Layered Finesse* on Cathy, and she will continue to play cards until she finds the blue card that matches the one in his hand.
* In other words, most *Layered Finesses* cause unrelated cards to blind-play that do not match the type of clue given.
* With that said, it is also possible to perform a *Layered Finesse* for unrelated cards that **do** match the type of the clue given. When this happens, it is hidden from the receiver of the clue, so we call it a *Clandestine Finesse* to disambiguate it from a (more obvious) *Layered Finesse*.
* For example, in the following screenshot:
  * Zealousy's hand has a green 2 and a green 3 that are already touched with a green clue.
  * Instantiation clues number 3 to Zealousy, which touches only one brand new card, the purple 3. Thus, the purple 3 is the focus of the clue.
  * Hyphen-ated knows that the purple 3 is currently unplayable, so it must be a *Finesse*. He attempts to play purple 2 from his *Finesse Position* (slot 1). It is instead a red 2.
  * Normally, Zealousy would think that he has the red 3 on his slot 1, because the card that was blind-played matches the clue. (Number 2 matches number 3.)
  * However, Zealousy also sees that Hyphen-ated had a purple 2 on his *Second Finesse Position* at the time of the clue. So there is a possibility that this was a *Clandestine Finesse* instead of a normal *Finesse*. Thus, Zealousy has to give Hyphen-ated a chance to blind-play the purple 2. If he does not, then Zealousy does indeed have the red 3. Zealousy discards.
  * Instantiation also discards.
  * Hyphen-ated was surprised that he played the red 2, but now knows that it was a *Clandestine Finesse* instead of a normal *Finesse*. He blind-plays his slot 2, and it is the purple 2. If he did not do this, then Zealousy would misplay purple 3 as red 3.
  * Zealousy plays purple 3.

![Clandestine Finesse](img/clandestine_finesse.png)

* Since we are allowed to lie in *Bluff Seat*, doing a *Layered Finesse* in *Bluff Seat* typically won't work. Instead of getting a big layered chain of cards, it will be interpreted as a *Bluff*, and only one card will be played. However, note that a *Clandestine Finesses* can get around this restriction, because it induces a potential misplay. The blind-playing player **must** continue to blind-play cards, or else the player receiving the clue will assume that the *Finesse* is "over" and will play the clued card.

### The Stacked Finesse

* If a player has been *Finessed*, then their *Finesse Position* moves right one slot, exactly like if the blind card was clued. (This is a similar concept to how the chop moves left one slot when a player is *Chop Moved*.)
* If **another** *Finesse* is performed on the player who has already been *Finessed*, it is stacking a 2nd *Finesse* on top of the first, and they are expected to blind-play the new *Finesse Position* card.
* However, because of the possibility of *Layered Finesses*, players should always blind-play their cards in order from left to right (and not jump ahead).
* In rare cases, players can determine that a *Layered Finesse* was impossible (due to negative clues or some other piece of context). In this situation, if the play order of the cards does not matter, players should always "jump ahead" and play the second card to demonstrate to the team that they "got" both *Finesses*.

### The Layered Gentleman's Discard

* One great reason to want to do a *Gentleman's Discard* is if the card you are discarding is also behind playable cards. This is similar to a *Layered Finesse*, only it was initiated by a discard instead of a clue.
* For example, on the first turn of a 3-player game:
  * Alice clues number 1 to Cathy, touching one 1.
  * Bob clues red to Cathy, filling in the already-touched 1 as red 1, as well as touching a new card, which must be red 2.
  * Cathy discards the known red 1 as a *Gentleman's Discard*.
  * Alice blind-plays her *Finesse Position* card as red 1, but it is green 1.
  * Alice knows that she is promised the red 1, so she will blind-play her slot 2 on her next turn.

### The Trash Push

* Normally, when a useless card is clued, it signifies a *Trash Chop Move*. However, what if the useless card is actually the card on chop? Then it wouldn't be *Chop Moving* anything.
* From *Good Touch Principle*, we know that it is pointless to spend a clue to touch a useless card on someone's chop, because if we just do nothing, the useless card will get automatically discarded.
* Subsequently, if this is done deliberately, it must have a meaning. By doing this, it means that we want to "push" the card that is next to the useless card onto the table.
* For example, in a 3-player game:
  * All of the 1's are played on the stacks.
  * Bob has no clued cards in his hand. His chop is his slot 5.
  * Alice clues Bob number 1, which only touches his slot 5 card.
  * Bob blind-plays his slot 4 card, and it is a playable red 2.
* Sometimes, a *Trash Push* is the only way to get a card played that is sitting between two other annoying cards.

### The Trash Bluff

* Normally, when a useless card is clued, it signifies a *Trash Chop Move* or a *Trash Push*. However, for both of these strategies to work, it is assumed that the recipient of the clue will know that the card that was touched is useless.
* What if the recipient of the clue does **not** know that the card that was clued is useless? They will go on to misplay that card, mistaking it for a "normal" *Play Clue*.
* When you see this occur, it works like a *Bluff*; you must blind-play your *Finesse Position* card, or the player who received the clue will go on to misplay.
* *Trash Bluffs* are a good tool to get a card played that is sitting behind other annoying cards.
* For example, in a 3-player game:
  * On the stacks, all of the 1's are played **except** for red 1.
  * Cathy has no clued cards in her hand.
  * Alice clues Cathy number 1, which only touches her newest (slot 1) card. This card is a blue 1, so Cathy will assume that it is a red 1.
  * Bob blind-plays his *Finesse Position* card, and it is a playable blue 2.
  * Cathy now knows that her 1 must not be red 1, or else Bob would not have blind-played anything. The 1 must be some other trash card.
* Just like normal *Bluffs*, *Trash Bluffs* can only be done while in *Bluff Seat*.
* If multiple cards are clued that cause a *Trash Bluff*, it means that **all** of the cards are trash. However, the focus of the clue should be the first thing discarded, which allows for the possibility of your teammates to give a follow-up *Fix Clue*.

### The Trash Finesse (Strong Form)

* In a *Finesse*, we would say that the clue "matches" the blind-play. For example, a blue clue on a blue 2 matches a blind-play of blue 1. Or, a number 2 clue on blue 2 matches a blind-play of blue 1.
* In a *Bluff*, we would say that the clue does not "match" the blind-play. For example, a blue clue on a blue 2 does not match a blind-play of a red 1. Or, a number 2 clue on a blue 2 does not match the blind-play of a red 2.
* In the *Trash Bluff* example above, a blue 1 is used to *Trash Bluff* a blue 2. Similar to a *Bluff*, we would say this number 1 clue does not match the blind-play of a blue 2.
* What is the *Trash Bluff* instead got a red 1 to blind-play? In this context, the red 1 would actually "match" the number 1 clue. Another way of saying this is that by cluing the trash 1 with a number 1 clue, the clue giver is saying that they **see** a matching 1 that is good.
* Thus, it is possible to perform a a *Trash Bluff* outside of *Bluff Seat* if the "matching" card is on someone's *Finesse Position*. When this is done, it promises that someone has that specific card, so we call it a *Trash Finesse* rather than a *Trash Bluff*.
* For example, in a 4-player game:
  * All the 1's are played on the stacks except for red 1.
  * Alice clues number 1 to Donald, which touches a blue 1. To Donald, this will look like it is a red 1.
  * At first glance, Bob might think this is a *Trash Bluff*, causing him to blind-play his *Finesse Position* card as either red 1 or some other currently-playable card.
  * However, Bob also sees that Cathy has a red 1 on her *Finesse Position*. Thus, Alice's clue was a *Trash Finesse* instead of a *Trash Bluff*, since it is promises a playable 1.
  * Thus, Bob discards.
  * Cathy blind-plays her *Finesse Position* card and it is red 1.
  * Donald discards his known-trash 1.
* *Double Trash Finesses* are explicitly disallowed. Thus, it is possible to perform a *Trash Finesse* in a situation like this:
  * All the 1's are played on the stacks except for red 1 and blue 1.
  * Alice clues number 1 to Donald, which touches two green 1's on slot 1 and 2. To Donald, this will look like it is both the red 1 and the blue 1.
  * Like in the previous example, Bob sees that Cathy has a red 1 on her *Finesse Position*.
  * At first glance, Bob might think that Alice is promising both red 1 and blue 1, which would mean that he would need to blind-play the blue 1.
  * However, a *Trash Finesse* only promises at least one matching card, and since he sees that Cathy has a matching card, then that is good enough. Thus, Bob discards.
  * Cathy blind-plays her *Finesse Position* card and it is red 1.
  * Donald knows that the focus of the clue (slot 1) is certainly trash, since that caused Cathy to blind-play.
  * Furthermore, Donald knows that his slot 2 card is also trash, because all the cards touched in a *Trash Bluff* or *Trash Finesse* are guaranteed to be trash.

### The Trash Finesse (Weak Form)

* After deciding on the target of a clue, players carefully choose between using a color clue and a number clue in order to avoid violating *Good Touch Principle* with the ancillary cards that will be touched (since every clued card is treated as a card that will eventually be played). Sometimes, when both a color clue **and** a number would violate *Good Touch Principle*, players are forced to pick between the lesser of two evils.
* However, sometimes you can see that it **is** possible to use a color or number clue to uniquely touch a clue target without "picking up" extra bad cards. So, when extra bad cards are deliberately touched in this way, it promises that the other players have the exact "missing" cards that the trash cards would look like.
* This is more subtle than the strong *Trash Finesse*. In the strong form, the focus of the clue causes an immediate misplay (if no-one blind-plays). In the weak form, the non-focused cards are what causes the blind-play.
* For example, in a 3-player game:
  * Red 2 is played on the stacks. All of the other suits have the 1 played on the stacks. 
  * Bob's hand is as follows, from newest to oldest: red 3, red 1, blue 1, green 1, yellow 1.
  * Alice wants to give a play clue to the red 3. Everyone on the team can see that she can give either 3s or red.
    * If she clues number 3, then it will uniquely touch the red 3 (and not violate *Good Touch Principle*).
    * If she clues red, then it will touch the red 3 and the red 1 (which **will** violate *Good Touch Principle*).
  * Alice clues red to Bob. Since nothing was stopping her from cluing number 3, this is very strange.
  * Bob plays the red 3.
  * Cathy knows that sometimes, when this type of thing happens, the aim is to protect a card on chop (when all cards of the suit are visible). But Alice sees that Bob's hand is filled with trash, so this cannot be the case.
  * Alice must be sending a signal to the team that someone has a red card ready to play. Thus, Cathy immediately blind-plays her *Finesse Position* card, and it is the red 4.
  * Bob sees Cathy blind-play the next red card for seemingly no reason, so he is able to deduce that his slot 2 card is trash.

### The Trash Pull

* Sometimes, towards the end of the game, there can be a playable card in the middle of someone's hand that is not cluable directly due to the presence of other blocking cards.
* In this situation, players often resort to a *Trash Push* in order to "get" the card without cluing it directly. However, this will obviously only work if the player has a trash card on their chop, which may not always be the case.
* Another tool to "get" a card in the middle of a hand is by doing the opposite of a *Trash Push* - a *Trash Pull*.
* If an off-chop trash card is clued, this would typically be interpreted as a *Trash Chop Move*. However, towards the end of the game, a *Chop Move* would be pointless, as there are no cards left to chop move. Thus, the player should know that it is a *Trash Pull* instead of a *Trash Chop Move*, and should blind-play the card to the right of the trash.
* Just like how a *5 Pull* can only be done in the *Early Game*, a *Trash Pull* can only be done at the end of the game.
* Since players often perform *Burn* clues for stalling purposes in the *End-Game*, care has to be taken to not confuse a normal *Burn* clue with a *Trash Pull*. This is especially true if there was nothing else obvious for the clue giver to do!
* *Trash Pulls* should typically be used as a last-resort since they might be misinterpreted.

### A Trash Flowchart

There are a lot of different moves that involve cluing trash. [Here is a handy flowchart](https://raw.githubusercontent.com/Zamiell/hanabi-conventions/master/flowcharts/cluing_trash_flowchart.png) for determining the difference between the different types of special moves that touch trash.

### The Certain Discard Duplication Promise

* As the recipient of a *Finesse*, you are promised a card that you have to blind-play. However, as long as it is not a *Certain Finesse*, you **have** to account for the possibility of a *Layered Finesse*. This means that you can never blind-discard the promised card to perform a *Gentleman's Discard*, for example.
* After the *Finesse* has occurred, but before the promised card has been blind-played, there is a window where a teammate might find strategic value in duplicating the promised card in someone else's hand.
* Unless the duplication was a last-resort, if the teammate duplicates the blind card, it **promises** that the duplicated card is on *Finesse Position* (and there is **no** *Layered Finesse*), which allows the recipient of the *Finesse* to blind-discard that card, similar to a *Certain Discard*.
* Finally, from the perspective of the player receiving the clue, if they end up playing the duplicated card first, then they should know that the focus of the original clue was on the other, non-duplicated card, and they can play it immediately afterwards. (Otherwise, the original clue would be fairly low-value.)
* Note that as long as the duplication clue touches two or more cards, the *Certain Discard Duplication Promise* interpretation takes priority over the *Unknown Trash Ejection* interpretation. (*Ejection* is covered later on.)
* Examples:
  * Game #6817, turn 15
  * Game #6799, turn 5

### The Out-of-Order Finesse (Triple O / OOO / O.O.O.)

* Sometimes, a *Finesse* is invoked by giving a color clue to two or more cards where the next card in the sequence is clued, but it is **not** the focus of the clue.
* When this happens, the *Finesse* will still work: a player will blind-play a matching card. However, a *Fix Clue* must then be given to the player who originally received the clue, or they will go on to misplay.
* Normally, after receiving a *Fix Clue*, a player would normally "stop" and not assume anything else about his hand. However, this is a special situation: when the original *Finesse* was given, it was a message that the focus of the clue was playable. *Information Lock Principle* applies, and it means that the original focus of the clue is also playable.
* For example, in a 3-player game:
  * At the beginning of the game, Alice goes first.
  * Bob has a red 3 and a red 2 (on slots 1 and 2 respectively).
  * Cathy has a red 1 on slot 1 (in *Finesse Position*).
  * Alice clues Bob red (as an *Out-of-Order Reverse Finesse*). The focus of the clue is the red 3 on slot 1.
  * Bob sees the red 1 on Cathy's *Finesse Position*, so he has to respect that it could be *Reverse Finesse*. Bob discards.
  * Cathy blind-plays red 1.
  * Alice must now give a *Fix Clue* to Bob, or else red 3 will be misplayed as red 2.
  * Alice clues number 2 to Bob.
  * Bob plays red 2.
  * Bob knows that his other red card **must** be red 3, since it was originally clued as playable and it caused a *Reverse Finesse*.

### Finesses with a Lie Component

* *Good Lie Principle* states all that lies must resolve immediately. However, some players will occasionally perform *Finesses* that violate this principle. We would say that such *Finesses* have a *Lie Component*.
* Typically, when players lie out of *Bluff Seat*, the game quickly falls apart; subsequent clues will have different meanings to different players and everyone will become "desynchronized". This typically leads to a loss.
* With that said, it is sometimes possible to construct **safe** lines that contain a *Lie Component*. There is usually deep levels of nuance involved in these lines, so this kind of thing is only recommended for advanced and expert players.
* The previously mentioned *Out-of-Order Finesse* is an specific example of a *Finesse* with a *Lie Component*. One key attribute of the *Out-of-Order Finesse* is that the player who receives the *Fix Clue* knows that **all** of the related cards are playable, or it would not have been worth the risk (and the confusion) to perform a line with a *Lie Component* in the first place.
* This concept can be generalized to all *Finesses* that have a *Lie Component*. After a player receives a *Fix Clue* in such a situation, they should assume that the *Finesse* is "still on". So, depending on the situation, they should either know that the initial card that was clued is playable (like in an *Out-of-Order Finesse*) or continue to blind-play cards to the right of the card that got the *Fix Clue* (if more blind cards need to be played to fulfill the initial *Finesse*).

### The Priority Bluff & The Layered Priority Finesse

* It is possible to lie to the next player and imply a *Priority Finesse* when they have an unrelated card on *Finesse Position*.
* After the unrelated card is played, since the player who lied was in *Bluff Seat*, no further cards should be promised.
* If an unrelated card was played and the player who lied was not in *Bluff Seat*, it implies a *Priority Layered Finesse*.

### The Speculation Prompt & The Speculation Finesse

* Normally, a player needs to know the exact identity of a card in order to initiate a *Priority Prompt* or *Priority Finesse*. However, it is somewhat common that a player will get a *Play Clue* on a card and they will not know its exact identity. (For example, when they get a color *Play Clue* in a multi-color variant.) In this situation, the rules of *Priority* still apply, as enumerated above in the previous section.
* Subsequently, if a player plays a non-priority card that they do not know the exact identity of, this can be quite strange. In this situation, they are trying to perform a speculative *Priority Prompt* or *Priority Finesse* with the intent that it will only work if they happen to be playing a specific suit. This is called a *Speculation Prompt* or a *Speculation Finesse* for short.
* We agree that a *Speculation Prompt* or *Speculation Finesse* only promises the next card in the suit that is the left-most of the possible suits that it could be (when looking at the suits in the middle of the table).
* For example, in a no variant game:
  * Blue 1 and red 1 are played on the stacks.
  * Alice has a known playable yellow 1. She also has a known playable 2 that could be either blue 2 or red 2.
  * The yellow 1 has *Priority* and Alice is expected to play that. Instead, she plays the 2 as a *Speculation Finesse*.
  * Between blue and red, the blue suit is the *Speculation Target*, since it is the left-most suit between blue and red.
  * The card happens to be blue 2. The rest of the team is promised the blue 3, just like a normal *Priority Prompt* or *Priority Finesse*.
* It is also possible for the *Speculation* to fail, meaning that the card does not happen to be the left-most suit. In this situation, the rest of the team is still promised the *Speculation Target*, but they should write *Speculation Elimination Notes* for the card.
* For example, in a no variant game:
  * The setup is the same as the previous example.
  * The card happens to be the red 2 (instead of blue 2).
  * The rest of the team knows that the blue 3 was promised. Bob does not see anyone else with the blue 3, so he writes *Speculation Elminiation Notes* on every card in his hand.
* Note that we agree that it is illegal for players to perform a *Amiguous Speculation Finesse*, so players do not have to account for that possibility.

### The Speculation Layered Finesse

* Similar to a *Layered Priority Finesse*, it is also possible to *Layered Speculation Finesse*. This is safe to do because if the *Speculation* fails, no lie will have occured, since the other player will write *Elminiation Notes* on their entire hand.

<br />

## Level 3 - Variant-Specific Strategies

### Hard Variants & Easy Variants

* Some variants demand an enormous amount of efficiency. Since our normal conventions result in conservative play, we agree to change the way that we play in some specific variants in order to win more consistently.
* The necessary efficiency needed in order to win each variant is located on [the efficiency tables page](https://github.com/Zamiell/hanabi-conventions/blob/master/misc/Efficiency.md).
* We define any variant that requires equal to or greater than 1.25 efficiency as a "hard" variant. (Note that a variant can be considered easy in 4-player, but hard in 5-player, for example.)
* In hard variants, the following changes are made to the conventions:
  * Players are not allowed to *Double Discard Avoid*. Any clue given in a *Double Discard* situation will instead be treated like a normal clue.
  * Players are not allowed to *5 Stall* in the *Early Game*. Any clue that looks like a *5 Stall* is instead treated as either a *5's Chop Move* or a *5 Pull*.
  * Players are not required to clue anything in the *Early Game*; they are allowed to initiate the *Mid-Game* whenever they see fit.

### 3 Suit Conventions

* These conventions applies to any variant with only 3 suits.

#### No 3 Bluffs

* The *3 Bluff* convention is "turned off". (This is because *Double Finesses* are much more likely in these variants.)

#### The Full Finesse

* The *5 Stall*, *5's Chop Move*, and *5 Pull* conventions are "turned off".
* If a 5 is clued, then it is to be treated as a *Finesse* on the full suit from 1 to 5.

### White Conventions

* These conventions apply to any variant with a white (colorless) suit.

#### White Compromise (5 Chop Moves)

* When you clue a white 5 that is one away from chop, it would normally look like a *5's Chop Move*.
* However, if the white 4 is currently played, all 5 clues that could be *5's Chop Moves* are treated instead *Play Clues* on white 5.

#### White Compromise (5 Pulls)

* When you clue a white 5 in the *Early Game* that is two or more away from chop, it would normally look like a *5 Pull*.
* However, if there are white cards visible and it could be a *Finesse* on the white 5, then it should be treated as a *Finesse* instead of a *5 Pull*.

### Black Conventions

* These conventions apply to any variant with a black (one of each) suit.

#### Black 2 & Black 5 Saves

* Players should save black 2's and black 5's with a number clue instead of a color clue. (This helps narrow down what card is being clued.)
* There are four exceptions to this:
  * if the black clue touched two or more brand new black cards **or** critical Rainbow cards
  * if the black clue was required to avoid violating *Good Touch Principle*
  * if the black clue "filled in" an ancillary card
  * if the black clue gave important negative information to one or more cards in the hand (which mostly applies to the *Wild & Crazy* variant)
* Subsequently, if a black clue is used to touch a black 2 or a black 5 (and the above exceptions are not applicable), then it implies a *Finesse*.

#### Black 3 & Black 4 Saves

* Players should save black 3's and black 4's with a color clue instead of a number clue. (This helps narrow down what card is being clued.)
* There is one exception to this:
  * if the number clue also touched another critical card
* Subsequently, if a number clue is used to touch a black 3 or a black 4 (and the above exception is not applicable), then it implies a *Finesse*.

#### Black 4 Bluffs

* Building on the *3 Bluffs* convention, we also agree that is possible for a card that initiates a *Bluff* to be a copy of black 4.
* However, it is only possible to do this with a black color clue.

#### The Black Save Bluff

* Normally, if a black 1 is on chop, it is clued with number 1 instead of black. This is because a black color clue would make it look like a *Save Clue* on either black 3 or black 4, and then it would sit there, not being played.
* Furthermore, if a black 1 is on chop and it was clued as black **and** the clue touched other brand new black cards in the hand, then the clue could also be a *Save Clue* on black 2 (as per the *Save Clue* rules outlined in the *Black 2 Saves* section).
* Thus, if another player intentionally clues a black 1 on chop with a black color clue **and** it touched other brand new black cards, this would be quite strange, as it would not get the black 1 to play, so they must be trying to communicate something extra.
* This is a sneaky signal that the next player has a playable card on their *Finesse Position*. By blind-playing it, they can show that a *Bluff* is happening.
* In a normal *Bluff*, the player receiving the clue would think that it is a one-away from playable card. In this case, if it was a normal *Bluff*, they would think that they have the black 2.
* However, as noted above, in this situation black 2's on chop are allowed to be touched as a *Save Clue*. So, touching a black 2 in this way would **not** cause a blind-play.
* Thus, by convention, the card should be black 1, and they can play it.
* It is also possible to use this convention to perform a *Black Save Bluff* on cards other than the black 1. For example, in a 3-player game:
  * Alice has if a player can cleanly clue number 2 to a black 2 on chop, but they instead clue a black 2 in the situation 

### Rainbow & Dual-Color Conventions

* These conventions apply to any variant with a rainbow (touched by all colors) or dual-color suit.

#### The Free Choice Finesse

* When performing a *Prompt* by touching a sole rainbow card, the player doing the clue may have a free choice between multiple colors. In other words, there may exist multiple colors that will **only** touch the rainbow card.
* If a player has a free choice to choose the color that matches the intended *Prompt* target but instead deliberately chooses a different color, this signals that it is actually a *Finesse* instead of a *Prompt*.
* For example, on the first turn of a 3-player game:
  * Alice clues Bob red, which touches a red 1 in slot 1 and a red 3 in slot 2.
  * Bob plays red 1 from slot 1. He draws a rainbow 1, which is now in his slot 1.
  * Cathy discards.
  * Alice notices that Bob has a rainbow 1 in *Finesse Position*. And Cathy has a rainbow 2 in her hand.
  * Since *Prompts* take precedence over *Finesses*, if Cathy clues the rainbow 2 with red, then Bob will misplay the red 3 as rainbow 1. This is a problem.
  * However, Cathy has no red cards, no blue cards, and no other rainbow cards in her hand. Thus, if Alice wants to clue the rainbow 2 with a color, Alice has a free choice between cluing red and cluing blue.
  * Alice clues blue to Cathy, which only touches the rainbow 2.
  * Bob knows that since Alice had a free choice and did not color-match with red, he should play his slot 1 instead of his slot 2.

#### The Free Choice Bluff

* It is possible to use the *Free Choice* convention to communicate to a teammate that you want a *Finesse* instead of a *Prompt* in order to get them to play an unrelated playable card from their *Finesse Position*.
* Like a normal *Bluff*, after a *Free Choice Bluff*, the player who blind-played does not necessarily have the "matching" card in their hand.

#### The Suboptimal Color Bluff

* Often, when giving a color clue to a Rainbow or dual-color card, you want to pick a color that will "fill-in" ancillary cards in the hand as to give the maximum amount of information.
* If a suboptimal color is chosen that does not fill in ancillary cards, it follows from *High Value Principle* that there must be a reason, so you should blind-play your *Finesse Position* card.
* This move is contextual in that you don't want to make it appear as if the clued card is currently unplayable. Thus, it is best performed as a *Reverse Bluff* or a *Long-Distance Bluff*.

### Dark Rainbow Saves

* This convention applies to any variant with a dark rainbow (touched by all colors and one of each) suit.
* Players should save dark rainbow 3 and dark rainbow 4 with a number clue.
* There are two exceptions to this:
  * if the color clue also touched another critical card (that is not dark rainbow)
  * if the color matches a suit that is already completely played or accounted for
* Note that this convention does **not** apply to the *Black & Dark Rainbow* variant. In that variant, you must save dark rainbow 3 and dark rainbow 4 with a black color clue.

### Color Blind Conventions

* These conventions apply to the *Color Blind* variants.
* Number clues mean the same thing as normal.
* All color clues have a special meaning:
  * Blue means play slot 1.
  * Green means play slot 2.
  * Yellow means play slot 3.
  * Red means play slot 4.
  * Purple means play slot 5 (in 2-player and 3-player games).
  * Purple means for two people to blind-play their *Finesse Position* card (in 4-player and 5-player games).
    * The two blind-plays do not necessarily have to be on two players in a row - they can be on anyone.
    * To reduce confusion, the purple clue should be given to the first player who will be blind-playing.
    * To reduce confusion, the purple clue is only legal if there are exactly two cards on *Finesse Position* (so that it won't be *Ambiguous*).
  * Orange means chop move.
* All color *Play Clues* have to be treated as potential *Delayed Play Clues*, *Prompts*, and *Reverse Finesses*.

### The Mismatch Finesse

* This convention only applies to *Color Blind* variants.
* If a player has two of the same playable card in their hand, players are expected to give a *Play Clue* to the left-most one.
* If a player instead gives a *Play Clue* to the right-most one, then they are trying to communicate something extra.
* This means that the next player should blind-play their *Finesse Position* as any unrelated playable card.
* *Mismatch Finesses* can also rarely give a player a safe discard.
* For example, on the first turn of a 3-player game:
  * Cathy has a red 1 in slot 1 and another red 1 in slot 2.
  * Alice clues green to Cathy, giving a *Play Clue* to Cathy's slot 2.
  * Bob knows that since Cathy had a duplicate card on slot 1 and slot 2, Alice was supposed to get the leftmost card, the slot 1.
  * Alice must be doing the *Mismatch Finesse*. Bob blind-plays his *Finesse Position*, and it is a blue 1.
  * Cathy assumes that Alice did a *Finesse* - due to Bob's blind-play, she must have the blue 2 in her slot 2. Cathy plays her slot 2, and it is revealed to be red 1.
  * Cathy now knows that it was not a normal *Finesse* at all - it was instead a *Mismatch Finesse*, because there is no other explanation for why Bob would blind-play from a *Play Clue* on a red 1.
  * Cathy also knows that she must have another red 1 in her hand. Since there is only one card to the left of her slot 2, she knows that the red 1 has to be exactly in her slot 1 (at the time of the clue).
  * Due to this, when Cathy needs to discard next, she will blind-discard her slot 2 card (since slot 1 has now shifted down to slot 2 after she played the red 1).

### The Negative Prompt

* This convention applies to the *Dual-Color (6 Suits)* variant.
* In this variant, since negative color information conveys just as much information as positive color information, you should include that when deciding which card to play into a *Prompt*.
* For example:
  * Alice has a red card in slot 1 and a red card in slot 2.
  * Alice is *Prompted* for a mahogany 2. (Mahogany is composed of red and black.)
  * Normally, Alice would play slot 1, since *Prompts* promise the left-most card.
  * However, Alice's slot 1 card has no negative clues, and her slot slot 2 card has a negative yellow clue.
  * Thus, this is a *Negative Prompt* and Alice plays slot 2 instead of slot 1.

### Multi-Fives Conventions

* These conventions apply to the *Multi-Fives* variants.

#### Multi-Five Saves

* Since 5's cannot be *5 Saved*, a number 2 clue must be used to save them as a pseudo-*2 Save*.

#### 4 Stalls & Early 4's Chop Move & 4 Pull

* In the *Early Game*, since it is not possible to clue number 5, players cannot *5 Stall*. However, we agree that a number 4's clue in the early game indicates that the card is really a 5. Thus, it is possible to *4 Stall*. (A *4 Stall* interpretation takes precedence over a *Self-Finesse*.)
  * This is only legal if the clue **only** touches real 5's. In other words, players may not give a *4 Stall* if touches a mix of 4's and 5's.
  * Similar to a *5 Stall*, if there are other things to do and a *4 Stall* is given, then it transforms into a *Early 4's Chop Move* or a *4 Pull*.
  * Once the *Early Game* is over, players may not *4 Stall*.

### Up or Down Conventions

* These conventions apply to the *Up or Down* variants.
* The *2 Saves* convention is turned off. (2's are not valuable in this variant.)
* The *3 Bluffs* convention is turned off. (3's are not valuable in this variant.)
* The *5 Stall*, *5's Chop Move*, and *5 Pull* conventions are turned off.
* At the beginning of the game, number 5's is a play clue (similar to a number 1's clue).
* If there are any stacks going up, a number 5 clue to a chop card is to be treated as a normal *5 Save*.
* If there are any stacks going down, a number 1 clue to a chop card is to be treated as a *1 Save*.

### Wild & Crazy Conventions

* These conventions apply to the *Wild & Crazy* variant.

#### Crazy 3 Saves & Crazy 4 Saves

* In this variant, it is possible to violate *Good Touch Principle* by cluing black to save a black 3 or a black 4, because there can be other useless rainbow cards in the hand.
* Thus, for the *Wild & Crazy* variant, a second exception to the *Black 3 and Black 4 Saves* convention is added:
  * if the number clue was required to avoid violating *Good Touch Principle*
* *Crazy 3 Saves* & *Crazy 4 Saves* do **not** apply to 5-player games; see the "Wild & Crazy 5-Player Alterations" section below.

#### 5-Player Alterations

* These conventions only apply to the *Wild & Crazy* variant with 5 players.
* Nearly all of the conventional "rules" are closely followed in 5-player games, regardless of the variant. And the same goes for 4-player games in the *Wild & Crazy* variant.
* However, 5-player *Wild & Crazy* is extremely difficult. Thus, we have slightly altered some conventions to be more "aggressive" in this game type:
  1) No *Crazy 3 Saves* and no *Crazy 4 Saves* – you must duplicate a rainbow card if you want to save a black 3 or black 4
  2) No Locked Hand Saves – locked players must perform a "hard burn" if they have no normal *Play Clues* or *Save Clues* or off-chop 5's to clue
* Besides these specific alterations, you should also account for the fact that the team will play more risky in general – more aggressive discards, more letting cards "ride" on chop, and so forth.

### Empty Clues

* *Empty Clues* are clues that touch no cards in a hand. On Hanabi Live, each game has the option to allow *Empty Clues*, and we typically disallow this option since it makes the game too easy.
* If *Empty Clues* are enabled, it allows for a much wider channel of information transfer. We have developed an entire convention framework around this channel and it is too complicated to cover in a single section here.
* If you are interested in learning about in the extended *Empty Clue* conventions, they are documented [on a separate page](https://github.com/Zamiell/hanabi-conventions/blob/master/misc/Empty_Clues.md).

<br />

## Level 3 - Rarely Used Advanced Strategies

### Hard Bluffs

* Sometimes, it can be ambiguous as to whether a player blind-played a card into a *Bluff* or a *Finesse* + *Prompt*. In this situation, *Occam's Razor* applies, so players should always opt with the former (simpler) interpretation. When such a *Bluff* occurs, it is called a *Hard Bluff* to disambiguate from situations where *Bluffs* happen with no ambiguity.
* For example, this is a *Finesse* + *Prompt* and **not** a *Hard Bluff*:
  * Only red 1 is played on the stacks.
  * Cathy has a 3 clued in her hand (with no color information on it).
  * Alice clues Cathy about a brand new 4.
  * Bob blind-plays red 2.
  * In a normal *Bluff*, a one-away from playable card is clued. However, Cathy sees that the highest stack is the red stack, so the 4 in her hand must be two-away.
  * Thus, Cathy does **not** read it as a *Bluff*; she is promised red 3 and red 4, so she plays the unknown 3 as a *Self-Prompt* on the red 3.
* For example, this **is** a *Hard Bluff*:
  * Red 1 and blue 2 are played on the stacks.
  * Cathy has a 3 clued in her hand (with no color information on it).
  * Alice clues Cathy about a brand new 4.
  * Bob blind-plays red 2.
  * This could be a *Bluff* if the 4 in her hand is blue 4, since blue 4 is currently one-away from playable. Thus, Cathy **does not** assume that her 4 is red 4, and subsequently, does **does not** assume that her unknown 3 is a red 3. However, it could **also** be the case that the 4 is a red 4 (if the 3 in her hand happens to be red 3).
  * Thus, Cathy marks down both possibilities for later and does not play anything right now.

### 2 Saves (Off Chop on the First Turn)

* On the first turn of the game, it is not possible to discard. If there is absolutely nothing else to do, it is permissible in this situation to use a number 2 clue to save a 2 that is **not** on chop, but only if the other players can see that you had no other choice.
* This situation typically only happens in 3-player games.

### The Fake Save

* We are only able to perform *Save Clues* on specific cards and in specific ways, as outlined in the Beginner's Guide. For example, we all agree that we must save 5's with number 5.
* In some specific circumstances, the team will have only one clue available and multiple cards must be saved with a single clue. In this situation, to prevent losing the game (or losing a currently-playable card), it is permissible to "lie" to the player and perform a non-legal *Save Clue*. The player will mark their chop card as something other than what it really is, so this move commits the team to giving a *Fix Clue* at some point in the future.
* For example, in a 3-player game:
  * Alice has 1 clue available.
  * Bob has a red 5 on chop, followed by a red 4. The other copy of the red 4 is in the discard pile, so there are two critical cards in a row.
  * Alice is not allowed to save the red 5 with a red clue, because then it would look like a *Save Clue* on a red 4.
  * However, if Alice clues number 5 to Bob, then he will discard the red 4.
  * Thus, Alice performs a *Fake Save* on both red cards by cluing red.
  * Bob will mark his chop as the red 4, so the team will have him number 5 as a *Fix Clue* at some point in the future. At that point, he will be able to retroactively see that Alice was in a very tight spot and had to give a *Fake Save*.

### The Unnecessary Generation Discard

* Sometimes, in order to satisfy *Save Principle*, a player will perform an unnecessary *Generation Discard*, which generates a clue to save a card that they actually already have in their hand.
* This puts the next player in an ambiguous situation: was it really a *Generation Discard*, or could it a *Scream Discard*? In order to cover both situations, they should not *Chop Move*, but they should also not discard on this turn.
* For example, in a 3-player game:
  * Red 3 is played on the stacks. No blue cards are played on the stacks.
  * Alice has a blue 1 in her hand. She knows the exact identity of it, so it is known playable.
  * Alice also has a 4 clued in her hand. She does not know what color it is.
  * There are 0 clues, so if Alice plays the blue 1, Bob will be forced to discard.
  * Alice sees that Cathy has a red 4 on chop, which is playable. If Alice does not have red 4 in her hand, then Cathy could potentially discard the red 4 (after Bob is forced to discard).
  * So, Alice performs a *Generation Discard* to generate a clue so that Bob can clue the get the red 4, if necessary.
  * Bob sees that Alice does indeed already have the red 4 in her hand, so from his perspective, if Alice was performing a *Generation Discard*, it was unnecessary.
  * However, it could also be the case that Bob's chop is unsafe. So, Bob will **not** clue the red 4 on Cathy's chop, but he **will** spend the clue in some other productive fashion. If Bob has nothing productive to do, he must "burn" a clue, similar to what happens when a *Scream Discard* occurs.

### The Composition Discard

* In rare cases, it is possible for a discard to be both a *Scream Discard* and a *Generation Discard* at the same time, for two different players.
* For example, in a 4-player game:
  * There are 0 clues in the bank.
  * Alice needs to plan ahead for her turn.
  * Bob and Donald both have a critical chop card. Cathy has a safe discard.
  * Alice and Bob both have one known playable card in their hand. 
  * So, if Alice plays, Bob will perform a *Generation Discard*, and discard a critical card. This is not an option.
  * Therefore, Alice must discard. This is a *Scream Discard* to Bob, and he should *Chop Move*. It is also a *Generation Discard* to Cathy, and she should not *Chop Move*.

### The Fresh Play Clue (for Locked Players)

* If a player's chop is their slot 1, *Locked* players are **not** allowed to *Locked Hand Save* it. This follows from basic logic: it would be unlikely for a player with a *Locked Hand* to want to lock another player on the team with a non-critical card.
* Therefore, when a slot 1 chop card is clued by a *Locked* player, a *Play Clue* interpretation always takes priority over a *Locked Hand Save* interpretation.
* This type of *Play Clue* is called a *Fresh Play Clue* in order to disambiguate it from a *Locked Hand Save*.

### Double Tempo Clue Inversion (Immediate Double Clue)

* If you are clued the exact same thing twice before it gets to be your turn, it means that you can play **all** of the cards that the clue applies to, but in the opposite order than normal (right-to-left, since you would normally play cards from left-to-right).
  * If one of the cards includes the chop card, it means to play all of the cards from 2nd oldest to newest, and then the chop last.
* If you are re-clued about a bunch of cards after you have already taken a turn, see the *Double Tempo Clue* section.

### Spillover Chop Move

* If an *Order Chop Move* or a *Trash Order Chop Move* is performed, but the player who is supposed to *Chop Move* already has every single card in their hand clued, then this is very strange.
* In this situation, the *Chop Move* should "skip" over that player and *Chop Move* the next person after that.

### The Elimination Riding Deduction Bluff

* Typically, when a player has two cards with *Elimination Notes* and the "true" copy of the card is on chop, you must clue it to let them know.
* However, if the other card is also playable, you can "lie" to them and not clue anything.
* Next, the player should perform an *Elimination Riding Deduction*, and play the unrelated card.
* After that, there will be only one card left with an *Elimination Note*, so they will go on to play the "true" card on their next turn.

### The Elimination Finesse

* Normally, if a player is *Finessed*, they are supposed to play their *Finesse Position* card. However, if the player has two or more *Elimination Notes* in their hand for the specific *Finessed* card, then they know that it cannot be on *Finesse Position*.
* In this situation, the player is expected to play the **oldest** of the cards with the *Elimination Notes* on them (not counting *Chop Moved* cards, if any).
* For example, in a 3-player game:
  * Blue 2 is played on the stacks.
  * Alice has a completely unclued hand.
  * Alice discards a blue 3. She writes *Elimination Notes* for the other blue 3 on slots 2, 3, 4, and 5.
  * Bob clues Cathy blue, which touches a blue 4.
  * Cathy discards.
  * Alice knows that this is some sort of *Reverse Finesse*, as it is calling for the blue 3. However, the blue 3 cannot be in her *Finesse Position* (slot 1), as she knows from the *Elimination Notes* that it must be either on slot 2, 3, 4, or 5. So it must instead be a *Reverse Elimination Finesse*.
  * The *Elimination Finesse* promises that it is her oldest card, so she plays slot 5 as blue 3.
* As mentioned above, *Chop Moved* cards should be skipped over when finding the *Elimination Finesse* target. If there are two or more cards with *Elimination Notes* on them and they are all *Chop Moved*, then the oldest *Chop Moved* card should be played.
* *Elimination Finesses* apply to **all** types of situations with *Elimination Notes* (including *Discard Elimination Notes*, *Play Elimination Notes*, and *Double Discard Elimination Notes*). Subsequently, you can more specifically describe an *Elimination Finesse* as a *Discard Elimination Finesse*, a *Play Elimination Finesse*, or a *Double Discard Elimination Finesse*.
* Note that normal *Finesses* take priority over *Self-Elimination Finesses*. For example:
  * On the stacks, blue 2 and green 2 are played.
  * Alice has *Elimination Notes* on slot 3 and slot 4 for red 3.
  * Someone clues a number 4 in Alice's slot 1 as a *Self-Finesse*.
  * Alice must assume that it is a normal *Self-Finesse* and play blue 3 from slot 2. (If it was an *Elimination Self-Finesse*, she would play red 3 from slot 4.)

### The Speculation Elimination Finesse

* In a normal *Elimination Finesse*, the right-most card is called for.
* However, if an *Elimination Finesse* calls for a card that specifically has *Speculation Elimination Notes* on it, then the **left-most** card is called for instead of the right-most card.

### The Chop Transfer

* Sometimes, cards are accidentally chop moved through a mistake or through a complicated situation. In these kinds of situations, it is pointless to waste a clue to "undo" the chop move; you can just continue to allow them to discard normally. That is, until they get something good on chop.
* Only then will the team bother cluing the chop directly to convey that it is useless. And then, the player receiving the clue will know that the card they were about to discard is important, and permanently chop move that card, and discard the now known useless card.
* Thus, this is nearly the same thing as a *Early Fix Clue Chop Move*, but when the *Fix Clue* is given to a card that was already chop moved (and had no positive clues on it already).

### The Scream Blind-Play (Blind-Playing Chop)

* The *Scream Discard* is a powerful last-resort move that "screams" at the next player, telling them that their chop is unsafe. This is useful because you can do it even when the team is currently at 0 clues. However, you can only perform this move if you have a known playable card in your hand. In some situations, you will need to "scream" at the next player even when you do not have a known playable card.
* If you can't give a clue, as a last resort you can send a signal to your teammate by blind-playing a card. You don't want to accidentally blind-play a critical card, so the safest card to blind-play is your chop.
* By doing this, it "screams" at the next player, accomplishing the same thing as a Scream Discard, namely:
  * they should chop move a card
  * if there are 1 or more clues in the bank, they are not allowed to discard on their next turn
* If you see someone blind-play their chop and it works, your first thought may be that it could be a *Scream Blind-Play*. However, it could also be a *Negative Blind-Play* (which is covered later), so it is important to not confuse these two strategies.
* Note that a *Stop Blind-Play* (listed below) is almost exactly the same as this move, but it has a completely different interpretation. Whether or not a move is a *Scream Blind-Play* or a *Stop Blind-Play* is entirely dependent on the context of the situation.

### The Stop Blind-Play (Blind-Playing Chop)

* Sometimes, due to a mistake or a complicated situation, you can see that the next player after you is going to misplay a critical card. Additionally, there may be no "fix" clue that you can give that will remedy the situation, or perhaps you are currently at 0 clues.
* If you can't give a clue, as a last resort you can send a signal to your teammate by blind-playing a card. You don't want to accidentally blind-play a critical card, so the safest card to blind-play is your chop.
* By doing this, it sends an emergency signal to the next player, warning them to **stop** whatever it is they were about to do.
* If you see someone blind-play their chop and it works, your first thought may be that it could be a *Stop Blind-Play*. However, it could also be a *Negative Blind-Play* (which is covered later), so it is important to not confuse these two strategies.
* Note that a *Scream Blind-Play* (listed above) is almost exactly the same as this move, but it has a completely different interpretation. Whether or not a move is a *Scream Blind-Play* or a *Stop Blind-Play* is entirely dependent on the context of the situation.

### The Whisper Discard Chop Move

* Occasionally, a player will have known trash in their hand. They are always expected to discard the known trash first before discarding their right-most unclued card.
* Thus, if a player instead discards their right-most unclued card instead of the known trash, it must be a signal that something is wrong, exactly like a *Scream Discard*. This is more subtle than a *Scream Discard* though, so it is called a Whisper Discard.
* *Whisper Discards* are to be treated identically to *Scream Discards*. In short, this means that they 1) cause a *Chop Move* and 2) force a clue to be given on the next turn.

### The Echo Scream Discard Chop Move

* A *Scream Discard Chop Move* is done only as a last resort. So, if the next player has an unimportant card on chop, then the move is usually a *Generation Discard* and does not chop move anyone.
* However, what if a *Scream Discard* is done and the next player has either:
  * a known playable card
  * a known safe trash discard
* Since *Scream Discards* are only done as a last resort, the clue must have some other meaning. So, it *Chop Moves* both the next player **and** the player after that. This is called an *Echo Scream Discard*, because it "bounces" off the next player and travels to the next player after that as a "double scream".
* Similar to a normal *Scream Discard*, all of the players who are *Chop Moved* are not allowed to discard on their next turn.
* In the unlikely scenario where **two** people in a row have known plays / known safe discards, then the *Echo Scream Discard* will bounce off of two people and perform **three** *Chop Moves* in total. (And three people in a row cause four chop moves, and so forth.)
* An *Echo Whisper Discard* works in the same way.

### The Double Scream Discard Chop Move

* If a player has a known playable card and a known trash card, and they discard instead of playing, then that is a *Scream Discard* and the next player should *Chop Move*.
* If a player has a known playable card and two known trash cards, and they discard the oldest trash card instead of playing, then that is both a *Scream Discard Chop Move* and a *Trash Order Chop Move* at the same time.
* In this situation, the next player should *Chop Move* twice.

### The Stop Discard

* Normally, when someone discards with a known play and the next player already has something to do, it is an *Echo Scream Discard*.
* However, it could also be the case that the next player after that does not have a playable/critical card on chop. Or, alternatively, it could be the case that **everyone** has something to do on their turn. Thus, discarding is normally considered a mistake.
* If the player who is discarding is not making a mistake, then they are communicating that the very next player with a "known play" should **stop** what they are doing, because the card is not actually playable.
* This is very similar to a *Stop Blind-Play*, but since the player has a known play, there is no reason to use up one of the strikes when the same message can be communicated in a safer way.
* If there is a card that could potentially be playable on on chop, then the *Echo Scream Discard* interpretation takes priority over the *Stop Discard* interpretation.

### The Double Half Bluff

* Sometimes, you see that two players in a row have playable *Finesse Position* cards. However, they are unrelated, so you can't get them both played with a *Double Finesse*. In this situation, by performing a clue that looks like a *Double Finesse*, you can get the first card played like a normal *Finesse* and the second card like a *Bluff*.
* For example, on the first turn of a 4-player game:
  * Alice clues Donald red, which touches a red 3 as a *Play Clue*.
  * Bob goes next and assumes that it is a *Double Self-Finesse* - he has the red 1 and red 2 in his two newest slots. Thus, he blind-plays his left-most and it is red 1, as expected.
  * Cathy goes next. Cathy sees that Donald does **not** have red 2 in his next newest slot, so she must have the red 2. Cathy blind-plays her left-most card. However, it is **not** the red 2, but the blue 1.
  * Bob now knows he does not have the red 2 anymore, since Cathy blind-played.
  * Cathy now knows that since two blind-plays happened in a row, she does **not** have the red 2 and that she was *Bluffed*.
  * At first, Donald thought that the red card in his hand was red 1 (as a *Play Clue*).
  * After Alice blind-played, Donald thought that the red card in his hand was red 2 (as a *Finesse*).
  * After Bob blind-played, Donald knows that he must have the red 3 (as a *Double Half Bluff*).
* Normally, you are only allowed to *Bluff* while in *Bluff Seat*. But *Double Half Bluffs* do not violate *Good Lie Principle*, so we allow them.

### The Double Bluff

* Similar to a *Double Half Bluff*, it is also possible to get 2 cards played in a row that are completely unrelated.
* For example, in a 4-player game:
  * Red 2 is currently played on the stacks.
  * Alice clues Donald red, which touches a red 5 as a *Play Clue*.
  * Since red 5 is playable right now, Bob thinks he has the red 3 and the red 4. Bob blind-plays his *Finesse Position* card, but it is actually a blue 1.
  * Cathy sees that Bob blind-played because of the red clue. However, since the red 5 is a two-away card instead of one-away card, it must mean that it is a *Double Bluff* instead of a single *Bluff*. Cathy blind-plays her *Finesse Position* card and it is yellow 1.
  * At first, Donald thought that the red card in his hand was red 3 (as a *Play Clue*).
  * After Alice blind-played, Donald thought that the red card in his hand was red 4 (as a *Bluff*).
  * After Bob blind-played, Donald knows that he must have the red 5 (as a *Double Bluff*).
* Normally, you are only allowed to *Bluff* while in *Bluff Seat*. But *Double Bluffs* do not violate *Good Lie Principle*, so we allow them.

### The Triple Bluff / The Triple Two-Thirds Bluff

* Following from the *Double Bluff* convention, it is possible to perform a *Triple Bluff*. For example, on the first turn of the game:

![Triple Bluff](img/triple_bluff.png)

* In this screenshot, if Zealousy blind-played a red 2 from newest **and** the focus of the initial clue was red 4, then it would be a *Triple Two-Thirds Bluff* instead of a *Triple Bluff*.

### The No-Information Double Finesse & The No-Information Double Bluff

* Sometimes, cards are re-clued in order to initiate a *Finesse* or a *Bluff*. Most times, the clue will "fill in" or give extra information to the existing card.
* Other times, the clue will give no information (e.g. re-cluing number 3 to an already known 3). In this situation, if it was merely a *Bluff*, it would be pretty low value.
* Thus, by convention it **must** "get" at least 2 new cards (as opposed to a single *Bluff* that only gets 1 brand new card).
* For example, in a 3-player game:
  * Nothing is played on the stacks.
  * Alice clues 3's to Cathy, which touches one 3, the red 3.
  * Bob blind-plays blue 1. At this point, everyone knows that Alice has performed a *3 Bluff*, and from Cathy's perspective, her 3 can be any 3 at all.
  * Cathy discards.
  * Alice clues 3's to Cathy, which re-touches the red 3 (and gives no additional information to it).
  * Bob blind-plays red 1. If this was a *3 Bluff*, then no-one would be promised the red 2. However, since no new information was given, it must be a *No-Information Double Finesse*. Bob sees that Cathy does not have the red 2, so he must have the red 2, and can blind-play it on his next turn.
* Usually, a "no-information" clue conveys a *Double Finesse*. But you can also use it to perform a *Double Bluff* (or a *Double Half Bluff*). For example, in a 3-player game:
  * Nothing is played on the stacks.
  * Alice clues 3's to Cathy, which touches one 3, the red 3.
  * Bob blind-plays blue 1. At this point, everyone knows that Alice has performed a *3 Bluff*, and from Cathy's perspective, her 3 can be any 3 at all.
  * Cathy discards.
  * Alice clues 3's to Cathy, which re-touches the red 3 (and gives no additional information to it).
  * Bob blind-plays green 1. If this was a *3 Bluff*, then no-one would be promised the green 2. However, since no new information was given, it must be a *No-Information Double Finesse*.
  * Cathy sees that Bob does not have the green 2, so she must have the green 2, so she blind-plays her *Finesse Position* card, and it is yellow 1 instead of green 2.
  * Since two cards were blind-played (that did not match), everyone now knows that the *No-Information* clue was a *Double Bluff* instead of a *Double Finesse*. From Cathy's perspective, her 3 can (still) be any 3 at all.

### The Bad Touch Finesse (For 1's)

* In the *Trash Finesse* / *Trash Bluff*, it is possible to clue number 1 to a player in order to get someone to blind-play a card.  After the blind-play, it is understood that all of the 1's are trash.
* However, what if this is done on the first turn of the game, touching two 1's? If nothing is played on the stacks, then the 1 of every single suit is needed. In this situation, both of the 1's that are clued cannot be trash.
* In this situation, the 1's clue only communicates that *Good Touch Principle* was violated and that both of the 1's are the same suit.
* For example, on the first turn of a 3-player game:
  * Alice clues number 1 to Cathy, touching two red 1's.
  * Bob sees that Alice could have done something else (like do a *5 Save* to a 5 on Cathy's chop).
  * Bob knows that Alice's clue violated *Good Touch Principle*. If the clue is not communicating something extra, then it would be a real lousy clue. Therefore it must be a *Good Touch Finesse*, so Bob blind-plays his *Finesse Position* card, and it is a blue 1.
  * Cathy knows that since this is the first turn of the game, both of her 1's cannot be trash. Similar to a *Stale 1's Clue*, Cathy skips over the older 1 and plays the newest 1. (She would normally play her 1's from right-to-left.) She will then discard the other 1 later.

### The Bad Touch Double Finesse & The Bad Touch Double Bluff (For 3's)

* Normally, a *3 Bluff* takes priority over a *Double Finesse*. This means that if someone clues a blue 3 using the number 3, and then a blue 1 blind-plays on the very next turn, no-one is promised the blue 2.
* However, if **both** blue 3's were touched with the number 3 clue, then that would violate *Good Touch Principle*, and this would be considered a "bad touch".
* If someone is violating *Good Touch Principle*, they must have a very good reason, so the clue must be a *Double Finesse* instead of a *3 Bluff*. In the above example, the next player should blind-play the blue 2 from their *Finesse Position*.
* After that, the player who received the clue can safely discard the focused 3.
* In the same way, it is also possible to *Bad Touch Double Bluff* (or *Bad Touch Double Half Bluff*) in order to get unrelated cards played from *Finesse Position*.

### The Suboptimal Save Prompt & The Suboptimal Save Finesse

* If the other copy of a card is in the trash already, then the remaining copy needs to be saved. These cards are allowed to be saved with either a color clue or a number clue.
* If both types of clues will **only** introduce one new card, then it is said that that there is a "free choice" between the two clue types.
* In this situation, the clue type will be chosen that "fills in" the other ancillary cards in the hand or gives important negative information.
* If a clue type is chosen that is clearly worse than the other one, then the clue giver must be trying to communicate something extra.
* The means that this innocent-looking *Save Clue* is really a *Play Clue*, and all of the in-between cards are called for.

### The Sacrifice Discard

* It is generally undesirable for a player to have a "fully locked" hand, but sometimes it happens. And sometimes, one card in the locked hand is useful in the future, but not critical (meaning there is another copy of the card in someone else's hand or still in the deck).
* Normally, you are never supposed to discard cards that have clues on them, as if you do, it implies a *Sarcastic Discard* or a *Gentleman's Discard*. However, in this situation, the player who is locked can choose to "sacrifice" one of the cards in their hand that is non-critical. And in this situation, it does **not** imply a *Sarcastic Discard* or a *Gentleman's Discard*.

### Self-Bluffs with Color Clues (illegal)

* It is possible (and fairly common) to perform a *Self-Bluff* on a player with a rank clue.
* For example, in a 3-player game:
  * Red 2 is played on the stacks.
  * Alice clues number 4 to Bob, which touches one brand new 4 as a *Play Clue*.
  * Bob knows that this is probably red 4, but he does not see any red 3's. Thus, Bob knows he must have the red 3, and blind-plays his *Finesse Position* card. It is blue 1.
  * Bob now knows that he was *Bluffed* and that the 4 in his hand is exactly red 4.
* *Self-Bluffs* on players with color clues are nonsensical, so players should not have to entertain that possibility. 
* For example, in a 3-player game:
  * Red 2 is played on the stacks.
  * Alice clues red to Bob, touching one brand new red card  as a *Play Clue*.
  * Bob has a negative 3 clue on his red card, so he knows it cannot be red 3.
  * Bob does not see any red cards in other player's hands.
  * Bob cannot have the red 3 in his *Finesse Position*, because that card has negative red.
  * Bob now needs to figure out what the clue means. When going through all of the possibilities, he can safely put aside the possibility of a *Self-Bluff with Color* / a *Known Self-Bluff*, because we agree that they are illegal. The clue must have some other meaning and Bob will defer to whatever the next-most-likely thing is.

<br />

## Level 4 - Rarely Used Expert Strategies

### The Top Hat Clue

* Since the *Layered Gentleman's Discard* is so efficient, clever players that see the opportunity to perform one will almost always want to do so.
* Thus, it follows that in rare cases, when a teammate gives you a play clue on some card, they **do not** intend for you to play it. They intend for you to see the opportunity for a *Layered Gentleman's Discard*, and then immediately discard the card.
* This kind of clue is called a *Top Hat Clue* because you are giving them an opportunity to be a gentleman.
* Note that you should not mistake a *Top Hat Clue* for a clue that initiates a *Layered Finesse*. You are only allowed to discard the card if you can determine its exact identity.

### The Certain Finesse Clandestine Exception

* This section outlines a specific and rare edge-case for *Certain Finesses*.
* We agree that *Bluffs* take precedence over *Certain Finesses*. This means that a *Certain Finesse* cannot normally be performed from *Bluff Seat*.
* *Certain Finesses* **can** be performed from *Bluff Seat* if it is strictly impossible to be a *Bluff*. In other words, this means that it is illegal for a player to perform a *Clandestine Finesse* on the very next player that targets a potentially duplicated card **and** the other player can rule out the possibility of a *Bluff*.
* For example, in a 3-player game:
  * All of the 2's & blue 3 is played on the stacks. Green 3 is in the discard pile.
  * Alice has an unknown 3 in her hand that happens to be the red 3.
  * Alice clues number 4 to Cathy, touching a red 4 as a *Play Clue*.
  * Bob knows that Alice could be trying to perform a *Finesse* on a red 3. Normally, he would blind-discard his *Finesse Position* card as a *Certain Discard* in order to pass this card back to Alice.
  * However, Bob also knows that this might be a *Bluff*. But wait - his *Finesse Position* card has negative blue on it. So anything that he blind-plays here would have to be a 3. Thus, this cannot be a *Bluff*, since a 3 would match a 4 and look like a *Finesse*.
  * The only other possibility that Bob has to worry about is a *Clandestine Finesse*. For example, he could be blind-playing a green 3 **and then** a red 3 after that. If he blind-discarded, that could "kill" the green stack, since the other copy of green 3 is already discarded.
  * However, Bob **also** knows that you are not allowed to perform a *Clandestine Finesse* from *Bluff Seat* that could duplicate a card in your hand. Thus, he can discount both the possibility of a *Bluff* **and** the possibility of a *Clandestine Finesse*.
  * Bob performs a *Certain Discard* on his *Finesse Position* card and it is the red 3, successfully passing it back to Alice.
* If someone performs a *Certain Discard* and you have two or more clued cards that could be the target, then you are not promised the order, only that you have the card clued somewhere in your hand. (This part works in the exact same way as a more-ordinary *Sarcastic Discard*.)

### The Declined 5's Finesse

* The *5's Chop Move* is typically used to save a 5 and a critical non-5 at the same time. This is very efficient, because it saves both cards with one clue instead of having to spend two clues.
* So, when a player has this strategy available, but instead declines to do it and clues the critical card on chop directly (without touching any other cards), then this is quite strange.
* In this situation, the player must be trying to communicate something extra. Similar to an *Occupied Finesse*, the player is trying to signal that this seemingly innocent *Save Clue* is actually a *Play Clue* instead. Someone on the team must have the cards to make this critical card playable.
* In some situations, the blind-player may have to defer playing into the *Finesse* and instead give a *5 Save* to the player with the (now) unsafe chop. If they do, then this is not a problem - the clue receiver can retroactively determine that a *Declined 5's Finesse* has occurred and should not *Stomp* on the *Finesse*.

### The Elimination Bluff / The Elimination Layered Finesse

* It is possible to lie to a player who has *Elimination Notes* on their hand and pretend like you are performing an *Elimination Finesse* on them, causing them to play their oldest card as per the convention. This can cause an unrelated playable card to play.
* If the player who performed the clue was in *Bluff Seat*, then it is to be treated like a *Bluff*, and thus they will not know where the actual *Elimination Card* is. (However, in most cases, at this point there will only be one remaining card with an *Elimination Note* on it, so it won't matter.)
* If the player who performed the clue was not in *Bluff Seat*, then the blind-playing player is expected to keep playing until they find the intended card. This is similar to how a *Layered Finesse* works, but it is inverted such that they play cards from oldest to newest.

### The Patch Finesse

* If a player performs a *Layered Finesse* through a card that is one-away from being playable, it is possible to see that an impending misplay will occur.
* This is a signal to you that you need to "patch" the problem, so you have the matching card in your *Finesse Position* to make the one-away card actually playable.
* In general, you must give preference to a patch interpretation. However, it is illegal to perform a *Patch Finesse* when the player blind-playing the patching card comes after the player blind-playing into the *Layered Finesse*. Another way of saying that is that the *Patch Component* of the *Patch Finesse* cannot be in reverse.

### The Patch Gentleman's Discard

* Similar to a *Patch Finesse*, a *Gentleman's Discard* can also contain a *Patch Component*.

### The Repair Finesse

* Often times a player will have two similar clued cards in their hand with the left-most being unplayable and the right-most being playable. In this situation, you cannot use a *Prompt* to "get" the cards, since the left-most would misplay.
* What if someone does a *Prompt* on the right-most card, intentionally setting up the *Prompted* player to misplay their left-most card? The cluer must be communicating something deeper.
* If the card that is going to misplay is exactly one-away from being playable, then this should be treated as a *Finesse* on the one-away card. By blind-playing the card, it will "repair" the problem, and the *Prompted* player will no longer misplay anything.
* Note that the *Repair Finesse* will only work in the situations where the "repairing" blind-play will not stop the *Prompted* player from playing. In order words, if a *Prompted* player sees a blind-play immediately after a clue, they will assume that a normal *Bluff* has occurred, which is the simplest interpretation.
* The *Repair Finesse* is extremely similar to the *Patch Finesse*, with the difference being that the blind-play fixes a player playing a chain of *Prompted* cards instead of a chain of cards inside of a *Layered Finesse*.
* Examples:
  * Game #16695, turn 10

### The Reverse Bluff / The Out-of-Position Bluff (O.O.P. / OOP)

* Similar to a *Reverse Finesse*, it is possible to perform a *Reverse Bluff*. However, according to *Good Lie Principle*, you are only allowed to lie to the player who comes immediately after you, so this is illegal.
  * Why this policy? It is not possible to play with both *Layered Finesses* and *Reverse Bluffs* at the same time, and *Layered Finesses* are much better.
* However, you **can** rarely break the *Bluff Seat* rule if one of the following is true:
  * 1) the next player is at 0 clues (and won't blind-play anything / will blind-play an unrelated card)
  * 2) the next player will think that they have the *Bluffed* card in their own hand and will play something else (instead of *Finessing* or *Bluffing* the next player)
  * 3) the next player has negative information on their entire hand (so that they know they do not have the correct card)
* Essentially, #1 or #2 is true, then the next player cannot act on their state of misinformation. And if it is #3, then the next player will have full knowledge that a lie is occurring, so they will not mess anything up.
* Since valid *Reverse Bluffs* are so rare, it is important to remember that a valid *Reverse Bluff* is distinct from a *Layered Finesse*, and that blind-playing should stop after the first blind-play. (This is a common mistake.)

### The Good Touch Bluff

* Care has to be taken so that a *Bluff* does not look like a *Finesse*. For example, in a 4-player game:
  * Red 2 and blue 2 are played on the stacks.
  * Alice clues Cathy number 4, which touches a red 4.
  * Bob blind-plays a blue 3 from his *Finesse Position*.
  * Since 3 matches 4, Cathy knows she has the blue 4, and goes on to misplay red 4 as blue 4.
  * Thus, Alice should not have given this clue.
* However, what if in the same example, Donald **already** has a blue 4 clued in his hand. Now, Cathy will know that she does **not** have the blue 4, because then Alice's clue would have violated *Good Touch Principle*. Cathy will instead know that the 4 is some **other** one-away from playable 4.
* Furthermore, Donald can see that the above occurred and will know that he definitely has the blue 4 clued in his hand (if he did not know already).

### The Disease Bluff & The Heal Clue & The Double-Copy Bluff & The Pestilent (Double) Bluff

* In the *Good Touch Bluff*, a *Bluff* is given that looks like a *Finesse*. However, what if something that looks like a *Good Touch Bluff* is done, but the "matching" card is not yet clued?
* For example, on the first turn of a 4-player game:
  * Alice goes first.
  * Bob has a red 1 on slot 1 and a blue 2 on slot 2.
  * Alice clues Bob number 2, which touches the blue 2 on slot 2.
  * Bob doesn't see any other 1's on *Finesse Position*. Thus, the number 2 clue must be a *Self-Finesse*, so he blind-plays red 1.
  * Cathy comes next. From her perspective, Bob should currently think that his slot 2 card is red 2 (instead of blue 2). If nothing else happens, Bob will go on to misplay that card.
* From Cathy's perspective, there are 5 possible situations:

#### 1) A *Disease Bluff*

* Say that Cathy sees the red 2 in Donald's hand and she can uniquely clue it. If she does, Donald will go on to immediately play it.
* This would "heal" the problem, as Bob would not think that he has red 2 anymore. Thus, this clue is called a *Heal Clue*.
* The original *Bluff* is called a *Disease Bluff*, since it requires healing.
* The *Disease Bluff* interpretation is the highest priority interpretation!

![Disease Bluff](img/disease_bluff.png)

#### 2) A *Double-Copy Bluff* (with Cathy seeing one uncluable copy)

* Say that Cathy sees the red 2 in Donald's hand, but she cannot uniquely clue it due to other blocking cards.
* This cannot be a *Disease Bluff*, since Alice would not put Bob and Cathy in this bad situation if a clean *Heal Clue* was not available.
* Cathy should instead conclude that she has the other copy of red 2 somewhere in her own hand. If she does, Bob will **not** go on to misplay the blue 2 because he will see both copies.

#### 3) A *Pestilent (Double) Bluff* (with Cathy seeing zero copies):

* Say that Cathy does not see the red 2 anywhere.
* From *High Value Principle*, Cathy can conclude that Alice does not intend for Cathy to do a *Fix Clue*, as that would be inefficient.
* Instead, Cathy can blind-play her *Finesse Position* card as red 2. This is similar to a *Disease Bluff*, but instead of wasting a clue to heal the problem, the problem is healed by a blind-play.
* Note that Cathy could be blind-playing red 2, but could also be blind-playing **any** playable card. Whatever card it is, it will still heal the problem, since Bob can see that the blind-play was related to the clue he received.
* This is similar to a *Double Bluff*, but is different because the move was not initiated by a card that was 2-away from being playable.
* Note that in this situation, it could be possible for Cathy to have both red 2's in her hand and not necessarily have anything playable on *Finesse Position*. But by convention, the clue giver is intending her to play her *Finesse Position* card.

### The Rank Choice Bluff & The Rank Choice Finesse

* *Reverse Finesses* take precedence over *Bluffs*. This means that you cannot use cards to *Bluff* that have "matching" cards in the *Finesse Position* of other players, since the player you want to *Bluff* will pause to give a chance for the matching cards to play first.
* However, in some rare situations, when initiating a *Reverse Finesse*, you have a free choice between a color clue and a rank clue, meaning that both rank and color will **only** touch the one target card.
* By convention, if you use rank instead of color, you communicate that you really want a *Bluff* to happen, and that the next player should **not** wait for other matching cards to play first. This is called a *Rank Choice Bluff*.
* After communicating that you want a *Rank Choice Bluff* to happen, the next player will blind-play their *Finesse Position* card. But if that card matches the clued card, then it was actually a *Rank Choice Finesse* instead of a *Rank Choice Bluff*. A *Rank Choice Finesse* may be preferable to a (more ordinary) *Ambiguous Finesse*, which will resolve more slowly.
* Note that it is possible to use the *Rank Choice* convention with any kind of *Bluff*. Thus, it is possible to *Rank Choice 3 Bluff*, *Rank Choice Double Bluff*, *Rank Choice Triple Bluff*, and so forth.
* Examples:
  * Game #8129, turn 4 (cluing Hyakinthus' yellow 3)

### The Rank Choice Save Finesse

* When saving a card, players have to choose carefully between using a color clue or a rank clue. However, in some rare situations, it makes absolutely no difference which clue is used:
  * Both color and rank would only touch the specific card.
  * Both color and rank would communicate the exact identity of the specific card.
  * Both color and rank would not give any useful negative information to the other cards in the hand.
* In these situations, the player giving the clue has a completely free choice between rank and color. We agree that by default, players should use color to save the card.
* If players instead use a rank clue to save the card, this communicates a *Rank Choice Save Finesse*. (This is similar to the more-ordinary *Rank Choice Finesse*, except it is initiated with a *Save Clue* instead of a *Play Clue*).

### The Surreptitious Self-Finesse

* *Clandestine Finesses* are when a color or rank clue "matches" the card from a blind-play, but the clue receiver must wait for **additional** matching playable cards to blind-play. Another way of saying this is that *Clandestine Finesses* have a *Misplay Component*; if the blind-player does not continue to blind-play cards, then the clue receiver will go on to misplay the "matching" card.
* A similar situation can also happen when a rank clue "matches" the card from a blind-play, but the clue receiver sees NON-MATCHING rank cards in the blind-player's hand that are currently playable.
* If the clue receiver waits for these non-matching cards to blind-play, and they **do** blind-play, then it means that the original clue had a *Self-Finesse* component to it. This is called a *Surreptitious Self-Finesse* in order to disambiguate it from a more ordinary *Clandestine Finesse*.
* *Surreptitious Self-Finesses* have a *Misplay Component* in almost the exact same way that *Clandestine Finesses* do, but they just involve non-matching rank cards.
* Generally speaking, this means that when a **rank** clue initiates a *Finesse*, the clue receiver must always allow for the possibility that subsequent non-matching rank cards in the blind-player's hand (that are of a **lower** rank than the clue) can possibly be caught up in the *Finesse*.
* For example, in a 3-player game:
  * Red 1 is played on the stacks.
  * Alice clues number 3 to Cathy, which touches one 3.
  * Bob blind-plays red 2.
  * Cathy knows that red 2 "matches" number 3, so she knows that she probably has red 3.
  * However, Cathy also sees that before Bob blind-played the red 2, he had a blue 1 in the slot right after it.
  * Thus, it is possible for Cathy's 3 to actually be blue 3. If it is, Bob will blind-play the blue 1 and Cathy will know that she has blue 2 on her *Finesse Position*.
  * So, Cathy discards (instead of potentially playing the red 3 on this turn) to allow for the possibility of a *Surreptitious Self-Finesse*.

### The Continuation Clue (Touching Both Inside and Outside a Layer)

* Sometimes, a player who is blind-playing cards into a *Layered Finesse* receives another clue that touches cards **both** inside the layer and outside the layer.
* By default, the player should assume that it is another normal *Play Clue* or *Save Clue* on a card outside of the layer, and **continue** to blind-play cards. This follows from *Information Lock Principle*. *Play Clues* given in this manner are called *Continuation Clues*.
* Because *Continuation Clues* are the default interpretation, it can be difficult to give a *Fix Clue*, since a *Fix Clue* must **only** touch cards inside of the layer.
* An example of a *Continuation Clue* can be found by looking at the screenshot in the *Clandestine Finesse* section:
  * After SedNegi's initial clue, if 910dan clues purple to Zamiel, it would touch a card inside the layer (purple 1) and a card outside the layer (purple 2).
  * Thus, the focus of the clue would be on the card outside of the layer (purple 2), being a *Play Clue* on purple 2.
  * In this hypothetical, Zamiel would immediately blind-play slot 2 as yellow 1. On his subsequent turns, he would play purple 1, purple 2, and yellow 3 (in that order).

### The Just-In-Time Fix Clue (To Fix a Layered Finesse with a Lie Component) (JIT / J.I.T.)

* When performing a *Layered Finesse* with a *Lie Component*, if the plan is to give a *Fix Clue* to the *Finesse Target* card (the "final" card that is to be blind-played), then it is important to wait until the **last** moment to give the *Fix Clue*. This is because after receiving the *Fix Clue*, the player will not play any more blind cards.
* Thus, you should first wait for all of the "good" blind cards to play, and **then** give the *Fix Clue* to the *Finesse Target*, so that it comes "just in time" before the misplay.
* Alternatively, if the plan is to give a *Fix Clue* to some **other** card than the *Finesse Target* (e.g. a number 5 clue to a 5 in the middle of the hand), then the *Fix Clue* does not necessarily have to be just in time. It can be done early, and the player will know that they have to continue blind-playing cards until they find the *Finesse Target*.

### The Hesitation Blind-Play

* Sometimes, a player will get a *Play Clue* on a card. And then, instead of playing it, they will discard their chop instead. This would normally indicate a *Scream Discard*. However, sometimes the next player will know from the context of the game that their chop has to be safe.
* In such a situation, the only reason that the player would discard is that they are allowing for the possibility of a *Reverse Finesse*, and that the next player has a playable card on *Finesse Position* slot that "matches" the card that they got the *Play Clue* on. Thus, the next player may be able to just immediately blind-play their *Finesse Position* card as a *Hesitation Blind-Play*.
* However, doing this is not always safe, so players have to carefully evaluate what exact cards that they could be playing:
  * For example, if they played the other copy of the clued card (that caused the *Hesitation*), then that would cause a duplication and violate *Good Touch Principle*.
  * Another problem is if the blind-play causes the original clue to look like a *Double Finesse* with a "self" component. For example, if a number 4 clue causes a *Hesitation Blind-Play* of a red 2, the clue receiver might misplay their *Finesse Position* card as a red 3.

### The Pass Bluff

* It is possible for a *Hesitation Blind-Play* to occur without anyone intending it to happen. However, if a player intentionally tries to make a *Hesitation Blind-Play* occur, it is called a *Pass Bluff*.
* In other words, after a *Finesse* occurs that is directed at you, you will know that your *Finesse Position* card is playable. If the next immediate player also has an unrelated playable card on their *Finesse Position*, you can pretend like the *Finesse* wasn't directed at you. This will cause them to think that the *Finesse* was directed at them, and you will get the unrelated card played for free.
* After the unrelated card is played, the next player should **not** continue to blind-play cards (as a *Layered Finesse*) because:
  * You "passing" player fulfills the real *Finesse* on their next turn.
  * The "passing" player was in *Bluff Seat*.
* *Pass Bluffs* rely on contextual information in order to work, so the circumstances in which you can do them are narrow.
* It is illegal for a player to perform a *Pass Bluff* if they could be *Bluffed*. (This is because the first *Bluff* would not resolve immediately and would violate *Good Lie Principle*.)

### The Double/Triple Pass Bluff

* After a player performs a *Pass Bluff*, when it becomes their turn again, if they see an unrelated playable card on the *Second Finesse Position* of the next player, they can perform yet another *Pass Bluff*, implying that the first *Pass Bluff* was not a *Pass Bluff* at all and instead simply a *Layered Finesse* or *Clandestine Finesse*.
* Then, after the unrelated card is played, the player who initiated the *Double Pass Bluff* can go ahead and play into the real *Finesse*.
* Alternatively, if there continue to be playable cards, they can keep *Pass Bluffing*.

### The Hesitation Chop Move (From a Misplay)

* Remember that as a special exception, *Scream Discards* do **not** apply when a player has a "blind" card to play in their hand **and** the blind card can exist in your hand.
* Thus, when this occurs, you will usually want to blind-play your *Finesse Position* card, since this sequence of events indicates either an *Ambiguous Finesse* or a *Pass Bluff*.
* When you blind-play a card in this situation and it misplays, it means that the unusual discard really was a *Scream Discard* after all, so you should treat it like a normal *Scream Discard* and permanently chop move.
* This is called a *Hesitation Chop Move* for short, since it was triggered by a (failed) *Hesitation Blind-Play*.

### The Rebellious Discard

* Part of the *Scream Discard* convention states that after a *Scream Discard*, the next player **cannot** discard. Thus, a player in this situation must completely waste a clue if there is nothing productive to do.
* However, in some situations, the player who has been screamed at sees that if they give a clue, the next player will be left at 0 clues and will be forced to discard a critical card.
* Thus, in this situation, the player should chop move as normal and then discard their new chop, which will functionally act as a second *Scream Discard*. This second *Scream Discard* is called a *Rebellious Discard*, because they are not doing what they are told.

### The Redundant Save Chop Move

* Players that have two or more clued 1's in their hand will often use the *Order Chop Move* to *Chop Move* a 2, a 5, or a critical card on the next player's chop.
* Subsequently, if a player with two or more clued 1's in their hand does not play a 1 and instead gives a *Save Clue* to a 2, a 5, or a critical card on the next player's chop, this is very strange.
* In this situation, if there is nothing else special going on, the player who got clued should *Chop Move* the card next to the one that was explicitly saved.

### The Trash Push Prompt & The Trash Push Finesse

* If you see that a player *Trash Pushes* an unplayable one-away from playable card, it is a signal to you that you have the connecting card.

### The Distribution Finesse

* On the final round of the game, it is possible to perform a *Prompt* on a player that would be useless - they will not get a chance to play the *Prompted* card before the game ends.
* If a player does this anyway, then it must be communicating something extra. In this situation, it is to be interpreted as a *Finesse* instead of a *Prompt* for the purposes of better satisfying *Team Distribution Principle*.
* Examples:
  * Game #16887, turn 29 if Instantiation clues blue on the blue 5

### The Suboptimal Color Prompt & The Suboptimal Color Finesse

* When saving a critical card, players will generally choose either color or number in order to best satisfy *Good Touch Principle*. Or, in situations where either color or number will satisfy *Good Touch Principle*, they will choose the clue that touches the maximum amount of useful ancillary cards (in order to get a "2 for 1" or "3 for 1" instead of a "1 for 1").
* When a player does **not** do this, it very strange. From *High Value Principle*, it implies it is a *Play Clue* instead of a *Save Clue*, so it is either a *Prompt* or a *Finesse* on the critical card being saved.

### The Suboptimal Trash Bluff Chop Move

* The *Trash Bluff* is often done as a last resort - there was no other way to touch the next player's *Finesse Position* card without violating *Good Touch Principle*.
* However, sometimes there **is** a way to "cleanly" touch the next player's *Finesse Position* card, but the positive/negative information on the rest of the hand would be useless. In these types of situations, the *Trash Bluff* is used to stall out the discard of a potentially useful card in the clue receiver's hand.
* And other times, there **is** a way to "cleanly" touch the next player's *Finesse Position* card, and it would be a "free" touch on a useful ancillary card. Or, the positive/negative information on the rest of the hand would be very useful - it would "fill in" a mystery card, or make a mystery card playable.
* In this third situation, if a *Trash Bluff* is **still** used, then it follows from *High Value Principle* that it should *Chop Move* the clue receiver in addition to getting the blind-play. (It should only *Chop Move* one card.)
* *Suboptimal Trash Bluff Chop Moves* are tricky in that they have information asymmetry: the player who blind-plays will **not** know that the card is chop moved, while everyone else will. All players will have to keep this in mind until the chop move has been demonstrated.
* An alternate form of the *Suboptimal Trash Bluff Chop Move* exists where the suboptimality is **not** in the clue receivers hand but in someone else's hand. For example, in a 4-player game:
  * Blue 1 and red 4 are played on the stacks.
  * It is Alice's turn. Bob has blue 2 in his *Finesse Position*. It is possible for Alice to *Finesse* blue 2 by cluing blue 3 in Cathy's hand. This would be a 2-for-1 clue.
  * Instead, Alice clues red to Donald, which touches a red 1. This is a *Trash Bluff* because it makes Bob think he has red 5, but he instead blind-plays blue 2. This is a 1-for-1 clue.
  * Donald knows that since Alice did a 1-for-1 instead of a 2-for-1, he should chop move.
  * Cathy does not know that Donald will chop move until he demonstrates it or until the blue 3 in her hand is directly clued.

### Ejection

* *Ejection* refers to a move like a *Bluff*, but instead of playing an unrelated card from *Finesse Position*, someone plays an unrelated card from their *Second Finesse Position*. For example, if a player's hand hand is completely unclued, their *Second Finesse Position* is slot 2.
* Certain types of "wasted" clues with no other purpose signal an *Ejection*.

#### Known Trash Ejection

* Often times, a player can have one or more cards that are known duplicates / trash. They will discard them it without being told anything further.
* If a clue is given that **only** touches cards that are already known trash, then it must have some other purpose - it should signal an *Ejection* on the very next player.

#### Double Play Ejection

* If a player knows that a card in their hand is playable, and then they receive **another** clue on that card, it is usually a *Stop Clue*, which means that the card is actually bad and they should discard it instead of playing it.
* However, if this happens on a good card, the other players can see that the clue must have some other purpose - it should signal an *Ejection* on the very next player.

#### Unknown Trash Ejection

* In general, *Bluffs* work because the player who received the clue knows that they have a one-away from playable card of that color.
* If none of the stacks are finished and someone clues a trash card, it might look like a *Trash Bluff*. But, if the *Finesse Position* card is played, then the player will think that the card is actually a useful one-away card (instead of trash).
* Since that would be a lie, the clue must have some other purpose - it should signal an *Ejection* on the very next player.
* Since the *Second Finesse Position* card was played instead of the *Finesse Position* card, then the player who received the clue will know that the card is trash.
* With the *Trash Bluff*, if multiple cards are clued, it means that **all** of the cards are trash. However, with *Unknown Trash Ejection*, if multiple cards are clued, only the focus of the clue is trash.

#### Order Ejection

* When a player can perform an *Skipped Order Chop Move* on a critical 5 (or a critical black card) at the beginning of the game, and they don't do it, this is very strange.
* The player must be communicating something extra. In this scenario, they intend for the next person to blind-play slot 2.
* The *Order Ejection* will also get a free *Chop Move* in addition to getting the blind-play.
* For example, in a 4-player game:
  * Blue 1 is played on the stacks.
  * Alice clues Bob 1's, touching three 1's on slot 2, slot 3, and slot 4.
  * Donald has a 5 on chop (and the rest of his hand is trash).
  * Bob could play his 1 on slot 2 to *Skipped Order Chop Move* Donald's 5 for "free".
  * Bob instead plays his 1 on slot 4 (which does nothing special).
  * Cathy sees no possible reason for not getting a "free" *Chop Move* on a 5, so she knows that this is an *Order Ejection*. Cathy blind-plays slot 2 and it plays as a blue 2.
  * Donald knows that Cathy must be blind-playing slot 2 for a reason. The only thing that happened that could have possibly caused the blind-play was the order that Bob played his 1's in. Thus, Donald knows that an *Order Ejection* has occurred and that he should *Chop Move*.
  * Furthermore, Donald knows that his *Chop Moved* card **must** be a 5 or some other critical card. (This is unlike a normal *Order Chop Move*, since *Order Chop Moves* are alloweded to get non-critical cards.)
* Note that *Order Ejections* only apply if the player did not *Order Chop Move* a **critical** card. Unique 2's **do not** count as critical in this case.

#### Reverse Order Ejection

* It is also possible to do a *Reverse Order Ejection*, meaning that the blind-play will occur **after** the person with the critical card has a turn.
* For an *Order Ejection* to work, the player who initiates it must have three or more 1's to choose from. But a *Reverse Order Ejection* is more flexible in that it only requires two 1's.
* For example, in a 4-player game:
  * Blue 1 is played on the stacks.
  * Alice clues Bob 1's, touching a 1 on slot 2 and a 1 on slot 3.
  * Cathy has a 5 on chop (and the rest of her hand is trash).
  * If Bob plays the slot 2 card, this would be a "free" *Order Chop Move* on the 5.
  * Bob plays the 1 from slot 3 (which does nothing special).
  * Cathy clues number 5 to Bob as a *5 Save*.
  * Donald knows that Bob should have *Order Chop Moved* Cathy's 5, so he knows that this is a *Reverse Order Ejection*. Donald blind-plays his slot 2 card and it is a blue 2.
  * Cathy knows that Donald did not blind-play from her *5 Save*, so the blind-play must have been from something else. The only other thing that happened was Bob playing the 1. Thus, Cathy knows that an *Reverse Order Ejection* has occurred and she retroactively *Chop Moves* herself.
* Unlike a normal *Order Ejection*, the *Reverse Order Ejection* is not guaranteed to work. This is because Cathy is within her rights to "get" the *Second Finesse Position* card of Donald (with a direct *Play Clue* of her own). Thus, *Reverse Order Ejections* should only be done in specific circumstances where it is unlikely that Cathy will do so.
* If a *Reverse Order Ejection* fails, everyone on the team should be aware that they now need to save the chop of Cathy.
* For example, in a 4-player game:
  * The setup is exactly the same as in the previous example.
  * When it gets to Cathy's turn, instead of performing a *5 Save* on Bob, she instead clues Donald's blue 2 directly as a *Play Clue*.
  * Donald plays the blue 2.
  * Bob now knows that the *Reverse Order Ejection* failed and that the 5 will not get retroactively *Chop Moved* anymore. If Cathy might discard on the next turn, Bob should not play his remaining 1 and should instead give a *5 Save* to Cathy.

### The Dump Truck

* When someone blind-plays their chop, there is usually an emergency happening and it was either a *Scream Blind-Play* or a *Stop Blind-Play*.
* However, if someone blind-plays their chop and there was no emergency, it must be something else.
* This means that one player has a fully playable hand from left to right. Like a dump truck, they are expected to unload everything onto the table.
* Most times, all cards in the hand will be unclued. But if not, the player is still expected to play everything from left to right in order.
* In the middle of the game, it is relatively safe to blind-play your chop card, since it is known to not be a critical/playable card.
* In the beginning of the game, it may not be safe to blind-play your chop card. In this situation, you may see that multiple players have the opportunity to initiate the *Dump Truck*. Normally, it is best to let the player immediately before the blind-player do it. If they have an unsafe chop, then the 2nd player before the blind-player should do it, and so forth.

### The Distributed Dump Truck

* This convention only applies to 5-player games.
* In the *Dump Truck* convention, a blind-play of a chop card induces one person to blind-play their whole hand from left to right.
* Normally, a *Dump Truck* is not ambiguous - only one player can have a fully-playable hand, so it is clear what is going on.
* However, what if no players have a fully-playable hand? This must be communicating a different strategy. We agree that this should mean a *Quadruple Bluff*.
* For example, in 5-player game:
  * Near the beginning of the game, Alice blind-plays her chop and it fails to play.
  * Bob interprets this as a *Dump Truck*, and blind-plays his *Finesse Position* card. It is a red 1 and it successfully plays.
  * Cathy sees that this is **not** a *Dump Truck* - Bob does not have a fully-playable hand. Thus, this move must have some other meaning.
  * Cathy can see that Donald and Emily have playable cards on their *Finesse Position*. Thus, Cathy knows that this is a *Distributed Dump Truck*, and plays her *Finesse Position* card. It is a blue 1 and it successfully plays.
  * Donald can see what is going on, so he plays green 1 from his *Finesse Position*.
  * Emily plays green 2 from her *Finesse Position*.

### The Useless Bluff

* Normally, when a player clues a known-trash card that is off-chop, it communicates a *Trash Chop Move*. However, what if the *Chop Moved* card is also trash? Then this would be a completely useless *Chop Move*.
* In this situation, the player who gave the clue must be communicating something extra. They intend for the next player to play their *Finesse Position* card as a known *Bluff*.

### The Dupe Bluff

* This is where you perform a *Bluff* such that the card that is blind-played is already touched in someone else's hand **and** the player who has the other copy has full knowledge of the card.
* You wouldn't normally do this since it is only a 1-for-1 instead of a 2-for-1. However, it can be useful if you want to touch a card that you wouldn't otherwise be able to, like a one-away from playable card. Alternatively, you may strongly want to give ancillary information to some other card.

### The Negative Blind-Play

* Given enough negative clues on a card (and potentially some ancillary information based on the history of the game), it is possible to narrow down the identity of an unclued card in your hand to possibilities that only include playable cards that are not already touched in someone else's hand.
* In this situation, you are expected to blind-play the card.

### The Negative Self-Chop Move

* If a card has negative 1, 2, 3, and 4 on it, then it is explicitly known to be a 5, while not directly clued.
* In this situation, it would be a waste of a clue for the team to clue it directly.
* Thus, the player should self-chop move the card.

### The Speed-up Clue

* The *Layered Finesse* convention (and its derivatives) are very efficient (in terms of "X for 1"). However, sometimes it can be very slow (low tempo), as players will have to allow for all possible *Reverse Finesses* before playing anything. This is generally not a problem in 3-player games, but tempo is important in 5-player games.
* Normally, when the *Finesse Target* (the card that is to be blind-played) is clued directly, it is a mistake due to someone not paying close enough attention. We refer to this as *Stomping on a Finesse*.
* However, if high tempo is needed, a player can consider intentionally *Stomping* on a *Layered Finesse* in order to "speed up" the play of a specific card that leads into other players hands.
* One complicating factor of the *Speed-up Clue* is how to differentiate it from a more-ordinary *Fix Clue*. In other words, after the clued card is played, on their next turn, should the player go back and blind-play the other cards? If it was a *Speed-up Clue*, they should. If it was a *Fix Clue*, they should not.
* The key lies in the context of the clue:
  * Would another player have tried to blind-play something before the potential *Fix Clue* was given? If yes, then it is not a *Fix Clue*, and it is a *Speed-up Clue*.
  * Was it possible to take an equivalent line where a *Fix Clue* would not be needed? (In terms of the same number of clues, and no risk of discarding critical/playable cards.) If yes, it is not a *Speed-up Clue*.

### The Layered Jump

* If a player who is blind-playing into a *Layered Finesse* skips over a card, they are performing a *Layered Jump*. This player has deduced that the card they are skipping over is duplicated (or otherwise bad).
* The card skipped over in this way will be the next thing discarded, as it is now considered known trash.
* If a *Layered Jump* skips over a card that cannot be in your own hand, then you can determine that it must be a mistake. In this situation, the skipped-over card must be clued directly to re-signify that it is good.

### The Misplay Trash Push

* When a card is clued and the next player misplays that card, it is usually the *Misplay Chop Move* - they had no other options and had to protect an important card on chop.
* However, when a card **on chop** is clued and the next player misplays that card, it cannot be the *Misplay Chop Move* - it must be something else.
* Normally, when trash is clued on chop, it is a *Trash Push*. So they should go on to blind-play the card that was touching the trash on their next turn.

### Inverted Priority Finesse

* *Priority Finesses* are considered "free", since they do not cost a clue to perform. Thus, it is extremely rare that a player would decline to perform one if it was possible to do so.
* If a player declines to perform a *Priority Finesse*, and there is nothing else special going on, then they must be trying to communicate something extra.
* They are instead calling for a *Priority Finesse* on the card that had *Priority*. This is called an *Inverted Priority Finesse* because it gets a blind-play from playing a card with *Priority* (as opposed to getting a blind-play from playing a card without *Priority*).
* After a *Inverted Priority Finesse* occurs, the presence of a normal *Priority Finesse* is now known to everyone on the team. Thus, the normal *Priority Finesse* is preserved and should be played into on the next go-around of the table.
* For example, in a 3-player game:
  * Alice has a choice between playing a red 1 and a blue 2. Both cards are fully known, and no-one else has any clued cards, so the red 1 has *Priority*.
  * Alice plays the red 1.
  * Bob sees that if Alice had played the blue 2, she could have performed a *Priority Finesse* on Cathy's slot 1 card, the blue 3.
  * Bob knows that there was no reason for Alice to decline the *Priority Finesse*, so this must be an *Inverted Priority Finesse*. Bob blind-plays his slot 1 card, and it is the red 2.
  * Cathy knows that the red 1 had *Priority*, so playing it should not have caused Bob to blind-play anything. Thus, Cathy knows that this must be an *Inverted Priority Finesse*, and she knows that she has a blue 3 on her slot 1. Cathy discards.
  * Alice plays blue 2.
  * Bob discards.
  * Cathy blind-plays blue 3.

### The Skipped Discard Chop Move

* In emergency situations, players should perform *Scream Discards* and  *Generation Discards* to save important cards. These two moves, along with their derivatives, the *Echo Scream Discard* and the *Compositional Discard*, should be enough to "solve" almost every sticky situation that could ever come up.
* However, in an extremely difficult variant, or in a situation where one of the previous players has blundered, it might fall to one player to save the next player's critical chop card. In this situation, they might not be able to perform a *Scream Discard*, because they might not have any playable cards. And they might not be able to perform a *Scream Blind-Play*, because if the team is at 2 strikes, then the game would immediately end.
* In this situation, the player can discard a card one-away from their chop as a *Skipped Discard Chop Move*. This convention is normally only used in 2-player games, because it is very unsafe, risking the discard of a critical card.
* It is very common for players to accidently *Chop Move* a card. Thus, the *Skipped Discard Chop Move* interpretation should almost never be entertained, simply because of how rarely it is actually needed.
* Furthermore, this move should never be performed if there is a non-expert player playing or if it is likely to be interpreted as a mistake.

<br />

## Convention Attribution

* The general terms of chop, *Finesse*, and *Bluff* were not invented by this group. Those basic strategies were the building blocks for the current Hyphen-ated framework.
* The earliest mention of "chop" on the Board Game Geek forums comes from [Ben Small's post in 2013](https://boardgamegeek.com/article/13665606#13665606). He may be the originator of the term.
* Finesse is a common strategy in [bridge](https://en.wikipedia.org/wiki/Finesse), so that is the likely origin of the term.
* The earliest mention of "finesse" and "bluff" on the Board Game Geek forums comes from [Adam Kunsemiller's post in 2012](https://boardgamegeek.com/article/9317490#9317490). He uses the terms in a colloquial way, which implies that these strategies were commonly used at the time of writing.
* The specific inventors of some of our own strategies are listed below:

| Convention Name | Inventor
| --- | ---
| The 9 First Principles | Duneaught
| General Principles | Zamiel & Florrat
| 2 Saves | Hyphen-ated & Duneaught
| Chop-Focus | Zamiel & Hyphen-ated
| The Layered Finesse | Antizoubilamaka
| The Clandestine Finesse | Antizoubilamaka
| The Patch Finesse | Zamiel & Libster
| The 3 Bluff | Hyphen-ated
| The Double Bluff | Hyphen-ated
| The Double Half Bluff | Hyphen-ated
| The Triple Bluff | Zamiel
| The Triple Two-Thirds Bluff | Zamiel
| Playing 1's from Right to Left | Duneaught
| The Gentleman's Discard | Duneaught
| The Layered Gentleman's Discard | Duneaught
| The Tempo Clue Chop Move | Zamiel
| Discard Elimination & The Elimination Blind-Play | Aridolomo (with revisions from Hyphen-ated & Duneaught)
| Immediate Double Clue | Duneaught
| The Elimination Finesse | Zamiel & Ahming
| The Elimination Riding Deduction | Duneaught
| The Free Choice Finesse | Hyphen-ated
| The Trash Push | Duneaught
| The Trash Bluff | Duneaught
| The Trash Finesse | Duneaught
| The Double Trash Finesse | Duneaught
| The Trash Push Finesse | Duneaught
| The Hesitation Blind-Play | Zamiel
| The Priority Prompt & The Priority Finesse | Libster & Zamiel
| The Priority Bluff & The Priority Layered Finesse | Zamiel
| The Dupe Bluff | Duneaught
| The Certain Finesse | Zamiel
| The Negative Prompt | Zamiel & Libster
| The Weak Prompt | Hyphen-ated
| Crazy 3 Saves & Crazy 4 Saves | Libster
| The Scream Discard Chop Move | 910dan & Zamiel
| The Early Fix Clue Chop Move | Zamiel
| The Critical 4 Bluff | Libster
| The Chop Transfer | Duneaught
| The Whisper Discard Chop Move | Zamiel
| The Good Touch Bluff | Postmans
| The Negative Blind-Play | Ahming
| The Elimination Bluff | Zamiel
| The Elimination Layered Finesse | Zamiel
| The Rebellious Discard | Zamiel
| Focus Inversion | Zamiel
| Modified Black 3 & Black 4 Saves | Florrat
| The Early Game | Libster & Florrat
| The Double Tempo Clue | Hyphen-ated & Zamiel
| Hard Bluffs | Florrat
| White Compromise | Postmans
| Acid Trip Conventions | Zamiel & Florrat
| The Double/Triple Pass Bluff | Zamiel
| The Out-of-Order Finesse | Zamiel
| The Speed-up Clue | Libster
| The Misplay Trash Push | Zamiel
| The Disease Bluff & The Heal Clue | Zamiel
| The Double-Copy Bluff | Zamiel
| The Pestilent (Double) Bluff | Zamiel
| The Distribution Clue | Libster
| The Elimination Riding Deduction Bluff | Duneaught
| Self-Elimination Finesse Priority | 910dan
| Multiple-card Trash Bluff | Zamiel
| Play Elimination | Zamiel
| Double Discard Elimination | Zamiel
| The No-Information Double Finesse & The No-Information Double Bluff | Zamiel
| The Layered Jump | Libster
| The Free Choice Bluff | Zamiel
| The Suboptimal Color Prompt & The Suboptimal Color Finesse | Zamiel
| The Suboptimal Color Bluff | Zamiel
| The Continuation Clue | Libster
| The Just-In-Time Fix Clue | Zamiel
| The Occupied Play Clue & The Occupied Finesse | Zamiel
| The Echo Scream Discard | Florrat & Zamiel
| The Bad Touch Double Finesse & The Bad Touch Double Bluff | Sankala
| The Dump Truck | Ahming
| The Stop Discard | Zamiel
| Ejection | Razvogor & Zamiel & Sankala
| Order Chop Move | Zamiel
| Skipped Order Chop Move | Zamiel & Libster
| Trash Order Chop Move | Zamiel & Libster
| Wild & Crazy Black 4 Bluffs | Zamiel & Libster
| Duplication Responsibility | Zamiel
| Certain Discard Duplication Promise | Zamiel & Libster
| Suboptimal Trash Bluff Chop Move | Libster
| Surreptitious Self-Finesse | Sankala
| Rainbow 1oE Saves | Florrat & Libster
| Early 5 Chop Move | Libster
| The 5 Pull | Libster
| The 5 Pull Promise | Libster
| Rank Choice Bluff & Rank Choice Finesse | Zamiel
| The Load Clue | Zamiel
| The Redundant Save Chop Move | q
| The Composition Discard | Libster
| The Negative Self-Chop Move | Libster
| Empty Clues | Zamiel and Florrat
| The Empty Finesse | Instantiation
| The Flush Clue | Florrat
| The Fresh Play Clue | Instantiation
| The Speculation Prompt & The Speculation Finesse | Libster, Forrat, & Zamiel
| The Declined 5's Finesse | Zamiel
| The Empty Double-Play | Zamiel & Jeep
| The Suboptimal Save Prompt & The Suboptimal Save Finesse | Zamiel
| The Empty Bluff | Cory
| The Black Save Bluff | Sankala
| Inverted Priority Finesse | Zamiel
| Multi-Five Saves | Libster
| 4 Stalls & Early 4's Chop Move & 4 Pull | Andrew U.K.
| The Trash Pull | Libster
| The Repair Finesse | Zamiel
| The Paused Priority Finesse | Asddsa
| The Double Scream Discard Chop Move | Asddsa
| The Distribution Finesse | Asddsa
| The Full Finesse | NoMercy
| The Double Positional Misplay | Libster
| Order Ejection & Reverse Order Ejection | Zamiel & q
| The Scream Push | Zamiel
| The Useless Bluff | Zamiel
| The Double Scream Blind-Play | Zamiel
| The Bad Touch Finesse | Zamiel
| The Skipped Discard Chop Move | Libster
| The Mismatch Finesse | Zamiel
| The Distributed Dump Truck | Razvogor
