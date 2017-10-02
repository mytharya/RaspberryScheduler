<?
  $name = 'David';
  function getName() {
    global $name;
    echo $name;
  }
  getName();

?>
