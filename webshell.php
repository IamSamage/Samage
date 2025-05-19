<?php
  $cmd = "ls ".escapeshellcmd($_GET['filename'])." 2>&1";
  system($cmd);
?>
