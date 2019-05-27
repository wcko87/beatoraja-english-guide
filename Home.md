# Running Beatoraja

#### 1. Download 64-bit java
- beatoraja may not run properly on 32-bit java. Refer to [this error description](#2-invalid-maximum-heap-size--xmx4g) for more details.

#### 2. Download beatoraja
- Make sure you download the beatoraja release itself, from [Mocha Repository](https://mocha-repository.info/download.php), not the source code from Github!
- If `beatoraja.jar` is absent from your beatoraja directory, you probably downloaded the source code instead of the program itself.

#### 3. Run beatoraja
- run beatoraja by starting `beatoraja-config.bat`. Do not run beatoraja by launching the beatoraja.jar directly. If you wish to make a shortcut, point the shortcut to `beatoraja-config.bat`.
- If you are on mac/linux, use `beatoraja-config.command` instead.

### LOCALE ISSUES: READ THIS BEFORE PLAYING
As BMS has a largely Japanese community, there's a high chance that you might run into some encoding/locale issues later on. It might be best to take some pre-emptive steps to resolve this beforehand.

# Locale Fix

### Effects of locale issues
Not being on the correct locale can cause some issues in beatoraja. Most of the time, if you are experiencing crashes in beatoraja, it is due to a locale issue. Thankfully, there is an easy fix for all these crashes.

The problems locale issues will cause:
- On skins like LITONE5 which have option names in Japanese, these option names will not save. When beatoraja is closed, the skin-specific settings will be reset.
- On skins like LITONE5 which have folder names in Japanese, beatoraja might not be able to access resources inside those folders, and this can cause beatoraja to crash.
- If you load a bms with file or folder names in Japanese characters, certain parts of the bms may not load properly. Playing the bms twice in a row may cause beatoraja to crash.


### Fixing locale issues
There are two ways to fix locale issues in beatoraja. This fixes all the problems listed above.

- **Method 1:** Switch to Japanese locale on your PC
- **Method 2:** Run beatoraja using the UTF-8 encoding

### Running beatoraja with UTF-8 encoding

Open up `beatoraja-config.bat` (or `beatoraja-config.command`, depending on which you use to start beatoraja), and add `-Dfile.encoding="UTF-8"` to the end of the `_JAVA_OPTIONS=` line.

The line should look something like this:
```
set _JAVA_OPTIONS='-Dsun.java2d.opengl=true -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel' -Dfile.encoding="UTF-8"
```

Skin settings might reset after switching to UTF-8, because the skin settings may have been saved in the default encoding. It shouldn't be too much trouble to set the skin settings again, since you only need to do this once.

After switching to UTF-8, if you experience any crashes when loading the skins in game, try switching to the default skin, and back to your current skin. This refreshes the settings and saves them again in the correct encoding.

There should be no more crashes / issues after that.


# Configuring Beatoraja

This covers some of the more important things to configure when first starting the game. Refer to [beatoraja Configuration](Configuration) for more detailed information on what you can configure in beatoraja.

### In Config Menu (before starting game):

Go to the `Resources` tab to add your song folders. (add them under BMS Path, not Table URL!)
If you are looking for songs/charts, see [downloading songs/charts](Downloading-Songs) for more information.

If you wish to use [difficulty tables](Difficulty-Tables), add table links to the Table URLs and click `Load difficulty table` to load all the listed difficulty tables into the game.

If you are using a IIDX controller with axis input, you might want to turn on `ANALOG SCRATCH` under the `Input` tab. This needs to be turned on individually for each mode (7KEYS, 5KEYS, etc).

Most of the settings under `Play Option` can be configured in game.

It might also be good to get a good skin for beatoraja, like [LITONE5](https://desout2.000webhostapp.com/litone5-beatoraja/), LITONE6 (WIP) or [Brook](https://twitter.com/isocosa/status/1084583459266412544). The default skin is pretty bad. Skin settings can be set in the `Skin` tab.

If you play on the P2 side (turntable on right), you can switch to P2 in the skin settings.


### In Game (during music select):

Press 6 on the keyboard to open key config.

In the key config, you should have binded the START and SELECT buttons (default Q and W on keyboard). Hold START, SELECT or START+SELECT to access the three play options menus. These menus cover the majority of the play options available in the config.

Press F12 to open skin settings in-game.


### In Game (during play):

Before the song starts, the game gives you some time to adjust your scroll speed settings.
- Double-tap START to turn on the SUDDEN+ lanecover
- Hold START + turn turntable to adjust lanecover height (white number)
- Hold SELECT + turn turntable to adjust green number (related to scroll speed)

The song will not start until you have finished adjusting.
A full explanation on sudden+, scroll speed and green number is given here: [Green Number](Green-Number)


# How to navigate menus

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


# Common Issues


### Can't start up beatoraja - beatoraja-config.bat opens and closes instantly

Just before the .bat file closes, it actually displays an error message telling you what went wrong. Unfortunately, it closes too quickly to view the error message.

There are two ways you can view the error message:
1. Open command prompt in the beatoraja folder, and type `beatoraja-config.bat` to run beatoraja from the command prompt. This lets you view the error message because the command prompt doesn't automatically close.
2. Open beatoraja-config.bat in a text editor like notepad, and type `pause` on a new line at the bottom of the file. The "pause" command will prompt you to "Press Any Key to Continue" before the command window closes. You can remove the pause command after you're done diagnosing errors.

Here are the common errors you might see:

#### 1. java not found
- Then java is either not properly installed, or is installed but has not been added to the PATH environment variable. If you are not sure how to add java to PATH, reinstalling java should automatically add it to PATH for you.

#### 2. Invalid maximum heap size: -Xmx4g
- Then you are currently using 32-bit java. 64-bit java is recommended for running beatoraja.
- To check whether your current java installation is 32-bit or 64-bit, open command prompt (windows+R, type "cmd", enter) and type `java -version`. If you are on 64-bit java, it should say something along the lines of `64-Bit Server VM`. If you don't see that, you are on 32-bit java.
- You can technically run beatoraja on 32-bit java. This can be done by removing the `-Xmx4g` flag from beatoraja-config.bat. However, this is not recommended as the `-Xmx4g` flag is what allows beatoraja to run with a memory cap of 4GB rather than the default 1GB cap.

#### 3. beatoraja.jar is not found
- There should be a beatoraja.jar in the same folder as beatoraja-config.bat. If there is no beatoraja.jar, you probably downloaded the source code for the game instead of the game itself. beatoraja.jar is the main game executable, and so is definitely necessary.


### I added songs, but I can't see the folders in game

There are a few possible causes.

#### An error occurred while adding songs
This might have happened if you notice a bunch of errors in the command window and the song adding process halts suddenly.
- If this indeed happened, try to find out which is the offending bms that caused the song adding to crash.
- If you can figure out which bms is causing the issue, it would be nice to report it to the developers so that the problem can be identified.

#### A BMS folder is placed next to a song folder
This might have happened if you only see a few songs in your songwheel, and don't see any subfolders.
- Don't put song folders next to subfolders in your BMS song folder. We may not be able to differentiate between song folders and subfolders when this happens.
    This is an example of song folders next to subfolders. Don't do this.
    ```
    BMS
    |-> BOFU2016
    |-> song1
    '-> song2
    ```
    You can organize your BMS folder like this instead:
    ```
    BMS
    |-> BOFU2016
    '-> Misc Songs
        |-> song1
        '-> song2
    ````



