<?php
    $nl = "<br />";

    function addition($number1, $number2)
    {       
        $answer = $number1 + $number2;
        return $answer;
    }

    function sayHello()
    {
        echo "<h3>Hello</h3>";
    }

    function showSystemSettings()
    {
        global $nl;
        echo $_SERVER['SCRIPT_NAME'].$nl;
        echo $_SERVER['HTTP_HOST'].$nl;
    }

    function getImageFolderLocation()
    {
        $temp = $_SERVER['HTTP_HOST'];
        return $temp.'/images';
    }
?>