<!DOCTYPE html><!-- blog file for hariganesan.com--><html xmlns="http://www.w3.org/1999/xhtml"><head><!-- default header file--><meta name="keywords" content="Hari Ganesan video game software programming development blog portfolio website"><meta name="description" content="Hari Ganesan's website: a blog and portfolio of a software programmer"><meta http-equiv="content-type" content="text/html; charset=utf-8"><title>Hari Ganesan</title><link rel="shortcut icon" href="static/images/favicon.ico"><link href="http://fonts.googleapis.com/css?family=Kreon:400" rel="stylesheet" type="text/css"><link href="static/css/main.css" rel="stylesheet" type="text/css" media="screen"></head><body class="blue"><div id="header-wrapper"><div id="header" class="container"><div id="logo"><h1><a href="/">Hari Ganesan</a></h1></div><div id="menu"><ul><li><a href="/">Home</a></li><li><a href="portfolio">Portfolio</a></li><li class="current_page_item"></li><li><a href="about">About</a></li></ul></div></div></div><div id="wrapper"><div id="page" class="container"><div id="content"><div class="post">

<?
//check for sql injection attacks

$username="haji218_user";
$password="haji218_pass";
$database="haji218_blog";

mysql_connect(localhost, $username, $password);
@mysql_select_db($database) or die("Unable to select database");

$q1 = mysql_query("SELECT * FROM posts
					ORDER BY year DESC, month DESC, day DESC");
$numR = mysql_numrows($q1);

if (!($currPage=$_GET['page'])) {
	$currPage=1;
}

$prevPage=$currPage-1;
$nextPage=$currPage+1;


if (($beginPost=$numR-$currPage*5 + 1) < 1) // count correctly!
	$beginPost = 1;

$endPost=$numR-$currPage*5 + 5;

// no query was made
if(empty($_SERVER['QUERY_STRING'])) { 
	$query="SELECT * FROM posts WHERE post_id >= '$beginPost'
					ORDER BY year DESC, month DESC, day DESC";
} else {
   // use $_GET['page']
	$query="SELECT * FROM posts WHERE post_id >= '$beginPost' AND post_id <= '$endPost'
					ORDER BY year DESC, month DESC, day DESC";
}

$result=mysql_query($query);
$num=mysql_numrows($result);

$nextPageExists = ($beginPost != 1);

mysql_close();

for ($i=0; $i < $num; $i++) {
	$day = mysql_result($result, $i, "day");
	$month = mysql_result($result, $i, "month");
	$year = mysql_result($result, $i, "year");
	$entry = mysql_result($result, $i, "entry"); 
?>
<h3 class="title"> <? echo "$month/$day/$year"; ?> </h3>
<div class="entry"> <? echo "$entry"; ?> </div>
<?
// end for loop
}
?>
<div class="nav"><span "float:left">
<? if ($currPage > 1) { ?>
	<a href="blog?page=<?=$prevPage;?>">Previous</a>
<? } ?>
</span>
<span style="float:right">
<? if ($nextPageExists) { ?>
	<a href="blog?page=<?=$nextPage;?>">Next</a>
<? } ?>
</span>
</div>
</div><div style="clear: both;"> </div></div><!-- end #content--><div style="clear: both;"> </div></div><div id="push"></div></div><div id="footer"><p class="small">This website was created by... me! I'd like to thank the academy, as well as Node, Express, Jade...</p></div><!-- google analytics--><script>(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-41323771-1', 'hariganesan.com');
ga('send', 'pageview');</script></body></html>