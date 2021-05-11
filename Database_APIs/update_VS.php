<?php
//Update vital signs for specififc patient based on id

require "DataBase.php";
$db = new DataBase();

$data = json_decode(file_get_contents('php://input'), true);
#print_r($data);
    if ($db->dbConnect()) {
        if ($db->update_vs($data['patientid'] ,$data['temprature'],$data['spo'],$data['heartrate'])) {
            echo 'successfully updated';
        } else echo "editting Failed";
    } else echo "Error: Database connection";
?>