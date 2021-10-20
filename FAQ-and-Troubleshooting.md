# beatoraja Troubleshooting

### [Discussions Page](https://github.com/wcko87/beatoraja-english-guide/discussions)
If you need help and the section below does not answer your questions, please visit the [Discussions Page](https://github.com/wcko87/beatoraja-english-guide/discussions). I can try to provide a bit of tech support / answer questions there.

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

#### 4. Error: Could not find or load main class bms.player.beatoraja.MainLoader
- You might experience this error if you are on Java 9+ or using OpenJDK on Linux. This may be because JavaFX isn't included with your Java installation.
- If this is indeed the case, you may have to install JavaFX manually.
- If you are on Java 8 (Java 1.8) on Windows, you will definitely have JavaFX installed, so this shouldn't be the issue.
- If you have trouble installing JavaFX (especially on mac or linux), one option is to use [Liberica JDK 8](https://bell-sw.com/pages/downloads/), which is a version of Java that has JavaFX included by default.
  - **Note:** You need to select "Full JDK" instead of "Standard JDK" when downloading Liberica. Only the Full JDK includes JavaFX.


### I added songs, but I can't see the folders in game

Try restarting beatoraja first. The songs might show up after a restart.

If the songs still don't show up, there are a few possible causes.

#### You placed your songs in the beatoraja folder

i.e. you did something like this:
```
beatoraja 0.8.2
 '-> etc etc (beatoraja files)
 '-> songs
     '-> BOFU2016
     '-> BOFU2017
```
If your songs are in the beatoraja folder, beatoraja may not be able to read the songs. In general, I recommend having your song directory be **separate** from your beatoraja directory. Something like this:
```
BMS
 '-> BOFU2016
 '-> BOFU2017
 '-> MISC

beatoraja 0.8.2
 '-> etc etc (beatoraja files)
```
In general it is a good idea to keep your song folders separate from the game client. This is because you may upgrade or change your BMS client, but you will still be using the same BMS songs.

#### An error occurred while adding songs
This might have happened if you notice a bunch of errors in the command window and the song adding process halts suddenly.
- If this indeed happened, try to find out which is the offending BMS that caused the song adding to crash.
- If you can figure out which BMS is causing the issue, it would be nice to report it to the developers so that the problem can be identified.

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


### My skin settings are not saving

This is usually a symptom of locale issues. See [Fixing locale issues](#fixing-locale-issues) for more information, and make sure the UTF-8 fix is applied.
- If you had applied the UTF-8 fix manually, there is a chance that you did not apply it correctly.
- Also, do not run beatoraja through the beatoraja.jar file. The UTF-8 fix does nothing if you are not running beatoraja by starting beatoraja-config.bat.
- It is possible that you have also somehow corrupted your player config file. In that case, you might want to [reset your player config file](#how-to-replace-clear-your-config-file).


### My scores are not saving

Scores will always save after exiting the song (as long as you have hit at least 1 note in the song before exiting). If your scores aren't saving, it is most likely because you have some assist option on. Check out the following pages:
- [Assist and Miscellaneous Options](Configuration#assist-and-miscellaneous-options)
- [Random and Gauge Settings](Configuration#random-and-gauge-settings)

If your scores suddenly vanished, it may simply because you switched between [LN, CN and HCN modes](Configuration#ln-cn-and-hcn-mode). Scores are saved separately between the modes, for charts that have at least one long note in them.


### I connected my controller but my turntable does not work!

You probably did not bind the controller in the key config. Even the turntable needs to be assigned to F-SCR and R-SCR in the key config for it to work. Press 6 on the keyboard to open the key config in game.

If that was not the reason, there are a few other possible causes:
- Take note that the controller must be plugged in before starting beatoraja.
- If you have multiple controllers connected, make sure the correct controller device is selected in the key config. Press 2 on the keyboard in the key config menu to change the controller selection.
- Take note that the key config is set separately for each key mode. Notably, 5Keys and 7Keys have separate key configs. Press the left/right arrow keys on the key config menu to switch key mode.
- If the controller only does not work in the music select menu, this may be because you have the wrong "Music Select" setting in the key config menu. Press 1 on the keyboard to switch the "Music Select" setting. "2dx sp" means the 7Keys key config is used for music select. "2dx dp" means the 14Keys key config is used, and "popn" means the 9Keys key config is used.
- If the turntable is behaving wierdly, this may be due to analog scratch being set incorrectly. See: [Analog Scratch](Configuration#analog-scratch)

------------------------

------------------------

# Frequently Asked Questions

## What is beatoraja.jar?

You might notice that beatoraja uses a ".jar" file instead of an ".exe". What does this mean?

beatoraja was written in Java, and Java programs are typically packaged as .jar files. In other words, `beatoraja.jar` is the beatoraja game program itself.

To run JAR files like `beatoraja.jar`, Java is used. Java can either be installed into your PC so that .jar files can be run directly, or a portable version of Java can be used to run `beatoraja.jar`. If you had downloaded the "-jre-win64" version of beatoraja from the Mocha website, a portable version of Java can be found in the `\jre` directory in the beatoraja folder (specifically, `\jre\bin\java.exe`).

`beatoraja-config.bat` and `beatoraja.exe` (if you had downloaded the "-jre-win64" version) are not the program itself. You might notice this from how small these files are. All they do is use Java to run `beatoraja.jar` in the same directory, after setting a few important options. You can open up `beatoraja-config.bat` in notepad to see exactly what it is doing.

Therefore, if you are using `beatoraja-config.bat` to run beatoraja (which is recommended to use the UTF-8 fix), `beatoraja.exe` is not needed and can be deleted.

Note: Do not run beatoraja.jar directly by double-clicking it. It can run that way, but it is not recommended and also would skip the UTF-8 fix.

## Which version of Java should I download?
There are two good options: Oracle Java and Liberica OpenJDK

We suggest Java 8, as it has JavaFX included. beatoraja is compiled with Java 8, though it can still work on later versions of Java as long as JavaFX is present.

### Option 1: Oracle Java
Download From: https://www.java.com/en/download/manual.jsp
- Note: Make sure you select a version marked as **64-bit**

If you did not select a 64-bit version of Java, you will get the ["invalid maximum heap size"](https://github.com/wcko87/beatoraja-english-guide/wiki/FAQ-and-Troubleshooting#2-invalid-maximum-heap-size--xmx4g) error message when you run beatoraja.

You can technically run beatoraja on 32-bit java. This can be done by removing the `-Xmx4g` flag from beatoraja-config.bat. However, this is not recommended as the `-Xmx4g` flag is what allows beatoraja to run with a memory cap of 4GB rather than the default 1GB cap.

### Option 2: Liberica OpenJDK
Download From: https://bell-sw.com/pages/downloads/
- You might notice a few different options under "Package". You need to download a **Full* package, not the Standard package.
- Recommendation for simplest setup: **Full JRE**, **Download MSI**.

Note: If you downloaded Standard instead of Full, you will get the ["Could not find or load main class bms.player.beatoraja.MainLoader"](https://github.com/wcko87/beatoraja-english-guide/wiki/FAQ-and-Troubleshooting#4-error-could-not-find-or-load-main-class-bmsplayerbeatorajamainloader) error as JavaFX is not included with the Standard version.

### Liberica - JDK or JRE?
**JRE** = Java Runtime Environment, and **JDK** = Java Development Kit.
- Download "Full JRE" if all you care about is running Java (for beatoraja). Download "Full JDK" if you are also a Java developer.
- Full JRE is a smaller download.

### Liberica - Download MSI or ZIP?
**MSI** is an installer, **ZIP** is a portable version of Java (no install required).
- Downloading the MSI makes it easier to set up. After installing Java, beatoraja can simply be run from `beatoraja-config.bat`.
- If you download the ZIP instead, you will need to either configure your PATH environment variable or edit `beatoraja-config.bat` to run the portable version. More details below.

#### ZIP Option 1: Editing beatoraja-config.bat
Do this if you want a portable setup of beatoraja. More information on this page: [Guide: Setting up portable Java + beatoraja](https://github.com/wcko87/beatoraja-english-guide/discussions/37)

#### ZIP Option 2: Configuring PATH environment variable
Downloading and installing the MSI version does this step automatically for you. If you downloaded the ZIP instead, you will need to configure the PATH environment variable yourself.

Let's suppose that we have extracted Java to `D:\jre1.8.XXX\`. This means java.exe will be found in `D:\jre1.8.XXX\bin\`.

What configuring the PATH environment variable does:
- Notice that when you open command prompt in an arbitrary location and type `java` in it, nothing happens, because the computer does not even know whether you have Java installed, or where you have placed it if you have installed it.
- The PATH environment variable specifies the "default" folders for the computer to look into when you type a command straight into command prompt.
- In other words, after you have added your Java path `D:\jre1.8.XXX\bin\` from before to PATH, when you type `java` in command prompt, the computer will check the `D:\jre1.8.XXX\bin\` folder, find java.exe in it, and run it.
- Why does this matter? This is because when you run beatoraja-config.bat, it types "java" into the command prompt to run Java to run beatoraja. You can see this by opening beatoraja-config.bat in notepad.

How to configure the PATH environment variable:
1. Open the start menu, and type "environment variable" into the search box. You can choose to open "Edit the system environment variables" or "Edit the environment variables for your account". Either works.
2. Now look for an environment variable named "Path". There should be one in the box for environment variables for your account and one in the box for environment variables for the system. Either works.
3. Double-click the "Path" environment variable to open it. You should see a list of folders. Click new, and add your Java path (e.g. `D:\jre1.8.XXX\bin\`) to the list. Press Ok.
4. Note that you will need to restart command prompt before changes will apply, if you are trying to type "java" into the command prompt.

