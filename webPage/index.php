<html>
    <head>
        <link rel="stylesheet" href="index.css">
    </head>
    <body>
        <table class="styled-table">
            <thead>
                <tr>
                    <th>activity</th>
                    <th>category</th>
                    <th>deadline</th>
                    <th>completed</th>
                    <th>reminder</th>
                </tr>
            </thead>
            <tbody>
            <?php
            $db = new sqlite3('../src/rasa_ros/Cogrob_rasa_midterm/data.db');

            $results = $db->query('select * from unfoldings');
            while ($row = $results->fetchArray()) {
                $tmp = explode('T',$row['deadline']); 
                echo " 
                    <tr class='active-row'>
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
            } 
                ?>
            </tbody>
        </table> 
        <?php
        ?>
    </body>

</html>
