# SUDDEN+, HI-SPEED, BPM and Green Numbers

The way scroll speed is handled in beatoraja is very similar to beatmania IIDX. If you are already familiar with IIDX, this page won't be of much help to you.

For information on how to adjust these settings in beatoraja, refer to [the configuration page](configuration#sudden-hi-speed-green-number).

## SUDDEN+

SUDDEN+ is the name of the lane cover at the top of the screen. Press the START key twice while playing a song to toggle the SUDDEN+ lane cover.

During a song, turn the turntable while holding the START button to adjust the height of the lane cover. The height of the lane cover is indicated by a number known as the "white number".

## HI-SPEED and BPM

Higher HI-SPEED means notes scroll faster. Songs with higher BPM have notes that scroll faster. So generally, one would have to set a lower HI-SPEED on higher BPM songs to compensate for the faster-scrolling notes.

However, this is only conceptual. This does not matter in beatoraja, since we set the green number directly instead.

## Green number

Green number is a magic number that is calculated based on your SUDDEN+ lane cover height, HI-SPEED setting and song BPM. All of the above settings don't matter all that much, as long as your green number is fixed.

To adjust your green number during a song in beatoraja, turn the turntable while holding the SELECT button. Your green number is carried between songs.

If you adjust your lane cover height in beatoraja, your HI-SPEED setting will be automatically adjusted so that your green number remains constant. This is similar to what happens in the floating hi-speed mode in IIDX.

#### Technical details of Green number

The green number is the amount of time each note is visible for (i.e. starting from the time the note shows up from behind the SUDDEN+ lane cover, until the note is no longer visible).

The beatoraja green number uses different units from the green number in IIDX. The beatoraja green number indicates the number of milliseconds a note is visible for, while the IIDX green number indicates the number of frames a note is visible for, if the game runs at 600fps.

In short, `beatoraja green number = IIDX green number * 5/3`. A beatoraja green number of 500ms corresponds to a IIDX green number of 300.

Most players converge to a IIDX green number that's somewhere in the 270-310 range (that's 450-517 in beatoraja).

Your play skin may choose to display the beatoraja green number or the IIDX green number. Usually, if it's the IIDX green number, it is displayed in green, while the beatoraja green number may be displayed in another color like yellow or blue.

Play and find a green number and lane cover height (white number) that you're comfortable with.


## Hidden and Lift

Hidden and lift cover the bottom of the screen (while sudden covers the top). Hidden acts only as a cosmetic cover, hiding the bottom of the lanes. On the other hand, lift moves the judge line upward along with the cover.



