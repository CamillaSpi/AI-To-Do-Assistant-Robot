<?php
if ($_POST['brand']) {
    // Be sure to set up your SQL $conn variable here
    $conn = ...;
    $sql = "SELECT model FROM cars WHERE brand = '" . $_POST['brand'] . "'";
    $result = mysqli_query($conn, $sql);
    $data = []; // Save the data into an arbitrary array.
    while ($row = mysqli_fetch_assoc($result)) {
        $data[] = $row;
    }
    echo json_encode($data); // This will encode the data into a variable that JavaScript can decode.
}