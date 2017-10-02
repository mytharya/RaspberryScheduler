<?php
    function addition($number1, $number2)
    {       
        $answer = $number1 + $number2;
        return $answer;
    }

    function sayHello()
    {
        echo "<h3>Hello</h3>";
    }

    function showFunctionLocation()
    {
        echo $_SERVER['SCRIPT_NAME'];
    }
?>