<?php
session_start();
include 'conexao.php';

if ($_POST) {
    $email = sanitize($_POST['email']);
    $senha = $_POST['senha'];
    
    $database = new Database();
    $db = $database->getConnection();
    
    $query = "SELECT id, nome, email, senha, tipo FROM usuarios WHERE email = :email AND ativo = 1";
    $stmt = $db->prepare($query);
    $stmt->bindParam(":email", $email);
    $stmt->execute();
    
    if ($stmt->rowCount() > 0) {
        $row = $stmt->fetch(PDO::FETCH_ASSOC);
        
        if ($senha === $row['senha']) {
            $_SESSION['user_id'] = $row['id'];
            $_SESSION['user_name'] = $row['nome'];
            $_SESSION['user_email'] = $row['email'];
            $_SESSION['user_type'] = $row['tipo'];
            $_SESSION['logged_in'] = true;
            
            if ($row['tipo'] == 'aluno') {
                header("Location: area_restrita_aluno.php");
            } else {
                header("Location: area_restrita_professor.php");
            }
            exit();
        }
    }
    
    $_SESSION['login_error'] = "Email ou senha incorretos!";
    header("Location: ../login.html");
    exit();
}
?>