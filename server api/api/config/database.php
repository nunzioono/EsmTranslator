<?php
class Database
	{
	// credenziali
	private $host = "localhost";
	private $db_name = "my_esmtranslator";
	private $username = "esmtranslator";
	private $password = "F2dsBTkAMZDs";
	public $conn;
	// connessione al database
	public function getConnection()
		{
		$this->conn = null;
		try
			{
			$this->conn = new PDO("mysql:host=" . $this->host . ";dbname=" . $this->db_name, $this->username, $this->password);
			$this->conn->exec("set names utf8");
			}
		catch(PDOException $exception)
			{
			echo "Errore di connessione: " . $exception->getMessage();
			}
		return $this->conn;
		}
	}
?>