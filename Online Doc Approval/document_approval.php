<?php
// Database connection details
$db_host = "localhost:4306";
$db_user = "root";
$db_pass = "admin";
$db_name = "fileuploaddownload";
$conn = new mysqli($db_host, $db_user, $db_pass, $db_name);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $document_id = $_POST['document_id'];
    
    if (isset($_POST['approve'])) {
        $status = 'approved';
    } elseif (isset($_POST['reject'])) {
        $status = 'rejected';
    }

    $sql = "UPDATE files SET approval_status = '$status' WHERE id = $document_id";
    if ($conn->query($sql) === TRUE) {
        header("Location: appreq.php");
        exit();
    } else {
        echo "Error updating record: " . $conn->error;
    }
}

$conn->close();
?>
