import requests
from bs4 import BeautifulSoup as bs

f=open("C:\\Users\\arih\\Desktop\\links.txt","r")
a=f.read()
a=a.split("\n")

names=[]
links=a
print links

for i in range(len(a)):
	c=a[i].split(" ")
	
	c=c[0][5:][:-1]
	c=c.split("/")
	c=c[-1].split("_")
	names.append(" ".join(c))
	


html='''<html>
<head>
	<title>Pornister</title>
	<meta name="exads-verify" content="c51953a9098cd09f4495" />
	<meta name="xhamster-site-verification" content="4bec140c84145458fececfc8d40bd335"/>
	<meta charset="utf-8">
	<meta class="viewport" content="width=device-width, initial-scale=1">
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
	<!-- jquery -->
 	<script	src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

	<!-- icons script -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	  
	 
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
	<!--<link rel="stylesheet" href="http://bootswatch.com/united/bootstrap.min.css"></link>-->
	<link rel="stylesheet" href="/site.css">
	<link rel="stylesheet" href="C:\Users\\arih\Downloads\project\project\site.css"></link>
	<script src="/site.js"></script>
	<script src="C:\Users\\arih\Downloads\project\project\site.js"></script>
  
 	
</head>
<body>
<div class="navbar-inner bg-success"><a href="https://pornister.github.io/"><img src="/bg-pattern.png"></a></div>
<!-- navbar-->
<nav class="navbar navbar-inverse" style="background-color: #e3f2fd;">
	<div class="container">
	
		<div class="navbar-header"><a href="https://pornister.github.io/" class="navbar-brand"> HOME </a></div>
			<div class="dropdown">
				<!--<ul class="nav navbar-nav dropdown-toggle" data-toggle="dropdown"><li><a>Categories <span class="caret"></span></a></li></ul>-->
				<div class="row dropdown-menu" style="margin-top: 50px;">
				<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/18 Years Old.html">18 Years Old</a></li>
							<li class="divider"></li>
							<li><a href="/69.html">69</a></li>
							<li class="divider"></li>
							<li><a href="/African.html">African</a></li>
							<li class="divider"></li>
							<li><a href="/Agent.html">Agent</a></li>
													<li class="divider"></li>
							<li><a href="/Albanian.html">Albanian</a></li>
													<li class="divider"></li>
							<li><a href="/Algerian.html">Algerian</a></li>
													<li class="divider"></li>
							<li><a href="/Alien.html">Alien</a></li>
													<li class="divider"></li>
							<li><a href="/Amateur.html">Amateur</a></li>
													<li class="divider"></li>
							<li><a href="/Amateur (Gay).html">Amateur (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Amateur (Shemale).html">Amateur (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/American.html">American</a></li>
													<li class="divider"></li>
							<li><a href="/Anal.html">Anal</a></li>
													<li class="divider"></li>
							<li><a href="/Arab.html">Arab</a></li>
													<li class="divider"></li>
							<li><a href="/Argentinian.html">Argentinian</a></li>
													<li class="divider"></li>
							<li><a href="/Armenian.html">Armenian</a></li>
													<li class="divider"></li>
							<li><a href="/Asian.html">Asian</a></li>
													<li class="divider"></li>
							<li><a href="/Asian (Gay).html">Asian (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Ass Licking.html">Ass Licking</a></li>
													<li class="divider"></li>
							<li><a href="/Audition.html">Audition</a></li>
													<li class="divider"></li>
							<li><a href="/Australian.html">Australian</a></li>
													<li class="divider"></li>
							<li><a href="/Austrian.html">Austrian</a></li>
													<li class="divider"></li>
							<li><a href="/Azeri.html">Azeri</a></li>
													<li class="divider"></li>
							<li><a href="/Babe.html">Babe</a></li>
													<li class="divider"></li>
							<li><a href="/Babysitters.html">Babysitters</a></li>
													<li class="divider"></li>
							<li><a href="/Ballbusting.html">Ballbusting</a></li>
													<li class="divider"></li>
							<li><a href="/Bangladeshi.html">Bangladeshi</a></li>
													<li class="divider"></li>
							<li><a href="/Bareback (Gay).html">Bareback (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Bareback (Shemale).html">Bareback (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/BBC.html">BBC</a></li>
													<li class="divider"></li>
							<li><a href="/BBW.html">BBW</a></li>
													<li class="divider"></li>
							<li><a href="/BDSM.html">BDSM</a></li>
													<li class="divider"></li>
							<li><a href="/BDSM (Gay).html">BDSM (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/BDSM (Shemale).html">BDSM (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Beach.html">Beach</a></li>
													<li class="divider"></li>
							<li><a href="/Beach (Gay).html">Beach (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Bears (Gay).html">Bears (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Belgian.html">Belgian</a></li>
													<li class="divider"></li>
							<li><a href="/Big Asses (Shemale).html">Big Asses (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Big Boobs.html">Big Boobs</a></li>
													<li class="divider"></li>
							<li><a href="/Big Butts.html">Big Butts</a></li>
													<li class="divider"></li>
							<li><a href="/Big Clits.html">Big Clits</a></li>
													<li class="divider"></li>
							<li><a href="/Big Cock.html">Big Cock</a></li>
													<li class="divider"></li>
							<li><a href="/Big Cocks (Gay).html">Big Cocks (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Big Cocks (Shemale).html">Big Cocks (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Big Natural Tits.html">Big Natural Tits</a></li>
													<li class="divider"></li>
							<li><a href="/Big Nipples.html">Big Nipples</a></li>
													<li class="divider"></li>
							<li><a href="/Big Tits (Shemale).html">Big Tits (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Bikini.html">Bikini</a></li>
													<li class="divider"></li>
							<li><a href="/Bisexuals.html">Bisexuals</a></li>
													<li class="divider"></li>
							<li><a href="/Black (Shemale).html">Black (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Black and Ebony.html">Black and Ebony</a></li>
													<li class="divider"></li>
							<li><a href="/Black Gays (Gay).html">Black Gays (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Blondes.html">Blondes</a></li>
													<li class="divider"></li>
							<li><a href="/Blowjobs.html">Blowjobs</a></li>
													<li class="divider"></li>
							<li><a href="/Blowjobs (Gay).html">Blowjobs (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Blowjobs (Shemale).html">Blowjobs (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Bolivian.html">Bolivian</a></li>
													<li class="divider"></li>
							<li><a href="/Bondage.html">Bondage</a></li>
													<li class="divider"></li>
							<li><a href="/Bosnian.html">Bosnian</a></li>
													<li class="divider"></li>
							<li><a href="/Brazilian.html">Brazilian</a></li>
													<li class="divider"></li>
							<li><a href="/British.html">British</a></li>
													<li class="divider"></li>
							<li><a href="/Brunettes.html">Brunettes</a></li>
													<li class="divider"></li>
							<li><a href="/Bukkake.html">Bukkake</a></li>
													<li class="divider"></li>
							<li><a href="/Bukkake (Gay).html">Bukkake (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Bulgarian.html">Bulgarian</a></li>
													<li class="divider"></li>
						</ul>
					</div>
					<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/Cambodian.html">Cambodian</a></li>
							<li class="divider"></li>
							<li><a href="/Canadian.html">Canadian</a></li>
													<li class="divider"></li>
							<li><a href="/Cartoons.html">Cartoons</a></li>
													<li class="divider"></li>
							<li><a href="/Castings.html">Castings</a></li>
													<li class="divider"></li>
							<li><a href="/Cat Fights.html">Cat Fights</a></li>
													<li class="divider"></li>
							<li><a href="/Celebrities.html">Celebrities</a></li>
													<li class="divider"></li>
							<li><a href="/CFNM.html">CFNM</a></li>
													<li class="divider"></li>
							<li><a href="/Cheating.html">Cheating</a></li>
													<li class="divider"></li>
							<li><a href="/Cheerleaders.html">Cheerleaders</a></li>
													<li class="divider"></li>
							<li><a href="/Chilean.html">Chilean</a></li>
													<li class="divider"></li>
							<li><a href="/Chinese.html">Chinese</a></li>
													<li class="divider"></li>
							<li><a href="/Close-ups.html">Close-ups</a></li>
													<li class="divider"></li>
							<li><a href="/Coed.html">Coed</a></li>
													<li class="divider"></li>
							<li><a href="/College.html">College</a></li>
													<li class="divider"></li>
							<li><a href="/Colombian.html">Colombian</a></li>
													<li class="divider"></li>
							<li><a href="/Compilation.html">Compilation</a></li>
													<li class="divider"></li>
							<li><a href="/Cosplay.html">Cosplay</a></li>
													<li class="divider"></li>
							<li><a href="/Costa Rica.html">Costa Rica</a></li>
													<li class="divider"></li>
							<li><a href="/Cougars.html">Cougars</a></li>
													<li class="divider"></li>
							<li><a href="/Creampie.html">Creampie</a></li>
													<li class="divider"></li>
							<li><a href="/Creampie  (Shemale).html">Creampie  (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Croatian.html">Croatian</a></li>
													<li class="divider"></li>
							<li><a href="/Crossdressers (Gay).html">Crossdressers (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Cuckold.html">Cuckold</a></li>
													<li class="divider"></li>
							<li><a href="/Cum in Mouth.html">Cum in Mouth</a></li>
													<li class="divider"></li>
							<li><a href="/Cum Swallowing.html">Cum Swallowing</a></li>
													<li class="divider"></li>
							<li><a href="/Cum Tributes (Gay).html">Cum Tributes (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Cumshots.html">Cumshots</a></li>
													<li class="divider"></li>
							<li><a href="/Cunnilingus.html">Cunnilingus</a></li>
													<li class="divider"></li>
							<li><a href="/Czech.html">Czech</a></li>
													<li class="divider"></li>
							<li><a href="/Dad.html">Dad</a></li>
													<li class="divider"></li>
							<li><a href="/Daddies (Gay).html">Daddies (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Danish.html">Danish</a></li>
													<li class="divider"></li>
							<li><a href="/Deep Throats.html">Deep Throats</a></li>
													<li class="divider"></li>
							<li><a href="/Dildo.html">Dildo</a></li>
													<li class="divider"></li>
							<li><a href="/Dirty Talk.html">Dirty Talk</a></li>
													<li class="divider"></li>
							<li><a href="/Doctor.html">Doctor</a></li>
													<li class="divider"></li>
							<li><a href="/Dogging.html">Dogging</a></li>
													<li class="divider"></li>
							<li><a href="/Doggy Style.html">Doggy Style</a></li>
													<li class="divider"></li>
							<li><a href="/Double Penetration.html">Double Penetration</a></li>
													<li class="divider"></li>
							<li><a href="/Dutch.html">Dutch</a></li>
													<li class="divider"></li>
							<li><a href="/Ecuador.html">Ecuador</a></li>
													<li class="divider"></li>
							<li><a href="/Egyptian.html">Egyptian</a></li>
													<li class="divider"></li>
							<li><a href="/Emo.html">Emo</a></li>
													<li class="divider"></li>
							<li><a href="/Emo Boys (Gay).html">Emo Boys (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Escort.html">Escort</a></li>
													<li class="divider"></li>
							<li><a href="/Estonia.html">Estonia</a></li>
													<li class="divider"></li>
							<li><a href="/European.html">European</a></li>
													<li class="divider"></li>
							<li><a href="/Face Sitting.html">Face Sitting</a></li>
													<li class="divider"></li>
							<li><a href="/Facials.html">Facials</a></li>
													<li class="divider"></li>
							<li><a href="/Fat Gays (Gay).html">Fat Gays (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Female Choice.html">Female Choice</a></li>
													<li class="divider"></li>
							<li><a href="/Femdom.html">Femdom</a></li>
													<li class="divider"></li>
							<li><a href="/Fingering.html">Fingering</a></li>
													<li class="divider"></li>
							<li><a href="/Finnish.html">Finnish</a></li>
													<li class="divider"></li>
							<li><a href="/Fisting (Gay).html">Fisting (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Fisting.html">Fisting</a></li>
													<li class="divider"></li>
							<li><a href="/Flashing.html">Flashing</a></li>
													<li class="divider"></li>
							<li><a href="/Foot Fetish.html">Foot Fetish</a></li>
													<li class="divider"></li>
							<li><a href="/Footjob.html">Footjob</a></li>
													<li class="divider"></li>
							<li><a href="/French.html">French</a></li>
													<li class="divider"></li>
							<li><a href="/Fucking Machines.html">Fucking Machines</a></li>
													<li class="divider"></li>
							<li><a href="/Funny.html">Funny</a></li>
													<li class="divider"></li>
							<li><a href="/Gangbang.html">Gangbang</a></li>
													<li class="divider"></li>
						</ul>
					</div>
					<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/Gangbang (Gay).html">Gangbang (Gay)</a></li>
							<li class="divider"></li>
							<li><a href="/Gangbang (Shemale).html">Gangbang (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Gaping.html">Gaping</a></li>
													<li class="divider"></li>
							<li><a href="/Gaping (Gay).html">Gaping (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Gay Porn (Gay).html">Gay Porn (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/German.html">German</a></li>
													<li class="divider"></li>
							<li><a href="/Ghetto.html">Ghetto</a></li>
													<li class="divider"></li>
							<li><a href="/Glory Holes (Gay).html">Glory Holes (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Glory Holes.html">Glory Holes</a></li>
													<li class="divider"></li>
							<li><a href="/Gothic.html">Gothic</a></li>
													<li class="divider"></li>
							<li><a href="/Grannies.html">Grannies</a></li>
													<li class="divider"></li>
							<li><a href="/Greek.html">Greek</a></li>
													<li class="divider"></li>
							<li><a href="/Group Sex.html">Group Sex</a></li>
													<li class="divider"></li>
							<li><a href="/Group Sex (Gay).html">Group Sex (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Guadeloupe.html">Guadeloupe</a></li>
													<li class="divider"></li>
							<li><a href="/Guatemala.html">Guatemala</a></li>
													<li class="divider"></li>
							<li><a href="/Guy Fucks Shemale (Shemale).html">Guy Fucks Shemale (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Hairy.html">Hairy</a></li>
													<li class="divider"></li>
							<li><a href="/Halloween.html">Halloween</a></li>
													<li class="divider"></li>
							<li><a href="/Handjobs.html">Handjobs</a></li>
													<li class="divider"></li>
							<li><a href="/Handjobs (Gay).html">Handjobs (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Hardcore.html">Hardcore</a></li>
													<li class="divider"></li>
							<li><a href="/HD Gays.html">HD Gays</a></li>
													<li class="divider"></li>
							<li><a href="/HD Shemales.html">HD Shemales</a></li>
													<li class="divider"></li>
							<li><a href="/HD Videos.html">HD Videos</a></li>
													<li class="divider"></li>
							<li><a href="/Hentai.html">Hentai</a></li>
													<li class="divider"></li>
							<li><a href="/Hidden Cams.html">Hidden Cams</a></li>
													<li class="divider"></li>
							<li><a href="/High Heels.html">High Heels</a></li>
													<li class="divider"></li>
							<li><a href="/Hogtied.html">Hogtied</a></li>
													<li class="divider"></li>
							<li><a href="/Homemade.html">Homemade</a></li>
													<li class="divider"></li>
							<li><a href="/Hungarian .html">Hungarian </a></li>
													<li class="divider"></li>
							<li><a href="/Hunks (Gay).html">Hunks (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Indian.html">Indian</a></li>
													<li class="divider"></li>
							<li><a href="/Indonesian.html">Indonesian</a></li>
													<li class="divider"></li>
							<li><a href="/Interracial.html">Interracial</a></li>
													<li class="divider"></li>
							<li><a href="/Interracial (Gay).html">Interracial (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Interracial (Shemale).html">Interracial (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Interview.html">Interview</a></li>
													<li class="divider"></li>
							<li><a href="/Iranian.html">Iranian</a></li>
													<li class="divider"></li>
							<li><a href="/Irish.html">Irish</a></li>
													<li class="divider"></li>
							<li><a href="/Israeli.html">Israeli</a></li>
													<li class="divider"></li>
							<li><a href="/Italian.html">Italian</a></li>
													<li class="divider"></li>
							<li><a href="/Jamaican.html">Jamaican</a></li>
													<li class="divider"></li>
							<li><a href="/Japanese.html">Japanese</a></li>
													<li class="divider"></li>
							<li><a href="/Jewish.html">Jewish</a></li>
													<li class="divider"></li>
							<li><a href="/JOI.html">JOI</a></li>
													<li class="divider"></li>
							<li><a href="/Kissing.html">Kissing</a></li>
													<li class="divider"></li>
							<li><a href="/Korean.html">Korean</a></li>
													<li class="divider"></li>
							<li><a href="/Lactating.html">Lactating</a></li>
													<li class="divider"></li>
							<li><a href="/Ladyboys (Shemale).html">Ladyboys (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Latex.html">Latex</a></li>
													<li class="divider"></li>
							<li><a href="/Latex (Shemale).html">Latex (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Latin.html">Latin</a></li>
													<li class="divider"></li>
							<li><a href="/Latin (Gay).html">Latin (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Latin (Shemale).html">Latin (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Latvian.html">Latvian</a></li>
													<li class="divider"></li>
							<li><a href="/Lebanese.html">Lebanese</a></li>
													<li class="divider"></li>
							<li><a href="/Lesbians.html">Lesbians</a></li>
													<li class="divider"></li>
							<li><a href="/Lingerie.html">Lingerie</a></li>
													<li class="divider"></li>
							<li><a href="/Lingerie (Shemale).html">Lingerie (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Lithuanian.html">Lithuanian</a></li>
													<li class="divider"></li>
							<li><a href="/Locker Rooms (Gay).html">Locker Rooms (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Macedonian.html">Macedonian</a></li>
													<li class="divider"></li>
							<li><a href="/Maid.html">Maid</a></li>
							<li class="divider"></li>
						</ul>
					</div>
					<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/Malaysian.html">Malaysian</a></li>
							<li class="divider"></li>
							<li><a href="/Massage.html">Massage</a></li>
													<li class="divider"></li>
							<li><a href="/Massage (Gay).html">Massage (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Masturbation.html">Masturbation</a></li>
													<li class="divider"></li>
							<li><a href="/Masturbation (Gay).html">Masturbation (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Masturbation (Shemale).html">Masturbation (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Matures.html">Matures</a></li>
													<li class="divider"></li>
							<li><a href="/Medical.html">Medical</a></li>
													<li class="divider"></li>
							<li><a href="/Men (Gay).html">Men (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Mexican.html">Mexican</a></li>
													<li class="divider"></li>
							<li><a href="/Midgets.html">Midgets</a></li>
													<li class="divider"></li>
							<li><a href="/MILFs.html">MILFs</a></li>
													<li class="divider"></li>
							<li><a href="/Military (Gay).html">Military (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Military.html">Military</a></li>
													<li class="divider"></li>
							<li><a href="/Mistress.html">Mistress</a></li>
													<li class="divider"></li>
							<li><a href="/Moldavian.html">Moldavian</a></li>
													<li class="divider"></li>
							<li><a href="/Mom.html">Mom</a></li>
													<li class="divider"></li>
							<li><a href="/Moroccan.html">Moroccan</a></li>
													<li class="divider"></li>
							<li><a href="/Muscle (Gay).html">Muscle (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Muscular Women.html">Muscular Women</a></li>
													<li class="divider"></li>
							<li><a href="/Nigerian.html">Nigerian</a></li>
													<li class="divider"></li>
							<li><a href="/Nipples.html">Nipples</a></li>
													<li class="divider"></li>
							<li><a href="/Norwegian.html">Norwegian</a></li>
													<li class="divider"></li>
							<li><a href="/Nudist.html">Nudist</a></li>
													<li class="divider"></li>
							<li><a href="/Nylon.html">Nylon</a></li>
													<li class="divider"></li>
							<li><a href="/Old+Young.html">Old+Young</a></li>
													<li class="divider"></li>
							<li><a href="/Old+Young (Gay).html">Old+Young (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Orgasms.html">Orgasms</a></li>
													<li class="divider"></li>
							<li><a href="/Orgy.html">Orgy</a></li>
													<li class="divider"></li>
							<li><a href="/Outdoor (Gay).html">Outdoor (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Outdoor (Shemale).html">Outdoor (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Outdoor.html">Outdoor</a></li>
													<li class="divider"></li>
							<li><a href="/Pakistani.html">Pakistani</a></li>
													<li class="divider"></li>
							<li><a href="/Panama.html">Panama</a></li>
													<li class="divider"></li>
							<li><a href="/Pantyhose.html">Pantyhose</a></li>
													<li class="divider"></li>
							<li><a href="/Party.html">Party</a></li>
													<li class="divider"></li>
							<li><a href="/Peruvian.html">Peruvian</a></li>
													<li class="divider"></li>
							<li><a href="/Philippines.html">Philippines</a></li>
													<li class="divider"></li>
							<li><a href="/Piercing.html">Piercing</a></li>
													<li class="divider"></li>
							<li><a href="/Pissing.html">Pissing</a></li>
													<li class="divider"></li>
							<li><a href="/Polish.html">Polish</a></li>
													<li class="divider"></li>
							<li><a href="/Pornstars.html">Pornstars</a></li>
													<li class="divider"></li>
							<li><a href="/Portuguese.html">Portuguese</a></li>
													<li class="divider"></li>
							<li><a href="/POV.html">POV</a></li>
													<li class="divider"></li>
							<li><a href="/POV (Shemale).html">POV (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Pregnant.html">Pregnant</a></li>
													<li class="divider"></li>
							<li><a href="/Public Nudity.html">Public Nudity</a></li>
													<li class="divider"></li>
							<li><a href="/Puerto Rican.html">Puerto Rican</a></li>
													<li class="divider"></li>
							<li><a href="/Puffy Nipples.html">Puffy Nipples</a></li>
													<li class="divider"></li>
							<li><a href="/Pussy.html">Pussy</a></li>
													<li class="divider"></li>
							<li><a href="/Redheads.html">Redheads</a></li>
													<li class="divider"></li>
							<li><a href="/Retro.html">Retro</a></li>
													<li class="divider"></li>
							<li><a href="/Rimjob.html">Rimjob</a></li>
													<li class="divider"></li>
							<li><a href="/Romanian.html">Romanian</a></li>
													<li class="divider"></li>
							<li><a href="/Russian.html">Russian</a></li>
													<li class="divider"></li>
							<li><a href="/Saggy Tits.html">Saggy Tits</a></li>
													<li class="divider"></li>
							<li><a href="/Secretaries.html">Secretaries</a></li>
													<li class="divider"></li>
							<li><a href="/Serbian.html">Serbian</a></li>
													<li class="divider"></li>
							<li><a href="/Sex Toys.html">Sex Toys</a></li>
													<li class="divider"></li>
							<li><a href="/Sex Toys (Gay).html">Sex Toys (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Sex Toys (Shemale).html">Sex Toys (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Shemale Fucks Girl (Shemale).html">Shemale Fucks Girl (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Shemale Fucks Guy (Shemale).html">Shemale Fucks Guy (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Shemale Fucks Shemale (Shemale).html">Shemale Fucks Shemale (Shemale)</a></li>
							<li class="divider"></li>
						</ul>
					</div>
					<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/Shemales (Shemale).html">Shemales (Shemale)</a></li>
							<li class="divider"></li>
							<li><a href="/Showers.html">Showers</a></li>
													<li class="divider"></li>
							<li><a href="/Singaporean.html">Singaporean</a></li>
													<li class="divider"></li>
							<li><a href="/Skinny.html">Skinny</a></li>
													<li class="divider"></li>
							<li><a href="/Slave.html">Slave</a></li>
													<li class="divider"></li>
							<li><a href="/Slovakian.html">Slovakian</a></li>
													<li class="divider"></li>
							<li><a href="/Slovenian.html">Slovenian</a></li>
													<li class="divider"></li>
							<li><a href="/Small Cocks (Gay).html">Small Cocks (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Small Tits.html">Small Tits</a></li>
													<li class="divider"></li>
							<li><a href="/Small Tits Shemales (Shemale).html">Small Tits Shemales (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Softcore.html">Softcore</a></li>
													<li class="divider"></li>
							<li><a href="/Solo  (Shemale).html">Solo  (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/South African.html">South African</a></li>
													<li class="divider"></li>
							<li><a href="/Spandex.html">Spandex</a></li>
													<li class="divider"></li>
							<li><a href="/Spanish.html">Spanish</a></li>
													<li class="divider"></li>
							<li><a href="/Spanking.html">Spanking</a></li>
													<li class="divider"></li>
							<li><a href="/Spanking (Gay).html">Spanking (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Sports.html">Sports</a></li>
													<li class="divider"></li>
							<li><a href="/Squirting.html">Squirting</a></li>
													<li class="divider"></li>
							<li><a href="/Sri Lankan.html">Sri Lankan</a></li>
													<li class="divider"></li>
							<li><a href="/Stockings.html">Stockings</a></li>
													<li class="divider"></li>
							<li><a href="/Stockings (Shemale).html">Stockings (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Strapon.html">Strapon</a></li>
													<li class="divider"></li>
							<li><a href="/Striptease (Gay).html">Striptease (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Striptease.html">Striptease</a></li>
													<li class="divider"></li>
							<li><a href="/Swedish.html">Swedish</a></li>
													<li class="divider"></li>
							<li><a href="/Swingers.html">Swingers</a></li>
													<li class="divider"></li>
							<li><a href="/Swiss.html">Swiss</a></li>
													<li class="divider"></li>
							<li><a href="/Sybian.html">Sybian</a></li>
													<li class="divider"></li>
							<li><a href="/Tattoos.html">Tattoos</a></li>
													<li class="divider"></li>
							<li><a href="/Taxi.html">Taxi</a></li>
													<li class="divider"></li>
							<li><a href="/Teacher.html">Teacher</a></li>
													<li class="divider"></li>
							<li><a href="/Teens.html">Teens</a></li>
													<li class="divider"></li>
							<li><a href="/Teens  (Shemale).html">Teens  (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Thai.html">Thai</a></li>
													<li class="divider"></li>
							<li><a href="/Threesomes.html">Threesomes</a></li>
													<li class="divider"></li>
							<li><a href="/Tits.html">Tits</a></li>
													<li class="divider"></li>
							<li><a href="/Titty Fucking.html">Titty Fucking</a></li>
													<li class="divider"></li>
							<li><a href="/Top Rated.html">Top Rated</a></li>
													<li class="divider"></li>
							<li><a href="/Tunisian.html">Tunisian</a></li>
													<li class="divider"></li>
							<li><a href="/Turkish.html">Turkish</a></li>
													<li class="divider"></li>
							<li><a href="/Twinks (Gay).html">Twinks (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Ukrainian.html">Ukrainian</a></li>
													<li class="divider"></li>
							<li><a href="/Upskirts.html">Upskirts</a></li>
													<li class="divider"></li>
							<li><a href="/Valentine's Day.html">Valentine's Day</a></li>
													<li class="divider"></li>
							<li><a href="/Venezuelan.html">Venezuelan</a></li>
													<li class="divider"></li>
							<li><a href="/Vibrator.html">Vibrator</a></li>
													<li class="divider"></li>
							<li><a href="/Vietnamese.html">Vietnamese</a></li>
													<li class="divider"></li>
							<li><a href="/Vintage.html">Vintage</a></li>
													<li class="divider"></li>
							<li><a href="/Vintage (Gay).html">Vintage (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Vintage (Shemale).html">Vintage (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Voyeur.html">Voyeur</a></li>
													<li class="divider"></li>
							<li><a href="/Voyeur (Gay).html">Voyeur (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/VR Porn.html">VR Porn</a></li>
													<li class="divider"></li>
							<li><a href="/Webcams.html">Webcams</a></li>
													<li class="divider"></li>
							<li><a href="/Webcams (Gay).html">Webcams (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Webcams (Shemale).html">Webcams (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Whipping.html">Whipping</a></li>
													<li class="divider"></li>
							<li><a href="/Wife.html">Wife</a></li>
													<li class="divider"></li>
							<li><a href="/Wife Sharing.html">Wife Sharing</a></li>
													<li class="divider"></li>
							<li><a href="/Wrestling (Gay).html">Wrestling (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Xmas.html">Xmas</a></li>
													<li class="divider"></li>
							<li><a href="/Yoga.html">Yoga</a></li>
								<li class="divider"></li>
						</ul>
					</div>
			</div><!-- .row .dropdown-menu-->
			</div><!-- .dropdown -->
	</div><!-- .container -->
</nav>

<div class="container-fluid" id="container1">
	<div class="row shuffle" id="row1">
	<!--****************************** pagination*************************************************************************************-->
		<div class="col-md-12 text-center" id="pagination">

        
        <style type="text/css">.btn{ font-size: 30px !important;}</style>
    	</div>
    	<!--****************************** pagination*************************************************************************************-->
'''
		

