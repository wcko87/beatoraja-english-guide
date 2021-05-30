There are generally three places where you can configure things:
1. In the config menu (before starting the game)
2. During [music select](Music-Select) (in game)
3. During play (in game)

This list is organized by the settings you can configure. How and where you can configure each setting will be explained.

----------
## Key Config

#### During music select
Key config is done by pressing `6` on your keyboard during music select. Keys are configured separately for each play mode (5K, 7K, 9K etc).


----------
## Analog Scratch
If you are using a controller, there are two possible scratch input modes for it. 
1. **LR2 Mode:** Axis value reflects the **direction** the turntable is turning. It returns to center when the turntable is stopped.
(+1 when rotating clockwise, -1 when rotating counterclockwise, 0 when stopped.)
2. **Analog Mode:** Axis value reflects the current **position** of the turntable. It stays fixed when the turntable is stopped.
(Slow increase from -1 to +1 as you rotate clockwise, looping back to -1 the moment it passes +1. It decreases when you rotate counterclockwise.)

[Video: What the two input modes look like](https://user-images.githubusercontent.com/27341392/103452096-05acf000-4d0f-11eb-8033-e530ae2abc34.mp4)

Analog Mode is preferred for beatoraja.
- If your controller is in analog mode, make sure Analog Scratch is **checked** in the beatoraja config.
- If your controller is in LR2 mode, make sure Analog Scratch is **unchecked**.

The turntable will not be read by the game correctly otherwise.

You can find out which input mode your controller is in by opening the controller properties in Windows' control panel (you can find it by searching "set up usb game controllers" in the start menu). Alternatively, you can use the online [HTML5 Gamepad Tester](https://gamepad-tester.com/).

Most controllers allow you to switch between the two input modes. Analog mode is "HID mode" on Dao cons and "Mode 3" on a YuanCon.


**Note:** The Analog Scratch setting must be set separately for each keymode (5Keys, 7Keys, 14Keys etc).

#### In config menu
Under the `Input` tab.

----------
## Adding and Updating Song Folders in beatoraja

#### In config menu
Go to the `Resources` tab to add your BMS song folders. (add them under BMS Path, not Table URL!)

If you want to refresh the songs within a folder, the fastest way to do so is to hover over a song folder in game (during [music select](Music-Select)) and press F2. This refreshes the selected song folder.

In the config, the `Update Song Database when starting` setting will automatically refresh the song folder when starting beatoraja. However, this can slow down beatoraja especially if you haven't added any new songs to your song folders.

`Update BMS database` and `Rebuild BMS Database` can be very slow. I rarely use these options.


----------
## Difficulty Tables

Refer to the following page: [How to set up difficulty tables in beatoraja](Difficulty-Tables#using-difficulty-tables-in-beatoraja)


----------
## Skin Settings

Allows you to choose your skin, as well as set the options for your currently chosen skin. Note that you have to select your skin separately for each of the menus.

- [List of beatoraja skins](list-of-beatoraja-skins)

Here are the important categories to set a skin for:
- **7KEYS, 5KEYS, 14KEYS, 10KEYS, etc.**: Skin used during gameplay.
- **MUSIC SELECT**: The screen you are on most of the time, while selecting a song.
- **DECIDE**: The little animation that plays after you select a song, before transitioning to the gameplay screen.
- **RESULT**: The result screen after a song is over.
- **COURSE RESULT**: The result screen after a course is over.

#### In config menu
Under the `Skin` tab.

#### During music select
Press F12.


----------
## Replay Settings
beatoraja has four replay slots for each chart. A replay can be manually saved after a song is over by pressing 1,2,3 or 4 on the keyboard in the result screen, corresponding to which slot you wish to save the replay into.

Alternatively, you can set beatoraja to automatically save replays under certain conditions.

#### In config menu
The conditions to automatically save replays in each of the slots 1-4 can be configured under `Play Option`.

Personally, I like to set Replay1 to "Always" (my most recent replay), Replay3 to "Better or same Score" (my best score), and Replay4 to "Better or same Lamp" (my best clear).


----------
## SUDDEN+, HI-SPEED, Green Number
Explanation of these settings: [Scroll Speed and Green Number](Scroll-Speed-and-Green-Number)

#### In config menu
These can be configured in the `Play Option` tab.

#### During music select
The green number can be adjusted when holding START+SELECT.

#### During play
- Hold START and turn the turntable to adjust the lanecover height.
- Hold SELECT and turn the turntable to adjust the green number
- Double-tap START to toggle the SUDDEN+ lanecover.
- To adjust the hidden/lift height, double-tap START to turn off SUDDEN+, then use START + turn turntable to adjust the hidden/lift lanecover. (Note: hidden/lift needs to be turned on in the config menu first)

The song will not start until you have finished adjusting.


----------
## Offset

Offset is measured in milliseconds. If you are hitting fasts, make your offset more negative. If you are hitting slows, make your offset more positive. (Note that this is the opposite of the setting in IIDX)

Generally, your offset should stay within the ±20ms range, assuming you aren't on a display with significant visual delay. When adjusting offsets, it is usually sufficient to adjust it in intervals of around ±4ms.

Note that adjusting offset essentially only accounts for visual delay. Audio offset cannot be changed, as the game is keysounded. (the game can't be expected to play a keysound before you hit the key)

#### In config menu
In the `Play Option` tab.

#### During music select
Offset can be adjusted when holding START+SELECT.


----------
## Hidden and Lift
Explanation of these settings: [Hidden and Lift](Scroll-Speed-and-Green-Number#hidden-and-lift)

#### In config menu
Hidden/lift can be enabled/configured in the `Play Option` tab.

#### During play
See: [adjusting your lanecover height](#sudden-hi-speed-green-number)

To adjust the hidden/lift height in-game, double-tap START to turn off SUDDEN+, then use START + turn turntable to adjust the hidden/lift lanecover. (Note: hidden/lift needs to be turned on in the config menu first)


----------
## LN, CN and HCN mode

beatoraja offers multiple modes for long notes.
- **LN Mode**: Long Note. No release timing, long notes count as one note each. Similar to LR2.
- **CN Mode**: Charge Note. Has release timing, long notes count as two notes each; one for the start and one for the release. Long scratch notes (BSS notes) require you to reverse the turntable at the end of the note. Similar to IIDX.
- **HCN Mode**: Hell Charge Note. Similar to CN mode, except that long notes continue to drain health as long as you do not keep them held.

#### In config menu
The long note type can be selected in the `Play Option` tab.

#### During music select
Press `3` to toggle the long note type.

Note that on charts with long notes, scores/clears for LN, CN and HCN modes are saved separately. If you do not see any of your scores, you might be on a different mode from your usual.


----------
## Single play, Double play, etc

You start SP/DP mode by selecting a chart corresponding to the mode.
During music select, press `1` to toggle which charts are visible.


----------
## Song sort order
Press `2` during music select to toggle sort order.


----------
## Random and Gauge settings

The different gauges are explained here: [Gauges and Clears](Scores-and-Clears#gauges)

Note that the random settings on the right side are used only for double play (10K, 14K). The settings on the left side should be used for single play.

Random options (explained from the 7K perspective):
- **NORMAL**: default option, chart is unchanged.
- **MIRROR**: Flips columns horizontally. Columns 1234567 become 7654321.
- **RANDOM**: Shuffles the 7 columns.
- **R-RANDOM**: Random rotation/mirror of the columns 1-7. (e.g. 1234567 -> 4321765)
- **S-RANDOM**: Every note in the chart is individually shuffled.
- **SPIRAL**: A little complicated. Each consecutive note is given an increasing offset from its original position. For example, the first note may be shifted 2 columns right, the second note 4 columns right, the third note 6 columns right, the fourth note 1 column right, and so on.
- **H-RANDOM**(＊): Similar to s-rand but consecutive notes are shuffled to different columns (i.e. avoids jacks)
- **ALL-SCR**(＊): Shifts as many keys to the scratch lane as possible. For chords, only one note from each chord is moved to the scratch lane.
- **RANDOM+**(＊): RANDOM but shuffles scratch too
- **S-RANDOM+**(＊): S-RANDOM but shuffles scratch too

(＊) Scores and clears are not saved for H-RANDOM, ALL-SCR, RANDOM+ and S-RANDOM+.

DP Random settings:
- For DP, the random settings of the 1P and 2P sides are configured separately.
- Use the FLIP option to swap the left and right sides.
- Use the BATTLE option to play an SP chart on both sides.


#### In config menu
Random and Gauge settins can be configured in the `Play Option` tab.

#### During music select
Hold START to configure your Random and Gauge settings.
- Note that there are two Random settings. The one on the right is only used for double play (each side can have a separately-configured random setting).


----------
## Scroll Speed Fix
NOTE: This is not the same as the constant scroll speed assist option.

This matters for songs with BPM changes. Your [green number](Scroll-Speed-and-Green-Number) is saved between songs, so that the scroll speed you play at is fixed between songs. However, for songs where the BPM (and thus scroll speed) changes, one needs to decide which BPM to fix your desired scroll speed to.

tl;dr: Set this to "Main BPM" and you'll almost never need to think about this again.

- **OFF**: Disables scroll speed fix. Not recommended.
- **START BPM**: Fixes scroll speed to the BPM at the start of the song.
- **MIN BPM**: Fixes scroll speed to the lowest BPM of the song.
- **MAIN BPM**: Fixes scroll speed to the most used BPM in the song (i.e. the modal BPM). This is the recommend setting in almost all cases.
- **MAX BPM**: Fixes scroll speed to the highest BPM of the song.

The [note distribution chart](Music-Select#note-distribution-chart) in the music select screen also displays the variation in BPM over time in the currently selected chart. The BPM is displayed as a line going through the chart.

This "BPM line" is color coded. Blue = min BPM, Green = main BPM, Red = max BPM. The rest of the line is in yellow. This can be used to deicde which scroll speed fix setting to use.

The main BPM is also displayed in green next to the song's indicated BPM range.

----------
## Gauge Auto Shift

beatoraja has [multiple gauges](Scores-and-Clears#gauges) you can play a song on. By default, if you select a gauge that is too difficult for you on a song, you fail the song. Gauge Auto Shift is a feature in beatoraja to "play" all the gauges at once. You are awarded the clear corresponding to the hardest gauge you clear the song on in that play.

Note: beatoraja IRs may treat Gauge Auto Shift (GAS) clears differently. See the [IR services](Internet-Ranking-Services) page for more information.

Visually, if you start on the EX-HARD gauge, running out of hp on EX-HARD will switch the gauge view to display the HARD gauge instead. Running out of hp on HARD makes it display GROOVE/EASY/ASSIST EASY, depending on which of the three is the hardest gauge where you are currently above the "passing" range.

Note that you can always press key 6 on the result screen to view the gauge graph for each of the gauges.

Gauge Auto Shift (GAS) Options:
- **NONE**: Gauge Auto Shift is disabled.

- **CONTINUE**: If you hit 0% gauge on the survival gauges (HARD, EX-HARD, HAZARD), you can continue to play the song till the end. However, your gauge remains at 0% throughout the song and you will not receive any clears.

- **SURVIVAL TO GROOVE**: If you start on a survival gauge (HARD, EX-HARD, HAZARD), reaching 0% will switch you over to the NORMAL (Groove) gauge.

- **BEST CLEAR**: The game will always start you on EX-HARD, and switches gauges as you fail them in the manner explained at the start of this section.

- **SELECT TO UNDER**: The game will always start you on your currently selected gauge, and switches gauges as you fail them in the manner explained at the start of this section.

Bottom Shiftable Gauge Options:
- This option is to specify the lowest gauge you can shift to with Gauge Auto Shift. Useful if you don't want to flood your music select screen with assist clears.


#### In config menu
These options are available in the `Play Option` tab.

#### During music select
The Gauge Auto Shift option can be changed while holding START+SELECT.



----------
## Assist and Miscellaneous Options

Assist Options
- **CONSTANT**: Notes scroll at a constant rate regardless of BPM. Disables scores on charts with BPM changes.
- **BPM Guide**: Displays all bpm changes in the chart. Disables scores on charts with BPM changes.
- **LEGACY NOTE**: Turns all long notes into regular notes. Disables scores on charts with long notes.
- **NO MINE**: Removes mines. Disables scores on charts with mines.
- **EXPAND JUDGE**: Quadruples the size of the judge windows. Makes timing extremely easy. Disables scores.

Miscellaneous Options 
- **Show judge region**: Visual indicator for judge window sizes during gameplay.
- **Show hidden notes**: Some charts may have hidden keysounds that you can trigger if you know they are there. This option displays these hidden notes.
- **Mark processed note**: After a note is hit and removed, an outline of the note will remain until the note is no longer visible.
- **GUIDE SE**: A "clap" sound effect is played for each note hit, as a timing guide.

Miscellaneous Options (joke options for difficulty)
- **WINDOW HOLD**: A joke option from IIDX, which emulates holding the START button all the time, so every button press causes the HI-SPEED to change.
- **Extra Note**: Extra Mode from LR2. Adds unused keysounds from the song to the playfield in random lanes, making charts significantly harder (and unfun). Has three levels of difficulty. 0 turns off Extra Mode. 1-3 represents Extra Mode 1, 2, 3 respectively, in increasing order of difficulty.
- **Mine Mode**: An option from LR2. Adds mines to the chart. Has four options - REMOVE, ADD RANDOM, ADD NEAR, ADD ALL.
- **Scroll Mode**: An option from LR2. Adds arbitrary BPM changes to the chart. Has two options - REMOVE and ADD, which removes and adds bpm changes respectively.
- **Long Note Mode**: An option from LR2. Turns all notes into long notes. Has five options - REMOVE, ADD LN, ADD CN, ADD HCN, ADD ALL. The last option (ADD ALL) turns each note into a long note of a random type, so you get a chart that mixes [LNs, CNs and HCNs](#ln-cn-and-hcn-mode).

You get an assist clear instead of your usual clear when you play with assist options on (and scores aren't saved). Miscellaneous options don't affect your scores or clears.

#### In config menu
These options are available in the `Play Option` tab.

#### During music select
Most of these options can be toggled while holding SELECT.


EXPAND JUDGE is a little unique. If you toggle EXPAND JUDGE in game during music select, it only toggles between 100 (default) and 400 (4x judge windows). However, in the beatoraja config, you can set EXPAND JUDGE to any value between 25 and 400. 100 is the default, meaning the timing windows are 100% their usual size. Setting EXPAND JUDGE < 100 makes timing windows stricter, and setting EXPAND JUDGE > 100 makes timing windows less strict. Scores are only saved when EXPAND JUDGE <= 100.


----------
## Music Select Song Wheel Scroll Speed

If you find the song wheel (music select) to be scrolling too slowly or too quickly, this can be adjusted in the beatoraja config, under the `Input` tab.
In a typical menu scroll, pressing down the up/down key initially scrolls you up/down by one option. After a slight delay, the menu will start auto-scrolling as you continue holding down the key.

#### In config menu
There are two settings corresponding to this:
- **First song selection list scroll**: This is the amount of delay before the song wheel starts auto-scrolling.
- **After that**: This is the time interval between options during auto-scrolling.

If your song wheel is scrolling too slowly, decrease the duration of **After that**.

If you find it difficult to scroll one song at a time (e.g. you're always overshooting the song you want to select), increase the duration of **First song selection list scroll**.


----------
## Accelerated Skin Loading

#### In config menu
In the `Other` tab in the config there is an option to `Create (CIM) file for accelerated skin image loading`. Use this for skins to load more quickly.


----------
## Audio Settings

#### In config menu
Setting the Audio Output to PortAudio is generally recommended for lower latency.


----------
## Fast Forward Settings

During autoplay or watching replays, songs can be fast-forwarded or slowed down (See [Hotkeys](Hotkeys#during-autoplay--replay)). In [practice mode](Practice-Mode), songs can be played at an faster or slower speed (frequency).

#### In config menu
In the `Audio` tab, the `Frequency Option` and `Fast forward` settings offer two possible behaviors for keysounds when a song is played at a different speed.
- **FREQUENCY** slows down or speeds up each individual keysound.
- **UNPROCESSED** keeps the keysounds as they are. Fastforwarding thus only means that the keysounds are played at a faster rate. This option is not really recommended as it can make the song sound choppy.


----------
## Miss Layer duration

Some BMS's contain a miss layer, which is an image or animation that plays whenever you miss a note. The duration of the miss layer can be configured in the beatoraja config.

#### In config menu
The miss layer duration option can be found in the `Video` tab. Set it to 0ms to disable miss layers.

----------
## Menu Sounds and BGM Settings

- [You can find some sound sets here.](List-of-beatoraja-Skins#sound-sets)

#### In config menu
There are two ways menu sounds and menu BGM can be configured.
1. In the `Skin` tab, assign the BGM Path (LR2) and Sound Path (LR2) folders. This allows you to use LR2 sound sets.
2. In the `Skin` tab, under the category `SKIN SELECT`, assign a sound set from a skin. (As far as I know, no skins support this yet. The sound set included with LITONE5 is set up via the first method.)

----------
## Setting up Twitter score posting

- Get a Twitter developer account. This can be done by going to the [Twitter developer portal](https://developer.twitter.com/en/portal/dashboard).

- Create an application. Copy and paste the API Key and the API Key secret somewhere, but **DO NOT SHARE THEM**. These are your application keys.

- Edit your application to enable Read **and write** access. This is necessary to post tweets.

- Under the "Keys and Tokens" tab, generate an "Access token & secret" for your account (your handle should be specified). Paste the two tokens somewhere, but again, **DO NOT SHARE THEM**. These are your personal tokens.

#### In player/player(playernumber)/config.json
  
- Find the `twitterConsumerKey` line (usually at the end of the config.json file).

`twitterConsumerKey` and `twitterConsumerSecret` are your application keys.

`twitterAccessToken` and `twitterAccessTokenSecret` are your personal tokens.

Fill these lines with your tokens like so :

```
"twitterConsumerKey": "xxxxxxxxxxxxxxxxxxxxxxx",
"twitterConsumerSecret": "xxxxxxxxxxxxxxxxxxxxxxx",
"twitterAccessToken": "xxxxxxxxxxxxxxxxxxxxxxx",
"twitterAccessTokenSecret": "xxxxxxxxxxxxxxxxxxxxxxx"
```