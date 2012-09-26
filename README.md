The purpose of this program is to simulate the Spanish electoral system
in order to get objective insight on how it works despite the myths 
that exist about what is better to do on election day.

Some common myths and questions which are quite common within the 
spanish society are:
- When I vote to a minor party, is it a loose of force to avoid
some evil major party? Should I vote to a less evil major party?
- Who gets benefited or damaged when anyone does not vote, votes blank, 
null, or does a protest vote to a system protesting party?
- Is the electoral threshold actual damaging minor options?
Is that possible in a given election?

Using this program you can simulate vote flows from one option to
another, being the options not just parties but also abstention, 
blank and null votes.

You can also review historical results and use that data to establish
a worse case scenario for each so you can keep the faithful voters
when simulating vote flows.

![Screenshot of enVote](http://acampadadespi.org/blog/wp-content/uploads/2011/11/envote-AbstencioMaxima.png)


This program was started by the 15M movement activists in Sant 
Joan Despí (Barcelona, Spain) to provide objective arguments about
what is worth to do or not on the 2011 Spanish Congress elections,
with the hope that although our electoral and political 
system is quite unfair, we could find holes that we can use to
empower our democracy.


How to use it
=============

The program comes with several data sets of past elections
you can move from one to another and compare the results.
Also with some extreme hypothesis on the next election
but with real data about candidatures and electoral census.

The three pie charts above are, from left to right:
1. What every citizen choses to do, including abstention.
2. Proportion of candidatures (removing nulls, blank and abstentions)
3. Distribution of seats

In the middle of the application, you can find some buttons to:
- move from one election case to another
- transfer votes from one option to another
	- You can use the drop box or left and right click the
	  transfer sides on the charts.
- save the modified results
- create a renamed copy of the case
- revert the changes to the last saved state of the case

Cooking data
============

If you want to incorporate more data from the ministry
or hypotetical cases than the ones included, there is how:

Data consists in a set of tab separated files.
Each column must have 4 fields even if they are empty.
The header, which is ignored stands for
	Siglas, Vots, Escons, Candidatures
Which stands for
	Acronym, Votes, Seats, Candidature
The first rows represents special options with special
meaning:
	censo: means census, its 'votes' means the whole
		number of citizen with electoral rights,
		its 'seats' mean the available ones to elect
		and 'Candidature' is used to put the whole
		case description.
	participacion: means the voters that exercised
		their voting rights. Its 'votes' field is a
		redundant double check field.
	abstencion: The voters that didn't exercise their 
		voting rights. Its 'votes' is also redundant
		for double checking.
	nulos: The votes that were not emitted properly.
	blancos: The votes that were emitter without
		ballot in the envelope.

If other than 'censo' have 'seats', envote will consider
it a real case and will be a read only case (you cannot
overwrite it).

Indeed this data is thought to be easily converted from
Ministry official data which can be found here:
	http://www.infoelectoral.mir.es/min/home.html
	http://www.ine.es/oficina_censo/cifras_electores.htm
The original files of the included data are in sourceData.


* 'originalData' holds original xls files downloaded from 
  the ministry (to be compared if any file gets altered)
* 'cookedData' holds ods files with one election case each
  sheet with the four columns format explained above.
* 'data' holds csv (tab separated table data) with is handled
  directly by envote.

To convert cookedData into envote data you can use 
the generateData.sh script which is in the from cookedData. It is a
Unix/Linux shell script.




