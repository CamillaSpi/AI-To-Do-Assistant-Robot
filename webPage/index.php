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
        <table class='styled-table' id='table'>";
        }
if (isset($_POST['ajax'])) {
    
    // $data = json_decode(stripslashes($_POST['chosenOption']));
    // now here i've the matrix contains all the row in the html page 
    $db = new sqlite3('../src/rasa_ros/Cogrob_rasa_midterm/data.db');
    $results = $db->query($_POST['query']);
    $resultsCount = $db->query($_POST['query']);
    $data = $_REQUEST['chosenOptionArray'];
    // here I scroll the row fetchend in the db
    $count=0;
    $operation=False;
    $inverseOperation=False;
    $satisfied=False;
    $index=0;
    $id_index = '0';
    $numOldRow = $_POST['numOldRow'];
    $numActualRow = 0;
    $newCheck = False;
    while ($row = $resultsCount->fetchArray()) {
        ++$numActualRow;
    }
    if (($numOldRow == 1 && $numOldRow >= $numActualRow) || $numOldRow == 0){
        echo "refresh ".$numOldRow.' '.$numActualRow; 
    }else{

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
            ##REMOVE STATEMENT
            if($numOldRow > $numActualRow){
                if ($data[$count][0]!=$row[$id_index]){
                    echo "hidden ".$data[$count][0];
                    $satisfied=True;
                    break;
                }
            }
            ##ADD STATEMENT 
            if($numOldRow < $numActualRow){
                if ($data[$count][0]!=$row[$id_index]){
                    $id=$row[$id_index];
                    $toAdd=$count-1;
                    
                    echo "<tr id=$id class='active-row'>
                    <td id='index' hidden>".$data[$toAdd][0]."</td>";
                    for($k=1;$k<$length;++$k){
                        if($row[$k] == $row['deadline']  && $row[$k] != "0"){
                            $tmp = explode('T',$row['4']); 
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
            }
            ##MODIFY STATEMENT
            if($numOldRow == $numActualRow){
                $numDataRow = count($data[$count]);
                if($numDataRow > 3){
                    if($data[$count][$numDataRow-2] !=  $row['completed'] || $data[$count][$numDataRow-1] != $row['reminder']){
                        $newCheck = True;
                    }else{
                        $newCheck = False;
                    }
                    
                }
                if($newCheck){
                    echo "hidden ".$data[$count][0]." restart ".$data[$count][$numDataRow-2].$row['completed'].$data[$count][$numDataRow-1].$row['reminder'];
                    break;
                }
                if($operation == True && $idToCheck == $data[$count][0]){
                    echo "hidden ".$idSus." restart";
                    break;
                }else if($operation == True && $idToCheck != $data[$count][0]){
                    $operation = False;
                    $inverseOperation = True;
                }
                if ($data[$count][0]!=$row[$id_index]){
                    $operation = True;
                    $idSus = $data[$count][0];
                    $idToCheck = $row[$id_index];
                    if($count == $numActualRow-1){
                        echo "hidden ".$data[$count][0]." restart";
                        break;
                    }
                }
                if(($numOldRow == 2 && $count == $numActualRow-1) && $operation == True){
                    if($data[$count][0]==$row[$id_index]){
                        echo "hidden ".$data[$count-1][0]." restart";
                        break;
                    }
                }
                if ($inverseOperation == True){
                    if($data[$count][0]==$row[$id_index]){
                        echo "hidden ".$data[$count-1][0]." restart";
                        break;
                    }else if($count == $numActualRow-1){
                        echo "hidden ".$data[$count][0]." restart";
                        break;
                    }
                }
            }
            ++$count;
        }
    }

    if($numOldRow > $numActualRow && $satisfied==False){
        echo "hidden ".$data[$count][0];
    }
} else {

    $db = new sqlite3('../src/rasa_ros/Cogrob_rasa_midterm/data.db');
    $resultsCount = $db->query($_GET['query']);
    $results = $db->query($_GET['query']);
    $id_index = '0'; 
    $index=0;
    $count = 0;
    while ($row = $resultsCount->fetchArray()) {
        ++$count;
    }
    echo "<button type='button' id='numOldRows' hidden>".$count."</button>";
    echo "<button type='button' id='queryDone' hidden>".$_GET['query']."</button>";
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
            
            $index = 1;
        }
        $tmp = explode('T',$row['4']); 
        $id=$row[$id_index];
        #for to create table from db
        echo " <tr id=$id class='active-row'>";
        for($k=1;$k<$length;++$k){
            if($row[$k] == $row['deadline'] && $row[$k] != "0"){
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
        var numRow = document.getElementById('numOldRows').innerText;
        var matrix = []; 
        var queryString = document.getElementById('queryDone').innerText;
        if(numRow>0){
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
        }
        
        $.ajax({
            method: 'POST',
            url: 'index.php',
            dataType: 'html',   //expect html to be returned    
            data: { ajax: 'true', chosenOptionArray: matrix, query: queryString, numOldRow: numRow}, 
            success: function(response){   
                html = $.parseHTML( response );
                array = html[0].textContent.split(' ');
                if(array[0]=='refresh'){
                    
                    var reload = document.getElementById('refresh');
                    reload.click();
                }else{
                    if(array[0]=='hidden'){
                        row = document.getElementById(array[1]);
                        if(array[2] == 'restart'){
                            $(row).remove();
                        }else{
                            $(row).hide(1000).delay(2000).queue(function() { $(this).remove(); });
                        }                    
                        var tooOld = document.getElementById('numOldRows').innerText;
                        
                        document.getElementById('numOldRows').innerText=parseInt(tooOld)-1;
                        if(array[2] == 'restart'){
                            
                            document.getElementById('clickMe').click();
                        }
                    }else if(array[0]=='select'){}else{
                        
                        var tooOld = document.getElementById('numOldRows').innerText;
                        document.getElementById('numOldRows').innerText=parseInt(tooOld)+1;
                        var idWhereAppend = html[0].childNodes[1].textContent;
                        
                        
                        htmlString=response.split('</tr>')[0];
                        htmlString = htmlString.concat('</tr>');
                        
                        if(idWhereAppend == ''){
                            var table = document.getElementById('responsecontainer');
                            
                            var allRows = table.childNodes;
                            for(var i = 0; i < allRows.length; i++){
                                idWhereAppend=table.childNodes[i].id;
                                if(idWhereAppend === undefined){
                                    
                                }else{
                                    break;
                                }
                            }
                            var idWhereAppend = '#'.concat(idWhereAppend);
                            $(htmlString).insertBefore(idWhereAppend).hide().fadeIn(1000);
                        }else{
                            var idWhereAppend = '#'.concat(idWhereAppend);
                            $(htmlString).insertAfter(idWhereAppend).hide().fadeIn(1000); 
                        }
                        
                        
                    }         
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
        var numRow = document.getElementById('numOldRows').innerText;
        text = document.URL;
        
        if (text.includes('possessions') && numRow > 1){
            var inject = document.getElementById('clickMe');
            inject.click();
        } else{
            $.ajax({
        
                method: 'GET',
                url: 'index.php',
                dataType: 'html',   //expect html to be returned    
                data: {query: queryString}, 
                success: function(response){  
                    
                    $('body').html(response);  
                }
            });
        }
        
    });
</script>
";
}?>
