<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

include_once '../config/database.php';
include_once '../models/translator.php';

$database = new Database();
$db = $database->getConnection();

$translator = new Translator($db);

$stmt = $translator->read();
$num = $stmt->rowCount();

if($num>0){
    $translators_arr = array();
    $translators_arr["records"] = array();
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)){
        extract($row);
        $translator_item = array(
            "id" => $id,
            "name" => $name,
            "api_key" => $api_key, 
            "consumption" => $consumption,
            "limit" => $limit,
            "created_at" => $created_at,
            "last_update" => $last_update
        );
        array_push($translators_arr["records"], $translator_item);
    }
    echo json_encode($translators_arr);
}else{
    echo json_encode(
        array("message" => "Nessun Traduttore Trovato.")
    );
}
?>