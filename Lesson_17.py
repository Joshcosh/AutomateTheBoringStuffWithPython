# %% 
# 1 | dictionries
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur')
# %%
# 2 | dictionary keys and values can be anything
spam = {12345: 'Luggage combination', 42: 'The Answer'}
# %%
# 3 | in lists the order matters
print([1, 2, 3] == [3, 2, 1])
# %%
# 4 | but in dictionaries it's the content that matters
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
print(eggs == ham) 
# %%
# 5 | if we try to access a key the doesn'y exist we get an exception
eggs['color']
# %%
# 6 | check if a key exists in a dictionary
'name' in eggs
'name' not in eggs
# %%
# 7 | dictionaries also get passed by referense
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
# %%
print(list(eggs.keys())) # a new list of the keys
print(list(eggs.values())) # a new list of the values
print(list(eggs.items())) # a new tuples list of the items
# %%
type(eggs.keys())
for k in eggs.keys():
    print(k)
# %%
type(eggs.values())
for v in eggs.values():
     print(v)
# %%
type(eggs.items())
for k, v in eggs.items():
     print(k, v)
    #  print(str(k) + ' : ' + str(v))
# %%
type(eggs.items())
for i in eggs.items():
     print(i)
# %%
print('cat' in eggs.values())
# %%
# 8 | avoid missing key access tries from crashing the code
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}

if 'color' in eggs: # naive way
    print(eggs['color'])

print(eggs)
eggs.get('age', 0) # the smart way. the 2nd argument is the return value if the key is missing.
eggs.get('color', '')
# %%
# set default value if the key doesn't yet exist
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
print(eggs)
if 'color' not in eggs: # the naive way
    eggs['color'] = 'black' 
print(eggs)
print('species' in eggs)
print('cat' in eggs)
print('cat' in eggs.values())

# we can do this better with one line of code
eggs.setdefault('shape', 'oval')
print(eggs)

eggs.setdefault('color', 'purple') # won't change because the color is already an existing key
print(eggs)
# %%
# count the number of occurences of a letter in a string
message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {} # initialize a dict object
for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1
print(count)
# %%
# doing as above but with a huge text using the ''' trick
# will use the pprint lib trick as well
import pprint

