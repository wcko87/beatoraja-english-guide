Beatoraja supports usage of several different Internet Ranking (IR) Services, which allow submission of scores, and may also provide additional IR-specific features.
- Currently, scores can be sent to multiple services at the same time, with one of them set as the "Main IR".
- The Main IR adds certain features to the [music select](Music-Select) screen and is the one used for viewing chart pages when pressing `F11`.
- All IRs will BAN accounts for playing illegal BMS files.

# 1. [Mocha-Repository](https://mocha-repository.info)
The most populated IR, only available bundled with the compiled releases.
- It has rival support, settable course clear badges and a LEVEL REVIEW system.
- These features are available when mocha is set as the main IR.

### LEVEL REVIEW
A feature allowing players to declare the difficulty and comment on the charts they've played, similarly to the popular [STATISTIK](http://statistik.benhgreen.com/IIDX/ratings) website for IIDX. These ratings are then averaged and compiled into LEVEL REVIEW [difficulty table](Difficulty-Tables) for the 7KEY and 14KEY modes, accessible from music select.

### Collections
Users can create collections and courses which others can subscribe to via the mocha website, which adds those folders to the music select screen.

### Gauge Auto Shift
Mocha treats clears submitted using Gauge Auto Shift differently than the other IR services:
- The first score submitted to IR will register with the achieved clear lamp in all cases.
- Subsequent scores will only update the lamp on the IR if the clear achieved is equivalent to the selected gauge, otherwise it will register as an assist clear.

For example, if IR already has a normal clear and you want to update the IR lamp to a hard clear, you will need to select the hard gauge and clear for the IR lamp to update. Achieving a better clear than the selected gauge (ex-hard instead of hard) will still register as an assist clear on the IR.

# 2. [MinIR](https://www.gaftalk.com/minir/)
The main unique feature of this IR is the Unique ID which can be used to bind the profile with [Stellaway](https://lite.stellabms.xyz/#/stellaway/beatoraja) for the Satellite and Stella difficulty tables.
- When set as the main IR, it pushes the Satellite and Stella [difficulty tables](Difficulty-Tables) to your client, so it's best to not have them in your table list as it will duplicate them.
- Other unique feature are user-created scoring contests of varying lengths.
- Has rival and course support

# 3. [CitrusIR](https://citrus-ir.iidx.app/)
Another early IR implementation. No specific features when set as the main IR. 