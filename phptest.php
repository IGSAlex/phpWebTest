<html>
   
   <head>
      <title>Update a Record in MySQL Database</title>
   </head>
   
   <body>
      <?php 


$dbhost = 'localhost';
            $dbuser = 'phpadmin';
            $dbpass = 'phpadmin';

	$mysqli = new mysqli($dbhost, $dbuser, $dbpass, 'phptest');

		/* check connection */
		if (mysqli_connect_errno()) {
		    die('Could not connect: ' .  mysqli_connect_error());  
		    
		}

         if(isset($_POST['update']) || isset($_POST['delete']) || isset($_POST['deleteAll']) ) {
            
            
            $emp_id = $_POST['emp_id'];
            $emp_salary = $_POST['emp_salary'];

            

          
            	if(isset($_POST['update'])){
		
		$errormsg = validData($emp_id, $emp_salary);
		if ($errormsg != NULL ){
			die($errormsg);
		}

		$stmt = $mysqli->prepare("INSERT INTO employee (emp_id ,emp_salary ) VALUES (? , ?) ON DUPLICATE KEY UPDATE emp_id =?, emp_salary=? ");
		$stmt->bind_param('sdsd', $emp_id, $emp_salary, $emp_id, $emp_salary);
		$stmt->execute();

            	}else if(isset($_POST['deleteAll'])){
                    $stmt = $mysqli->prepare("TRUNCATE TABLE employee");
                    $stmt->execute();
                
		}else if(isset($_POST['delete'])){
			$errormsg = validData($emp_id, $emp_salary);
			if ($errormsg != NULL ){
				die($errormsg);
			}
                    $stmt = $mysqli->prepare("DELETE FROM employee WHERE emp_id = ? AND emp_salary = ?");
			$stmt->bind_param('sd', $emp_id, $emp_salary);
                    $stmt->execute();
                }
           
         }
 buildTable($mysqli);
$mysqli->close();
         ?>
            
               <form method = "post" action = "<?php $_PHP_SELF ?>">
                  <table width = "400" border =" 0" cellspacing = "1" 
                     cellpadding = "2">
                  
                     <tr>
                        <td width = "100">Employee ID</td>
                        <td><input name = "emp_id" type = "text" 
                           id = "emp_id"></td>
                     </tr>
                  
                     <tr>
                        <td width = "100">Employee Salary</td>
                        <td><input name = "emp_salary" type = "text" 
                           id = "emp_salary"></td>
                     </tr>
                  
                     <tr>
                        <td width = "100"> </td>
                        <td> </td>
                     </tr>
                  
                     <tr>
                        <td width = "100"> </td>
                        <td>
                           <input name = "update" type = "submit" 
                              id = "update" value = "Update">
                       
                           <input name = "delete" type = "submit" 
                              id = "delete" value = "Delete">

                           <input name = "deleteAll" type = "submit" 
                              id = "deleteAll" value = "Delete All">
                        </td>
                     </tr>
                  
                  </table>
               </form>
     
   </body>
</html>

<?php
function buildTable($mysqli){



$tableHTML= "<table border='1' > ";
$tableHTML= $tableHTML."<th>ID</th><th>Salary</th> ";
	$result  = $mysqli->query("Select * FROM  employee;");
	
	if ($result->num_rows > 0) {
	    // output data of each row
	    while($row = $result->fetch_assoc()) {
		$tableHTML = $tableHTML. "<tr> <td> ".$row["emp_id"]. "</td> <td> " . $row["emp_salary"] ."</td></tr>";
	    }
	} else {
	    $tableHTML = $tableHTML. "<tr> <td colspan='2' >0 results</td></tr>";
	}

$tableHTML= $tableHTML."</table>";
	echo $tableHTML;
}

function validData( $emp_id , $emp_salary ){
	if (strlen(trim($emp_id)) == 0 ){
                return "Please enter Empolyer ID.";
	}
        if (strlen(trim($emp_id)) >100 ){
                return "Empolyer ID too long.";
	}
	if (!is_numeric (trim($emp_salary))  ){
                return "Empolyer salary is not a number.";
        }
        return NULL;
}

?>


