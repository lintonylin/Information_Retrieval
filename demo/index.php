<?php

?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">


    <!-- 引入 ECharts 文件 -->
    <script src="https://cdn.staticfile.org/echarts/4.7.0/echarts.min.js"></script>
	<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css">
	<style type="text/css">.form{
		margin-left:5%;
		margin-top:7%;
		width: 400px;
	}.test {
		height: 200px;
		width: 300px;
	}
 </style>
</head>
</html>

<body>
    <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
	<div>
<form class="form" action="" method="post" >
	<div><h3>Insert Text</h3></div>
	<textarea class="test"  name ="text"></textarea><br/>

	  <button type="submit" class="btn btn-outline-dark mb-2" name="Start">Start</button>
</form>
</div>

 <?php
if (isset($_POST['Start'])) {
  include("123.php");
}
?>
</body>
</html>
