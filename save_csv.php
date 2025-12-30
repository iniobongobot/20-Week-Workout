<?php
// Only allow POST requests
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = $_POST['csv_data'];
    
    // Safety check: ensure we actually got data
    if (!empty($data)) {
        // Write the data to workout.csv (this overwrites the file)
        if (file_put_contents('workoutplan.csv', $data)) {
            http_response_code(200);
            echo "Success";
        } else {
            http_response_code(500);
            echo "Error: Could not write to file. Check file permissions.";
        }
    }
}
?>