There are generally two goals you can go for when playing a chart - a higher score or a better clear. Scoring is generally about getting as many PGREATs as possible, while clearing is generally about avoiding misses to keep your health gauge up.

Scoring and clearing often do not go hand-in-hand. Going for higher clears (e.g. a full combo) can cause your score to suffer and vice versa. The game records your highest score and highest clear on a charrt separately, so high scores and clears and be done on separate runs.

----------------------------

# Scoring

## Judgements
The set of judgements in beatoraja are the same as LR2/IIDX.

- **PGREAT**
  - The tightest judgement. Displays a flashing GREAT. Gives 2 EXSCORE.
- **GREAT**
  - Gives 1 EXSCORE
- **GOOD**
  - Gives no EXSCORE. Has lower gauge recovery than PGREAT and GREAT. It gives almost no recovery on the Hard and Ex-Hard gauges.
- **BAD**
  - You get a BAD if you hit a note off-timing (outside of the GOOD window but within the BAD window). Hitting a BAD on a note breaks your combo, gives no EXSCORE, makes you lose gauge (health), and no longer allows you to hit that note.
- **POOR**
  - You get a POOR if you completely miss the note. The effects are similar to BAD, except you generally take more (about twice as much) damage on a POOR as compared to a BAD.
- **Empty POOR / Excess POOR / Mash POOR / 空POOR**
  - This has many names, but this basically describes the POORs you get if you hit additional keys while a note is nearby (but not within the BAD range) in the same lane.
  - Empty POORs make you lose gauge, but do not break combo or affect your score.
  - Empty POORs also do not remove the note you get the empty POOR on. In fact, you can get as many empty POORs as you want on a single note.

#### Additional terms

- "Miss count", or "BP" refers to the total amount of BAD + POOR + E.POOR.
- "Combo breaks" refers to the total amount of BAD + POOR.


## EXSCORE (Score Calculation)
EXSCORE is the name of the scoring system in beatoraja/LR2/IIDX.
```
EXSCORE = 2*PGREAT + 1*GREAT
```
All other judgements give no score. The highest score you can get is 2*number of notes.

**Score Rate** is the score you get as a percentage of the maximum possible score.

Here are the possible grades you can get:

- **AAA**: Score rate >= 8/9 = 88.888...%
- **AA**: Score rate >= 7/9 = 77.777...%
- **A**: Score rate >= 6/9 = 66.666...%
- **B**: Score rate >= 5/9 = 55.555...%
- **C**: Score rate >= 4/9 = 44.444...%
- **D**: Score rate >= 3/9 = 33.333...%
- **E**: Score rate >= 2/9 = 22.222...%
- **F**: Otherwise


## Judgerank

In BMS, charts are allowed to set their own judgerank. The judgerank determines the strictness of the timing for the chart. The available judgeranks are VERY EASY, EASY, NORMAL, HARD and VERY HARD. The most commonly used judgerank is EASY.

On EASY judge in beatoraja, the timing window for a PGREAT is ±20ms (IIDX has a tighter judge, at around ±16.67ms).

Beatoraja NORMAL, HARD and VERY HARD judge has 0.75x, 0.50x and 0.25x the window sizes respectively (thus PGREAT is ±15ms, ±10ms and ±5ms respectively). The full set of judge timings can be found in the [source code](https://github.com/exch-bms2/beatoraja/blob/master/src/bms/player/beatoraja/play/JudgeProperty.java).

----------------------------

# Clearing

## Gauges
A gauge is your health bar. You can choose which gauge to play a song on. Here are the gauges in order of difficulty:

- Assist Easy
- Easy
- Normal
- Hard
- Ex-Hard
- Hazard

On the Assist Easy, Easy and Normal gauges, you start the song at 20% gauge, and have to end the song with your gauge above a certain level (60% for Assist Easy, 80% for Easy and Normal) to pass. The lowest your gauge can go is 2%, and you cannot fail out mid-song.

On the Hard and Ex-Hard gauges, you start the song at 100% gauge, and fail if your gauge hits 0%. You pass if you make it to the end of the song without failing out.

The Hazard gauge fails you if you break combo. The only way to pass a song on the Hazard gauge is to full combo the song. Using the Hazard gauge gives no special status. Generally, the Hazard gauge is only used to grind full combos on charts (automatic exit on combo break).

With the exception of the Hazard gauge, the game records the hardest gauge you have cleared the song on.

You can press key 6 on the result screen to view the gauge graph for each of the different gauges, as if you were playing the song on that gauge.


## Clear Status
Typically the clear status on a song represents the hardest gauge you have cleared a song on. However, there are other clear statuses, like a full combo, which can be obtained regardless of the gauge you play on.

The clear status if a song is displayed as a lamp next to the song in the song wheel. These are known as clear lamps. You obtain a clear lamp on a song folder if you obtain at least that lamp for every song in the folder.

In addition to the clear status corresponding to each gauge, the following clear status higher than Ex-Hard:

- **Full Combo**
  - Clear a song without any bads or poors. Empty poors are okay.
- **Perfect**
  - Clear a song without any goods, bads or poors. Empty poors are okay.
- **Max**
  - Clear a song without any greats, goods, bads or poors (basically a 100% score). Empty poors are okay.


## TOTAL value

BMS charts are also allowed to set their own TOTAL values. The TOTAL value indicates the rate your gauge builds up on the Assist Easy, Easy and Normal gauges.

On the Normal gauge, the recovery per note is `TOTAL / number of notes`. This means charts with more notes generally also have higher total values to compensate.
- A higher total means your gauge builds up faster.
- As an example, a chart having a total value of 500 means that if you hit every note in the chart with a GREAT or PGREAT, you will recover exactly 500% worth of gauge.

If you are making a chart, use the [BMS TOTAL calculator](https://hitkey.nekokan.dyndns.info/total.htm) as a reference when deciding on the TOTAL value to set for your chart (use IIDX supposition 1 as a baseline). Most charts have totals in the 350-550 range (rough estimate).

The HARD and EX-HARD gauges are also affected by TOTAL, but not in a significant manner. Only charts with very low TOTAL values (below 240) are affected. In LR2, having a very low TOTAL value will increase the damage per miss, while in beatoraja, having a very low TOTAL value will decrease the gauge recovery rate.
