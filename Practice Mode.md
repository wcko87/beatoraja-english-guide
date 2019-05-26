# How to Use Practice Mode

Practice mode can be started by pressing **KEY 3** instead of **KEY 1** to start the song. Practice mode settings are changed with the arrow keys.

In practice mode, you can try out a song under different settings (e.g. freq, total, judgerank), or play specific parts of songs.

Some examples of what practice mode can be used for:

- To play songs at a higher or lower freq. For example, playing at 80% freq means th song plays at 80% speed. 100% freq is the default. Freq can be used to adjust a song/chart you like to your desired difficulty.

- To play songs with a tighter or easier judge. Regularly playing practice mode on tighter judge settings can be used to improve timing, for example.

- To learn how to hit a scratch pattern or a burst in a specific chart. (by replaying only that section over and over again). Useful for learning gimmick charts.

- To mark out a specific section of a chart that may be good for general practice of certain patterns. For example, the chart may have a specific section that may be very good for practicing chords, but also has a long intro you'd have to sit through. Practice mode can be used to play only the desired section of the chart over and over again. This makes for efficient practice, especially with the RANDOM or R-RANDOM option on.

- To try out a chart from a dan course on the dan gauge, to check if you are ready to play the course, without having to commit to the course (use gauge type GRADE and gauge category LR2 for dan courses). You can also choose how much remaining gauge to start with. For example, one may try out the final song of a dan course starting with 15% gauge, if they expect to end the previous song with around 15% gauge remaining. This can also be used to compare the difficulty of the NORMAL and MIRROR options.

- To preview the rest of the chart if you had hard-failed out of it earlier. Simply scroll to where you had failed out before, and start playing the song from there.

- To play charts without saving scores. (e.g. for test playing a work-in-progress chart)

- To test play a chart you made to figure out the right total value to set for it.

# Practice Mode Options

Use the arrow keys on the keyboard to change practice mode settings.

### START TIME, END TIME
Select which part of the song you want to start from / end at. You can also look through the chart by scrolling through it via changing the start time.

### GAUGE TYPE
Select gauge to play on. GRADE, EX GRADE and EXHARD GRADE refer to the course gauge on normal, hard and exhard respectively. To play on the dan gauge, gauge category should also be set to LR2.

Refer to [Gauges and Clears](Scores-and-Clears#gauges) for the other gauges.

### GAUGE CATEGORY
The gauges for each mode behave slightly differently.
- SEVENKEYS: use beatoraja 7 keys gauge
- FIVEKEYS: use beatoraja 5 keys gauge
- PMS: use beatoraja 9 keys gauge
- KEYBOARD: use beatoraja 24 keys gauge
- LR2: use Lunatic Rave 2 gauges

### GAUGE VALUE
Select amount of remaining gauge at the start. 

### JUDGERANK
Customize the size of judge windows. 100 (100%) is EASY judge, while 75, 50, 25 are for NORMAL, HARD and VERY HARD judge respectively.
Example: EASY judge (100) has a 20ms PGREAT window. Setting JUDGERANK to 80 gives a 16ms PGREAT window.

### TOTAL
See [TOTAL value](Scores-and-Clears#total-value) for an explanation on TOTAL values.
Set a higher total for faster gauge recovery on the ASSIST EASY / EASY / NORMAL gauges.

Technical note: that if START TIME / END TIME is used to crop part of the song, the TOTAL will be scaled proportionally to the amount of notes in the crop.
- For example, on a 2000 note song with 400 total, if there are only 1500 notes in the crop (start time to end time), the actual total will be scaled down to 300.
- This does not affect the ASSIST EASY / EASY / NORMAL gauges, as the recovery is scaled proportionally.
- However, this may affect the HARD and EX-HARD gauges if the total goes below 240 after the scaling. It may be good to set very high totals when playing on HARD or EX-HARD so that damage (LR2) or recovery rate (beatoraja) will not be affected.

### FREQUENCY
This sets the speed of the song directly. The default value is 100, which is the default speed of the song. For example, setting it to 130 plays the song at 130% speed, and setting it to 60 plays it at 60% speed.
- freq 50 equates to LR2's FREQ-12, while freq 200 equates to LR2's FREQ+12.

### GRAPHTYPE
Choose the note graph displayed. Note that the graphs other than NOTETYPE may have performance issues.

### OPTION-1P / OPTION-2P / OPTION-DP
Configure random options. (and flip option for DP)
Refer to [Random and Gauge settings](Configuration#random-and-gauge-settings) for more information on random options.