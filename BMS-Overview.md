## Contents:
- [What is BMS?](#what-is-bms)
- [BMS Charting](#bms-charting)
- [BMS Community and Events](#bms-community)

----------
# What is BMS?

Short Answer: Be-Music Source (BMS) is a file format for rhythm game charts.

This file format was devised by Urao Yane in 1998. ([Original BMS Spec](http://bm98.yaneu.com/bm98/bmsformat.html))

In a [rhythm game](https://en.wikipedia.org/wiki/Rhythm_game), the player presses buttons in accordance with the music. The song refers to the music itself that plays, while the chart for the song is the "gameplay" - i.e. the sequence of buttons you have to press when you play the song in game. Refer to [BMS Charting](#bms-charting) for what a chart for a song looks like.

![bmsdance - ESA Winter 2020](https://user-images.githubusercontent.com/27341392/74804639-d9cb7c00-52ae-11ea-9650-417ed5088e4e.gif)
(Image credit: Chazoshtare @ ESA Winter 2020)

But a `.bms` chart is just a sequence of notes in a file. To play the charts, you use a [BMS Player](#what-is-a-bms-player) like Lunatic Rave 2 or beatoraja. Simply put, a BMS player is the game. It reads the chart files, and challenges you to clear the song.

(Note: BMS is technically a file format, but sometimes we just refer to the game as "BMS")

Here is a video example:
https://www.youtube.com/watch?v=EW4tv3mcQ-I

Note that we also use BMS to refer to related formats like .bme, .bml, .bmson and .pms.

BMS supports multiple play modes corresponding to the amount of keys, including:

- 7KEYS (mechanics based on beatmania IIDX)
- 5KEYS (mechanics based on 5key beatmania)
- 9KEYS (mechanics based on pop'n music. often we use the .pms extension for 9KEYS charts instead)
- 14KEYS (mechanics based on IIDX double play)
- 10KEYS (5key double play)
- 24KEYS (mechanics based on keyboardmania)
- 48KEYS (24KEYS double play)

7KEYS is the most common play mode in BMS.
One advantage of the BMS file format is that it is human-readable and relatively easy to work with. This makes it possible to edit charts manually in a text editor, and also relatively easy to write a parser for the BMS file format.

## BMS Music

A unique feature of the BMS community is that all of the music used for the game is composed by members of the community. This is partially driven by how all music in BMS are required to be fully [keysounded](#bms-charting). Refer to [BMS Community and Events](#bms-community) for more information.

- Please note that using or playing illegally-sourced music is not allowed. This refers to activities like taking a song that you do not own (or not made by the BMS community), and making a chart for it with silent keysounds. Using music that you do not own the rights to is illegal and the BMS community is against this sort of behavior. Please refer to [BMS Charting](making-charts) for more information.

----------
# What is a BMS Player?

A BMS player is used to play BMS songs/charts. The first BMS player is BM98, first introduced in 1998, as its name implies. Some commonly used BMS players today are Lunatic Rave 2 (LR2), beatoraja, ruv-it, bemuse, etc. There are many other BMS players out there.

- [How to set up BMS with beatoraja](home)

Note that Lunatic Rave 2 does not support the more recent .bmson file format, while beatoraja does.

Here is a (pretty long) [list of BMS players](https://www40.atwiki.jp/laser_bm/pages/16.html), sorted by release year/platform from 1998 to the current day (note: JP). Over 50 BMS players have been made since its introduction.

----------
# What does a BMS song contain?

Each BMS song is contained in its own folder. The folder for a single BMS song often contains hundreds of files. Here are the usual contents of the folder:

#### BMS Chart files (.bms/.bml/.bme etc)
- The chart files tie all the other files together
- Basically, a chart specifies when each keysound is to be played in the song, thus organizing the individual keysounds into a full song.
- A song can have multiple charts. A separate chart file is used for each difficulty (e.g. Normal, Hyper, Another).

#### Keysounds (generally .wav or .ogg)
- Each BMS song is broken up into (often) hundreds of individual keysounds. These keysounds a strung together in a chart to make up the song.

#### BGA or BGI files
- Many songs feature a background animation (BGA) in a video format or a background image (BGI) in an image format. Background animations can also be made by stringing together a series of images by specifying when each image is displayed in the BMS file.

#### Other miscellaneous files
- There are some other optional "metadata" files that can also be included in the song folder.
- **Stagefile**: A 640x480 preview image for the song.
- **Banner**: A wide banner preview image for the song.
- **Preview file**: A short clip of the song that plays during music select. (not common as preview files are not supported by LR2)


----------
# BMS Charting

Related: [Making Charts](making-charts)

BMS charts are fully keysounded. The use of unkeysounded notes is generally frowned upon by the community and unkeysounded songs are not allowed.

As mentioned above, BMS songs are broken down into (often) hundreds of keysounds. These keysounds are sequenced in the BMS file to make up the song. Each keysound is often used multiple times in the song (e.g. the same drum sample is may be played multiple times).

![chart_comparison](https://user-images.githubusercontent.com/27341392/58397688-aabc0d00-8084-11e9-9417-67ed3a644e5e.gif)

In a chart, each keysound in the song corresponds to a single note. Not all of the keysounds have to be made into playable notes. The red notes are those which have not been dragged into the playable columns (e.g. the 8 playable columns). These "unused" notes make up the background track during gameplay.

Most of the time, the majority of the keysounds will be used as the background track. More difficult charts can usually be made by dragging more notes out of the background track and into the playable columns.

The [process of charting a song](making-charts) usually involves deciding which notes to drag out of the background track into the playable columns, and deciding which columns to place the notes into. Different difficulties for the song are made by dragging out different notes from the background track into the playable columns.


Making an unkeysounded BMS is possible by making a single long keysound at the start of the song and using empty keysounds for the notes. However, unkeysounded BMS's are generally considered "illegal" and are not allowed to be used in most aspects of the BMS community. For example, LR2's Internet Ranking (LR2IR) has a rule that states that no single keysound in the BMS may exceed 60s. Charts violating this keysound rule cannot be uploaded into LR2IR.

This rule is generally enforced to restrict BMS songs to original compositions by the community. The next section gives a general idea of the structure of the community.

To find out where to download BMS songs, refer to [Downloading Songs](Downloading-Songs#where-do-i-find-songs).

----------
# BMS Community

The BMS Community is generally self-sustaining, with all its music created by the community itself. BMS charts are either made by the composers themselves, or by dedicated charters.

## BMS Events

While composers can release their BMS's on their own, this is not often done. Instead, most BMS compositions are submitted to BMS Events, where players and composers give feedback and rate each other's submissions. The biggest and most well known BMS events are the BMS of Fighters (BOF) series of events (e.g. [BOFU2016](http://bmsoffighters.net/bofu2016/), [BOFU2017](http://www.bmsoffighters.net/bofu2017/), [G2R2018](http://www.bmsoffighters.net/g2r2018/)), which are events also known outside of the BMS community. The BOF series of events attract hundreds of submissions each year.

- [Video showcase of the Top 5 (by score) songs from each BOF event from BOF2004 to BOFXV (2019)](https://youtu.be/M4A6f1XWNDE)

Aside from large events like BMS of Fighters, there are many other smaller events happening throughout the year (rough estimate: around 10 BMS events per year, with smaller events usually having around 20 to 100+ song submissions).

- A list of past and upcoming BMS events can be found here: [BMS event schedule](https://hitkey.nekokan.dyndns.info/bmsevt.htm#ALL)
- Information on downloading BMS event packs can be found here: [Downloading Event Packs](Downloading-Songs#event-packs)

A BMS event usually has two main phases: the **registration phase** and the **impression phase**.
The registration phase is the time window for BMS creators to submit their songs/charts. After the registration deadline is past, the submissions are usually gathered into a single downloadable song pack (the "event pack") and the impression phase starts. The impression phase is when players play the songs from the event and give ratings/feedback (i.e. "impressions") on the submissions. 
After the impression period, the results/scores of the submissions are tallied. What happens at this stage depends on the nature of the event. Some events announce winners, while others don't.

### Recurring BMS Events
Some BMS events are only held once, while some are part of a series. This section gives a rough overview of some of the recurring BMS events. Only a few of these recurring events (e.g. BMS of Fighters, PABAT!, Mumei / A-1 ClimaX) occur consistently every year. Refer to the [BMS event schedule](https://hitkey.nekokan.dyndns.info/bmsevt.htm#ALL) for the webpages corresponding to these events.

- [**BMS of Fighters**](https://www.bmsoffighters.net/)
    - Team-based BMS event (each team produces between 2 and 4 BMS works).
    - Held annually, usually in the last quarter of the year. First held in 2004.
    - Event name varies by year. BOF2004-BOF2013, G2R2014, BOFU2015-BOFU2017, G2R2018, BOFXV, BOFXVI
    - After each BOF event (since 2009), songs are specially selected be included in [GroundbreakinG](https://gdbg.tv/), a compilation album for the event. These albums are available for free download, and feature long or remastered versions of the selected songs by the artists themselves.

- [**PABAT! 20XX seasons**](http://k-bms.com/)
    - Held by the Korean BMS community.
    - Held annually, usually in the first quarter of the year. First held in 2013.
    - After each PABAT! event, bbangsami (organizer of PABAT!) publishes the [PABAT! special mixset](https://soundcloud.com/bbangsami/sets/pabat-special-mixset), a long mix of selected songs from the event submissions.

- **Mumei (無名) / A-1 ClimaX**
    - Mumei ("no-name") is for composers new to the BMS scene, while A-1 ClimaX is for composers who are less new.
    - These two events are always held together, and share an event venue (website).
    - Held annually, usually in the middle of the year. First held in 2002 (Mumei) / 2008 (A-1 ClimaX).

- **Touhou Ondanyuugi (東方音弾遊戯)** - Event for remixes of Touhou music. First held in 2006.
- **Spring/Summer/Autumn/Winter 9KEYS** - Event for making PMS (songs with 9Keys charts).
- **BOFOON** - Event for shitpost / meme BMS submissions. (example: [BOFOONXV stream](https://youtu.be/vqZalh_JQSk))
- **Mutual Faith** - Event where each submission is a collab work between two composers.
- **Be-Music West** - Event focusing on western BMS artists.
- **GENRE-SHUFFLE** - Artists draw lots that decide which genre of music they are to make.
- **B.J.Cup** - Themed event, a theme is selected beforehand and participants make songs according to the theme.
- **HYPER REMIX** - Event for remixes of existing BMS songs.

## BMS Tools

The BMS community is decentralized, being made up of a network of separate tools rather than being controlled by a central server. BMS tools refers to any part of the infrastructure of the BMS community. See [BMS Tools and Resources](BMS-Tools-and-Resources) for a list of helpful tools and resources for various aspects of BMS.