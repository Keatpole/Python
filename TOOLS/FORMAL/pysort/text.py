const { question } = require('readline-sync'); # Line: 1 | Tabs: 0
const { Functions, Player } = require("./other"); # Line: 2 | Tabs: 0
const { Card } = require("./card"); # Line: 3 | Tabs: 0
const { printName } = require("./interact"); # Line: 4 | Tabs: 0
class GameStats { # Line: 6 | Tabs: 0
} # Line: 76 | Tabs: 0
class Game { # Line: 78 | Tabs: 0
} # Line: 714 | Tabs: 0
exports.Game = Game; # Line: 716 | Tabs: 0
exports.GameStats = GameStats; # Line: 717 | Tabs: 0
constructor(game) { # Line: 7 | Tabs: 1
} # Line: 10 | Tabs: 1
cardUpdate(key, val) { # Line: 12 | Tabs: 1
} # Line: 43 | Tabs: 1
questUpdate(quests_name, key, val, plr = this.game.player) { # Line: 45 | Tabs: 1
} # Line: 62 | Tabs: 1
update(key, val) { # Line: 64 | Tabs: 1
} # Line: 75 | Tabs: 1
constructor(player1, player2) { # Line: 79 | Tabs: 1
} # Line: 110 | Tabs: 1
set(key, val) { # Line: 112 | Tabs: 1
} # Line: 114 | Tabs: 1
activatePassives(trigger) { # Line: 116 | Tabs: 1
} # Line: 120 | Tabs: 1
getPlayer1() { # Line: 122 | Tabs: 1
} # Line: 124 | Tabs: 1
getPlayer2() { # Line: 126 | Tabs: 1
} # Line: 128 | Tabs: 1
getPlayer() { # Line: 130 | Tabs: 1
} # Line: 132 | Tabs: 1
getOpponent() { # Line: 134 | Tabs: 1
} # Line: 136 | Tabs: 1
getTurns() { # Line: 138 | Tabs: 1
} # Line: 140 | Tabs: 1
getBoard() { # Line: 142 | Tabs: 1
} # Line: 144 | Tabs: 1
setPlayer1(player1) { # Line: 146 | Tabs: 1
} # Line: 148 | Tabs: 1
setPlayer2(player2) { # Line: 150 | Tabs: 1
} # Line: 152 | Tabs: 1
setPlayer(player) { # Line: 154 | Tabs: 1
} # Line: 156 | Tabs: 1
setOpponent(opponent) { # Line: 158 | Tabs: 1
} # Line: 160 | Tabs: 1
setTurns(turns) { # Line: 162 | Tabs: 1
} # Line: 164 | Tabs: 1
setBoard(board) { # Line: 166 | Tabs: 1
} # Line: 168 | Tabs: 1
plrNameToIndex(name) { # Line: 170 | Tabs: 1
} # Line: 175 | Tabs: 1
plrIndexToName(index) { # Line: 177 | Tabs: 1
} # Line: 182 | Tabs: 1
plrIndexToPlayer(index) { # Line: 184 | Tabs: 1
} # Line: 187 | Tabs: 1
getOtherPlayer(player) { # Line: 189 | Tabs: 1
} # Line: 192 | Tabs: 1
startGame() { # Line: 194 | Tabs: 1
} # Line: 249 | Tabs: 1
endGame(p) { # Line: 251 | Tabs: 1
} # Line: 257 | Tabs: 1
endTurn() { # Line: 259 | Tabs: 1
} # Line: 290 | Tabs: 1
startTurn() { # Line: 292 | Tabs: 1
} # Line: 339 | Tabs: 1
playCard(card, player) { # Line: 341 | Tabs: 1
} # Line: 559 | Tabs: 1
playMinion(minion, player, summoned = true, trigger_colossal = true) { # Line: 561 | Tabs: 1
} # Line: 600 | Tabs: 1
killMinions() { # Line: 602 | Tabs: 1
} # Line: 635 | Tabs: 1
attackMinion(minion, target) { # Line: 637 | Tabs: 1
} # Line: 713 | Tabs: 1
this.game = game; # Line: 8 | Tabs: 2
this.jadeCounter = 0; # Line: 9 | Tabs: 2
this.game.player.getHand().forEach(p => { # Line: 13 | Tabs: 2
}); # Line: 24 | Tabs: 2
this.game.getBoard().forEach(p => { # Line: 26 | Tabs: 2
}); # Line: 31 | Tabs: 2
if (this.game.player1.weapon) { # Line: 33 | Tabs: 2
} # Line: 36 | Tabs: 2
if (this.game.player2.weapon) { # Line: 37 | Tabs: 2
} # Line: 40 | Tabs: 2
this.game.activatePassives([key, val]); # Line: 42 | Tabs: 2
plr[quests_name].forEach(s => { # Line: 46 | Tabs: 2
}); # Line: 61 | Tabs: 2
if (!this[key]) this[key] = [[], []]; # Line: 65 | Tabs: 2
this[key][this.game.player.id].push(val); # Line: 67 | Tabs: 2
this.cardUpdate(key, val); # Line: 69 | Tabs: 2
this.questUpdate("secrets",    key, val, this.game.opponent); # Line: 71 | Tabs: 2
this.questUpdate("sidequests", key, val); # Line: 72 | Tabs: 2
this.questUpdate("quests",     key, val); # Line: 73 | Tabs: 2
this.questUpdate("questlines", key, val); # Line: 74 | Tabs: 2
// Choose a random player to be player 1 # Line: 80 | Tabs: 2
const functions = new Functions(); # Line: 81 | Tabs: 2
if (functions.randInt(0, 10) < 5) { # Line: 83 | Tabs: 2
} else { # Line: 86 | Tabs: 2
} # Line: 89 | Tabs: 2
this.player = this.player1; # Line: 91 | Tabs: 2
this.opponent = this.player2; # Line: 92 | Tabs: 2
this.Card = Card; # Line: 94 | Tabs: 2
this.Player = Player; # Line: 95 | Tabs: 2
this.functions = functions; # Line: 96 | Tabs: 2
this.stats = new GameStats(this); # Line: 97 | Tabs: 2
this.input = question; # Line: 98 | Tabs: 2
this.player1.id = 0; # Line: 100 | Tabs: 2
this.player2.id = 1; # Line: 101 | Tabs: 2
this.turns = 0; # Line: 103 | Tabs: 2
this.board = [[], []]; # Line: 104 | Tabs: 2
this.passives = []; # Line: 106 | Tabs: 2
this.player1.setGame(this); # Line: 108 | Tabs: 2
this.player2.setGame(this); # Line: 109 | Tabs: 2
this[key] = val; # Line: 113 | Tabs: 2
let ret = []; # Line: 117 | Tabs: 2
this.passives.forEach(i => ret.push(i(this, trigger))); # Line: 118 | Tabs: 2
return ret; # Line: 119 | Tabs: 2
return this.player1; # Line: 123 | Tabs: 2
return this.player2; # Line: 127 | Tabs: 2
return this.player; # Line: 131 | Tabs: 2
return this.opponent; # Line: 135 | Tabs: 2
return this.turns; # Line: 139 | Tabs: 2
return this.board; # Line: 143 | Tabs: 2
this.player1 = player1; # Line: 147 | Tabs: 2
this.player2 = player2; # Line: 151 | Tabs: 2
this.player = player; # Line: 155 | Tabs: 2
this.opponent = opponent; # Line: 159 | Tabs: 2
this.turns = turns; # Line: 163 | Tabs: 2
this.board = board; # Line: 167 | Tabs: 2
if (this.player1.getName() == name) return 0; # Line: 171 | Tabs: 2
if (this.player2.getName() == name) return 1; # Line: 172 | Tabs: 2
return -1; # Line: 174 | Tabs: 2
if (index == 0) return this.player1.getName(); # Line: 178 | Tabs: 2
if (index == 1) return this.player2.getName(); # Line: 179 | Tabs: 2
return null; # Line: 181 | Tabs: 2
if (index == 0) return this.player1; # Line: 185 | Tabs: 2
if (index == 1) return this.player2; # Line: 186 | Tabs: 2
if (player == this.player1) return this.player2; # Line: 190 | Tabs: 2
if (player == this.player2) return this.player1; # Line: 191 | Tabs: 2
let plr1_hand = []; # Line: 195 | Tabs: 2
let plr2_hand = []; # Line: 196 | Tabs: 2
this.player1.deck.forEach((c) => { # Line: 198 | Tabs: 2
}); # Line: 203 | Tabs: 2
this.player2.deck.forEach((c) => { # Line: 204 | Tabs: 2
}); # Line: 209 | Tabs: 2
this.player1.setHand(plr1_hand); # Line: 211 | Tabs: 2
this.player2.setHand(plr2_hand); # Line: 212 | Tabs: 2
while (this.player1.hand.length < 3) { # Line: 214 | Tabs: 2
} # Line: 216 | Tabs: 2
while (this.player2.hand.length < 4) { # Line: 218 | Tabs: 2
} # Line: 220 | Tabs: 2
this.functions.addToHand(new Card("The Coin", this.player2), this.player2, false) # Line: 221 | Tabs: 2
this.player1.setMaxMana(1); # Line: 223 | Tabs: 2
this.player1.setMana(1); # Line: 224 | Tabs: 2
this.turns += 1; # Line: 226 | Tabs: 2
this.player1.deck.forEach(c => { # Line: 228 | Tabs: 2
}); # Line: 232 | Tabs: 2
this.player2.deck.forEach(c => { # Line: 233 | Tabs: 2
}); # Line: 237 | Tabs: 2
this.player1.hand.forEach(c => { # Line: 239 | Tabs: 2
}); # Line: 243 | Tabs: 2
this.player2.hand.forEach(c => { # Line: 244 | Tabs: 2
}); # Line: 248 | Tabs: 2
printName(); # Line: 252 | Tabs: 2
console.log(`Player ${p.getName()} wins!`); # Line: 254 | Tabs: 2
exit(0); # Line: 256 | Tabs: 2
this.killMinions(); # Line: 260 | Tabs: 2
this.stats.update("turnEnds", this.turns); # Line: 262 | Tabs: 2
this.stats.cardsDrawnThisTurn = [[], []] # Line: 263 | Tabs: 2
if (this.player.mana > 0) { # Line: 265 | Tabs: 2
} # Line: 267 | Tabs: 2
this.getBoard()[this.player.id].forEach(m => { # Line: 269 | Tabs: 2
}); # Line: 271 | Tabs: 2
let _c = this.player1.hand.filter(c => !c.echo) # Line: 273 | Tabs: 2
this.player1.setHand(_c); # Line: 274 | Tabs: 2
_c = this.player2.hand.filter(c => !c.echo) # Line: 276 | Tabs: 2
this.player2.setHand(_c); # Line: 277 | Tabs: 2
this.player.attack = 0; # Line: 279 | Tabs: 2
this.player = this.opponent; # Line: 280 | Tabs: 2
this.player.setMaxMana(this.player.getMaxMana() + 1); # Line: 282 | Tabs: 2
this.player.setMana(this.player.getMaxMana()); # Line: 283 | Tabs: 2
this.opponent = this.getOtherPlayer(this.player); # Line: 285 | Tabs: 2
this.turns += 1; # Line: 287 | Tabs: 2
this.startTurn(); # Line: 289 | Tabs: 2
this.killMinions(); # Line: 293 | Tabs: 2
this.stats.update("turnStarts", this.turns); # Line: 295 | Tabs: 2
printName() # Line: 297 | Tabs: 2
if (this.player.weapon && this.player.weapon.stats[0]) { # Line: 299 | Tabs: 2
} # Line: 301 | Tabs: 2
this.player.mana -= this.player.overload; # Line: 303 | Tabs: 2
this.player.overload = 0; # Line: 304 | Tabs: 2
if (this.player.weapon) this.player.weapon.activateDefault("startofturn"); # Line: 306 | Tabs: 2
this.getBoard()[this.plrNameToIndex(this.player.getName())].forEach(m => { # Line: 308 | Tabs: 2
}); # Line: 331 | Tabs: 2
if (this.player.weapon && this.player.weapon.stats[0]) this.player.weapon.resetAttackTimes(); # Line: 333 | Tabs: 2
this.player.drawCard(); # Line: 335 | Tabs: 2
this.player.canUseHeroPower = true; # Line: 337 | Tabs: 2
this.player.hasPlayedCardThisTurn = false; # Line: 338 | Tabs: 2
this.killMinions(); # Line: 342 | Tabs: 2
if (player.getMana() < card.getMana()) { # Line: 344 | Tabs: 2
} # Line: 347 | Tabs: 2
if (card.keywords.includes("Tradeable")) { # Line: 349 | Tabs: 2
} # Line: 393 | Tabs: 2
player.setMana(player.getMana() - card.getMana()); # Line: 395 | Tabs: 2
card.setMana(card._mana); # Line: 396 | Tabs: 2
var n = [] # Line: 398 | Tabs: 2
var found = false; # Line: 400 | Tabs: 2
player.getHand().forEach(function(c) { # Line: 402 | Tabs: 2
}); # Line: 408 | Tabs: 2
if (card.type == "Spell" && card.keywords.includes("Twinspell")) { # Line: 410 | Tabs: 2
} # Line: 415 | Tabs: 2
if (card.keywords.includes("Echo")) { # Line: 417 | Tabs: 2
} # Line: 422 | Tabs: 2
player.setHand(n); # Line: 424 | Tabs: 2
if (card.getType() == "Minion" && this.board[player.id].length > 0 && card.keywords.includes("Magnetic")) { # Line: 426 | Tabs: 2
} # Line: 460 | Tabs: 2
if (card.getType() === "Minion") { # Line: 462 | Tabs: 2
} else if (card.getType() === "Spell") { # Line: 487 | Tabs: 2
} else if (card.getType() === "Weapon") { # Line: 503 | Tabs: 2
} else if (card.getType() === "Hero") { # Line: 507 | Tabs: 2
} # Line: 511 | Tabs: 2
if (player.hasPlayedCardThisTurn) { # Line: 513 | Tabs: 2
} # Line: 515 | Tabs: 2
player.hasPlayedCardThisTurn = true; # Line: 517 | Tabs: 2
this.stats.update("cardsPlayed", card); # Line: 519 | Tabs: 2
var corrupted = null; # Line: 521 | Tabs: 2
card.plr.hand.forEach(c => { # Line: 523 | Tabs: 2
}); # Line: 540 | Tabs: 2
if (corrupted) { # Line: 542 | Tabs: 2
} # Line: 556 | Tabs: 2
this.killMinions(); # Line: 558 | Tabs: 2
player.spellDamage = 0; # Line: 562 | Tabs: 2
var p = player.id; # Line: 564 | Tabs: 2
minion.turn = this.turns; # Line: 566 | Tabs: 2
if (minion.keywords.includes("Charge")) { # Line: 568 | Tabs: 2
} # Line: 570 | Tabs: 2
if (minion.keywords.includes("Rush")) { # Line: 572 | Tabs: 2
} # Line: 575 | Tabs: 2
if (minion.colossal && trigger_colossal) { # Line: 577 | Tabs: 2
} # Line: 585 | Tabs: 2
this.board[p].push(minion); # Line: 587 | Tabs: 2
if (summoned) { # Line: 589 | Tabs: 2
} # Line: 591 | Tabs: 2
this.getBoard()[p].forEach(m => { # Line: 593 | Tabs: 2
}); # Line: 599 | Tabs: 2
for (var p = 0; p <= 1; p++) { # Line: 603 | Tabs: 2
} # Line: 634 | Tabs: 2
this.killMinions(); # Line: 638 | Tabs: 2
if (minion instanceof Card && minion.frozen || minion instanceof Player && minion.frozen) return false; # Line: 640 | Tabs: 2
// Check if there is a minion with taunt # Line: 642 | Tabs: 2
var prevent = false; # Line: 643 | Tabs: 2
this.getBoard()[this.opponent.id].forEach(m => { # Line: 645 | Tabs: 2
}); # Line: 650 | Tabs: 2
if (prevent || target.immune) return false; # Line: 652 | Tabs: 2
if (!isNaN(minion)) { # Line: 654 | Tabs: 2
} else if (minion.attackTimes > 0) { # Line: 670 | Tabs: 2
} # Line: 712 | Tabs: 2
// Infuse # Line: 14 | Tabs: 3
if (key == "minionsKilled" && val.plr == this.game.player && p.infuse_num >= 0) { # Line: 15 | Tabs: 3
} # Line: 23 | Tabs: 3
p.forEach(m => { # Line: 27 | Tabs: 3
}); # Line: 30 | Tabs: 3
this.game.player1.weapon.activateDefault("unpassive", true); # Line: 34 | Tabs: 3
this.game.player1.weapon.activateDefault("passive", [key, val]); # Line: 35 | Tabs: 3
this.game.player2.weapon.activateDefault("unpassive", true); # Line: 38 | Tabs: 3
this.game.player2.weapon.activateDefault("passive", [key, val]); # Line: 39 | Tabs: 3
if (s["key"] == key) { # Line: 47 | Tabs: 3
} # Line: 60 | Tabs: 3
this.player1 = player1; # Line: 84 | Tabs: 3
this.player2 = player2; # Line: 85 | Tabs: 3
this.player1 = player2; # Line: 87 | Tabs: 3
this.player2 = player1; # Line: 88 | Tabs: 3
if (c.desc.includes("Quest: ") || c.desc.includes("Questline: ")) { # Line: 199 | Tabs: 3
} # Line: 202 | Tabs: 3
if (c.desc.includes("Quest: ") || c.desc.includes("Questline: ")) { # Line: 205 | Tabs: 3
} # Line: 208 | Tabs: 3
this.player1.drawCard(false); # Line: 215 | Tabs: 3
this.player2.drawCard(false); # Line: 219 | Tabs: 3
if (c.getType() == "Minion") { # Line: 229 | Tabs: 3
} # Line: 231 | Tabs: 3
if (c.getType() == "Minion") { # Line: 234 | Tabs: 3
} # Line: 236 | Tabs: 3
if (c.getType() == "Minion") { # Line: 240 | Tabs: 3
} # Line: 242 | Tabs: 3
if (c.getType() == "Minion") { # Line: 245 | Tabs: 3
} # Line: 247 | Tabs: 3
this.stats.update("unspentMana", this.player.mana); # Line: 266 | Tabs: 3
m.activateDefault("endofturn"); # Line: 270 | Tabs: 3
this.player.attack += this.player.weapon.stats[0]; # Line: 300 | Tabs: 3
m.activateDefault("startofturn"); # Line: 309 | Tabs: 3
m.canAttackHero = true; # Line: 310 | Tabs: 3
m.resetAttackTimes(); # Line: 311 | Tabs: 3
if (m.stealthDuration > 0 && this.turns > m.stealthDuration) { # Line: 313 | Tabs: 3
} # Line: 316 | Tabs: 3
if (m.dormant) { # Line: 318 | Tabs: 3
} else { # Line: 328 | Tabs: 3
} # Line: 330 | Tabs: 3
this.input("Not enough mana.\n"); # Line: 345 | Tabs: 3
return "mana"; # Line: 346 | Tabs: 3
var q = this.input(`Would you like to trade ${card.displayName} for a random card in your deck? (y: trade / n: play) `); # Line: 350 | Tabs: 3
if (q.startsWith("y")) { # Line: 352 | Tabs: 3
} # Line: 392 | Tabs: 3
if (c.displayName === card.displayName && !found) { # Line: 403 | Tabs: 3
} else { # Line: 405 | Tabs: 3
} # Line: 407 | Tabs: 3
card.removeKeyword("Twinspell"); # Line: 411 | Tabs: 3
card.setDesc(card.getDesc().split("Twinspell")[0].trim()); # Line: 412 | Tabs: 3
n.push(card); # Line: 414 | Tabs: 3
let clone = Object.assign(Object.create(Object.getPrototypeOf(card)), card) # Line: 418 | Tabs: 3
clone.echo = true; # Line: 419 | Tabs: 3
n.push(clone); # Line: 421 | Tabs: 3
let hasMech = false; # Line: 427 | Tabs: 3
this.board[player.id].forEach(m => { # Line: 429 | Tabs: 3
}); # Line: 433 | Tabs: 3
while (hasMech) { # Line: 435 | Tabs: 3
} # Line: 458 | Tabs: 3
if (player.counter && player.counter.includes("Minion")) { # Line: 463 | Tabs: 3
} # Line: 469 | Tabs: 3
if (this.board[player.id].length >= 7) { # Line: 471 | Tabs: 3
} # Line: 476 | Tabs: 3
if (card.dormant) { # Line: 478 | Tabs: 3
} else if (card.activateBattlecry() === -1) return "refund"; # Line: 482 | Tabs: 3
this.stats.update("minionsPlayed", card); # Line: 484 | Tabs: 3
this.playMinion(card, player, false); # Line: 486 | Tabs: 3
if (player.counter && player.counter.includes("Spell")) { # Line: 488 | Tabs: 3
} # Line: 494 | Tabs: 3
if (card.activateDefault("cast") === -1) return "refund"; # Line: 496 | Tabs: 3
this.stats.update("spellsCast", card); # Line: 498 | Tabs: 3
this.getBoard()[this.plrNameToIndex(player.getName())].forEach(m => { # Line: 500 | Tabs: 3
}); # Line: 502 | Tabs: 3
player.setWeapon(card); # Line: 504 | Tabs: 3
card.activateBattlecry(); # Line: 506 | Tabs: 3
player.setHero(card, 5); # Line: 508 | Tabs: 3
card.activateBattlecry(); # Line: 510 | Tabs: 3
card.activateDefault("combo"); # Line: 514 | Tabs: 3
if (c.keywords.includes("Corrupt")) { # Line: 524 | Tabs: 3
} # Line: 539 | Tabs: 3
var n = [] # Line: 543 | Tabs: 3
var found = false; # Line: 545 | Tabs: 3
this.player.getHand().forEach(function(c) { # Line: 547 | Tabs: 3
}); # Line: 553 | Tabs: 3
player.setHand(n); # Line: 555 | Tabs: 3
minion.turn = this.turns - 1; # Line: 569 | Tabs: 3
minion.turn = this.turns - 1; # Line: 573 | Tabs: 3
minion.canAttackHero = false; # Line: 574 | Tabs: 3
minion.colossal.forEach((v, i) => { # Line: 578 | Tabs: 3
}); # Line: 582 | Tabs: 3
return "colossal"; # Line: 584 | Tabs: 3
this.stats.update("minionsSummoned", minion); # Line: 590 | Tabs: 3
m.keywords.forEach(k => { # Line: 594 | Tabs: 3
}); # Line: 598 | Tabs: 3
var n = []; # Line: 604 | Tabs: 3
this.getBoard()[p].forEach(m => { # Line: 606 | Tabs: 3
}); # Line: 610 | Tabs: 3
this.getBoard()[p].forEach(m => { # Line: 612 | Tabs: 3
}); # Line: 631 | Tabs: 3
this.board[p] = n; # Line: 633 | Tabs: 3
if (m.keywords.includes("Taunt") && m != target) { # Line: 646 | Tabs: 3
} # Line: 649 | Tabs: 3
if (target.keywords.includes("Divine Shield")) { # Line: 655 | Tabs: 3
} # Line: 659 | Tabs: 3
target.remStats(0, minion) # Line: 661 | Tabs: 3
if (target.stats[1] > 0) { # Line: 663 | Tabs: 3
} # Line: 665 | Tabs: 3
this.killMinions(); # Line: 667 | Tabs: 3
return; # Line: 669 | Tabs: 3
if (minion.getStats()[0] <= 0) return false; # Line: 671 | Tabs: 3
minion.attackTimes--; # Line: 673 | Tabs: 3
this.stats.update("enemyAttacks", [minion, target]); # Line: 675 | Tabs: 3
this.stats.update("minionsThatAttacked", [minion, target]); # Line: 676 | Tabs: 3
this.stats.update("minionsAttacked", [minion, target]); # Line: 677 | Tabs: 3
minion.remStats(0, target.stats[0]); # Line: 679 | Tabs: 3
if (minion.keywords.includes("Divine Shield")) { # Line: 681 | Tabs: 3
} # Line: 684 | Tabs: 3
if (minion.stats[1] > 0) minion.activateDefault("frenzy"); # Line: 686 | Tabs: 3
if (minion.keywords.includes("Stealth")) minion.removeKeyword("Stealth"); # Line: 688 | Tabs: 3
minion.activateDefault("onattack"); # Line: 690 | Tabs: 3
this.stats.update("minionsAttacked", [minion, target]); # Line: 691 | Tabs: 3
if (target.keywords.includes("Poisonous")) minion.setStats(minion.stats[0], 0); # Line: 693 | Tabs: 3
if (target.keywords.includes("Divine Shield")) { # Line: 695 | Tabs: 3
} # Line: 698 | Tabs: 3
if (minion.keywords.includes("Lifesteal")) minion.plr.addHealth(minion.stats[0]); # Line: 700 | Tabs: 3
if (minion.keywords.includes("Poisonous")) target.setStats(target.stats[0], 0); # Line: 701 | Tabs: 3
target.remStats(0, minion.stats[0]) # Line: 703 | Tabs: 3
if (target.getStats()[1] > 0) target.activateDefault("frenzy"); # Line: 705 | Tabs: 3
if (target.getStats()[1] < 0) minion.activateDefault("overkill"); # Line: 706 | Tabs: 3
if (target.getStats()[1] == 0) minion.activateDefault("honorablekill"); # Line: 707 | Tabs: 3
this.killMinions(); # Line: 709 | Tabs: 3
return true; # Line: 711 | Tabs: 3
p.setDesc(p.desc.replace(`Infuse (${p.infuse_num})`, `Infuse (${p.infuse_num - 1})`)); # Line: 16 | Tabs: 4
p.infuse_num -= 1; # Line: 17 | Tabs: 4
if (p.infuse_num == 0) { # Line: 19 | Tabs: 4
} # Line: 22 | Tabs: 4
m.activateDefault("unpassive", true); # Line: 28 | Tabs: 4
m.activateDefault("passive", [key, val]); # Line: 29 | Tabs: 4
if (!s["manual_progression"]) s["progress"][0]++; # Line: 48 | Tabs: 4
const normal_done = (s["value"] + this[key][plr.id].length - 1) == this[key][plr.id].length; # Line: 50 | Tabs: 4
if (s["callback"](val, this.game, s["turn"], normal_done)) { # Line: 52 | Tabs: 4
} # Line: 59 | Tabs: 4
plr1_hand.push(c); # Line: 200 | Tabs: 4
this.player1.deck.splice(this.player1.deck.indexOf(c), 1); # Line: 201 | Tabs: 4
plr2_hand.push(c); # Line: 206 | Tabs: 4
this.player2.deck.splice(this.player2.deck.indexOf(c), 1); # Line: 207 | Tabs: 4
c.activateDefault("startofgame"); # Line: 230 | Tabs: 4
c.activateDefault("startofgame"); # Line: 235 | Tabs: 4
c.activateDefault("startofgame"); # Line: 241 | Tabs: 4
c.activateDefault("startofgame"); # Line: 246 | Tabs: 4
m.stealthDuration = 0; # Line: 314 | Tabs: 4
m.removeKeyword("Stealth"); # Line: 315 | Tabs: 4
if (this.turns > m.dormant) { # Line: 319 | Tabs: 4
} # Line: 325 | Tabs: 4
m.turn = this.turns; # Line: 327 | Tabs: 4
m.frozen = false; # Line: 329 | Tabs: 4
if (player.getMana() < 1) { # Line: 353 | Tabs: 4
} # Line: 356 | Tabs: 4
player.setMana(player.getMana() - 1); # Line: 358 | Tabs: 4
player.shuffleIntoDeck(card); # Line: 360 | Tabs: 4
var n = [] # Line: 362 | Tabs: 4
var found = false; # Line: 364 | Tabs: 4
player.getHand().forEach(function(c) { # Line: 366 | Tabs: 4
}); # Line: 372 | Tabs: 4
if (card.type == "Spell" && card.keywords.includes("Twinspell")) { # Line: 374 | Tabs: 4
} # Line: 379 | Tabs: 4
if (card.keywords.includes("Echo")) { # Line: 381 | Tabs: 4
} # Line: 386 | Tabs: 4
player.setHand(n); # Line: 388 | Tabs: 4
player.drawCard(); # Line: 390 | Tabs: 4
return "traded"; # Line: 391 | Tabs: 4
found = true; # Line: 404 | Tabs: 4
n.push(c); # Line: 406 | Tabs: 4
if (m.tribe == "Mech") { # Line: 430 | Tabs: 4
} # Line: 432 | Tabs: 4
let m = this.input("Do you want to magnetize this minion to a mech? (y: yes / n: no) "); # Line: 436 | Tabs: 4
if (!m.toLowerCase().startsWith("y")) break; # Line: 437 | Tabs: 4
let loc = this.functions.selectTarget(`\nWhich minion do you want this to Magnetize to: `, false, "self", "minion"); # Line: 439 | Tabs: 4
this.stats.update("minionsPlayed", card); # Line: 441 | Tabs: 4
if (loc.tribe == "Mech") { # Line: 443 | Tabs: 4
} # Line: 457 | Tabs: 4
player.counter.splice(player.counter.indexOf("Minion"), 1); # Line: 464 | Tabs: 4
this.input("Your minion has been countered.\n") # Line: 466 | Tabs: 4
return "counter"; # Line: 468 | Tabs: 4
this.input("\nYou can only have 7 minions on the board.\n"); # Line: 472 | Tabs: 4
this.functions.addToHand(card, player, false); # Line: 473 | Tabs: 4
player.mana += card.mana; # Line: 474 | Tabs: 4
return "space"; # Line: 475 | Tabs: 4
card.frozen = true; # Line: 479 | Tabs: 4
card.immune = true; # Line: 480 | Tabs: 4
card.dormant = card.dormant + this.turns; # Line: 481 | Tabs: 4
player.counter.splice(player.counter.indexOf("Spell"), 1); # Line: 489 | Tabs: 4
this.input("Your spell has been countered.\n") # Line: 491 | Tabs: 4
return "counter"; # Line: 493 | Tabs: 4
m.activate("spellburst", null, () => m.hasSpellburst = false, m.plr, this, m); # Line: 501 | Tabs: 4
if (card.mana > c.mana) { # Line: 525 | Tabs: 4
} # Line: 538 | Tabs: 4
if (c.displayName === corrupted.displayName && !found) { # Line: 548 | Tabs: 4
} else { # Line: 550 | Tabs: 4
} # Line: 552 | Tabs: 4
let card = new Card(v, player); # Line: 579 | Tabs: 4
this.playMinion(card, player, false, false); # Line: 581 | Tabs: 4
if (k.startsWith("Spell Damage +")) { # Line: 595 | Tabs: 4
} # Line: 597 | Tabs: 4
if (m.getStats()[1] <= 0) { # Line: 607 | Tabs: 4
} # Line: 609 | Tabs: 4
if (m.getStats()[1] <= 0) { # Line: 613 | Tabs: 4
} else { # Line: 628 | Tabs: 4
} # Line: 630 | Tabs: 4
prevent = true; # Line: 647 | Tabs: 4
return; # Line: 648 | Tabs: 4
target.removeKeyword("Divine Shield"); # Line: 656 | Tabs: 4
return false; # Line: 658 | Tabs: 4
target.activateDefault("frenzy"); # Line: 664 | Tabs: 4
minion.removeKeyword("Divine Shield"); # Line: 682 | Tabs: 4
return false; # Line: 683 | Tabs: 4
target.removeKeyword("Divine Shield"); # Line: 696 | Tabs: 4
return false; # Line: 697 | Tabs: 4
p.activateDefault("infuse"); # Line: 20 | Tabs: 5
p.setDesc(p.desc.replace(`Infuse (${p.infuse_num})`, "Infused")); # Line: 21 | Tabs: 5
s["progress"][0]++; # Line: 53 | Tabs: 5
plr[quests_name].splice(plr[quests_name].indexOf(s), 1); # Line: 54 | Tabs: 5
if (quests_name == "secrets") this.game.input("\nYou triggered the opponents's '" + s.name + "'.\n"); # Line: 56 | Tabs: 5
if (s["next"]) new Card(s["next"], plr).activateDefault("cast"); # Line: 58 | Tabs: 5
m.dormant = false; # Line: 320 | Tabs: 5
m.frozen = false; # Line: 321 | Tabs: 5
m.immune = false; # Line: 322 | Tabs: 5
m.activateBattlecry(); # Line: 324 | Tabs: 5
this.input("Not enough mana.\n"); # Line: 354 | Tabs: 5
return "mana"; # Line: 355 | Tabs: 5
if (c.displayName === card.displayName && !found) { # Line: 367 | Tabs: 5
} else { # Line: 369 | Tabs: 5
} # Line: 371 | Tabs: 5
card.removeKeyword("Twinspell"); # Line: 375 | Tabs: 5
card.setDesc(card.getDesc().split("Twinspell")[0].trim()); # Line: 376 | Tabs: 5
n.push(card); # Line: 378 | Tabs: 5
let clone = Object.assign(Object.create(Object.getPrototypeOf(card)), card) # Line: 382 | Tabs: 5
clone.echo = true; # Line: 383 | Tabs: 5
n.push(clone); # Line: 385 | Tabs: 5
hasMech = true; # Line: 431 | Tabs: 5
loc.addStats(card.stats[0], card.stats[1]); # Line: 444 | Tabs: 5
card.keywords.forEach(k => { # Line: 446 | Tabs: 5
}); # Line: 448 | Tabs: 5
loc.maxHealth += card.maxHealth; # Line: 450 | Tabs: 5
card.deathrattles.forEach(d => { # Line: 452 | Tabs: 5
}); # Line: 454 | Tabs: 5
return "magnetize"; # Line: 456 | Tabs: 5
corrupted = c; # Line: 526 | Tabs: 5
c.removeKeyword("Corrupt"); # Line: 528 | Tabs: 5
c.addKeyword("Corrupted"); # Line: 529 | Tabs: 5
let t = null; # Line: 531 | Tabs: 5
eval(`t = new ${c.type}(c.corrupt, c.plr)`); # Line: 533 | Tabs: 5
this.functions.addToHand(t, c.plr, false); # Line: 535 | Tabs: 5
return "corrupt"; # Line: 537 | Tabs: 5
found = true; # Line: 549 | Tabs: 5
n.push(c); # Line: 551 | Tabs: 5
player.spellDamage += parseInt(k.split("+")[1]); # Line: 596 | Tabs: 5
m.activateDefault("deathrattle"); # Line: 608 | Tabs: 5
this.stats.update("minionsKilled", m); # Line: 614 | Tabs: 5
if (m.keywords.includes("Reborn")) { # Line: 616 | Tabs: 5
} else { # Line: 625 | Tabs: 5
} # Line: 627 | Tabs: 5
n.push(m); # Line: 629 | Tabs: 5
found = true; # Line: 368 | Tabs: 6
n.push(c); # Line: 370 | Tabs: 6
loc.addKeyword(k); # Line: 447 | Tabs: 6
loc.addDeathrattle(d); # Line: 453 | Tabs: 6
let minion = new Card(m.getName(), this.plrIndexToPlayer(p)); # Line: 617 | Tabs: 6
minion.removeKeyword("Reborn"); # Line: 619 | Tabs: 6
minion.setStats(minion.stats[0], 1); # Line: 620 | Tabs: 6
this.playMinion(minion, this.plrIndexToPlayer(p), false); # Line: 622 | Tabs: 6
n.push(minion); # Line: 624 | Tabs: 6
m.activateDefault("unpassive", false); # Line: 626 | Tabs: 6
