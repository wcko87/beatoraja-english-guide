**Note:** If you have problems or questions about beatoraja or BMS, or have any comments on the guide, please make a post on the [Discussions Page](https://github.com/wcko87/beatoraja-english-guide/discussions). I actively monitor the Discussions page for messages.

Please **don't create issues in beatoraja's issue tracker!** The issue tracker is not for troubleshooting.

# What is beatoraja?

beatoraja is an open source BMS Player in active development.
- [beatoraja on Github](https://github.com/exch-bms2/beatoraja)

If you're here just for more information about BMS (and not beatoraja), check out the links below. These links are useful even if you are using LR2 or some other [BMS player](BMS-Overview#what-is-a-bms-player).
- [What is BMS?](BMS-Overview)
- [Where do I download BMS songs?](Downloading-Songs#where-do-i-find-songs)
- [Difficulty ratings and difficulty tables](Difficulty-Tables)

Another popular BMS player is Lunatic Rave 2 (LR2). Most of this guide is for beatoraja.
- Instructions for setting up LR2 can be found here: [Reddit LR2/BMS Setup Guide](https://www.reddit.com/r/lunaticrave2/wiki/index)

Note that judge timings and gauges in beatoraja differ slightly from LR2. There a version of beatoraja that has been modified to use LR2 judge timings and gauge (but it does not support beatoraja's internet rankings). It can be found [here](https://github.com/wcko87/lr2oraja).

----------
# Getting Started with beatoraja

This guide explains how to set up beatoraja properly, with the UTF-8 fix applied. We apply the UTF-8 fix now to avoid [potential locale-related issues](#locale-fix) later on.

If you run into any issues during setup, the [Troubleshooting](FAQ-and-Troubleshooting#beatoraja-troubleshooting) section might help.

There are two options for setting up beatoraja.
- **Option 1:** [Without Installing Java](#setting-up-beatoraja-without-installing-java)
- **Option 2:** [With a Java Installation](#setting-up-beatoraja-with-java)

----------
## Setting up beatoraja without Installing Java
This is for Windows only.

#### 1. Download beatoraja
- [Download beatoraja from here](https://mocha-repository.info/download.php).
   - You should see multiple links to choose from. Use the "**-jre-win64**" link.
- The "-jre-win64" link includes a portable build of Java in the download, which we will be using to run beatoraja.
- You might notice a "beatoraja.exe" file in the download. You can ignore (and even delete) this, as using the .exe means beatoraja will run without the UTF-8 fix.

#### 2. Apply the UTF-8 fix
- [Download beatoraja-config.bat from here](https://github.com/wcko87/beatoraja-english-guide/tree/resources/beatoraja-configs-win64jre)
- We will be using `beatoraja-config.bat` instead of `beatoraja.exe` to run beatoraja. This ensures that beatoraja runs with the UTF-8 fix already applied. [More information on the UTF-8 fix](#UTF-8-fix)

#### 3. Run beatoraja
- Double-click `beatoraja-config.bat` to run beatoraja.
- See [Configuring beatoraja](#configuring-beatoraja) for information on things you may want to configure before you start playing.

----------
## Setting up beatoraja with Java
You might want to set up beatoraja this way if you already have Java installed in your computer.

Note: If you are on Mac/Linux, use `beatoraja-config.command` instead of `beatoraja-config.bat`.

#### 1. Download 64-bit Java
- Possible Java downloads (choose):
   1. [Oracle Java](https://www.java.com/en/download/manual.jsp) (Note: Make sure you select a version marked as **64-bit**)
   2. [Liberica OpenJDK](https://bell-sw.com/pages/downloads/) (Note: Make sure you select the **Full** version instead of Standard)
- If you need more details, see: [Which version of Java should I download?](FAQ-and-Troubleshooting#which-version-of-java-should-i-download)

#### 2. Download beatoraja
- [Download beatoraja from here](https://mocha-repository.info/download.php).
   - You should see multiple links to choose from. Use the **-modernchic** link (not the win64 one).

#### 3. Apply the UTF-8 fix
- After extracting beatoraja, you should see a `beatoraja.jar` and a `beatoraja-config.bat` file in the folder.
- The easiest way to apply the UTF-8 fix is to replace `beatoraja-config.bat` with the one [over here](https://github.com/wcko87/beatoraja-english-guide/tree/resources/beatoraja-configs).
- Alternatively, you can just edit `beatoraja-config.bat` to apply the UTF-8 fix. Instructions are [over here](#locale-fix).

#### 4. Run beatoraja
- Double-click `beatoraja-config.bat` to run beatoraja.
- See [Configuring beatoraja](#configuring-beatoraja) for information on things you may want to configure before you start playing.

----------
# Locale Fix
Note: Also known as the UTF-8 fix. If you have followed the earlier instructions and have applied this fix, you may skip over this section.

### Effects of locale issues
Not being on the correct locale can cause some issues in beatoraja. Most of the time, if you are experiencing crashes in beatoraja, it is due to a locale issue. Thankfully, there is an easy fix for all these crashes.

The problems locale issues will cause:
- On skins like ModernChic or LITONE5 which have option names in Japanese, these option names will not save. When beatoraja is closed, the skin-specific settings will be reset.
- On skins like LITONE5 which have folder names in Japanese, beatoraja might not be able to access resources inside those folders, and this can cause beatoraja to crash.
- If you load a bms with file or folder names containing Japanese characters or garbled characters, certain parts of the bms may not load properly. Playing the bms twice in a row may cause beatoraja to crash.


### Fixing locale issues
There are two ways to fix locale issues in beatoraja. This fixes all the problems listed above.

- **Method 1:** Switch to Japanese locale on your PC
- **Method 2:** Run beatoraja using the UTF-8 encoding (Recommended solution)

Method 2 is highly recommended. If you are running beatoraja using the UTF-8 encoding, switching to Japanese locale is **NOT** required (I have not once switched to JP locale). Also, even if you are already using the Japanese locale, switching to UTF-8 encoding is still recommended, as this resolves crashes that happen if a BMS folder name is garbled.

**Note:** Opening .zip files is another reason frequently cited for switching to JP locale. Switching just for this reason is not recommended however, as there are better solutions to this. [More info here - locale issues when opening zip files](Downloading-Songs#locale-issues-when-opening-zip-files).

### How to run beatoraja with UTF-8 encoding
- **Remark:** If you don't want to try applying the fix manually, you can instead just replace your `beatoraja-config.bat` file with this file [over here](https://github.com/wcko87/beatoraja-english-guide/tree/resources/beatoraja-configs), which already has the fix applied.

The UTF-8 fix is applied by making a simple edit to the `beatoraja-config.bat` file (note that `beatoraja-config.bat` is what you are using to open beatoraja).

Open up `beatoraja-config.bat` (or `beatoraja-config.command`, depending on which you use to start beatoraja), and add `-Dfile.encoding="UTF-8"` to the end of the `_JAVA_OPTIONS=` line.

**Note:** The `-Dfile.encoding="UTF-8"` argument must be placed *outside* of the inverted commas `''`. This sounds odd, but the setting will do nothing otherwise. There must also be a space before `-Dfile.encoding="UTF-8"`.

The line should look like this:
```
set _JAVA_OPTIONS='-Dsun.java2d.opengl=true -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel' -Dfile.encoding="UTF-8"
```

Skin settings might reset after switching to UTF-8, because the skin settings may have been saved in the default encoding. It shouldn't be too much trouble to set the skin settings again, since you only need to do this once.

It might be possible that switching encodings might cause your player config file (in player/player1/config.json) to be unreadable. If the config file can't be fixed, you may have to replace the config file with a new one.

### How to replace (clear) your config file
1. Backup the player's config.json (player/player1/config.json)
2. Clear the contents of the file and replace it with just the characters `{}`. This forces beatoraja to generate a new config.json file from scratch (Note: beatoraja won't start without the `{}` in the file).
3. After the player profile has been cleared, open the beatoraja config again, go to the skin select menu and make sure a skin is properly set (i.e. not blank) for each of the important categories (e.g. 7KEYS, DECIDE, RESULT, SKIN SELECT). beatoraja crashes if it tries to load a blank skin.

**Note:** The player's config.json is different from the config.json you see in the main beatoraja folder! The player's config json is in the `player/player1` (or player2 etc) folder, and contains settings that are specific to the player profile, like skin settings.

There should be no more crashes / issues after that.


----------
# Configuring Beatoraja

This covers some of the more important things to configure when first starting the game. Refer to [beatoraja Configuration](Configuration) for more detailed information on what you can configure in beatoraja.

### Songs and Skins
**[Songs]** If you are looking for BMS songs, see [downloading songs/charts](Downloading-Songs) for more information on where to find them.
- I recommend downloading the [GENOSIDE 2018 starter pack](Downloading-Songs#starter-packs) if you don't know where to start, it gives a good initial selection of songs to start off with.

**[Skins]** The default skin, ModernChic, is already a pretty good skin. Refer to the [List of beatoraja Skins](List-of-beatoraja-Skins) for other skins.
- If you can't find a play skin that looks exactly like what you want, I recommend the [Simple Play](List-of-beatoraja-Skins#simple-play) skin, as it is extremely customizable (you can customize the positions and dimensions of just about every aspect of the skin, including things like the individual widths, heights and colors of notes).

### In Config Menu (before starting game):

**[Adding Songs]** Go to the `Resources` tab to add your song folders. (add them under BMS Path, not Table URL!)
- Note: Don't place your songs in your beatoraja folder. Place them somewhere else and specify the folders in the resources tab.
- If you can't see the songs in-game, see: [I added songs but I can't see the folders in game](FAQ-and-Troubleshooting#i-added-songs-but-i-cant-see-the-folders-in-game)

**[Difficulty Tables]** (not necessary) If you wish to use [difficulty tables](Difficulty-Tables), add table links to the Table URLs and click `Load difficulty table` to load all the listed difficulty tables into the game.

**[Analog Scratch]** If you are using a IIDX controller with axis input, you might want to turn on `ANALOG SCRATCH` under the `Input` tab. This needs to be turned on individually for each mode (7KEYS, 5KEYS, etc). See [Analog Scratch](Configuration#analog-scratch) for more information.

Most of the settings under `Play Option` can be configured in game.

**[Skin Settings]** If you have other skins downloaded, place them in the skin folder. You should be able to see them in the config menu, in the "skin" tab. For more information, see: [Skin settings](Configuration#skin-settings)
- If you are using ModernChic (the default skin), you should also be able to set the language shown in the music select menu to English.
- If you play on the P2 side (turntable on right), you can switch to P2 in the skin settings.


### In Game (during music select):

**[Key Config]** Press 6 on the keyboard to open key config.

**[Play Options]** In the key config, you should have bound the START and SELECT buttons (default Q and W on keyboard). Hold START, SELECT or START+SELECT to access the three play options menus. These menus cover the majority of the play options available in the config.
- The default gauge is ASSIST EASY, it might be a good idea to switch to the EASY, NORMAL or HARD gauges as these are more commonly used. See: [Gauges](Scores-and-Clears#gauges)

**[Skin Settings]** Press F12 to open skin settings in-game.

Check the [Music Select](Music-Select) page to find out what else you can do in this screen.

### In Game (during play):

**[Scroll Speed and Lane Cover]** Before the song starts, the game gives you some time to adjust your scroll speed settings.
- Double-tap START to turn on the SUDDEN+ lanecover
- Hold START + turn turntable to adjust lanecover height (white number)
- Hold SELECT + turn turntable to adjust green number (related to scroll speed)

The song will not start until you have finished adjusting.
- A full explanation on sudden+, scroll speed and green number is given here: [Scroll Speed and Green Number](Scroll-Speed-and-Green-Number)


----------
# How to Navigate Menus

The main menu screen you are on is called the "Music Select" menu.
- The [Music Select](Music-Select) page explains what you can do on this menu.

The turntable (scratch up / scratch down) is used to scroll through menus.

Notation: keys 1 to 7 are the keys from left to right. White keys are 1,3,5,7 and black keys are 2,4,6.

Generally, white keys go forward in menus and black keys go backward.
However, in beatoraja, each key actually has a slightly different purpose.

- Key 1: Go forward / start song
- Key 3: Go forward / start song on practice mode
- Key 5: Go forward / start song on autoplay mode
- Key 7: Go forward / play selected replay
- Key 2,4: Go back / change sort order if you are on topmost level
- Key 6: Select replay

