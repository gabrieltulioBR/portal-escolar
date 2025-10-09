<?php
session_start();
include 'conexao.php';

// Verificar autenticação
checkAuth();
checkUserType(['professor', 'admin']);

$user_id = $_SESSION['user_id'];
$user_name = $_SESSION['user_name'];

// Buscar dados do professor
$database = new Database();
$db = $database->getConnection();

$query = "SELECT p.*, u.nome as nome_completo 
          FROM professores p 
          JOIN usuarios u ON p.usuario_id = u.id 
          WHERE p.usuario_id = :user_id";
$stmt = $db->prepare($query);
$stmt->bindParam(":user_id", $user_id);
$stmt->execute();

$professor = $stmt->fetch(PDO::FETCH_ASSOC);

// Buscar turmas do professor
$query_turmas = "SELECT DISTINCT turma FROM turmas_professores WHERE professor_id = :professor_id";
$stmt_turmas = $db->prepare($query_turmas);
$stmt_turmas->bindParam(":professor_id", $professor['id']);
$stmt_turmas->execute();

$turmas = $stmt_turmas->fetchAll(PDO::FETCH_COLUMN);

// Buscar tarefas pendentes
$query_tarefas = "SELECT titulo, descricao, data_limite 
                  FROM tarefas 
                  WHERE professor_id = :professor_id 
                  AND concluida = 0 
                  AND data_limite >= CURDATE()
                  ORDER BY data_limite ASC 
                  LIMIT 5";
$stmt_tarefas = $db->prepare($query_tarefas);
$stmt_tarefas->bindParam(":professor_id", $professor['id']);
$stmt_tarefas->execute();

$tarefas = $stmt_tarefas->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Área do Professor - Portal Escolar</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">
                <span class="logo-icon">🏫</span>
                <h1>Portal Escolar</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="../index.html">Início</a></li>
                    <li><a href="../professores.html">Professores</a></li>
                    <li><a href="../noticias.html">Notícias</a></li>
                    <li><a href="../galeria.html">Galeria</a></li>
                    <li><a href="../contato.html">Contato</a></li>
                    <li><a href="../logica.html">Exercícios</a></li>
                    <li><a href="logout.php" class="login-btn">Sair</a></li>
                </ul>
            </nav>
            <div class="mobile-menu">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="container">
                <h2>Área do Professor</h2>
                <p>Bem-vindo, <?php echo $user_name; ?>!</p>
            </div>
        </section>

        <section class="area-restrita">
            <div class="container">
                <div class="perfil">
                    <h3>👤 Meu Perfil</h3>
                    <p><strong>Nome:</strong> <?php echo $professor['nome_completo'] ?? $user_name; ?></p>
                    <p><strong>Disciplina:</strong> <?php echo $professor['disciplina'] ?? 'N/A'; ?></p>
                    <p><strong>Turmas:</strong> <?php echo implode(', ', $turmas); ?></p>
                    <p><strong>Notificações:</strong> <span class="notificacao"><?php echo count($tarefas); ?></span></p>
                </div>

                <div class="ferramentas-grid">
                    <div class="ferramenta-card">
                        <h3>📝 Lançar Notas</h3>
                        <p>Registre as notas dos alunos</p>
                        <button class="btn" onclick="alert('Funcionalidade em desenvolvimento')">Acessar</button>
                    </div>
                    <div class="ferramenta-card">
                        <h3>📚 Planejamento</h3>
                        <p>Planeje suas aulas</p>
                        <button class="btn" onclick="alert('Funcionalidade em desenvolvimento')">Acessar</button>
                    </div>
                    <div class="ferramenta-card">
                        <h3>👥 Turmas</h3>
                        <p>Gerencie suas turmas</p>
                        <button class="btn" onclick="alert('Funcionalidade em desenvolvimento')">Acessar</button>
                    </div>
                    <div class="ferramenta-card">
                        <h3>📢 Comunicados</h3>
                        <p>Envie avisos para alunos</p>
                        <button class="btn" onclick="alert('Funcionalidade em desenvolvimento')">Acessar</button>
                    </div>
                </div>

                <?php if (!empty($tarefas)): ?>
                <div class="tarefas-pendentes">
                    <h3>📋 Tarefas Pendentes</h3>
                    <ul>
                        <?php foreach($tarefas as $tarefa): ?>
                        <li>
                            ✅ <?php echo $tarefa['titulo']; ?>
                            <br><small><?php echo $tarefa['descricao']; ?></small>
                            <br><small><strong>Prazo:</strong> <?php echo date('d/m/Y', strtotime($tarefa['data_limite'])); ?></small>
                        </li>
                        <?php endforeach; ?>
                    </ul>
                </div>
                <?php endif; ?>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2024 Portal Escolar. Todos os direitos reservados.</p>
        </div>
    </footer>

    <script src="../js/main.js"></script>
</body>
</html>