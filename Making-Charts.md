# How do I chart BMS?
- [General Structure of BMS Songs/Charts](#general-structure-of-bms-songscharts)
- [How to Get Started with Charting](#how-to-get-started-with-Charting)
- [How to Make Charts Using uBMSC](#how-to-make-charts-using-ubmsc)
- [Chart Metadata](#chart-metadata)
- [Frequently Asked Questions](#frequently-asked-questions)


## General Structure of BMS Songs/Charts

BMS charts are generally fully keysounded. The use of unkeysounded notes is frowned upon by the community.

What this means is that each BMS song is split up into lots of individual sounds - every single drum beat, piano, synth etc you hear in the song is a separate keysound. These keysounds play in sequence to form the song.

The image below shows the keysound objects from part of a song (about 3 measures of keysounds).

![keysounds](https://user-images.githubusercontent.com/27341392/71384886-08c8b880-25b2-11ea-9acf-116a605a86df.png)

Each object in the above image has a label from 00 to ZZ. Each label corresponds to a different keysound file. The BMS file contains a table that maps each label to an audio file:

![keysound_labels](https://user-images.githubusercontent.com/27341392/71384885-08c8b880-25b2-11ea-94a1-e7a8a881e1e0.png)

This process of breaking down a song into individual keysounds is done by a composer. Refer to [Dolphin's Guide to Keysounding](https://www.youtube.com/watch?v=xYAeD4YPbAM) if you want to learn about the keysounding process.

To turn a BMS into a playable chart, these keysounds are dragged horizontally into the playfield (e.g. the 7+1 playable lanes).

![dragging notes into playable lanes](https://user-images.githubusercontent.com/27341392/58397688-aabc0d00-8084-11e9-9417-67ed3a644e5e.gif)

Each keysound thus corresponds to a single note. Not all keysounds need to be used in the chart. The keysounds in the playable lanes will be the keysounds you need to play in game, and the unused keysounds (red) will make up the background track of the song. Most of the time, the majority of the keysounds will remain as the background track.


## How to Get Started with Charting

### Required Software
1. Chart Editor
    - Recommended: [uBMSC](https://github.com/zardoru/iBMSC/releases)
    - Alternatives: iBMSC, BMSE
2. BMS Preview Tool (pick one)
    - [uBMplay](http://ucn.tokonats.net/archives/ubmplay/ubmplay_152.zip). Issue: Can be a pain to get working.
    - [BMIIDXView2015](http://www.charatsoft.com/software/bmview/index.html). Issue: Lacks a lot of features.
    - [mBMplay](https://misty.orz.hm/mbmplay.html). Good features, but can be a little slow, and lacks the ability to pause.

### Finding Something to Chart
Note that the keysounding process is done by composers. Charting is when you shift the keysounds into the playable lanes. As a charter, there are a couple of ways you can get started with charting:
1. Compose your own song and keysound it, then chart it (and maybe submit it to an [event](BMS-Overview/#bms-events).
2. Collaborate with a composer, and help to chart their song after they have keysounded it.
3. Make a [Sabun](Downloading-Songs#downloading-songs-and-sabuns). This generally refers to an additional chart for an existing BMS song.

Most charters make [sabuns](Downloading-Songs#downloading-songs-and-sabuns) (option 3). To make a sabun, look for an existing BMS song and open up the song folder. Each .bms (or .bme, .bml, .pms, .bmson) file corresponds to a chart for the song. Make a copy of one of these files and give it your own title. 
- **Note:** Many composers include a "template" file for making sabuns. Look for a file with a strange extension (e.g. `._bms`, `.sabun`, `.bmssss` etc), or within a .zip or subfolder. These are usually blank template files meant to be used for sabun makers. An example is in the image below:

![template_file](https://user-images.githubusercontent.com/27341392/71384892-09614f00-25b2-11ea-8cbf-0bc1195c80cd.png)

You can then open up your new chart with a chart editor (like uBMSC) and edit it. More information on how to make a chart is given in the next section.

### Finishing and Distributing Your Chart

All you need to distribute is the `.bms` file for your chart. However, please make sure it is clear what song your chart is for!

A popular place to upload charts is the [BMS Sabun Uploader](http://gnqg.rosx.net/upload/). Any new charts uploaded to BMS Sabun Uploader will be automatically posted on the [BMS Sabun Uploader Twitter](https://twitter.com/bmsuploader) account.

You can also opt to upload your charts elsewhere (e.g. your own personal website). It is useful to understand how people typically [download songs and sabuns](Downloading-Songs#downloading-songs-and-sabuns).


## How to Make Charts Using uBMSC

### Downloading the Necessary Tools
[uBMSC](https://github.com/zardoru/iBMSC/releases) is the recommended tool for making BMS charts. (there are older alternative editors like iBMSC and BMSE, but they are not recommended)

Note that uBMSC cannot preview the BMS song/chart on its own. You need a BMS Preview Tool to view the BMS on autoplay. Refer to [Required Software](#required-software) for links to BMS preview tools.

### Configuration
Configuration Checklist:
1. Set Preview Tool in Player Options
2. Text Encoding
3. Number of B Columns
4. Color Scheme

##### 1. Set Preview Tool in Player Options
When you press F5 or F6 to preview the song, the BMS preview tool is launched. Under `Options -> Player Options`, you can configure which preview tool will be launched by default. The following image shows the Player Options window.

![player_options](https://user-images.githubusercontent.com/27341392/71384891-09614f00-25b2-11ea-9658-f3a8f643b74a.png)

##### 2. Text Encoding
Most of the time, .bms files are saved in the Shift-JIS encoding. Thus, we recommend setting the Text Encoding to Shift-JIS under `Options -> General Options`.

![general_options_text_encoding](https://user-images.githubusercontent.com/27341392/71384884-08c8b880-25b2-11ea-9365-edac53b06af8.png)

##### 3. Number of B Columns
B Columns refer to the columns B1, B2, B3, etc. These columns contain keysounds that have not been mapped to any of the playable lanes. By default, only 15 B columns are visible. However, composers frequently place keysounds on columns above B15. So that you don't miss potentially useful keysounds, we recommend increasing the number of visible B columns (around 50 might be good).

To increase the number of visible B columns, expand on of the boxes on the side panel to reveal the "Number of B Columns" option. (see the image below)

![number_of_b_columns](https://user-images.githubusercontent.com/27341392/71384890-09614f00-25b2-11ea-88e0-b55493d715b5.png)

##### 4. Color Scheme
In a 7keys layout, column A1 is supposed to be the scratch, while columns A2-A8 are the 7 keys. However, uBMSC's default color scheme can be a little misleading.

This is uBMSC's default color scheme:
![notes_and_keysounds_old_colors](https://user-images.githubusercontent.com/27341392/71384889-09614f00-25b2-11ea-8ba9-4db0889178df.png)

This is the modified color scheme I use:
![notes_and_keysounds](https://user-images.githubusercontent.com/27341392/71384888-09614f00-25b2-11ea-9480-a3163137909c.png)

To switch to a 7keys theme, go to `Options -> Theme` and select `IIDX.Theme.xml`. Alternatively, you can manually configure the color scheme in `Options -> Visual Options`.

### Charting Tips

**Important:** Make sure you enable "Disable vertical moves" under the Grid settings on the side panel (see image). This option is useful as moving notes vertically would change how the music sounds, which is often not what you want. This option can be toggled with the "D" key.

![disable_vertical_moves](https://user-images.githubusercontent.com/27341392/71384882-08c8b880-25b2-11ea-90bc-f96de6ccb201.png)

Miscellaneous uBMSC tips:
- Hold SHIFT and drag a note vertically to convert it into a Long Note. You can convert it back to a regular note by dragging the top of the note back to the bottom of the note.
- Clicking on a note (in uBMSC) allows you to hear the keysound associated with the note.


Miscellaneous charting tips:
- Keysounds are important. Similar drums usually go on similar lanes. (and drum kicks usually go on key 1)
- Generally, scratches are used for cymbal crashes, vocal samples, scratch sound effects, etc.
- Make sure you set a proper [#TOTAL value](Scores-and-Clears#total-value)! Not setting a proper TOTAL can make your chart unplayable.

## Chart Metadata

A BMS chart has the following metadata that can be set:

![metadata](https://user-images.githubusercontent.com/27341392/71384887-09614f00-25b2-11ea-87a7-c4f9fe62c646.png)

**Note:** When making a sabun, please do not change the song title, artist, genre or BPM.

**Note:** Don't forget to set the **TOTAL** value!

- **Title:** Title of the song
    - Sometimes, the subtitle is appended to the end of the title instead of being written into the subtitle field. (e.g. having "Cursed Nightshade [NORMAL]" as the title)
- **Artist:** Composer of the song
- **Genre:** Genre of the song
- **BPM:** Base BPM of the song
- **Player:** Play Mode (e.g. Single / Double Play)
- **Rank:** [Judge Rank](Scores-and-Clears#judgerank) of the chart
    - This determines how difficult the timing windows are.
    - "Easy" is the most common judge rank. "Normal" is sometimes used but is not as common.
- **Play Level:** The numerical "difficulty level" of the chart.
    - This is the [number displayed next to the chart](Music-Select#chart-level-and-difficulty).

The following pieces of metadata will be revealed if you click "Expand" on the side panel (highlighted in the above image).

- **SubTitle:** Subtitle of the chart.
    - This will be appended after the name of the chart in game.
    - Commonly used for [sabun subtitles](Downloading-Songs#downloading-songs-and-sabuns).
    - Note: A strange issue with LR2IR happens if the song Title (not subtitle) contains text at the back surrounded by dashes (e.g. Awaking Beat-From the Next Generation-). If this happens, the text surrounded by the dashes (i.e. -From the Next Generation-) will automatically be interpreted as the subtitle in LR2IR, and adding a subtitle (e.g. [ANOTHER]) will overwrite this text, making the song show up as "Awaking Beat [ANOTHER]" in LR2IR. To work around this problem, you can add the sabun subtitle to the end of the song title instead of to the subtitle field (so that you get "Awaking Beat-From the Next Generation- [ANOTHER]")
- **SubArtist:** Similar to Subtitle, but for the artist field
    - This can be useful for adding the name of the BGA maker, chart maker etc.
    - Common practice is to write something like "obj. ChartersName", where ChartersName refers the name of the charter.
- **Stage File:** Image used as the [Stage File](BMS-Overview#other-miscellaneous-files) for the song.
- **Banner:** Image used as the [Banner](BMS-Overview#other-miscellaneous-files) for the song.
- **Bank BMP:** don't remember what this is
- **Difficulty:** displayed difficulty type (BEGINNER/NORMAL/HYPER/ANOTHER/INSANE)
    - See [chart level and difficulty](Music-Select#chart-level-and-difficulty).
- **ExRank:** not commonly used. Changes judge windows in an odd way.
- **Total:** [#TOTAL value](Scores-and-Clears#total-value) for the chart.
    - Remember to set this!
- **Comment:** does nothing. Comment is readable in the .bms file or a chart editor.
- **LnObj:** LN format for the chart. We recommend keeping it as "None (#LnType 1)"
    - As the original BMS format did not support Long Notes (LNs), there were multiple competing implementations of LN support in the format.
    - This option has no effect on gameplay. It only affects how LN format in the .bms file.
    - Using "None" treats an LN as a single note of a different type. This is the simplest to work with. Use SHIFT+drag to convert a note between a regular note and a long note.
    - If it is set to any other option, then each LN is made out two notes - a regular note and an LN ending note. For example, let's say LnObj is set to "ZZ". Then objects of label ZZ will be used to designate the endings of long notes.



## Frequently Asked Questions

##### Q: What is the difference between `.bms`, `.bme`, `.bml`, `.pms` and `.bmson`?

A: Other tham `.bmson`, these extensions do not matter and can be used interchangably. `.bms` is the standard, though some people use `.bme` or `.bml` instead. Modern BMS players read them all the same way. `.pms` is usually used to represent 9K charts.

- `.bmson` represents a completely different file format. It is a newer, json-based file format that never really took off. uBMSC cannot be used to edit `.bmson` files. LR2 cannot play `.bmson` songs, though beatoraja can.
- Why there are multiple extensions that mean the same thing: `.bms` was originally used for 5key charts, `.bme` was then introduced for 7key charts, and `.bml` added long note support. However, this distinction no longer exists in modern BMS players. `.bms`, `.bme` and `.bml` all support 5keys, 7keys, long notes etc and refer to the exact same format.

##### Q: "Warning: Note overlapping detected. Increasing Maximum Grid Partition will resolve this."

A: If you get this error, go to `Options -> General Options` and increase the "Max Grid Partition in BMS" setting. I usually have it very high, like 10000.

The default value is 192. This means the smallest possible subdivision allowed when saving the BMS is 192ths. This may be important for some legacy applications. However, some songs make use of subdivisions smaller than 192ths, and it may be necessary to increase the max grid partition in order for these songs to save correctly.