integer=raw_input("enter an integer: ")
import os
os.system("mkdir "+integer)
file=open(integer+".html","w")
file.write(html)
	
for i in range(len(names)):
	middle='''<div class="col-xs-6 col-sm-6 col-md-3">
			<div class="panel panel-primary">
				<div class="panel-body" style="padding:0px !important;"> <a href="/'''+integer+'''/'''+names[i][:-4]+'''.html
						" target="_blank">
    				<div style="position:absolute;z-index:500;height:245px;width:100%;"></div>
    					<iframe type="text/html" frameborder="0" height="245" width="100%" src="'''+links[i]+'''"></iframe>
  						</a>
  				</div>
  					<div class="panel-footer"><i class="fa fa-eye"><a href="/'''+integer+'''/'''+names[i][:-4]+'''.html" style="text-decoration: none;"> '''+names[i][:-4]+'''</a></i></div>
			</div>
		</div><!-- .col-md-3 -->
		'''
	
	file.write(middle)
	file.write("\n")
	


end='''
</div><!-- .row1 -->
</div><!-- .container1 -->
</body>
</html>'''
file.close()

page='''<html>
<head>
	<title>Pornister</title>
	<meta charset="utf-8">
	<meta class="viewport" content="width=device-width, initial-scale=1">
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
	<!-- jquery -->
 	<script	src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

	<!-- icons script -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	  
	 
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
	<!--<link rel="stylesheet" href="http://bootswatch.com/united/bootstrap.min.css"></link>-->
	<link rel="stylesheet" href="/site.css">
  <script>
	$(function(){
		var el= $(window).width();
		if (el<=500)
			{
				$("#i-div").addClass('embed-responsive embed-responsive-16by9');
				$("iframe").addClass('embed-responsive-item');
			}
		else{
			i=1;
		}
	});
	
</script>
 	
</head>
<body>
<div class="navbar-inner bg-success"><a href="https://pornister.github.io/"><img src="/bg-pattern.png"></a></div>
<!-- navbar-->
<nav class="navbar navbar-inverse" style="background-color: #e3f2fd;">
	<div class="container">
	
		<div class="navbar-header"><a href="https://pornister.github.io/" class="navbar-brand"> HOME </a></div>
			<div class="dropdown">
				<!--<ul class="nav navbar-nav dropdown-toggle" data-toggle="dropdown"><li><a>Categories <span class="caret"></span></a></li></ul>-->
				<div class="row dropdown-menu" style="margin-top: 50px;">
				<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/18 Years Old.html">18 Years Old</a></li>
							<li class="divider"></li>
							<li><a href="/69.html">69</a></li>
							<li class="divider"></li>
							<li><a href="/African.html">African</a></li>
							<li class="divider"></li>
							<li><a href="/Agent.html">Agent</a></li>
													<li class="divider"></li>
							<li><a href="/Albanian.html">Albanian</a></li>
													<li class="divider"></li>
							<li><a href="/Algerian.html">Algerian</a></li>
													<li class="divider"></li>
							<li><a href="/Alien.html">Alien</a></li>
													<li class="divider"></li>
							<li><a href="/Amateur.html">Amateur</a></li>
													<li class="divider"></li>
							<li><a href="/Amateur (Gay).html">Amateur (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Amateur (Shemale).html">Amateur (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/American.html">American</a></li>
													<li class="divider"></li>
							<li><a href="/Anal.html">Anal</a></li>
													<li class="divider"></li>
							<li><a href="/Arab.html">Arab</a></li>
													<li class="divider"></li>
							<li><a href="/Argentinian.html">Argentinian</a></li>
													<li class="divider"></li>
							<li><a href="/Armenian.html">Armenian</a></li>
													<li class="divider"></li>
							<li><a href="/Asian.html">Asian</a></li>
													<li class="divider"></li>
							<li><a href="/Asian (Gay).html">Asian (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Ass Licking.html">Ass Licking</a></li>
													<li class="divider"></li>
							<li><a href="/Audition.html">Audition</a></li>
													<li class="divider"></li>
							<li><a href="/Australian.html">Australian</a></li>
													<li class="divider"></li>
							<li><a href="/Austrian.html">Austrian</a></li>
													<li class="divider"></li>
							<li><a href="/Azeri.html">Azeri</a></li>
													<li class="divider"></li>
							<li><a href="/Babe.html">Babe</a></li>
													<li class="divider"></li>
							<li><a href="/Babysitters.html">Babysitters</a></li>
													<li class="divider"></li>
							<li><a href="/Ballbusting.html">Ballbusting</a></li>
													<li class="divider"></li>
							<li><a href="/Bangladeshi.html">Bangladeshi</a></li>
													<li class="divider"></li>
							<li><a href="/Bareback (Gay).html">Bareback (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Bareback (Shemale).html">Bareback (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/BBC.html">BBC</a></li>
													<li class="divider"></li>
							<li><a href="/BBW.html">BBW</a></li>
													<li class="divider"></li>
							<li><a href="/BDSM.html">BDSM</a></li>
													<li class="divider"></li>
							<li><a href="/BDSM (Gay).html">BDSM (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/BDSM (Shemale).html">BDSM (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Beach.html">Beach</a></li>
													<li class="divider"></li>
							<li><a href="/Beach (Gay).html">Beach (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Bears (Gay).html">Bears (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Belgian.html">Belgian</a></li>
													<li class="divider"></li>
							<li><a href="/Big Asses (Shemale).html">Big Asses (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Big Boobs.html">Big Boobs</a></li>
													<li class="divider"></li>
							<li><a href="/Big Butts.html">Big Butts</a></li>
													<li class="divider"></li>
							<li><a href="/Big Clits.html">Big Clits</a></li>
													<li class="divider"></li>
							<li><a href="/Big Cock.html">Big Cock</a></li>
													<li class="divider"></li>
							<li><a href="/Big Cocks (Gay).html">Big Cocks (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Big Cocks (Shemale).html">Big Cocks (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Big Natural Tits.html">Big Natural Tits</a></li>
													<li class="divider"></li>
							<li><a href="/Big Nipples.html">Big Nipples</a></li>
													<li class="divider"></li>
							<li><a href="/Big Tits (Shemale).html">Big Tits (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Bikini.html">Bikini</a></li>
													<li class="divider"></li>
							<li><a href="/Bisexuals.html">Bisexuals</a></li>
													<li class="divider"></li>
							<li><a href="/Black (Shemale).html">Black (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Black and Ebony.html">Black and Ebony</a></li>
													<li class="divider"></li>
							<li><a href="/Black Gays (Gay).html">Black Gays (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Blondes.html">Blondes</a></li>
													<li class="divider"></li>
							<li><a href="/Blowjobs.html">Blowjobs</a></li>
													<li class="divider"></li>
							<li><a href="/Blowjobs (Gay).html">Blowjobs (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Blowjobs (Shemale).html">Blowjobs (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Bolivian.html">Bolivian</a></li>
													<li class="divider"></li>
							<li><a href="/Bondage.html">Bondage</a></li>
													<li class="divider"></li>
							<li><a href="/Bosnian.html">Bosnian</a></li>
													<li class="divider"></li>
							<li><a href="/Brazilian.html">Brazilian</a></li>
													<li class="divider"></li>
							<li><a href="/British.html">British</a></li>
													<li class="divider"></li>
							<li><a href="/Brunettes.html">Brunettes</a></li>
													<li class="divider"></li>
							<li><a href="/Bukkake.html">Bukkake</a></li>
													<li class="divider"></li>
							<li><a href="/Bukkake (Gay).html">Bukkake (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Bulgarian.html">Bulgarian</a></li>
													<li class="divider"></li>
						</ul>
					</div>
					<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/Cambodian.html">Cambodian</a></li>
							<li class="divider"></li>
							<li><a href="/Canadian.html">Canadian</a></li>
													<li class="divider"></li>
							<li><a href="/Cartoons.html">Cartoons</a></li>
													<li class="divider"></li>
							<li><a href="/Castings.html">Castings</a></li>
													<li class="divider"></li>
							<li><a href="/Cat Fights.html">Cat Fights</a></li>
													<li class="divider"></li>
							<li><a href="/Celebrities.html">Celebrities</a></li>
													<li class="divider"></li>
							<li><a href="/CFNM.html">CFNM</a></li>
													<li class="divider"></li>
							<li><a href="/Cheating.html">Cheating</a></li>
													<li class="divider"></li>
							<li><a href="/Cheerleaders.html">Cheerleaders</a></li>
													<li class="divider"></li>
							<li><a href="/Chilean.html">Chilean</a></li>
													<li class="divider"></li>
							<li><a href="/Chinese.html">Chinese</a></li>
													<li class="divider"></li>
							<li><a href="/Close-ups.html">Close-ups</a></li>
													<li class="divider"></li>
							<li><a href="/Coed.html">Coed</a></li>
													<li class="divider"></li>
							<li><a href="/College.html">College</a></li>
													<li class="divider"></li>
							<li><a href="/Colombian.html">Colombian</a></li>
													<li class="divider"></li>
							<li><a href="/Compilation.html">Compilation</a></li>
													<li class="divider"></li>
							<li><a href="/Cosplay.html">Cosplay</a></li>
													<li class="divider"></li>
							<li><a href="/Costa Rica.html">Costa Rica</a></li>
													<li class="divider"></li>
							<li><a href="/Cougars.html">Cougars</a></li>
													<li class="divider"></li>
							<li><a href="/Creampie.html">Creampie</a></li>
													<li class="divider"></li>
							<li><a href="/Creampie  (Shemale).html">Creampie  (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Croatian.html">Croatian</a></li>
													<li class="divider"></li>
							<li><a href="/Crossdressers (Gay).html">Crossdressers (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Cuckold.html">Cuckold</a></li>
													<li class="divider"></li>
							<li><a href="/Cum in Mouth.html">Cum in Mouth</a></li>
													<li class="divider"></li>
							<li><a href="/Cum Swallowing.html">Cum Swallowing</a></li>
													<li class="divider"></li>
							<li><a href="/Cum Tributes (Gay).html">Cum Tributes (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Cumshots.html">Cumshots</a></li>
													<li class="divider"></li>
							<li><a href="/Cunnilingus.html">Cunnilingus</a></li>
													<li class="divider"></li>
							<li><a href="/Czech.html">Czech</a></li>
													<li class="divider"></li>
							<li><a href="/Dad.html">Dad</a></li>
													<li class="divider"></li>
							<li><a href="/Daddies (Gay).html">Daddies (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Danish.html">Danish</a></li>
													<li class="divider"></li>
							<li><a href="/Deep Throats.html">Deep Throats</a></li>
													<li class="divider"></li>
							<li><a href="/Dildo.html">Dildo</a></li>
													<li class="divider"></li>
							<li><a href="/Dirty Talk.html">Dirty Talk</a></li>
													<li class="divider"></li>
							<li><a href="/Doctor.html">Doctor</a></li>
													<li class="divider"></li>
							<li><a href="/Dogging.html">Dogging</a></li>
													<li class="divider"></li>
							<li><a href="/Doggy Style.html">Doggy Style</a></li>
													<li class="divider"></li>
							<li><a href="/Double Penetration.html">Double Penetration</a></li>
													<li class="divider"></li>
							<li><a href="/Dutch.html">Dutch</a></li>
													<li class="divider"></li>
							<li><a href="/Ecuador.html">Ecuador</a></li>
													<li class="divider"></li>
							<li><a href="/Egyptian.html">Egyptian</a></li>
													<li class="divider"></li>
							<li><a href="/Emo.html">Emo</a></li>
													<li class="divider"></li>
							<li><a href="/Emo Boys (Gay).html">Emo Boys (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Escort.html">Escort</a></li>
													<li class="divider"></li>
							<li><a href="/Estonia.html">Estonia</a></li>
													<li class="divider"></li>
							<li><a href="/European.html">European</a></li>
													<li class="divider"></li>
							<li><a href="/Face Sitting.html">Face Sitting</a></li>
													<li class="divider"></li>
							<li><a href="/Facials.html">Facials</a></li>
													<li class="divider"></li>
							<li><a href="/Fat Gays (Gay).html">Fat Gays (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Female Choice.html">Female Choice</a></li>
													<li class="divider"></li>
							<li><a href="/Femdom.html">Femdom</a></li>
													<li class="divider"></li>
							<li><a href="/Fingering.html">Fingering</a></li>
													<li class="divider"></li>
							<li><a href="/Finnish.html">Finnish</a></li>
													<li class="divider"></li>
							<li><a href="/Fisting (Gay).html">Fisting (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Fisting.html">Fisting</a></li>
													<li class="divider"></li>
							<li><a href="/Flashing.html">Flashing</a></li>
													<li class="divider"></li>
							<li><a href="/Foot Fetish.html">Foot Fetish</a></li>
													<li class="divider"></li>
							<li><a href="/Footjob.html">Footjob</a></li>
													<li class="divider"></li>
							<li><a href="/French.html">French</a></li>
													<li class="divider"></li>
							<li><a href="/Fucking Machines.html">Fucking Machines</a></li>
													<li class="divider"></li>
							<li><a href="/Funny.html">Funny</a></li>
													<li class="divider"></li>
							<li><a href="/Gangbang.html">Gangbang</a></li>
													<li class="divider"></li>
						</ul>
					</div>
					<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/Gangbang (Gay).html">Gangbang (Gay)</a></li>
							<li class="divider"></li>
							<li><a href="/Gangbang (Shemale).html">Gangbang (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Gaping.html">Gaping</a></li>
													<li class="divider"></li>
							<li><a href="/Gaping (Gay).html">Gaping (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Gay Porn (Gay).html">Gay Porn (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/German.html">German</a></li>
													<li class="divider"></li>
							<li><a href="/Ghetto.html">Ghetto</a></li>
													<li class="divider"></li>
							<li><a href="/Glory Holes (Gay).html">Glory Holes (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Glory Holes.html">Glory Holes</a></li>
													<li class="divider"></li>
							<li><a href="/Gothic.html">Gothic</a></li>
													<li class="divider"></li>
							<li><a href="/Grannies.html">Grannies</a></li>
													<li class="divider"></li>
							<li><a href="/Greek.html">Greek</a></li>
													<li class="divider"></li>
							<li><a href="/Group Sex.html">Group Sex</a></li>
													<li class="divider"></li>
							<li><a href="/Group Sex (Gay).html">Group Sex (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Guadeloupe.html">Guadeloupe</a></li>
													<li class="divider"></li>
							<li><a href="/Guatemala.html">Guatemala</a></li>
													<li class="divider"></li>
							<li><a href="/Guy Fucks Shemale (Shemale).html">Guy Fucks Shemale (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Hairy.html">Hairy</a></li>
													<li class="divider"></li>
							<li><a href="/Halloween.html">Halloween</a></li>
													<li class="divider"></li>
							<li><a href="/Handjobs.html">Handjobs</a></li>
													<li class="divider"></li>
							<li><a href="/Handjobs (Gay).html">Handjobs (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Hardcore.html">Hardcore</a></li>
													<li class="divider"></li>
							<li><a href="/HD Gays.html">HD Gays</a></li>
													<li class="divider"></li>
							<li><a href="/HD Shemales.html">HD Shemales</a></li>
													<li class="divider"></li>
							<li><a href="/HD Videos.html">HD Videos</a></li>
													<li class="divider"></li>
							<li><a href="/Hentai.html">Hentai</a></li>
													<li class="divider"></li>
							<li><a href="/Hidden Cams.html">Hidden Cams</a></li>
													<li class="divider"></li>
							<li><a href="/High Heels.html">High Heels</a></li>
													<li class="divider"></li>
							<li><a href="/Hogtied.html">Hogtied</a></li>
													<li class="divider"></li>
							<li><a href="/Homemade.html">Homemade</a></li>
													<li class="divider"></li>
							<li><a href="/Hungarian .html">Hungarian </a></li>
													<li class="divider"></li>
							<li><a href="/Hunks (Gay).html">Hunks (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Indian.html">Indian</a></li>
													<li class="divider"></li>
							<li><a href="/Indonesian.html">Indonesian</a></li>
													<li class="divider"></li>
							<li><a href="/Interracial.html">Interracial</a></li>
													<li class="divider"></li>
							<li><a href="/Interracial (Gay).html">Interracial (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Interracial (Shemale).html">Interracial (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Interview.html">Interview</a></li>
													<li class="divider"></li>
							<li><a href="/Iranian.html">Iranian</a></li>
													<li class="divider"></li>
							<li><a href="/Irish.html">Irish</a></li>
													<li class="divider"></li>
							<li><a href="/Israeli.html">Israeli</a></li>
													<li class="divider"></li>
							<li><a href="/Italian.html">Italian</a></li>
													<li class="divider"></li>
							<li><a href="/Jamaican.html">Jamaican</a></li>
													<li class="divider"></li>
							<li><a href="/Japanese.html">Japanese</a></li>
													<li class="divider"></li>
							<li><a href="/Jewish.html">Jewish</a></li>
													<li class="divider"></li>
							<li><a href="/JOI.html">JOI</a></li>
													<li class="divider"></li>
							<li><a href="/Kissing.html">Kissing</a></li>
													<li class="divider"></li>
							<li><a href="/Korean.html">Korean</a></li>
													<li class="divider"></li>
							<li><a href="/Lactating.html">Lactating</a></li>
													<li class="divider"></li>
							<li><a href="/Ladyboys (Shemale).html">Ladyboys (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Latex.html">Latex</a></li>
													<li class="divider"></li>
							<li><a href="/Latex (Shemale).html">Latex (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Latin.html">Latin</a></li>
													<li class="divider"></li>
							<li><a href="/Latin (Gay).html">Latin (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Latin (Shemale).html">Latin (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Latvian.html">Latvian</a></li>
													<li class="divider"></li>
							<li><a href="/Lebanese.html">Lebanese</a></li>
													<li class="divider"></li>
							<li><a href="/Lesbians.html">Lesbians</a></li>
													<li class="divider"></li>
							<li><a href="/Lingerie.html">Lingerie</a></li>
													<li class="divider"></li>
							<li><a href="/Lingerie (Shemale).html">Lingerie (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Lithuanian.html">Lithuanian</a></li>
													<li class="divider"></li>
							<li><a href="/Locker Rooms (Gay).html">Locker Rooms (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Macedonian.html">Macedonian</a></li>
													<li class="divider"></li>
							<li><a href="/Maid.html">Maid</a></li>
							<li class="divider"></li>
						</ul>
					</div>
					<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/Malaysian.html">Malaysian</a></li>
							<li class="divider"></li>
							<li><a href="/Massage.html">Massage</a></li>
													<li class="divider"></li>
							<li><a href="/Massage (Gay).html">Massage (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Masturbation.html">Masturbation</a></li>
													<li class="divider"></li>
							<li><a href="/Masturbation (Gay).html">Masturbation (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Masturbation (Shemale).html">Masturbation (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Matures.html">Matures</a></li>
													<li class="divider"></li>
							<li><a href="/Medical.html">Medical</a></li>
													<li class="divider"></li>
							<li><a href="/Men (Gay).html">Men (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Mexican.html">Mexican</a></li>
													<li class="divider"></li>
							<li><a href="/Midgets.html">Midgets</a></li>
													<li class="divider"></li>
							<li><a href="/MILFs.html">MILFs</a></li>
													<li class="divider"></li>
							<li><a href="/Military (Gay).html">Military (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Military.html">Military</a></li>
													<li class="divider"></li>
							<li><a href="/Mistress.html">Mistress</a></li>
													<li class="divider"></li>
							<li><a href="/Moldavian.html">Moldavian</a></li>
													<li class="divider"></li>
							<li><a href="/Mom.html">Mom</a></li>
													<li class="divider"></li>
							<li><a href="/Moroccan.html">Moroccan</a></li>
													<li class="divider"></li>
							<li><a href="/Muscle (Gay).html">Muscle (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Muscular Women.html">Muscular Women</a></li>
													<li class="divider"></li>
							<li><a href="/Nigerian.html">Nigerian</a></li>
													<li class="divider"></li>
							<li><a href="/Nipples.html">Nipples</a></li>
													<li class="divider"></li>
							<li><a href="/Norwegian.html">Norwegian</a></li>
													<li class="divider"></li>
							<li><a href="/Nudist.html">Nudist</a></li>
													<li class="divider"></li>
							<li><a href="/Nylon.html">Nylon</a></li>
													<li class="divider"></li>
							<li><a href="/Old+Young.html">Old+Young</a></li>
													<li class="divider"></li>
							<li><a href="/Old+Young (Gay).html">Old+Young (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Orgasms.html">Orgasms</a></li>
													<li class="divider"></li>
							<li><a href="/Orgy.html">Orgy</a></li>
													<li class="divider"></li>
							<li><a href="/Outdoor (Gay).html">Outdoor (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Outdoor (Shemale).html">Outdoor (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Outdoor.html">Outdoor</a></li>
													<li class="divider"></li>
							<li><a href="/Pakistani.html">Pakistani</a></li>
													<li class="divider"></li>
							<li><a href="/Panama.html">Panama</a></li>
													<li class="divider"></li>
							<li><a href="/Pantyhose.html">Pantyhose</a></li>
													<li class="divider"></li>
							<li><a href="/Party.html">Party</a></li>
													<li class="divider"></li>
							<li><a href="/Peruvian.html">Peruvian</a></li>
													<li class="divider"></li>
							<li><a href="/Philippines.html">Philippines</a></li>
													<li class="divider"></li>
							<li><a href="/Piercing.html">Piercing</a></li>
													<li class="divider"></li>
							<li><a href="/Pissing.html">Pissing</a></li>
													<li class="divider"></li>
							<li><a href="/Polish.html">Polish</a></li>
													<li class="divider"></li>
							<li><a href="/Pornstars.html">Pornstars</a></li>
													<li class="divider"></li>
							<li><a href="/Portuguese.html">Portuguese</a></li>
													<li class="divider"></li>
							<li><a href="/POV.html">POV</a></li>
													<li class="divider"></li>
							<li><a href="/POV (Shemale).html">POV (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Pregnant.html">Pregnant</a></li>
													<li class="divider"></li>
							<li><a href="/Public Nudity.html">Public Nudity</a></li>
													<li class="divider"></li>
							<li><a href="/Puerto Rican.html">Puerto Rican</a></li>
													<li class="divider"></li>
							<li><a href="/Puffy Nipples.html">Puffy Nipples</a></li>
													<li class="divider"></li>
							<li><a href="/Pussy.html">Pussy</a></li>
													<li class="divider"></li>
							<li><a href="/Redheads.html">Redheads</a></li>
													<li class="divider"></li>
							<li><a href="/Retro.html">Retro</a></li>
													<li class="divider"></li>
							<li><a href="/Rimjob.html">Rimjob</a></li>
													<li class="divider"></li>
							<li><a href="/Romanian.html">Romanian</a></li>
													<li class="divider"></li>
							<li><a href="/Russian.html">Russian</a></li>
													<li class="divider"></li>
							<li><a href="/Saggy Tits.html">Saggy Tits</a></li>
													<li class="divider"></li>
							<li><a href="/Secretaries.html">Secretaries</a></li>
													<li class="divider"></li>
							<li><a href="/Serbian.html">Serbian</a></li>
													<li class="divider"></li>
							<li><a href="/Sex Toys.html">Sex Toys</a></li>
													<li class="divider"></li>
							<li><a href="/Sex Toys (Gay).html">Sex Toys (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Sex Toys (Shemale).html">Sex Toys (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Shemale Fucks Girl (Shemale).html">Shemale Fucks Girl (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Shemale Fucks Guy (Shemale).html">Shemale Fucks Guy (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Shemale Fucks Shemale (Shemale).html">Shemale Fucks Shemale (Shemale)</a></li>
							<li class="divider"></li>
						</ul>
					</div>
					<div class="col-md-3 text-center" style="width: 200px !important;">
						<ul class="list-unstyled">
							<li><a href="/Shemales (Shemale).html">Shemales (Shemale)</a></li>
							<li class="divider"></li>
							<li><a href="/Showers.html">Showers</a></li>
													<li class="divider"></li>
							<li><a href="/Singaporean.html">Singaporean</a></li>
													<li class="divider"></li>
							<li><a href="/Skinny.html">Skinny</a></li>
													<li class="divider"></li>
							<li><a href="/Slave.html">Slave</a></li>
													<li class="divider"></li>
							<li><a href="/Slovakian.html">Slovakian</a></li>
													<li class="divider"></li>
							<li><a href="/Slovenian.html">Slovenian</a></li>
													<li class="divider"></li>
							<li><a href="/Small Cocks (Gay).html">Small Cocks (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Small Tits.html">Small Tits</a></li>
													<li class="divider"></li>
							<li><a href="/Small Tits Shemales (Shemale).html">Small Tits Shemales (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Softcore.html">Softcore</a></li>
													<li class="divider"></li>
							<li><a href="/Solo  (Shemale).html">Solo  (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/South African.html">South African</a></li>
													<li class="divider"></li>
							<li><a href="/Spandex.html">Spandex</a></li>
													<li class="divider"></li>
							<li><a href="/Spanish.html">Spanish</a></li>
													<li class="divider"></li>
							<li><a href="/Spanking.html">Spanking</a></li>
													<li class="divider"></li>
							<li><a href="/Spanking (Gay).html">Spanking (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Sports.html">Sports</a></li>
													<li class="divider"></li>
							<li><a href="/Squirting.html">Squirting</a></li>
													<li class="divider"></li>
							<li><a href="/Sri Lankan.html">Sri Lankan</a></li>
													<li class="divider"></li>
							<li><a href="/Stockings.html">Stockings</a></li>
													<li class="divider"></li>
							<li><a href="/Stockings (Shemale).html">Stockings (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Strapon.html">Strapon</a></li>
													<li class="divider"></li>
							<li><a href="/Striptease (Gay).html">Striptease (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Striptease.html">Striptease</a></li>
													<li class="divider"></li>
							<li><a href="/Swedish.html">Swedish</a></li>
													<li class="divider"></li>
							<li><a href="/Swingers.html">Swingers</a></li>
													<li class="divider"></li>
							<li><a href="/Swiss.html">Swiss</a></li>
													<li class="divider"></li>
							<li><a href="/Sybian.html">Sybian</a></li>
													<li class="divider"></li>
							<li><a href="/Tattoos.html">Tattoos</a></li>
													<li class="divider"></li>
							<li><a href="/Taxi.html">Taxi</a></li>
													<li class="divider"></li>
							<li><a href="/Teacher.html">Teacher</a></li>
													<li class="divider"></li>
							<li><a href="/Teens.html">Teens</a></li>
													<li class="divider"></li>
							<li><a href="/Teens  (Shemale).html">Teens  (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Thai.html">Thai</a></li>
													<li class="divider"></li>
							<li><a href="/Threesomes.html">Threesomes</a></li>
													<li class="divider"></li>
							<li><a href="/Tits.html">Tits</a></li>
													<li class="divider"></li>
							<li><a href="/Titty Fucking.html">Titty Fucking</a></li>
													<li class="divider"></li>
							<li><a href="/Top Rated.html">Top Rated</a></li>
													<li class="divider"></li>
							<li><a href="/Tunisian.html">Tunisian</a></li>
													<li class="divider"></li>
							<li><a href="/Turkish.html">Turkish</a></li>
													<li class="divider"></li>
							<li><a href="/Twinks (Gay).html">Twinks (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Ukrainian.html">Ukrainian</a></li>
													<li class="divider"></li>
							<li><a href="/Upskirts.html">Upskirts</a></li>
													<li class="divider"></li>
							<li><a href="/Valentine's Day.html">Valentine's Day</a></li>
													<li class="divider"></li>
							<li><a href="/Venezuelan.html">Venezuelan</a></li>
													<li class="divider"></li>
							<li><a href="/Vibrator.html">Vibrator</a></li>
													<li class="divider"></li>
							<li><a href="/Vietnamese.html">Vietnamese</a></li>
													<li class="divider"></li>
							<li><a href="/Vintage.html">Vintage</a></li>
													<li class="divider"></li>
							<li><a href="/Vintage (Gay).html">Vintage (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Vintage (Shemale).html">Vintage (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Voyeur.html">Voyeur</a></li>
													<li class="divider"></li>
							<li><a href="/Voyeur (Gay).html">Voyeur (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/VR Porn.html">VR Porn</a></li>
													<li class="divider"></li>
							<li><a href="/Webcams.html">Webcams</a></li>
													<li class="divider"></li>
							<li><a href="/Webcams (Gay).html">Webcams (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Webcams (Shemale).html">Webcams (Shemale)</a></li>
													<li class="divider"></li>
							<li><a href="/Whipping.html">Whipping</a></li>
													<li class="divider"></li>
							<li><a href="/Wife.html">Wife</a></li>
													<li class="divider"></li>
							<li><a href="/Wife Sharing.html">Wife Sharing</a></li>
													<li class="divider"></li>
							<li><a href="/Wrestling (Gay).html">Wrestling (Gay)</a></li>
													<li class="divider"></li>
							<li><a href="/Xmas.html">Xmas</a></li>
													<li class="divider"></li>
							<li><a href="/Yoga.html">Yoga</a></li>
								<li class="divider"></li>
						</ul>
					</div>
			</div><!-- .row .dropdown-menu-->
			</div><!-- .dropdown -->
	</div><!-- .container -->
</nav>
<div class="container-fluid" id="container1">
					<div class="row" id="row1">
'''
for i in range(len(names)):
	names[i]=names[i][:-4]
	individual_page=open(names[i]+".html","w")
	individual_page.write(page)
	individual_page.write('''<div class="col-md-offset-2 col-md-6 col-xs-12 col-sm-12" id="i-div"><h4>'''+names[i]+'''</h4><iframe src="'''+links[i]+'''" frameborder=0 marginwidth=0 marginheight=0 scrolling=no width=640 height=360 allowfullscreen></iframe>
					</div>
					<div class="col-md-6 col-xs-6 col-sm-6" style="height:400px; width: 400px;margin-top: 20px;">ADVERTISE HERE<img src="https://www.placehold.it/300x300"></div>
					
				</div><!-- .row1 -->
				<div class="row">
					<div class="col-md-offset-1 col-md-4 col-xs-offset-1 col-sm-offset-1 col-xs-4 col-sm-4" style="height:200px; width: 300px; background-color: lightgrey;margin-top:10px;"><strong>ADVERTISE HERE</strong></div>
					<div class="col-md-offset-1 col-md-4 col-xs-offset-1 col-sm-offset-1 col-xs-4 col-sm-4" style="height:200px; margin-top:10px; width: 300px; background-color: lightgrey;"><strong>ADVERTISE HERE</strong></div>
					<div class="col-md-offset-1 col-md-4 col-xs-offset-1 col-sm-offset-1 col-xs-4 col-sm-4" style="height:200px; width: 300px; background-color: lightgrey;margin-top:10px;"><strong>ADVERTISE HERE</strong></div>
				</div></div><!--.container-->
		</body>
		</html>''')

	individual_page.close()