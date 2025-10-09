<?php
include 'conexao.php';

header('Content-Type: application/json');

try {
    $database = new Database();
    $db = $database->getConnection();
    
    $query = "SELECT n.titulo, n.resumo, n.imagem, u.nome as autor, n.data_publicacao 
              FROM noticias n 
              JOIN usuarios u ON n.autor_id = u.id 
              WHERE n.ativo = TRUE 
              ORDER BY n.data_publicacao DESC 
              LIMIT 10";
    
    $stmt = $db->prepare($query);
    $stmt->execute();
    
    $noticias = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    echo json_encode([
        'success' => true,
        'data' => $noticias
    ]);
    
} catch(PDOException $exception) {
    echo json_encode([
        'success' => false,
        'message' => 'Erro ao carregar notícias: ' . $exception->getMessage()
    ]);
}
?>