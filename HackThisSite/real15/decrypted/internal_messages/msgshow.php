<?php
/*-- called by internal_messages.php --*/
session_start();


include("showmessages.inc.php"); /* under construction, I will devide this into different files soon */

$msg_password = $_POST['password'];
$msg_username = $_POST['username'];
$filename = "msgpasswords.txt";

include("msgauth.php");


showmessage($msg_username);


?>
