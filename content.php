<?php
    require 'headers/helperFunctions.php';

    // each statement must end in semicolon
    echo "alfa\n";
    echo "<strong>beta</strong>";
    echo "<h1>gamma</h1>";
    echo "<p>First program!</p>";

    //variables
    $name = 'John';
    $age = 25;
    echo $name;

    //constants
    define("MSG", "<p>Hello other world!</p>");
    echo MSG;
    //constant with case insensitive name
    define("MSG2", 52018, true);
    echo MSG2;

    //Data Types
    $string1 = "hello world";
    $string2 = "hello world 2";
    $negative_number = -42;
    $valxa = true;
    //concatenation .
    echo "<p>".$string1.' '.$string2."\r\n".$negative_number."</p>";
    

    $str = "10";
    $int = 20;
    $sum = $str + $int;
    echo($sum);

    //variable scopes + functions
    $name = "David";
    function getName() {
         global $name;
         echo $name;
    }

    getName();

    echo nl2br("test");

    //variable variable
    $aa = "aaa";
    $aaa = "test";

    echo $$aa."\r\n";

    //arrays
    $names = array("David", "Amy", "John");
    echo $names[0];

    $myArray[0] = "John";
    $myArray[1] = "<strong>PHP</strong>";
    $myArray[2] = 21;

    echo "$myArray[0] is $myArray[2] and knows $myArray[1]";

    //associative arrays
    $people = array("David"=>"27", "Amy"=>"21", "John"=>"42");
    //alternative
    $people['David'] = "27";
    echo $people["David"];

    //multi size arrays and combinations
    $peoplex = array(
        'online'=>array('David', "Amy"),
        "offline"=>array("John", 'Rob', 'Jack'),
        'away'=>array('Arthur', 'Daniel')
    ); //very important close statement

    echo $peoplex['online'][0];

    //control statements
    $age = 10;
    if($age > 18)
    {
        echo "Major";
    }
    elseif ($age < 2)
    {
        echo "small child";
    }
    else
    {
        echo "minor";
    }

    //while 
    $i = 0;
    while($i < 3)
    {
        echo $i.$nl;
        $i++;
    }

    // do while
    do {
        echo "alfa".$nl;
        $i--;
    } while ($i > 0);

    //for
    for($i=0;$i<3;$i++)
    {
        echo "value of i:$i$nl";
    }

    //foreach
    $names = array("John", "David", "Amy");
    foreach ($names as $name) {
        echo $name.$nl;
    }

    //switch
    $today = "Sunday";
    switch ($today) {
        case 'Monday':
            echo "It's Monday!$nl";
            break;
        
        case 'Sunday':
            echo "It's Sunday!$nl";
            break;


        default:
            echo "It's not a day of the week someohow!$nl";
            break;
    };

    //functions
    sayHello();
    $value3 = 3;
    $value4 = 4;
    $returnValue = addition($value3, $value4);
    echo "Sum of $value3 and $value4 is :$returnValue$nl";

    //predefined variables
    // echo $_SERVER['SCRIPT_NAME'].$nl;
    // showSystemSettings();

    function showAppleImage()
    {
        $dir = getImageFolderLocation();
        $file = "apple.jpg";
        
        // echo $dir.'/'.$file;

        echo '<img src="'.$dir.'/'.$file.'" alt="'.$file.'">';
    }

    showAppleImage();
?>

<form action="form.php" method="post">
    <p>Name: <input type="text" name="name" /></p>
    <p>Age: <input type="text" name="age" /></p>
    <p><input type="submit" name="submit" value="Submit" /></p>
  </form>