# Number One Jams

<img src="https://upload.wikimedia.org/wikipedia/en/c/cc/Lady_Gaga_-_Bad_Romance.png" width="25%" />

*Hot take: the greatest record of the 21st Century so far is "Bad Romance" twelve times*.

## Description
*Billboard* magazine publishes weekly charts tracking the popularity of songs and albums across a variety of genres. 

In this project you’ll work with a data set containing information from 64 years of the *Billboard* charts.
We're going to work with data taken from the **Hot 100**, which tracks the 100 most popular songs in the country, determined
by aggregating various factors, including radio airplay and, in the modern era, streams.

**You don't have to turn anything in for this lab**. It's intended to help you get more practice working with structured files and strings.

## Source
The data for the project is taken from the TSorT music pages, which compile lots of information about music charts from all over the world:

https://tsort.info/music/

I have processed the raw CSV file containing all of their chart entries to extract only the data for songs that made the US Hot 100 
music charts from 1950 to the beginning of 2013, which was the most recent data at the time I put together the data set.


## Get the Data

Download the file `billboard_chart_data.txt` from Canvas and upload it to Mimir using the same steps you used for `words.txt`, as
described in the README file for this unit.

## Looking at the File

You can look at the contents of the file using `cat` in the terminal:
```
cat billboard_chart_data.txt
```
You'll see output like this:
```
Psy;Gangnam Style;2012;2;31
Adele;Skyfall;2012;8;20
Flo-Rida & Sia;The Wild Ones;2012;5;36
Justin Bieber;Die In Your Arms;2012;17;2
Jason Mraz;I Won't Give Up;2012;8;44
Madonna;Give Me All Your Luvin';2012;10;6
Taylor Swift;Stay Stay Stay;2012;91;1
Alicia Keys;Girl On Fire;2012;11;30
Katy Perry;Wide Awake;2012;2;26
Carly Rae Jepsen;Call Me Maybe;2012;1;50
Skrillex;Bangarang;2012;72;20
Calvin Harris;Feel So Close;2012;12;26
Melanie Martinez;Too Close;2012;94;1
Glee Cast;Black Or White;2012;64;1
Terry McDermott;I Want to Know What Love Is;2012;84;1
Neon Trees;Everybody Talks;2012;6;39
Ellie Goulding;Lights;2012;2;56
Glee Cast;Wanna Be Startin' Something;2012;78;1
Adam Levine;Yesterday;2012;68;1
The Lumineers;Ho Hey;2013;3;62
```
Each line records information on one song. The five fields are:
- The artist
- The song title
- The year the song was released
- The maximum position attained by the song during its life on the charts
- The total number of weeks on the charts

For example, the output above shows that Psy's "Gangnam Style", released in 2012, made it up to number 2 and spent a total of 31 weeks
 on the charts.
 
 
## Practice Questions
<img src="https://upload.wikimedia.org/wikipedia/en/f/f5/Elvis_Presley_LPM-1254_Album_Cover.jpg" width="25%" />

1. How many songs are in the entire data set?

2. Which artist has more all-time chart appearances: Prince or Madonna?

3. Find and print all of the number one hits by Elvis Presley.

4. Which song spent the greatest total number of weeks on the charts?

5. A major change in the charts took place in late 1991, when *Billboard* switched to using Nielsen’s SoundScan 
technology to automatically track radio play of songs. Prior to 1991, song popularity was determined from surveys filled 
out by radio stations. It’s been said that the switch to SoundScan led to popular songs remaining on the charts longer
than the old survey system. Determine if this is empirically true by calculating the average time spent on the charts
for songs released in 1991 or earlier and songs released in 1992 or later.
