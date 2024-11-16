<?php

$host="localhost:4306";
$user="root";
$pass="admin";
$db="fileuploaddownload";
$conn=new mysqli($host,$user,$pass,$db);
if($conn->connect_error){
    echo "Failed to connect DB".$conn->connect_error;
}
?>