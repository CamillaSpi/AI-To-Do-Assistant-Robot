<?php 
// $url = 'http://localhost:80/webPage/';
// $query = $_GET['query'];
// $data = array('query' => $query);

// // use key 'http' even if you send the request to https://...
// $options = array(
//     'http' => array(
//         'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
//         'method'  => 'POST',
//         'content' => http_build_query($data)
//     )
// );
// $context  = stream_context_create($options);
// $result = file_get_contents($url, false, $context);
// if ($result === FALSE) { /* Handle error */ }

// echo($result);
?>



<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['ajax'])) {} else {
        echo 
        "<html>
        <head>
            <link rel='stylesheet' href='index.css'>
            <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js'></script>
            
        </head>
        <body>
            <button type='button' id='clickMe' hidden>CLICK ME TO RUN PHP</button>
            <table class='styled-table'>";
            }if (isset($_POST['ajax'])) {
                
                // $data = json_decode(stripslashes($_POST['chosenOption']));
                // now here i've the matrix contains all the row in the html page 
                $db = new sqlite3('../src/rasa_ros/Cogrob_rasa_midterm/data.db');
                $results = $db->query($_POST['query']);
                $data = $_REQUEST['chosenOptionArray'];
                // here I scroll the row fetchend in the db
                $count=0;
                $operation=False;
                $satisfied=False;
                while ($row = $results->fetchArray()) {
                    
                    if($count < sizeof($data)){
                        if($operation==True){
                            //echo "confronta:  ".$data[$count][0];
                            //echo "con questo:  ".$row['id_unfolding'];
                            //modify operation
                            if ($data[$count][0]==$row['id_unfolding']){
                                
                            $str.="modify ".$data[$count-1][0]." to ".$value[0];
                            for($k=1;$k<6;++$k){
                                if($data[$count-1][$k]!=$value[$k]){
                                    $str=$str." ".$k." ".$value[$k]." ";
                                }
                            }
                            $satisfied=True;
                            echo $str;
                            break;
                            }
                            //remove operation
                            else{
                                $satisfied=True;
                                echo "hidden ".$data[$count-1][0];
                                break;
                            }
                            $operation=False;
                        }
                        if ($data[$count][0]!=$row['id_unfolding']){
                            $operation=True;
                            $value[0]=$row['id_unfolding'];
                            $value[1]=$row['activity'];
                            $value[2]=$row['category'];
                            $value[3]=$row['deadline'];
                            $value[4]=$row['completed'];
                            $value[5]=$row['reminder'];
                        }
                    }else{
                        $id=$row['id_unfolding'];
                        echo " 
                            <tr id=$id class='active-row'>
                                <td>{$row['activity']}</td>
                                <td>{$row['category']}</td>
                                <td>"; 
                                if(empty($tmp)){
                                    echo "{$row['deadline']}";
                                }else
                                    $tmpSub= substr($tmp[1], 0, 5);
                                    echo "{$tmp[0]} {$tmpSub}";
                                echo "</td>
                                <td>{$row['completed']}</td>
                                <td>{$row['reminder']}</td>
                            </tr>
                        ";
                        break;
                        }
                    ++$count;
                }
                if($count < sizeof($data) && $satisfied==False){
                    
                    if($operation==True){
                        echo "hidden ".$data[$count-1][0];
                    }else{
                        echo "hidden ".$data[$count][0];
                    }
                }
                else if($operation==True && $satisfied==False){
                    // if($count+1 <= sizeof($data)){
                    //     //echo "hidden id=".$data[$count-1][0];
                    // }
                    //else{
                    $str.="modify ".$data[$count-1][0]." to ".$value[0];;
                    for($k=1;$k<6;++$k){
                        
                        if($data[$count-1][$k]!=$value[$k]){
                            $str=$str." ".$k." ".$value[$k]." ";
                        }
                    }
                    echo $str;
                        
                    //}
                    $operation=False;
                }
            } else {
            ?>
            <thead>
                <tr>
                    <th>activity</th>
                    <th>category</th>
                    <th>deadline</th>
                    <th>completed</th>
                    <th>reminder</th>
                </tr>
            </thead>
            <tbody id="responsecontainer">
            <?php
    
                $db = new sqlite3('../src/rasa_ros/Cogrob_rasa_midterm/data.db');
                $results = $db->query($_POST['query']);
                echo "<button type='button' id='queryDone' hidden>".$_POST['query']."</button>";
                while ($row = $results->fetchArray()) {
                    $tmp = explode('T',$row['deadline']); 
                    $id=$row['id_unfolding'];
                    echo " 
                        <tr id=$id class='active-row'>
                            <td>{$row['activity']}</td>
                            <td>{$row['category']}</td>
                            <td>"; 
                            if(empty($tmp)){
                                echo "{$row['deadline']}";
                            }else
                                $tmpSub= substr($tmp[1], 0, 5);
                                echo "{$tmp[0]} {$tmpSub}";
                            echo "</td>
                            <td>{$row['completed']}</td>
                            <td>{$row['reminder']}</td>
                        </tr>
                    ";
                    $id++;
                } 
            echo "
                </tbody>
            </table>
        </body>
    </html>";
    echo "<script type='text/javascript'>
        $('#clickMe').click(function(){
            var j = 0;
            var chosenOption= $('#1');
            var matrix = []; 
            var queryString = document.getElementById('queryDone').innerText;
            $( 'tr' ).each( function( index, element ){
                if(element.hidden==false){
                    if(j > 0){
                        matrix.push([]);
                        for ( var i = 0; i < 4; i++ ) {
                            if(i==0){
                                matrix[j-1].push(element.id);
                            }
                            matrix[j-1].push(element.cells[i].innerText);
                        }
                    }
                    j=j+1;
                }   
            });
            
            // alert($(chosenOption).serializeArray())
            // var jsonString = JSON.stringify($(chosenOption))
            $.ajax({
            
                method: 'POST',
                url: 'index.php',
                dataType: 'html',   //expect html to be returned    
                data: { ajax: 'true', chosenOptionArray: matrix, query: queryString}, 
                success: function(response){   
                    
                    html = $.parseHTML( response );
                    alert('sto per aggiornare');
                    array = html[0].textContent.split(' ');
                    if(array[0]=='hidden'){
                        row = document.getElementById(array[1]);
                        row.hidden = true;
                    }else if(array[0]=='modify'){
                        row = document.getElementById(array[1]);
                        row.id = array[3];
                        childs = row.children;
                        var i=4;
                        alert(i);
                        while(array.length != i){
                            (childs[array[i]-1]).innerHTML = array[i+1];
                            i=i+3;
                            alert(i);
                        }
                    }else if(array[0]=='select'){}else{
                        $('#responsecontainer').append(response); 
                    }                
                }
            });
        });
    </script>
    ";}
}else{
    
    echo "<form id='myForm' action='constructPOSTrequest.php' method='post'>";
    $query = $_GET['query'];
    echo '<input type="hidden" name=query value="'.$query.'">';
    echo "
        </form>
    <script type='text/javascript'>
        document.getElementById('myForm').submit();
    </script>";
}
?> 