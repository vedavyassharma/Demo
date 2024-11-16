<?php
//database connection details

$db_host = "localhost:4306";
$db_user = "root";
$db_pass = "admin";
$db_name = "fileuploaddownload";

 $conn = new mysqli($db_host, $db_user, $db_pass, $db_name);


 if ($conn->connect_error) {
                    die("Connection failed: " . $conn->connect_error);
                }

 //Fetch the uploaded files from the database

 $sql = "SELECT *FROM files";
 $result = $conn->query($sql);

?>


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uploaded files</title>

    <script src="includes/jquery.js"></script>
    <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
    <script src="bootstrap/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="css/styles.css">

</head>
<body>
    <div class="row" id="header">
        <div class="col-md-12">
            <div class="col-md-4" style="display: inline-block;">
                <h3>Online Document Approval</h3>
            </div>
            <div class="col-md-6" style="display: inline-block;text-align: right">
                <b>Email:</b> Test@gmail.com
                <span><b>Name: </b>Test User</span>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-2" id="left_sidebar">
            <table class="table">
                
                <tr>
                    <td style="text-align: center;">
                        <a href="overview.php" type="button" id="overview_link">Overview</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a href="submit.php" type="button" id="submit_link">Submit Project</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a href="view.php" type="button" id="view_link">View Projects</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a href="status.php" type="button" id="status_link">Project Status</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a href="update.php" type="button" id="update_link">Update Project</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a href="logout.php" type="button" id="logout_link">Logout</a>
                    </td>
                </tr>
            </table>
        </div>
        <div class="col-md-10" id="right_sidebar">
        <div class="container mt-5">
        <h2>Uploaded Files</h2>
        <table class="table table-bordered table-striped">
            <thead>
                <tr>
                    <th>File Name</th>
                    <th>File Size</th>
                    <th>File Type</th>
                    <th>Download</th>
                </tr>
            </thead>
            <tbody>
                <?php
                // Display the uploaded files and download links
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        $file_path = "uploads/" . $row['filename'];
                        ?>
                        <tr>
                            <td><?php echo $row['filename']; ?></td>
                            <td><?php echo $row['filesize']; ?> bytes</td>
                            <td><?php echo $row['filetype']; ?></td>
                            <td><a href="<?php echo $file_path; ?>" class="btn btn-primary" download>Download</a></td>
                        </tr>
                        <?php
                    }
                } else {
                    ?>
                    <tr>
                        <td colspan="4">No files uploaded yet.</td>
                    </tr>
                    <?php
                }
                ?>
            </tbody>
        </table>
    </div>

        </div>
    </div>
