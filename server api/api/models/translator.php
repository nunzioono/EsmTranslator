<?php
class Translator
	{
	private $conn;
	private $table_name = "translators";
	// proprietà di un libro
	public $id;
	public $name;
	public $api_key;
    public $consumption;
    public $limit;
    public $created_at;
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
        
    function readById(){
	    $query = "SELECT
                        *
                    FROM
                   " . $this->table_name.  "
                   WHERE id=:id;";
		$stmt = $this->conn->prepare($query);
        $this->id = htmlspecialchars(strip_tags($this->id));
        $stmt->bindParam(":id", $this->id);
		// execute query
		$stmt->execute();
		return $stmt;
    }
    
    function update(){
	 
	  if($this->consumption<=$row->limit){
        $query = "UPDATE
                        " . $this->table_name . "
                    SET
                        consumption = :consumption,
                        last_update = ".$actual_datetime."
                    WHERE
                        id = :id";

        $stmt = $this->conn->prepare($query);

        $this->id = htmlspecialchars(strip_tags($this->id));
        $this->consumption = htmlspecialchars(strip_tags($this->consumption));
        // binding
        $stmt->bindParam(":id", $this->id);
        $stmt->bindParam(":consumption", $this->consumption);

        // execute the query
        if($stmt->execute()){
          return true;
        }

        return false;
      }
	  }
      

	}
?>