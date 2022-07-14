<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
include_once '../config/database.php';
include_once '../models/translator_language.php';
$database = new Database();
$db = $database->getConnection();

$translator_language = new TranslatorLanguage($db);

$stmt = $translator_language->read();
$num = $stmt->rowCount();

if($num>0){

    $languages_arr = array();
    $languages_arr["records"] = array();
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)){
        extract($row);
        $translator_item = array(
            "translator_id" => $translator_id,
            "language_tag" => $language_tag,
            "language" => $language, 
            "destination" => $destination
        );
        array_push($languages_arr["records"], $translator_item);
    }
    echo json_encode($languages_arr);
}else{
    echo json_encode(
        array("message" => "Nessun Linguaggio Trovato.")
    );
}
?>