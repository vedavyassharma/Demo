<?php
// Database connection details
$servername = "localhost:4306";
$username = "root";
$password = "admin";
$dbname = "wordtohtml";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
    $fileName = $_FILES['file']['name'];
    $fileSize = $_FILES['file']['size'];
    $fileType = $_FILES['file']['type'];
    $fileContent = file_get_contents($_FILES['file']['tmp_name']);

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO files (filename, filesize, filetype, filecontent) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("siss", $fileName, $fileSize, $fileType, $fileContent);

    if ($stmt->execute()) {
        echo "File uploaded successfully";
    } else {
        echo "Error uploading file: " . $stmt->error;
    }

    $stmt->close();
}

$conn->close();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Word Document</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 flex items-center justify-center h-screen">
    <div class="bg-white p-8 rounded shadow-md">
        <h2 class="text-2xl font-bold mb-4">Upload Word Document</h2>
        <form action="upload.php" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".docx" class="block w-full text-sm text-gray-500 
                file:mr-4 file:py-2 file:px-4
                file:rounded-full file:border-0
                file:text-sm file:font-semibold
                file:bg-blue-50 file:text-blue-700
                hover:file:bg-blue-100 mb-4">
            <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Upload</button>
        </form>
    </div>
</body>
</html>
