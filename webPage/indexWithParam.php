<?php
if (isset($_POST['ajax'])) {} else {
    echo 
    "<html>
    <head>
        <link rel='stylesheet' href='index.css'>
        <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js'></script>
        
    </head>
    <body>
        <button type='button' id='clickMe'>CLICK ME TO RUN PHP</button>
        <table class='styled-table'>";
        }if (isset($_POST['ajax'])) {
            echo "
            <tr class='active-row'>
                <td id='div1'>{$_POST['activity']}</td>
                <td>{$_POST['category']}</td>
                <td>"; 
                if(empty($tmp)){
                    echo "{$_POST['deadline']}";
                }else
                    $tmpSub= substr($tmp[1], 0, 5);
                    echo "{$tmp[0]} {$tmpSub}";
                echo "</td>
                <td>{$_POST['completed']}</td>
                <td>{$_POST['reminder']}</td>
            </tr>";
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

            $results = $db->query('select * from unfoldings');
            while ($row = $results->fetchArray()) {
                $tmp = explode('T',$row['deadline']); 
                echo " 
                    <tr class='active-row'>
                        <td id='div1'>{$row['activity']}</td>
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
            } 
        echo "
            </tbody>
        </table>
    </body>
</html>";}?>
<script type="text/javascript">
    var scriptString = 'THIS IS MY STRING';
    $('#clickMe').click(function(){
        $.ajax({
        method: 'POST',
        url: 'index.php',
        dataType: "html",   //expect html to be returned    
        data: { ajax: "true", activity: "play", category: "music", deadline: "tomorrow", completed: "false", reminder: "false"}, 
        success: function(response){                    
            $("#responsecontainer").append(response); 
        }
        });
    });
</script>
