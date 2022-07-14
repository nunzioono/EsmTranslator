<?php
class TranslatorLanguage
	{
	private $conn;
	private $table_name = "language_translators";
	// proprietà di un libro
	public $translator_id;
	public $language_tag;
	public $language;
    public $destination;

    // costruttore
	public function __construct($db)
		{
		$this->conn = $db;
		}
	// READ libri
	function read()
		{
		// select all
		$query = "SELECT
                        *
                    FROM
                   " . $this->table_name.  ";";
		$stmt = $this->conn->prepare($query);
		// execute query
		$stmt->execute();
		return $stmt;
		}
        
	}
?>