<?php
session_start();
include("connectdoc.php");

// Fetch counts
$sql_pending = "SELECT COUNT(*) as count FROM files WHERE approval_status = 'pending'";
$sql_approved = "SELECT COUNT(*) as count FROM files WHERE approval_status = 'approved'";
$sql_rejected = "SELECT COUNT(*) as count FROM files WHERE approval_status = 'rejected'";

$result_pending = $conn->query($sql_pending)->fetch_assoc();
$result_approved = $conn->query($sql_approved)->fetch_assoc();
$result_rejected = $conn->query($sql_rejected)->fetch_assoc();
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
</head>
<body>
<div class="row" id="header">
    <div class="col-md-12">
        <div class="col-md-4" style="display: inline-block;">
            <h3>Online Document Approval</h3>
        </div>
        <div class="col-md-6" style="display: inline-block;text-align: right">
            <b>Email:</b> Test@gmail.com <span><b>Name: </b>Test User</span>
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
            <h2> Overview</h2>
            <div class="alert alert-info" role="alert">
                <p>Pending Documents: <?php echo $result_pending['count']; ?></p>
            </div>
            <div class="alert alert-success" role="alert">
                <p>Approved Documents: <?php echo $result_approved['count']; ?></p>
            </div>
            <div class="alert alert-danger" role="alert">
                <p>Rejected Documents: <?php echo $result_rejected['count']; ?></p>
            </div>
        </div>
    </div>
</div>
</body>
</html>
