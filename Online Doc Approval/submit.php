<?php
session_start();
include("connect.php");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Your form submission processing code here

    // Redirect to submit_document.php after processing the form
    header("Location: submit_document.php");
    exit; // Ensure no further code execution after redirection
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ODA</title>
    <script src="includes/jquery.js"></script>
    <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
    <script src="bootstrap/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="css/styles.css">
    
   
	<title>File upload and download</title>

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
        <form method="post" enctype="multipart/form-data" action="submit_document.php">
    <div class="row">

        <div class="col-md-10" id="right_sidebar">
            <div class="container mt-5">
                <h2>Upload a file</h2>
                <div class="mb-3">
                    <label for="file" class="forsm-label">Select file</label>
                    <input type="file" class="form-control" name="file" id="file">
                </div>
                <button type="submit" class="btn btn-primary">Upload file</button>
            </div>
        </div>
    </div>
</form>


<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Your form submission processing code here

    // Redirect to submit_document.php after processing the form
    header("Location: submit_document.php");
    exit; // Ensure no further code execution after redirection
}
?>

	</div>

        </div>
    </div>
