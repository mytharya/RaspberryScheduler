<<html>
<<head>
<<title>Hello World!</title>
</head>
<<body>
<?php
    
    // use include when you want to continue in case it's not found
    include 'content.php';

    //use require to give a fatal error and stop
    require 'headers/header2.php'
?>
</body>
</html>