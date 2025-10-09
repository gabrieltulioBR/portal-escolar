<?php
session_start();
include 'conexao.php';

// Verificar autenticação
checkAuth();
checkUserType(['aluno']);

$user_id = $_SESSION['user_id'];
$user_name = $_SESSION['user_name'];

// Buscar dados do aluno
$database = new Database();
$db = $database->getConnection();

$query = "SELECT * FROM alunos WHERE usuario_id = :user_id";
$stmt = $db->prepare($query);
$stmt->bindParam(":user_id", $user_id);
$stmt->execute();

$aluno = $stmt->fetch(PDO::FETCH_ASSOC);

// Buscar notas do aluno
$query_notas = "SELECT d.nome as disciplina, n.nota, n.bimestre 
                FROM notas n 
                JOIN disciplinas d ON n.disciplina_id = d.id 
                WHERE n.aluno_id = :aluno_id 
                ORDER BY d.nome, n.bimestre";
$stmt_notas = $db->prepare($query_notas);
$stmt_notas->bindParam(":aluno_id", $aluno['id']);
$stmt_notas->execute();

$notas = $stmt_notas->fetchAll(PDO::FETCH_ASSOC);

// Buscar avisos recentes
$query_avisos = "SELECT titulo, mensagem, data_publicacao 
                 FROM avisos 
                 WHERE (destinatario = 'alunos' OR destinatario = 'todos')
                 AND data_publicacao >= DATE_SUB(NOW(), INTERVAL 30 DAY)
                 ORDER BY data_publicacao DESC 
                 LIMIT 5";
$stmt_avisos = $db->prepare($query_avisos);
$stmt_avisos->execute();

$avisos = $stmt_avisos->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Área do Aluno - Portal Escolar</title>
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
                <h2>Área do Aluno</h2>
                <p>Bem-vindo, <?php echo $user_name; ?>!</p>
            </div>
        </section>

        <section class="area-restrita">
            <div class="container">
                <div class="perfil">
                    <h3>👤 Meu Perfil</h3>
                    <p><strong>Nome:</strong> <?php echo $aluno['nome_completo'] ?? $user_name; ?></p>
                    <p><strong>Matrícula:</strong> <?php echo $aluno['matricula'] ?? 'N/A'; ?></p>
                    <p><strong>Turma:</strong> <?php echo $aluno['turma'] ?? 'N/A'; ?></p>
                    <p><strong>Notificações:</strong> <span class="notificacao"><?php echo count($avisos); ?></span></p>
                </div>

                <?php if (!empty($avisos)): ?>
                <div class="avisos-grid">
                    <?php foreach($avisos as $aviso): ?>
                    <div class="aviso-card <?php echo strpos(strtolower($aviso['titulo']), 'importante') !== false ? 'importante' : ''; ?>">
                        <h3>📢 <?php echo $aviso['titulo']; ?></h3>
                        <p><?php echo $aviso['mensagem']; ?></p>
                        <small>Publicado em: <?php echo date('d/m/Y', strtotime($aviso['data_publicacao'])); ?></small>
                    </div>
                    <?php endforeach; ?>
                </div>
                <?php endif; ?>

                <?php if (!empty($notas)): ?>
                <div class="notas">
                    <h3>📊 Minhas Notas</h3>
                    <div class="tabela-notas">
                        <table>
                            <thead>
                                <tr>
                                    <th>Disciplina</th>
                                    <th>1º Bim</th>
                                    <th>2º Bim</th>
                                    <th>3º Bim</th>
                                    <th>4º Bim</th>
                                    <th>Média</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php
                                $notas_por_disciplina = [];
                                foreach($notas as $nota) {
                                    $disciplina = $nota['disciplina'];
                                    if (!isset($notas_por_disciplina[$disciplina])) {
                                        $notas_por_disciplina[$disciplina] = ['', '', '', ''];
                                    }
                                    $notas_por_disciplina[$disciplina][$nota['bimestre']-1] = $nota['nota'];
                                }
                                
                                foreach($notas_por_disciplina as $disciplina => $notas_bimestre):
                                    $notas_validas = array_filter($notas_bimestre, function($n) { return $n !== ''; });
                                    $media = !empty($notas_validas) ? array_sum($notas_validas) / count($notas_validas) : 0;
                                ?>
                                <tr>
                                    <td><?php echo $disciplina; ?></td>
                                    <?php for($i = 0; $i < 4; $i++): ?>
                                    <td><?php echo $notas_bimestre[$i] ?: '-'; ?></td>
                                    <?php endfor; ?>
                                    <td><strong><?php echo number_format($media, 1); ?></strong></td>
                                </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
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