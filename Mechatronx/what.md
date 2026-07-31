# Ideas for project

## Disc rot keep-in-checker? / Mold please-dont-grow-in-my-sink detector

### Will need:
- Moisture detector
- Temperature detector
- Light sensor (maybe)
- Some way to detect ultraviolet rays? (REALLY maybe)
- Multicoloured LEDs and/or a speaker.
- A switch(???)

### This relates by:
I am a PC software archivist. Many of my older PC games/programs are on CD-ROMs or DVD-ROMs. I am worried about some rotting. Some have already rotted. (rest in pepperonis Eureka's 601 Games Volume 2, and Spongebob RotFD for PS2 (in some part), Spider-Man: The Ultimate Villain Showdown, and one of my Ice Age 3s on Blu-Ray, even though they werent my fault.) Many, more discs I just own, and dont have as much incentive to archive, but I would still like to keep the discs' longevity, even if disc rot in the first place is really rare.

Alongside optical media, I also own a small amount of various videocassette tapes. Mold is an issue I've seen way more than once, either in my grandmother's own collection or in thrift / antique stores. Mold, unlike disc rot, is more common and affects all magnetic media formats equally. I know there's specialised cleaners for VHS tapes and cassette tapes, but more obscure formats like MiniDV or Video 2000 might not. And besides, I think prevention is better. Removers might scrape off some of the magnetic coating on the tape.

Alternatively, I might get into collecting / archiving old PC / Commodore 64 / Amiga / Famicom Disk System / whatever floppy disks (& relatives) just to "extend my archival efforts" or something like that. Mold. like cassette tapes also grow on floppy disks.

I guess I also noticed some black mold growing on / around the plug hole cover in one of my bathrooms (fortunately not severe, yet). Might be more useful to a wider demographic than just Grandma with her 24 years of television from 1980 to 2004.

oh yeah also it might also be useful in areas where a dehumidifier wouldn't be as viable to be on 24/7.

###### does mold grow better in hotter environments?

#### Really specific optical media cases where I don't think it would be worth it making things for them because the discs are either really common or are really not necessary to archive or i just dont collect them or they all died:
- UK made PDO CDs. (Bronzing caused by acid.)
- LaserDiscs. (Don't collect them)
- Warner HD DVDs (Don't collect them)
- Other optical media formats other than CD, Video CD, DVD, Blu-Ray, 4K Blu-ray, and whatever disc formats that weren't used by video game consoles (don't collect them)
- Flexplay (They already died. Besides, they most likely have stock US DVD ISOs on them. Either that or it's just the movie in DVD quality, which is already readily availible.)
- Warner Bros distributed DVDs from 2005 to 2009 (Most likely only very specific regional DVDs affected.) I'm Australian so this likely doesn't affect me. (except if my Region 1 copy of The Matrix is affected, then there *might* be an issue.)


### Progress guide:
1. Find a way to make each individual sensor work on its own.
- A. Moisture detector should detect humidity. Should not be over ~50%. Moisture promotes mold growth, and might seep into discs.
- B. Temperature detector should detect extreme heat. I think extreme heat may also promote mold growth however I need to double check. Additionally, severe temperatures might warp discs. Prolly bout 40 celsius
2. Find a way to make each sensor work in tandem.
3. Make an alert system to warn of what's wrong. (eg. 1 beep for too humid, 2 beeps for too warm) A series of multicoloured LEDs might also help.
4. Make a power system where you can turn on/off the system if for some reason you want to turn it off.

### In layman's terms:
1. If:
- Moisture detector goes over 50%, buzz, 1 LED.
- OR temperature detector goes over ~45ish???°C, buzz, 2 LED.
2. If both are out of range, make 1st LED blink.
3. Make an on/off switch. Enables / disables the thing.

### Oh, look! It's a
# TABLE
|Test Case|Input|Expected Output|
|---------|-----|---------------|
|Temperature too hot|Temperature sensor detects over 40°C|Buzz twice, show 2 LEDS.|
|Too much moisture|Moisture detector detects over 50%|Buzz once, show 1 LED.|
|Temperature too hot and too humid|Temperature sensor detects over 45°C and moisture detector detects over 50%|Buzz three times, blink LED 1, keep LED 2 on.|

### other random things:
**Efficiency:** Effective as a detector. Could probably link up a system to a dehumidifier.

**Response Time:** Probably between 20-30 seconds.

**Accuracy:** Should be ± 3 of target.