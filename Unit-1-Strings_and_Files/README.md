# Strings and Files

## Description

This is our first post-break unit, one of the three we're going to complete before the end of the semester.


## 


## Project: Number One Jams

<img src="https://upload.wikimedia.org/wikipedia/en/a/ad/Gangnam_Style_Official_Cover.png" width="25%" />

### Description

*Billboard* magazine publishes weekly charts tracking the popularity of songs and albums across a variety of genres. 
In this project you’ll work with a data set containing information from the last 64 years of the *Billboard* charts.
We're going to work with data taken from the **Hot 100**, which tracks the 100 most popular songs in the country, determined
by aggregating various factors, including radio airplay and, more recently, streams.

### Source

The data for the project is taken from the TSorT music pages, which compile lots of information about music charts from all over the world:

http://www.tsort.info/music/index.htm

I have processed the raw CSV file containing all of their chart entries to extract only the data for songs that made the US Hot 100 music charts from
1950 to the beginning of 2013.

### Getting the Data

Download the file `billboard_chart_data.txt` that's posted to Canvas. Upload it to your Mimir workspace by going to `File --> Upload` and
then selecting `billboard_chart_data.txt` from your downloads directory.

Mimir automatically uploads the file into your home directory. You can move it to `CMS_195/Strings_and_Files` using the command

```
mv billboard_chart_data.txt CMS_195/Strings_and_Files
```

Once you've moved the file, `cd` to `CMS_195/Strings_and_Files` and use the `ls` command to check that the file exists.

### Looking at the File

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
 
 
### Questions to Answer

1. How many songs are in the entire data set?

2. Which artist has more all-time chart appearances: Prince or Madonna?

3. Find and print all of the number one hits by Elvis Presley.

4. Which song spent the longest number of weeks on the charts?

5. A major change in the charts took place in late 1991, when *Billboard* switched to using Nielsen’s SoundScan 
technology to automatically track radio play of songs. Prior to 1991, song popularity was determined from surveys filled 
out by radio stations. It’s been said that the switch to SoundScan led to popular songs remaining on the charts longer
than the old survey system. Determine if this is empirically true by calculating the average time spent on the charts
for songs released in 1991 or earlier and songs released in 1992 or later.

### Submission

Write one `.py` file for each question. Upload all your files and **text files containing the outputs of your programs** to the assignment
I've created on Canvas.

**Please upload an individual submission**, even if you've worked with other to complete the project.

### Tips

- **Start early**! **Don't wait until the last minute**!

- Watch all of the videos posted to Canvas. You'll need to use the strategies described in the last video to step through each line
of the file and break it into its components.

- Remember that you can work with your team or other members of the class to finish the project.



