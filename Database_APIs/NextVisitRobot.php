<?php
//Retrive if there is a visit schedualed now 

require "DataBase.php";
$db = new DataBase();
$data = json_decode(file_get_contents('php://input'), true);
    if ($db->dbConnect()) {
        if ($response = $db->istherenow($data['day'] , $data['time']) ) {
            echo  $response;
        } else echo $response;
    } else echo "Error: Database connection";
?>