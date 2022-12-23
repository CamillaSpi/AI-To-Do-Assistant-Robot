<?php
if (isset($_POST['ajax'])) {} else {
    echo 
    "<html>
    <head>
        <link rel='stylesheet' href='index.css'>
        <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js'></script>
        
    </head>
    <body>
        <button type='button' id='clickMe' hidden>CLICK ME TO MODIFY</button>
        <button type='button' id='refresh' hidden>CLICK ME TO SUBSTITUTE PAGE</button>
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
            $index=0;
            $id_index = '0';
            while ($row = $results->fetchArray()) {
                if($index==0){
                    $keys = array_keys($row);
                    $keyLen = sizeof($keys);
                    for($k=0;$k<$keyLen;++$k){
                        if($keys[$k]=="ID"){
                            if($k=='1'){
                                $id_index = '1'; 
                            }
                        }
                    }
                    $index = 1;
                }
                $length = sizeof($row)/2;
                if($count < sizeof($data)){
                    if($operation==True){
                        //echo "confronta:  ".$data[$count][0];
                        //echo "con questo:  ".$row['id_unfolding'];
                        //modify operation
                        if ($data[$count][0]==$row[$id_index]){
                            
                        $str.="modify ".$data[$count-1][0]." to ".$value[0];
                        for($k=1;$k<$length;++$k){
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
                    if ($data[$count][0]!=$row[$id_index]){
                        $operation=True;
                        $value[0]=$row[$id_index];
                        for($k=2;$k<$length;++$k){
                            $value[$k-1]=$row[$k];
                        }
                    }
                }else{
                    $id=$row[$id_index];
                    echo " <tr id=$id class='active-row'>";
                    for($k=1;$k<$length;++$k){
                        if($row[$k] == $row['deadline']){
                            echo "<td>"; 
                            if(empty($tmp)){
                                echo "{$row[$k]}";
                            }else
                                $tmpSub= substr($tmp[1], 0, 5);
                                echo "{$tmp[0]} {$tmpSub}";
                            echo "</td>";
                        }else if($keys[1+$k*2]=="ID"){
                        
                        }else{
                            echo "<td>{$row[$k]}</td>";
                        }
                        
                    }
                    echo "</tr>";   
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
                for($k=1;$k<$length;++$k){
                    
                    if($data[$count-1][$k]!=$value[$k]){
                        $str=$str." ".$k." ".$value[$k]." ";
                    }
                }
                echo $str;
                    
                //}
                $operation=False;
            }
        } else {

            $db = new sqlite3('../src/rasa_ros/Cogrob_rasa_midterm/data.db');
            $results = $db->query($_GET['query']);
            $id_index = '0'; 
            $index=0;
            while ($row = $results->fetchArray()) {
                $length = sizeof($row)/2;
                $keys = array_keys($row);
                $keyLen = sizeof($keys);
                if($index==0){
                    echo "
                    <thead>
                        <tr>";
                    for($k=0;$k<$keyLen;++$k){
                        if($keys[$k]=="ID"){
                            if($k=='1'){
                                $id_index = '1'; 
                            }
                        }else if($keys[$k]=="id_unfolding"){
                        }
                        else if($keys[$k]=="id_possession"){
                        }else{
                            if (is_numeric($keys[$k])){}else{
                                echo "<th>$keys[$k]</th>";
                            }
                        }
                    }
                    echo "</tr>
                    </thead>
                    <tbody id='responsecontainer'>";
                    echo "<button type='button' id='queryDone' hidden>".$_GET['query']."</button>";
                    $index = 1;
                }
                $tmp = explode('T',$row['4']); 
                $id=$row[$id_index];
                #for to create table from db
                echo " <tr id=$id class='active-row'>";
                for($k=1;$k<$length;++$k){
                    if($row[$k] == $row['deadline']){
                        echo "<td>"; 
                        if(empty($row['deadline'])){
                            echo "{$row[$k]}";
                        }else
                            $tmpSub= substr($tmp[1], 0, 5);
                            echo "{$tmp[0]} {$tmpSub}";
                        echo "</td>";
                    }else if($keys[1+$k*2]=="ID"){
                        
                    }else{
                        echo "<td>{$row[$k]}</td>";
                    }
                    
                }
                echo "</tr>";                    
                $id++;
            } 
        echo "
            </tbody>
        </table>
    </body>
</html>";
echo "<script type='text/javascript'>
    $('table tr').hide();
    $('table tr').each(function(index){
        $(this).delay(index*500).show(1000);
    });

    $('#clickMe').click(function(){
        var j = 0;
        var chosenOption= $('#1');
        var matrix = []; 
        var queryString = document.getElementById('queryDone').innerText;
        $( 'tr' ).each( function( index, element ){
            if(element.hidden==false){
                if(j > 0){
                    matrix.push([]);
                    for ( var i = 0; i < element.cells.length; i++ ) {
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
                alert(html);
                array = html[0].textContent.split(' ');
                if(array[0]=='hidden'){
                    row = document.getElementById(array[1]);
                    $(row).hide(1000);
                }else if(array[0]=='modify'){
                    row = document.getElementById(array[1]);
                    row.id = array[3];
                    childs = row.children;
                    var i=4;
                    while(array.length != i){
                        (childs[array[i]-1]).innerHTML = array[i+1];
                        i=i+3;
                    }
                    $(row).hide().fadeIn(1000);
                }else if(array[0]=='select'){}else{
                    $(response).appendTo('#responsecontainer').hide().fadeIn(1000); 
                }                
            }
        });
    });
</script>
";
echo "
<script type='text/javascript'>
    
    $('#refresh').click(function(){  
        var queryString = document.getElementById('queryDone').innerText;

        $.ajax({
        
            method: 'GET',
            url: 'index.php',
            dataType: 'html',   //expect html to be returned    
            data: {query: queryString}, 
            success: function(response){   
                $('body').html(response);  
            }
        });
    });
</script>
";
}?>