message = '''
Wiki Loves Monuments: Photograph a monument, help Wikipedia and win!
Learn more
Page semi-protected
Israel Adesanya
From Wikipedia, the free encyclopedia
Jump to navigationJump to search
Israel Adesanya
Israel Adesanya at UFC 230.jpg
Israel Adesanya at UFC 234
Born	Israel Oluwafemi Adesanya[citation needed]
22 July 1989 (age 31)
Lagos, Nigeria
Nickname(s)	The Last Stylebender
Residence	Auckland, New Zealand
Nationality	Nigerian
New Zealander
Height	193 cm (6 ft 4 in)
Weight	84 kg (185 lb; 13 st 3 lb)
Division	Middleweight
Reach	80 in (203 cm)[1]
Style	Kickboxing, Boxing
Stance	Orthodox
Fighting out of	Auckland, New Zealand
Team	City Kickboxing
Trainer	Eugene Bareman
Rank	Blue belt in Brazilian Jiu-Jitsu under André Galvão[2]
Years active	2009–present
Professional boxing record
Total	6
Wins	5
By knockout	1
Losses	1
By knockout	0
Kickboxing record
Total	80
Wins	75
By knockout	29
Losses	5
By knockout	1
Mixed martial arts record
Total	20
Wins	20
By knockout	15
By decision	5
Losses	0
Other information
Boxing record from BoxRec
Mixed martial arts record from Sherdog
Israel Adesanya (born 22 July 1989) is a Nigerian-born New Zealand professional mixed martial artist. He has also competed in kickboxing and boxing.[3] As a mixed martial artist, he is currently signed to the Ultimate Fighting Championship (UFC), where he is the UFC Middleweight Champion and has an undefeated record of 20 wins and no losses. In kickboxing, he is the former Glory middleweight contender winner and King in the Ring two-time cruiserweight and heavyweight champion. As of 24 May 2020, he is #4 in the UFC men's pound-for-pound rankings.[4] Adesanya is often regarded as one of the best strikers in the world of mixed martial arts as well as one of the best in sport's history.[5][6][7][8]


Contents
1	Background
2	Mixed martial arts career
2.1	Glory World Series
2.2	King in the Ring
2.3	Early career
2.4	Ultimate Fighting Championship
2.4.1	UFC Middleweight Championship
3	Personal life
4	Championships and accomplishments
4.1	Mixed martial arts
4.2	Kickboxing
4.3	Boxing
5	Mixed martial arts record
6	Kickboxing record (incomplete)
7	Boxing career
7.1	Prize-fighting tournaments
7.2	Professional boxing record
8	See also
9	References
10	External links
Background
Israel Adesanya was born in Lagos, Nigeria to a family of five children.[9] His father, Femi, is an accountant and his mother, Taiwo, is a nurse.[10] Israel attended Chrisland School, Opebi, and enrolled in its Taekwondo after-school club until he was removed by his mother due to an injury.[9][11][12] In early 2001, he relocated to Ghana with his family for 10 months,[13] but due to his parents wanting their children to receive a well-recognised higher education,[14] he settled in Rotorua, New Zealand at age 10[15] and attended Rotorua Boys' High School.[16] Adesanya was not interested in sport during high school; instead he was interested in Japanese anime such as Death Note[17] and Naruto.[18] He was heavily bullied during his high school years[19] and attributes the mistreatment he experienced to his decision to pursue martial arts later in life.[20]

At the age of 18, Adesanya started training in kickboxing, after being inspired by the Muay Thai film Ong-Bak.[12] He went on to amass an amateur kickboxing record of 32–0 before moving to and fighting in China.[21][22] At the age of 21, Adesanya moved to Auckland, New Zealand, and began training under Eugene Bareman at City Kickboxing, with other established MMA fighters such as Dan Hooker, Kai Kara-France and Alexander Volkanovski.[23][24][25]

Mixed martial arts career
Glory World Series
In March 2014, Adesanya became the first New Zealander to sign a deal with the Glory promotion company after he spent the past previous six months in China fighting full-time.[26] He lost a unanimous points decision in his debut fight to Belgian Filip Verlinden at Glory 15 in Istanbul, Turkey.[27] It was only his second loss of the then 24-year-old's career.[27]

King in the Ring
After picking up his thirty-third career win over Charles August, Adesanya announced he would compete in the King in the Ring last-man-standing tournament in Auckland, New Zealand.[28] Adesanya was scheduled to enter in the cruiserweight division at ASB Stadium the following week.[29] He won the event with wins over fellow countrymen Slava Alexeichik, Pati Afoa and Jamie Eades.

Early career
Adesanya made his professional debut in 2012. Fighting in Hong Kong, Australia and China over the next five-and-a-half years, he amassed a record of 11–0, with all wins coming via KO/TKO, prior to being signed by the UFC.[30]

Ultimate Fighting Championship
In December 2017, it was announced that Adesanya had signed with the UFC. He made his debut against Rob Wilkinson on 11 February 2018, at UFC 221.[31] He won the fight via TKO in the second round.[32] This win earned him the Performance of the Night bonus.[33]

Adesanya's next fight was scheduled on 14 April 2018, against Marvin Vettori at UFC on Fox 29.[34] He won the fight via split decision.[35]

Adesanya faced Brad Tavares on 6 July 2018, at The Ultimate Fighter 27 Finale.[36] Adesanya won the one-sided fight via unanimous decision.[37] This win earned him his second Performance of the Night award.[38]

Adesanya faced Derek Brunson on 3 November 2018, at UFC 230.[39] He won the fight via technical knockout in round one.[40] This win earned him the Performance of the Night award for a third time.[41]

Adesanya faced Anderson Silva on 10 February 2019, at UFC 234.[42] He won the fight via unanimous decision.[43] This fight earned him the Fight of the Night award.[44]

UFC Middleweight Championship
Adesanya faced Kelvin Gastelum for the interim UFC Middleweight Championship on 13 April 2019, at UFC 236.[45] He won the fight via unanimous decision.[46] This fight earned him the Fight of the Night award.[47] The fight was widely regarded as the best fight of the year, earning the nomination from most of the MMA news outlets.

Adesanya faced Robert Whittaker in a title unification bout on 6 October 2019 at UFC 243.[48] He won the fight via knockout in the second round to become the undisputed UFC middleweight champion.[49] This win earned him his fourth Performance of the Night award.[50]

Adesanya next faced Yoel Romero on 7 March 2020 UFC 248.[51] He won the fight via unanimous decision and defended the UFC middleweight championship successfully for the first time. Many fans and pundits felt disappointed due to the low activity by both fighters which resulted in a largely uneventful fight in which neither fighter was able to deliver any significant offense.[52][53]

In his next title defense, Adesanya faced Paulo Costa on September 27, 2020 at UFC 253.[54] He won the fight via technical knockout in the second round.[55] This win earned him his fifth Performance of the Night award.[56]

Personal life
Before taking up fighting, Adesanya regularly competed in dance competitions across New Zealand.[57] He highlighted his passion for dance in a choreographed walkout at UFC 243.[58][59]

Adesanya is a fan of anime and would like to start an anime production company after retiring from fighting.[60] His nickname "The Last Stylebender" is a reference to Avatar: The Last Airbender, an anime-influenced cartoon series.[61] Adesanya has the image of one of the show's main characters, Toph Beifong, tattooed on his forearm.[62]

Adesanya has endorsed the 2020 New Zealand cannabis referendum.[63]

Championships and accomplishments
Mixed martial arts
Ultimate Fighting Championship
UFC Middleweight Championship (One time, current)
One successful title defense
Interim UFC Middleweight Championship (One time)
Performance of the Night (Five times) vs. Rob Wilkinson, Brad Tavares, Derek Brunson, Robert Whittaker and Paulo Costa[33][38][41][64][56]
Fight of the Night (Two times) vs. Anderson Silva and Kelvin Gastelum[65][47]
Most Knockdowns in a UFC Title Fight (4)[66]
Australian Fighting Championship
AFC Middleweight Champion (one time)
Hex Fighting Series Middleweight
Hex Fighting Series Middleweight Champion (one time)
MMAJunkie.com
2018 Newcomer of the Year[67]
2019 April Fight of the Month vs. Kelvin Gastelum[68]
2019 Fight of the Year vs. Kelvin Gastelum[69]
2019 Male Fighter of the Year[70]
MMA Fighting
2018 Breakthrough Fighter of the Year[71]
2019 Fight of the Year vs. Kelvin Gastelum[72]
2019 Fighter of the Year[73]
CombatPress.com
2018 Breakout Fighter of the Year[74]
2019 Male Fighter of the Year[75]
2019 Fight of the Yearvs. Kelvin Gastelum[76]
CagesidePress.com
2019 Fighter of the Year[77]
2019 Fight of the Year vs. Kelvin Gastelum[78]
MMADNA.nl
2018 Rising Star of the Year.[79]
The Body Lock
2019 Fighter of the Year[80]
World MMA Awards
2018 Breakthrough Fighter of the Year[81]
MMAMania.com
2019 Fighter of the Year[82]
2019 Fight of the Year vs. Kelvin Gastelum[83]
Halberg Awards
2019 New Zealand Sportsman of the Year[84]
Wrestling Observer Newsletter
Most Outstanding Fighter of the Year (2019)
MMA Match of the Year (vs. Kelvin Gastelum, 2019)
Kickboxing
Glory
Glory 34: Denver – Middleweight Contender Tournament Champion
King in the Ring
King in the Ring 86 – The Cruiserweights II Tournament Champion.
King in the Ring 86 – The Cruiserweights III Tournament Champion.
King in the Ring 100 – The Heavyweights III Tournament Champion.
Most titles in King in the Ring history (3)
Boxing
Super 8 III (Cruiserweight II)
Super 8 IV (Cruiserweight III)
Mixed martial arts record
Professional record breakdown	
20 matches	20 wins	0 losses
By knockout	15	0
By decision	5	0
Res.	Record	Opponent	Method	Event	Date	Round	Time	Location	Notes
Win	20–0	Paulo Costa	TKO (punches)	UFC 253	September 27, 2020	2	3:59	Abu Dhabi, United Arab Emirates	Defended the UFC Middleweight Championship. Performance of the Night.
Win	19–0	Yoel Romero	Decision (unanimous)	UFC 248	7 March 2020	5	5:00	Las Vegas, Nevada, United States	Defended the UFC Middleweight Championship.
Win	18–0	Robert Whittaker	KO (punches)	UFC 243	6 October 2019	2	3:33	Melbourne, Australia	Won and unified the UFC Middleweight Championship. Performance of the Night.
Win	17–0	Kelvin Gastelum	Decision (unanimous)	UFC 236	13 April 2019	5	5:00	Atlanta, Georgia, United States	Won the interim UFC Middleweight Championship. Fight of the Night.
Win	16–0	Anderson Silva	Decision (unanimous)	UFC 234	10 February 2019	3	5:00	Melbourne, Australia	Fight of the Night.
Win	15–0	Derek Brunson	TKO (knees and punches)	UFC 230	3 November 2018	1	4:51	New York City, New York, United States	Performance of the Night.
Win	14–0	Brad Tavares	Decision (unanimous)	The Ultimate Fighter: Undefeated Finale	6 July 2018	5	5:00	Las Vegas, Nevada, United States	Performance of the Night.
Win	13–0	Marvin Vettori	Decision (split)	UFC on Fox: Poirier vs. Gaethje	14 April 2018	3	5:00	Glendale, Arizona, United States	
Win	12–0	Rob Wilkinson	TKO (knees and punches)	UFC 221	11 February 2018	2	3:37	Perth, Australia	Performance of the Night.
Win	11–0	Stuart Dare	KO (head kick)	Hex Fighting Series 12	24 November 2017	1	4:53	Melbourne, Australia	Won the vacant Hex Fight Series Middleweight Championship.
Win	10–0	Melvin Guillard	TKO (punches)	Australia Fighting Championship 20	28 July 2017	1	4:49	Melbourne, Australia	Won the AFC Middleweight Championship.
Win	9–0	Murad Kuramagomedov	TKO (punches)	Wu Lin Feng: E.P.I.C. 4	28 May 2016	2	1:05	Henan, China	
Win	8–0	Andrew Flores Smith	TKO (corner stoppage)	Glory of Heroes 2	7 May 2016	1	5:00	Shenzhen, China	
Win	7–0	Dibir Zagirov	TKO (punches)	Wu Lin Feng: E.P.I.C. 2	13 March 2016	2	2:23	Henan, China	
Win	6–0	Vladimir Katykhin	TKO (doctor stoppage)	Wu Lin Feng: E.P.I.C. 1	13 January 2016	2	N/A	Henan, China	
Win	5–0	Gele Qing	TKO (elbows)	Wu Lin Feng 2015: New Zealand vs. China	19 September 2015	2	3:37	Auckland, New Zealand	
Win	4–0	Maui Tuigamala	TKO (body kick)	Fair Pay Fighting 1	5 September 2015	2	1:25	Auckland, New Zealand	
Win	3–0	Song Kenan	TKO (head kick)	The Legend of Emei 3	8 August 2015	1	1:59	Shahe, China	
Win	2–0	John Vake	TKO (punches)	Shuriken MMA: Best of the Best	15 June 2013	1	4:43	Auckland, New Zealand	
Win	1–0	James Griffiths	TKO (punches)	Supremacy Fighting Championship 9	24 March 2012	1	2:09	Auckland, New Zealand	Middleweight debut.
[85]

Kickboxing record (incomplete)
Kickboxing record (incomplete)
75 wins, 5 losses, 0 draws[hide]
Date	Result	Opponent	Event	Location	Method	Round	Time	Record
2017-03-04	Loss	Brazil Alex Pereira	Glory of Heroes 7	Sao Paulo, Brazil	KO (left hook)[86]	3	0:42	23-5
2017-01-20	Loss	Netherlands Jason Wilnis	Glory 37: Los Angeles	Los Angeles, California, US	Decision (unanimous)[87]	5	3:00	23-4
For the Glory Middleweight Championship.
2016-10-21	Win	Netherlands Yousri Belgaroui	Glory 34: Denver – Middleweight Contender Tournament Finals	Broomfield, Colorado, US	Decision (split)	3	3:00	23-3
Wins Glory 34: Denver – Middleweight Contender Tournament Championship.
2016-10-21	Win	Canada Robert Thomas	Glory 34: Denver – Middleweight Contender Tournament, Semi Finals	Broomfield, Colorado, US	Decision (unanimous)	3	3:00	22-3
2016-10-01	Win	Romania Bogdan Stoica	Glory of Heroes 5	Zhengzhou, China	KO (left mid kick)	2	1:45	21-3
2016-09-17	Win	France Romain Falendry	Rise of Heroes 1	Chaoyang, Liaoning, China	Decision (unanimous)	3	3:00	20-3
2016-08-06	Win	Netherlands Yousri Belgaroui	Glory of Heroes 4	Changzhi, China	Decision (unanimous)	3	3:00	19-3
2016-06-25	Win	Ukraine Vitaly Kodin	Wu Lin Feng	China	Decision (unanimous)	3	3:00	18-3
2016-04-02	Loss	Brazil Alex Pereira	Glory of Heroes 1	Shenzhen, China	Decision (unanimous)[88]	3	3:00	17-3
2016-01-30	Win	Sweden Carl N'Diaye	The Legend of Emei 7 – Wenjiang	Wenjiang, China	KO (left hook to the body)	1	3:00	17-2
2015-10-31	Win	New Zealand Jamie Eades	King in the Ring 100 – The Heavyweights III, Final	Auckland, New Zealand	Decision (unanimous)	3	3:00	16-2
Wins King in the Ring 100 – The Heavyweights III Tournament Championship.
2015-10-31	Win	Australia Dan Roberts	King in the Ring 100 – The Heavyweights III, Semi Finals	Auckland, New Zealand	KO	1	0:26	15-2
2015-10-31	Win	Australia Nase Foai	King in the Ring 100 – The Heavyweights III, Quarter Finals	Auckland, New Zealand	TKO	2	N/A	14-2
2015-04-11	Win	New Zealand Pati Afoa	King in the Ring 86 – The Cruiserweights III, Final	Auckland, New Zealand	KO	1	N/A	13-2
Wins King in the Ring 86 – The Cruiserweights III Tournament Championship.
2015-04-11	Win	Australia Mark Timms	King in the Ring 86 – The Cruiserweights III, Semi Finals	Auckland, New Zealand	TKO	2	N/A	12-2
2015-04-11	Win	Australia Kim Loudon	King in the Ring 86 – The Cruiserweights III, Quarter Finals	Auckland, New Zealand	TKO	3	N/A	11-2
2015-02-14	Win	Australia Kim Loudon	Knees of Fury 50	Adelaide, Australia	TKO	4	N/A	10-2
2014-08-30	Win	New Zealand Jamie Eades	King in the Ring 86 – The Cruiserweights II, Final	Auckland, New Zealand	KO	1	N/A	9-2
Wins King in the Ring 86 – The Cruiserweights II Tournament Championship.
2014-08-30	Win	New Zealand Pati Afoa	King in the Ring 86 – The Cruiserweights II, Semi Finals	Auckland, New Zealand	KO	N/A	N/A	8-2
2014-08-30	Win	New Zealand Slava Alexeichik	King in the Ring 86 – The Cruiserweights II, Quarter Finals	Auckland, New Zealand	Decision (unanimous)	3	3:00	7-2
2014-07-02	Win	Belgium Filip Verlinden	Glory of Heroes 3	Jiyuan, Henan, China	Decision (unanimous)	3	3:00	6-2
2014-04-12	Loss	Belgium Filip Verlinden	Glory 15: Istanbul	Istanbul, Turkey	Decision (unanimous)[89]	3	3:00	5-2
2014-02-16	Loss	Canada Simon Marcus	Kunlun Fight 2 – 80kg tournament, Semi Finals	Zhengzhou, China	Ext. R Decision (split)[90]	4	3:00	5-1
2013-11-27	Win	China Qin Shan	Wu Lin Feng 2013	Anyang, China	TKO	3	N/A	5-0
2013-0-0	Win	China Nurla Mulali	Wu Lin Feng 2013	Kashi, China	Decision (unanimous)	3	3:00	4-0
2012-07-21	Win	China Niu Xiaoqiang	Wu Lin Feng 2012	Auckland, New Zealand	KO (punches)	3	N/A	3-0
2012-06-23	Win	China Xu Yi	Wu Lin Feng 2012	Foshan, China	Decision (unanimous)	3	3:00	2-0
2011-09-24	Win	China Guo Qiang	Wu Lin Feng 2011	Kuala Lumpur, Malaysia	TKO (referee stoppage)	3	N/A	1-0
Legend:   Win ‹See Tfd›   Loss ‹See Tfd›   Draw/No contest ‹See Tfd›   Notes ‹See Tfd›

Boxing career
Prize-fighting tournaments
Adesanya began his professional boxing career in November 2014 against two-time Australian champion Daniel Ammann.[91] He was granted one of two wildcards to enter the inaugural cruiserweight Super 8 Boxing Tournament.[92] The event was headlined by Shane Cameron and Kali Meehan at the North Shore Events Centre in Auckland, New Zealand.[93] He suffered a controversial loss via unanimous decision after he looked to have outpointed Ammann in the quarter-finals.[94]

Adesanya re-entered the Super 8 tournament in May 2015, held at Horncastle Arena in Christchurch. It was the second cruiserweight series with the winner receiving $25,000 NZD and a new car.[95] He won his first professional fight against fellow New Zealander Asher Derbyshire in the first seed. Adesanya knocked his opponent out in the second round.[citation needed]

Professional boxing record

This section does not cite any sources. Please help improve this section by adding citations to reliable sources. Unsourced material may be challenged and removed. (Learn how and when to remove this template message)
Professional record summary 
6 fights	5 wins	1 loss
By knockout	1	0
By decision	4	1
No.	Result	Record	Opponent	Type	Round, time	Date	Location	Notes
6	Win	5–1	New Zealand Zane Hopman	UD	3	3 Nov 2015	New Zealand SkyCity, Auckland, New Zealand	Super 8 Boxing Tournament: Cruiserweight III & Light-heavyweight – Final
5	Win	4–1	New Zealand Lance Bryant	UD	3	3 Nov 2015	New Zealand SkyCity, Auckland, New Zealand	Super 8 Boxing Tournament: Cruiserweight III & Light-heavyweight – Semi-final
4	Win	3–1	United States Brian Minto	SD	3	28 Mar 2015	New Zealand Horncastle Arena, Christchurch, New Zealand	Super 8 Boxing Tournament: Cruiserweight II – Final
3	Win	2–1	New Zealand Lance Bryant	MD	3	28 Mar 2015	New Zealand Horncastle Arena, Christchurch, New Zealand	Super 8 Boxing Tournament: Cruiserweight II – Semi-final
2	Win	1–1	New Zealand Asher Derbyshire	KO	2 (3)	28 Mar 2015	New Zealand Horncastle Arena, Christchurch, New Zealand	Super 8 Boxing Tournament: Cruiserweight II – Quarter-final
1	Loss	0–1	Australia Daniel Ammann	UD	3	22 Nov 2014	New Zealand North Shore Events Centre, Auckland, New Zealand	Super 8 Boxing Tournament: Cruiserweight I – Quarter-final
See also
List of male kickboxers
List of current UFC fighters
List of male mixed martial artists
List of undefeated mixed martial artists
References
 "Israel Adesanya | UFC". www.ufc.com. Retrieved 19 January 2020.
 "After promoting Israel Adesanya, André Galvão will be part of Anderson Silva's camp". Graciemag. 4 December 2018.
 Reive, Christopher (20 February 2018). "New Israel Adesanya was bullied as a child – now he's a New Zealand fight sensation". NZ Herald. ISSN 1170-0777. Retrieved 4 November 2018.
 "Rankings | UFC". www.ufc.com. Retrieved 25 May 2020.
 https://www.hitc.com/en-gb/2020/08/14/ufc-4-top-10-strikers-best-fighters/
 https://www.thefight-site.com/home/the-bending-of-the-style-israel-adesanya-in-6-fights
 https://www.bloodyelbow.com/2018/11/2/18053958/ufc-230-israel-adesanya-striking-technique-breakdown-derek-brunson-fight-overview-editorial-mma
 https://www.tapology.com/rankings/top-ten-all-time-greatest-mma-and-ufc-strikers
 How Israel Adesanya's roots led him on a journey to the brink of UFC stardom | ESPN MMA, retrieved 19 October 2019
 "Israel Mobolaji Adesanya : The Last Stylebender". Nigeria Monthly. 3 August 2019. Retrieved 14 November 2019.
 "Israel Adesanya was booted from martial arts: 'I was kicking everything in the house'". FanSided. 8 February 2019. Retrieved 19 October 2019.
 "Photos: The Israel Adesanya Story". MMA India. 13 April 2018. Retrieved 19 October 2019.
 "How a movie changed my life – Israel Adesanya", Athletes Voice, retrieved 2 September 2019
 Youngs, Jose (24 December 2020). "From Nigeria to New Zealand, Israel Adesanya is on a quest to earn a 'masters degree in ass whooping'". MMA Fighting. Retrieved 19 October 2019.
 "'It's go time' for Kiwi Israel Adesanya as he finally arrives in the UFC". NZ Stuff. 10 February 2018. Retrieved 10 February 2018.
 "The pain behind Israel Adesanya's rise to the UFC". Sporting News. 9 February 2018. Retrieved 9 February 2018.
 "Israel Adesanya explains 'Death Note' anime reference at UFC 243". Bloody Elbow. 7 October 2019. Retrieved 18 October 2019.
 "How Israel Adesanya embraces Japanese anime in the UFC". ESPN Australia. 11 April 2019. Retrieved 27 July 2019.
 "Israel Adesanya was bullied as a child – now he's a New Zealand fight sensation". NZ Herald. 21 February 2018. Retrieved 1 November 2018.
 "From bullied in high school to UFC champion: The untold journey of Kiwi MMA superstar Israel Adesanya". 1 News Now. 13 May 2019. Retrieved 6 November 2019.
 "Israel 'The Last Style Bender' Adesanya : Glory Fighter". Glory Kickboxing. Retrieved 29 December 2017.
 Reive, Christopher (20 February 2018). "MMA: Israel Adesanya was bullied as a child – now he's a New Zealand fight sensation". NZ Herald. ISSN 1170-0777. Retrieved 4 November 2018.
 Malili, Faleatua (10 August 2018). "'I'm going to do great things' – Kiwi fighter Israel Adesanya's amazing journey from Whanganui to the UFC". 1 News Now. Retrieved 10 August 2018.
 https://www.youtube.com/watch?v=asDaGqnU0Sk
 Bruce, Sam (12 December 2018). "Kara-France, Volkanovski are City Kickboxing's dynamic Vegas duo". ESPN. Retrieved 12 December 2018.
 "All guts and glory for champion fighter". New Zealand Herald. 23 March 2014. Retrieved 10 March 2020.
 "Adesanya loses Glory kickboxing debut". New Zealand Herald. 13 April 2014. Retrieved 10 March 2020.
 "Adesanya happy to fight on home soil". New Zealand Herald. 29 August 2014. Retrieved 10 March 2020.
 "Adesanya set for King in the Ring". New Zealand Herald. 23 August 2014. Retrieved 10 March 2020.
 Sherdog.com. "Israel". Sherdog. Retrieved 29 December 2017.
 "Undefeated prospect Israel Adesanya makes UFC debut against Rob Wilkinson in Perth". MMA Fighting. Retrieved 29 December 2017.
 "UFC 221 results: Israel Adesanya takes out Rob Wilkinson with TKO in UFC debut". MMAjunkie. 11 February 2018. Retrieved 11 February 2018.
 "UFC 221 bonuses: Much-hyped newcomer among night's $50,000 winners". MMAjunkie. 11 February 2018. Retrieved 11 February 2018.
 "Top prospect Israel Adesanya returns against Marvin Vettori at UFC on FOX 29". MMA Fighting. Retrieved 23 February 2018.
 "UFC on FOX 29 results: Israel Adesanya stays unbeaten despite late charge from Marvin Vettori". MMAjunkie. 15 April 2018. Retrieved 15 April 2018.
 Staff (30 April 2018). "Brad Tavares vs Israel Adesanya headlines The Ultimate Fighter 27 Finale in July". mmajunkie.com. Retrieved 30 April 2018.
 "TUF 27 Finale Results | Israel Adesanya defeats Brad Tavares (Highlights) | BJPenn.com". | BJPenn.com. 6 July 2018. Retrieved 7 July 2018.
 "TUF 27 Finale post-fight bonuses: Adesanya wins rare POTN bonus without a finish". Bloody Elbow. Retrieved 7 July 2018.
 Shaun Al-Shatti (3 August 2018). "Derek Brunson vs. Israel Adesanya slated for UFC 230". mmafighting.com. Retrieved 6 August 2018.
 "UFC 230 Results: Israel Adesanya finishes Derek Brunson in Round 1 | BJPenn.com". | BJPenn.com. 4 November 2018. Retrieved 4 November 2018.
 "UFC 230 bonuses: Israel Adesanya cashes another $50,000 check". MMAjunkie. 4 November 2018. Retrieved 4 November 2018.
 "UFC 234 fight card: Former champ Anderson Silva returning to face Israel Adesanya in Australia". CBSSports.com. Retrieved 25 November 2018.
 "UFC 234 results: Israel Adesanya stays unbeaten, outpoints game Anderson Silva". MMAjunkie. 10 February 2019. Retrieved 10 February 2019.
 "UFC 234 bonuses: Israel Adesanya, Anderson Silva collect extra $50,000". MMAjunkie. 10 February 2019. Retrieved 10 February 2019.
 Brett Okamoto (19 February 2018). "Israel Adesanya named as replacement opponent for Kelvin Gastelum at UFC 236". espn.com. Retrieved 19 February 2019.
 "UFC 236 results: Israel Adesanya tops Kelvin Gastelum in thrilling classic to claim interim title". MMA Junkie. 14 April 2019. Retrieved 15 April 2019.
 MMA Junkie Staff (13 April 2019). "UFC 236 bonuses: No surprise with two $50,000 'Fight of Night' winners". MMAjunkie. Retrieved 13 April 2019.
 Andrew Richardson (20 June 2019). "Midnight Mania! Whittaker Vs. Adesanya Is Set!". mmamania.com. Retrieved 20 June 2019.
 Doherty, Dan (6 October 2019). "UFC 243 Results: Israel Adesanya Knocks Out Robert Whittaker to Claim Throne". Cageside Press. Retrieved 6 October 2019.
 Alexander Lee (6 October 2019). "UFC 243 bonuses: Israel Adesanya rewarded for championship-winning knockout". mmafighting.com. Retrieved 6 October 2019.
 "Israel Adesanya defends middleweight title against Yoel Romero at UFC 248". MMA Junkie. 17 January 2020. Retrieved 17 January 2020.
 "UFC 248 results: Israel Adesanya keeps title in bizarre win over Yoel Romero". MMA Junkie. 8 March 2020. Retrieved 8 March 2020.
 Henry McKenna (8 March 2020). "UFC 248: Dana White calls out 'terrible' fighter for unimpressive main event". ftw.com. Retrieved 4 August 2020.
 "Sources: UFC sets Adesanya-Costa for Sept. 19". ESPN.com. 18 July 2020. Retrieved 19 July 2020.
 "UFC 253 updates: Adesanya defeats Costa". NewsComAu. 27 September 2020. Retrieved 27 September 2020.
 Alexander K. Lee (27 September 2020). "UFC 253 bonuses: Israel Adesanya, Jan Blachowicz cash in with championship performances". mmafighting.com. Retrieved 27 September 2020.
 Harris, Scott (2 October 2019). "From Dancer to Fighter: How Israel Adesanya Battled His Way to UIsrael AdesanyaFC 243". Bleacher Report. Retrieved 27 May 2020.
 Lee, Alexander K. (6 October 2019). "Israel Adesanya talks elaborate UFC 243 entrance: 'If I could sing, trust me, Justin Bieber wouldn't even have a job'". MMA Fighting. Retrieved 27 May 2020.
 Hooper, Natasha (5 March 2020). "Israel Adesanya explains how dancing helped him become a fighter". bjpenn.com. Retrieved 27 May 2020.
 Bruce, Sam (10 April 2019). "How Israel Adesanya embraces Japanese anime in the UFC". ESPN. Retrieved 27 May 2020.
 Porter, Jack (7 March 2020). "How Anime Fuelled Israel Adesanya's Ambition, Ability And Style In The UFC". The Sportsman. Retrieved 27 May 2020.
 "UFC Fighter Israel Adesanya Breaks Down His Tattoos | GQ Sports".
 Foote, Stephen (25 May 2020). "UFC: Israel Adesanya lends support to cannabis legalisation in New Zealand". Newshub. Retrieved 27 May 2020.
 "UFC 243 bonuses: Israel Adesanya rewarded for championship-winning knockout". www.mmafighting.com. Retrieved 6 October 2019.
 MMAjunkie.com. "UFC 234 bonuses: Israel Adesanya, Anderson Silva collect extra $50,000". MMA Junkie. Retrieved 10 February 2019.
 MMAjunkie.com. "UFC 236 post-event facts: Israel Adesanya sets title-fight record for most knockdowns". MMA Junkie. Retrieved 16 April 2019.
 Fernanda Prates (3 January 2019). "MMAjunkie's 2018 'Newcomer of the Year': The human highlight reel who promised and delivered". mmajunkie.com.
 "MMA Junkie's 'Fight of the Month' for April: Which UFC 236 title fight got the nod?". mmajunkie.com. 4 May 2019.
 Mike Bohn (4 January 2020). "MMA Junkie's 2019 'Fight of the Year': Israel Adesanya vs. Kelvin Gastelum". mmajunkie.com.
 John Morgan (8 January 2020). "MMA Junkie's 2019 'Male Fighter of the Year': Israel Adesanya continues mind-blowing run". mmajunkie.com.
 Jose Youngs (3 January 2019). "MMA Fighting's 2018 Breakthrough Fighter of the Year: Israel Adesanya". mmafighting.com.
 Steven Marrocco (1 January 2020). "MMA Fighting's 2019 Fight of the Year: Israel Adesanya vs. Kelvin Gastelum". mmafighting.com.
 Alexander K. Lee (3 January 2020). "MMA Fighting's 2019 Fighter of the Year: Israel Adesanya". mmafighting.com.
 Dan Kuhl (25 January 2019). "Adesanya is the 2018 Combat Press Breakout Fighter of the Year". CombatPress.com.
 Bryan Henderson (14 January 2020). "Adesanya is the 2019 Combat Press Fighter of the Year". CombatPress.com.
 Dan Kuhl (22 January 2020). "Adesanya-Gastelum is the 2019 Combat Press Fight of the Year". CombatPress.com.
 Staff (31 December 2019). "MMA 2019 Year in Review: Fighter of the Year". CagesidePress.com.
 Staff (31 December 2019). "MMA 2019 Year in Review: Fight of the Year". CagesidePress.com.
 DNA, MMA. "MMA DNA UFC Awards 2018 : De Uitslagen!!!". Retrieved 28 January 2019.
 Connelly, Shane (5 January 2020). "Israel Adesanya is The Body Lock's 2019 Fighter of the Year". The Body Lock. Retrieved 5 January 2020.
 Bryan Tucker (4 July 2019). "World MMA Awards 2019 Results". mmafighting.com.
 Patrick L. Stumberg (25 December 2019). "UFC/MMA 'Fighter of the Year' 2019 – Top 5 List". mmamania.com.
 Patrick L. Stumberg (25 December 2019). "UFC/MMA 'Fights of the Year' 2019 – Top 5 List". mmamania.com.
 Meshew, Jed (13 February 2020). "Morning Report: Israel Adesanya wins New Zealand Sportsman of the Year award, gives speech honoring combat sports legends". MMA Fighting. Retrieved 14 February 2020.
 Sherdog.com. "Israel". Sherdog. Retrieved 6 October 2019.
 http://www.veoh.com/watch/v119377020mpB72ZEC
 GLORY Kickboxing (7 April 2017). "GLORY 37 Los Angeles: Jason Wilnis vs. Israel Adesanya (Middleweight Title Fight)". Retrieved 13 April 2019 – via YouTube.
 Torres, Luis (2 April 2016). "WLF Glory of Heroes 2016 Results". Retrieved 13 April 2019.
 "Filip Verlinden – İsrael Adesanya GLORY 15 İstanbul (Bilgehan Demir Anlatımı) – Dailymotion Video". Dailymotion. Retrieved 13 April 2019.
 Phon Xieng (29 January 2015). "Simon Marcus vs Israel Adesanya". Retrieved 13 April 2019 – via YouTube.
 Josh Leeson (31 October 2014). "Doberman Daniel Ammann prepares for Super 8 Last Man Standing". Newcastle Herald. Retrieved 10 February 2019.
 Liam Napier (1 November 2014). "Israel Adesanya into Super8 bout on wildcard". Stuff. Retrieved 10 February 2019.
 "Cameron gets thumbs up to fight". New Zealand Herald. 12 September 2014. Retrieved 11 February 2019.
 "SUPER 8: Kali Meehan vs Shane Cameron". VS LIVE. 22 November 2014. Retrieved 10 February 2019.
 Jack Salter (28 March 2015). "Boxing: Fighters talk up their chances ahead of tournament". Otago Daily Times. Retrieved 11 February 2019.
External links
Profile at GLORY
Israel Adesanya at UFC
Professional MMA record for Israel Adesanya from Sherdog
Boxing record for Israel Adesanya from BoxRec
Sporting positions
Mixed martial arts titles
Preceded by
Robert Whittaker	2nd UFC Middleweight Champion
10 October 2019 – Present	Incumbent
Kickboxing titles
Preceded by
TY Williams	2nd King in the Ring Cruiserweight Champion
30 August 2014 – 11 April 2015
Vacated	Vacant
Vacant	3rd King in the Ring Cruiserweight Champion
11 April 2015 – 17 November 2017
Vacated	Succeeded by
Slava Alexeichik
Preceded by
Antz Nansen	3rd King in the Ring Heavyweight Champion
31 October 2015 – 30 June 2017
Vacated	Succeeded by
Carlos Ulberg
Awards
Preceded by
Tom Walsh	New Zealand's Sportsman of the Year
2019	Incumbent
vte
Ultimate Fighting Championship current champions
vte
UFC Middleweight Champions
Categories: 1989 birthsLiving peopleSportspeople from LagosNew Zealand male kickboxersNigerian male kickboxersHeavyweight kickboxersMiddleweight kickboxersGlory kickboxersNigerian emigrants to New ZealandNaturalised citizens of New ZealandNew Zealand people of Nigerian descentNew Zealand male boxersNigerian male boxersCruiserweight boxersNew Zealand male mixed martial artistsNigerian male mixed martial artistsSportspeople from AucklandLightweight mixed martial artistsKunlun Fight kickboxersUltimate Fighting Championship championsUltimate Fighting Championship male fighters
Navigation menu
Not logged inTalkContributionsCreate accountLog in
ArticleTalk
ReadView sourceView historySearch
Search Wikipedia
Main page
Contents
Current events
Random article
About Wikipedia
Contact us
Donate
Contribute
Help
Learn to edit
Community portal
Recent changes
Upload file
Tools
What links here
Related changes
Special pages
Permanent link
Page information
Cite this page
Wikidata item
Print/export
Download as PDF
Printable version
In other projects
Wikimedia Commons

Languages
Español
Français
Italiano
Magyar
日本語
Polski
Português
Русский
Tiếng Việt
7 more
Edit links
This page was last edited on 27 September 2020, at 05:48 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.
Privacy policyAbout WikipediaDisclaimersContact WikipediaMobile viewDevelopersStatisticsCookie statementWikimedia FoundationPowered by MediaWiki
'''
count = {} # initialize a dict object
for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1
# pprint.pprint(count)
rjtext = pprint.pformat()
print(rjtext)
pprint.pformat()
pprint.pformat()