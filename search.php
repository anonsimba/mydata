<?php 
$input=$_POST['searchbox'];
$input1='"' . $input . '"';
$cmd="sudo python /var/www/html/usersearch.py ".$input1;
shell_exec($cmd);
?>
