<?php
$str = "Hello, world!";
$length = strlen($str);
$newstr = "";

for ($i = $length - 1; $i >= 0; $i--) {
  $newstr .= $str[$i];
}

echo $newstr;
?>