<?php
/*  --- called by msgshow.php --- */


session_start();

if ($_SESSION['msgauth'][$msg_username] != "OK")
{
      
   if (strlen($msg_username)==0 || strlen($msg_password)==0 || strlen($filename)==0)
     die();
   
   $msg_password = addcslashes($msg_password, ".[(*$^+\|");
   $msg_username = addcslashes($msg_username, ".[(*$^+\|");
   
     
   $fp = @fopen("files/" . $filename, "r");
   if (!$fp) die(); 
   
   while(!feof($fp) && $_SESSION['msgauth'][$msg_username] != "OK") {
     $strLine = fgets($fp,200);
                                                      // line may have carriage return line feed ,
                                                      // only carriage return,  or none of them
     if (ereg($msg_username . ": " . $msg_password . "\r*\n*$", $strLine, $regs))
       $_SESSION['msgauth'][$msg_username] = "OK";
   }
   fclose($fp);

   if ($_SESSION['msgauth'][$msg_username] != "OK") die("wrong username/password!");
}

?>

