<?php 

include 'connect.php';



if(isset($_POST['signInn'])){
   $email=$_POST['email'];
   $password=$_POST['password'];
   $password=($password) ;
   
   $sql="SELECT * FROM admins WHERE email='$email' and password='$password'";
   $result=$conn->query($sql);
   if($result->num_rows>0){
    session_start();
    $row=$result->fetch_assoc();
    $_SESSION['email']=$row['email'];
    header("Location: adminhomepage.php");
    exit();
   }
   else{
    echo "Not Found, Incorrect Email or Password";
   }

}
?>