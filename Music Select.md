The Music Select menu is the menu you'll be on most of the time.
This screen is where you'll see the song wheel, where you select a chart to play.

----------
# Useful hotkeys to take note of

Press 6 on the keyboard to configure keybinds. You also need to do this to set up your controller.

Hold START, SELECT or START+SELECT to open the play options menus. (use the keys and turntable to while the menu is open to change settings)

Press the white keys to go into song folders (keys 1,3,5,7)

Press the black keys to go backward (keys 2,4, but not 6)

Press F2 on a song folder to refresh the song folder (e.g. to load new songs)

For the rest of the hotkeys, refer to the [Music Select Hotkeys](Hotkeys#music-select)


----------
# Song Wheel

In the song wheel, there are three types of folders to find your songs:

### Song Folders
Song folders that follow your BMS directory structure.

### Tables and Courses
If you had clicked "Load difficulty table" in the beatoraja config, you should be able to see your the loaded tables and courses here too. Refer to [Difficulty Tables](Difficulty-Tables) for more information.

### Special and Custom Folders
These special folders are filters to find certain songs more quickly.
The definitions of these special folders can be found in `folder/default.json` in your beatoraja directory. You can edit the `default.json` file to define your own custom filters to find songs.

Here are some of the default special folders.

- **LAMP UPDATE**: Lists charts which you have obtained new clears on recently (in the last X days)
- **SCORE UPDATE**: Lists charts which you have raised scores on recently (in the last X days)
- **MY BEST**: Misleading name. Lists your most played charts.
- **FAVORITE SONG**: Lists songs marked as favorite (use F8 to mark a song as favorite)
- **FAVORITE CHARTS**: Lists charts marked as favorite (use F9 to mark a specific chart as favorite)
- **CLEAR TYPE**: Lists charts by clear type (FC, EXHC, HARD, CLEAR, etc)
- **SCORE RANK**: Lists charts by grade (AAA, AA, A, B etc)
- **DENSITY**: Lists charts by AVERAGE, PEAK, or END densities. See [Density Ratings](#density-ratings) for more information on density.
- **FEATURE**: Lists charts by special features - e.g. scratch-heavy and LN-heavy charts.
- **LEVEL**: Lists charts by level
- **NEW**: Lists newly-added charts

## Clear Lamps

Next to each song is a Clear Lamp that indicates the [Clear Status](Scores-and-Clears#clear-status) of the song. Folders may also have clear lamps. For example, a HARD clear lamp on a folder indicates that every song in the folder has been hard cleared.

Under the folder name in the songwheel, you can also see a visualization of the proportions of your clear lamps of the songs in the folder. This is similar to the clear lamp graphs you can see on stairway or the [beatoraja Lamp Graph](http://lnt.softether.net/cgi-bin/beatoraja/index.php) website.

## Chart Information

You can view some information about the chart before playing it.

### Play Mode
Each chart indicates what play mode (7Keys, 14Keys, 9Keys etc) it is played in. Pressing 1 on the keyboard can be used to display only charts from a specific play mode.

### Chart Level and Difficulty
Each chart has a level (a number) and a difficulty (BEGINNER, NORMAL, HYPER, ANOTHER, INSANE).

The difficulty is only used to distinguish charts of the same song. Most songs will have a NORMAL, HYPER and ANOTHER chart. Some songs will also have a BEGINNER chart. All other, more difficult charts (usually [sabuns](Downloading-Songs#downloading-songs-and-sabuns)) are generally labeled with INSANE.

7Keys charts are generally labeled on a scale of 1-12, similar to the level scale in beatmania IIDX. Note that these levels are assigned by the chart maker, and thus may not be accurate. Also, while you can generally rely on the chart's level rating for songs in the level range 1-11, level 12 charts tend to be labeled in stranger ways.

Some ways "level 12" charts may be labeled:
- Some charts just use "12" as the level, no matter how hard it is.
- Some charts use level 13, 14, 15 etc to indicate that they are "harder than most 12s"
- Some charts use a level range of 1-25, representing the chart's difficulty if it were on the [insane scale](Difficulty-Tables#insane-table). Usually, charts labeled this way also have the difficulty set to INSANE. Thus, if you see a chart labeled INSANE and has the level 4, the chart might be around ★4 on the insane scale.
- And finally, some charts just use "0" as the level to indicate that the charter isn't sure what level to label it as.

Thus, it is advisable to take the displayed level rating of charts with a grain of salt. The notecount, note distribution graph and density rating can also clue you in to whether a chart is a "normal 4" or an "insane 4". For more accurate level ratings, it might be better to rely on [Difficulty Tables](Difficulty-Tables).

9Keys charts are usually labeled on a scale of 1-50, similar to the level scale in pop'n music.

### Song Duration and Notecount
Self explanatory. Most BMS songs are around 2 minutes in length.

### TOTAL value and Judgerank
The TOTAL value and Judgerank can affect the difficulty of the chart.

Higher TOTAL -> Faster gauge recovery on ASSIST EASY/ EASY/ NORMAL gauge -> Easier chart
More information on TOTAL: [TOTAL value](Scores-and-Clears#total-value)

Most charts have judgerank EASY. Charts with judgerank NORMAL, HARD etc have tighter timing windows.
More information on judgerank: [Judgerank](Scores-and-Clears#judgerank)


### Note Distribution Chart

beatoraja also displays a chart indicating the distribution of notes in the currently selected chart. White squares are regular notes, red squares are scratches, blue squares are long notes and green squares are BSS (long scratch) notes.

Thus, if you see a lot of red, expect a scratch chart. If you see a lot of blue, expect a long note chart.

The note distribution graph is also helpful to identify where the dense parts of a chart are. For example, a large spike in notecount at the end of the song indicates a difficult ending.

Dark red squares represent mines. Mines deal a bit if damage if the key is held down when the mine passes the judge line. Most of the time, mines in BMS charts are only used as note art, rather than as actual mines.

### BPM

BPM stands for "beats per minute". It indicates the tempo of the song. While songs of higher or lower bpms may have different feels, BPM is no indicator of difficulty.

Some songs may display a range of BPMs rather than a single BPM value. These are songs with BPM changes (soflans). If the BPM increases during a song, the note scroll speed increases. If the BPM decreases, the note scroll speed decreases. The changing scroll speeds can make songs with BPM changes difficult to play.

For songs with BPM changes, the note distribution chart also displays the change in BPM over time. The current BPM is displayed as a line going through the chart. More information can be found in the [Scroll Speed Fix](Configuration#scroll-speed-fix) section.

### Density Ratings

You might also notice an odd non-integer number displayed as the "difficulty" of the chart (e.g. "12.7"). This number indicates the average density of the chart.
This is an automatically generated rating for all charts, and it may not be very accurate.

This average density rating can be used as a rough indicator of the difficulty of the chart. The density rating is on a scale similar to the IIDX scale of 1-12. For example, a chart with a density rating of 7.1 is probably around a lv7 in difficulty. However, for harder 12s, you'll normally see the ratings go above 12 (e.g. "13.5", "18.6", "21.3").

However, note that the average density rating is just a rough indicator, it may not be very accurate. Here are a few things to watch out for:
- Scratch charts are often rated lower than they should be.
- LN charts are rated far lower than they should be.
- Charts with complex patterns or jacks are often rated lower than they should be.
- This density rating gives the **average** density. This means songs with long break sections (that contain few notes) often end up being rated a lot lower than they should be, as the density is averaged out.

Note that this is the same density as the average density used in the [DENSITY special folder](#special-and-custom-folders).

