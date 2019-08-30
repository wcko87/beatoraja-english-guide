# What are difficulty tables?

Difficulty tables are collections of "recommended" charts to play. These tables do not contain the charts or songs themselves. They are simply lists of charts (containing chart hashes so that the game can identify the charts).
Charts in difficulty tables are listed by difficulty.

An example of a well-known difficulty table is the [Insane scale](http://www.ribbit.xyz/bms/tables/insane.html), which divides charts into 25 levels, ★1 to ★25. For example, when we say a chart is ★10, it means it belongs to ★10 on the insane scale.

After loading a difficulty table into your BMS player (e.g. beatoraja), you will be able to see the list of charts in-game, and can play the charts by selecting them from the table. However, you will need to have the songs/charts already downloaded (i.e. somewhere in your BMS folder) before you can play them. 
See [downloading songs/charts](Downloading-Songs) for more information.

# Why use difficulty tables?

As BMS events are open for anyone to create and submit songs/charts, by design there is no quality control on the submissions. BMS events will contain both high and low quality songs/charts.
Difficulty tables, in a sense, work as some sort of quality filter.

Difficulty tables also serve as level ratings for charts. The level indicated on the chart itself is set by the chart creator, and this level may not be accurate. The levels in the difficulty tables are decided by the creator of the table, and often has gone through some discussion within the community.


# What are dan courses?

Courses can be included in difficulty tables. Among these courses are what people call "dan courses". A dan course is a specific set of (usually 4) songs used to test one's ability. In a course, you have to clear the sequence of given songs using a single health gauge that carries between songs. A player is said to have achieved a dan rank if they are able to clear the dan course corresponding to that rank.

The current "standard" set of dan courses used in BMS is the GENOSIDE 2018 dan courses. This is a set of 22 courses. In order of increasing difficulty, the courses are:
- GENOSIDE 2018 初段 (normal 1st dan) to GENOSIDE 2018 十段 (normal 10th dan)
- GENOSIDE 2018 発狂初段 (insane 1st dan) to GENOSIDE 2018 発狂十段 (insane 10th dan)
- GENOSIDE 2018 発狂皆伝 (insane kaiden)
- GENOSIDE 2018 overjoy

The song list for each of these courses can be viewed here: [GENOSIDE 2018 Dan Courses](http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=gradelist)

There are also other similar dan courses, like the Satellite/Stella courses, or the LN dan courses.


# Using difficulty tables in beatoraja

beatoraja tables use the glassist table format. Tables are hosted on webpages, and these pages have embedded .json files containing the table data.

To use a table in beatoraja, go to the `Resources` tab in the beatoraja config, and add the URL to a table into the list of table URLs. By default, the list already contains some common tables, like the Normal2, Insane2 and LN tables.

However, none of these tables will load until you click on `Load difficulty table` at the bottom of the config. This button fetches the table data from the webpages in the list.

After clicking on `Load difficulty table`, you should be able to see the tables in-game.

When scrolling through the tables in-game, you might find songs that have their names in red. This means you do not have the song/chart currently downloaded. Selecting an undownloaded song in beatoraja will open up the download links for the song and the chart in your default browser.


### How do I play dan courses in beatoraja?

beatoraja courses are stored in tables. LR2 course files (.lr2crs files) cannot be used in beatoraja.

The GENOSIDE 2018 normal dans (初段 - 十段) can be found in the Normal2 table. The GENOSIDE 2018 insane dans (発狂初段 - overjoy) can be found in the Insane2 table. The LN dans can be found in the LN table.
Thus, they are playable by default (just click `Load difficulty table`) as long as you have the songs.

With a few exceptions (below), all the songs required for the GENOSIDE 2018 dan courses are included in the [GENOSIDE 2018 Starter Package](http://nekokan.dyndns.info/~lobsak/genocide/grade.html). You may also need to download the Append package and merge it into the GENOSIDE 2018 folder. (the Append package contains additional charts, which may be needed for the insane dans.)

These are the only dan songs missing from the GENOSIDE 2018 Starter Package:
- ★20 ひつぎとふたご [7KEY/LUNATIC] - for insane 9th dan course
- ★24 Love & Justice [GOD] - for insane kaiden course
- ★25 FREEDOM DiVE [FOUR DIMENSIONS] - for overjoy course

Satellite Skill Analyzer and Stella Skill Simulator have separate beatoraja links on the [Satellite](https://lite.stellabms.xyz/#/skill)/[Stella](https://stellabms.xyz/#/skill) websites.

All of these dan courses include a contraint that forces beatoraja to use the LR2 dan gauge, to ensure consistency in difficulty with the same dan courses in LR2.

# Popular difficulty tables

This section contains a brief list of some of the more commonly-used tables. For a more extensive list of tables, please refer to [Ribbit's list of difficulty tables](http://www.ribbit.xyz/bms/tables/table_list.html).

The Normal2, Insane2 and LN tables are included in beatoraja by default.

We recommend the Normal2, Insane2, Satellite and Stella tables, as they contain more recent songs and are more frequently updated, unlike the Normal, Insane and Overjoy tables.

### [Normal table](http://www.ribbit.xyz/bms/tables/normal.html)
- Levels rated from ☆1-☆12. Covers the "IIDX" level range.
- ☆12 correspons to the easiest 12s in IIDX. Anything harder than the easiest 12s is in the insane scale.

### [Insane table](http://www.ribbit.xyz/bms/tables/insane.html)
- Levels rated from ★1-★25. These 25 levels subdivide the level "12" in the IIDX level range.

### [Overjoy table](http://www.ribbit.xyz/bms/tables/overjoy.html)
- Levels rated from ★★1-★★7. ★★1 corresponds to ★21 and ★★5 corresponds to ★25.

### [Normal2 table](http://bmsnormal2.syuriken.jp/table.html)
- Similar to the Normal table, but contains more recent songs, and is more frequently updated. Songs rated from ▽1-▽12.

### [Insane2 table](http://bmsnormal2.syuriken.jp/table_insane.html)
- Similar to the Insane table, but contains more recent songs, and is more frequently updated. Songs rated from ▼1-▼25.

### [Satellite table](https://lite.stellabms.xyz/table.html)
- A new table containing many high quality charts. New songs are added every two weeks by a system of community voting. More information can be found here: [Satellite website](https://lite.stellabms.xyz)
- Charts are rated on a scale of sl0-sl12. Covers the level range ☆11-★19.

### [Stella table](https://stellabms.xyz/table.html)
- A new table containing many high quality charts. New songs are added every two weeks by a system of community voting. More information can be found here: [Stella website](https://stellabms.xyz)
- Charts are rated on a scale of st0-st11. Covers the level range ★20 and up, as well as the overjoy difficulty range.

### [Scratch (sara) table](http://minddnim.web.fc2.com/sara/3rd_hard/bms_sara_3rd_hard.html)
- For scratch charts.

### [LN (long note) table](http://flowermaster.web.fc2.com/lrnanido/gla/LN.html)
- For LN charts. Not frequently updated.
