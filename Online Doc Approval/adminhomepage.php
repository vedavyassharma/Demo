<?php
session_start();
include("connectdoc.php");
include("connect.php");

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
                        <a href="adminoverview.php" type="button" id="overview_link">Overview</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a href="appreq.php" type="button" id="appreq_link">Approval Requests</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a href="approved.php" type="button" id="approved_link">Approved Projects</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a href="disapproved.php" type="button" id="disapproved_link">Disapproved Projects</a>
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
            
        </div>
    </div>