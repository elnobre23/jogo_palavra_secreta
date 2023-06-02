<body>
  <h1>Documentação do Código: Jogo de Adivinhação de Palavras</h1>
  <p>
    Este código em Python implementa um jogo de adivinhação de palavras onde um jogador digita uma palavra e o outro jogador tenta adivinhá-la, fornecendo letras como palpites.
  </p>

  <h2>Importação</h2>
  <p>
    O código utiliza a biblioteca <code>os</code> para executar o comando de limpar a tela do console.
  </p>

  <h2>Inicialização</h2>
  <p>
    O código inicia solicitando ao usuário que digite uma palavra para ser adivinhada pelo outro jogador utilizando a função <code>input()</code>. A palavra é armazenada na variável <code>palavra_secreta</code>. Em seguida, a tela do console é limpa utilizando o comando <code>os.system('cls')</code> (apenas em sistemas operacionais Windows).
  </p>

  <h2>Laço Principal</h2>
  <p>
    O código utiliza um laço <code>while True:</code> para continuar a execução até que o jogo seja encerrado manualmente.
  </p>
  <p>
    Dentro do laço, o código realiza as seguintes etapas:
  </p>
  <ol>
    <li>
      <code>letra_digitada = input('Informe uma letra para tentar descobrir a palavra secreta: ')</code>: Solicita ao jogador que informe uma letra como palpite e armazena a entrada na variável <code>letra_digitada</code>.
    </li>
    <li>
      <code>contador_tentativas += 1</code>: Incrementa o contador de tentativas em 1.
    </li>
    <li>
      <code>if len(letra_digitada) != 1:</code>: Verifica se o jogador digitou mais de uma letra.
      <ul>
        <li><code>print('Digite somente uma letra por vez!')</code>: Exibe uma mensagem de erro informando que o jogador deve digitar apenas uma letra por vez.</li>
        <li><code>continue</code>: Continua para a próxima iteração do laço utilizando a instrução <code>continue</code>.</li>
      </ul>
    </li>
    <li>
      <code>if letra_digitada in palavra_secreta:</code>: Verifica se a letra digitada pelo jogador está presente na palavra secreta.
      <ul>
        <li><code>letra_descoberta += letra_digitada</code>: Adiciona a letra digitada à variável <code>letra_descoberta</code> que armazena as letras corretamente adivinhadas.</li>
      </ul>
    </li>
    <li>
      <code>else:</code>: Executa caso a letra digitada pelo jogador não esteja na palavra secreta.
      <ul>
        <li><code>print('A letra não está na palavra secreta')</code>: Exibe uma mensagem informando que a letra digitada não faz parte da palavra secreta.</li>
      </ul>
    </li>
    <li>
      <code>palavra_formada = ''</code>: Inicializa uma variável <code>palavra_formada</code> vazia que será utilizada para exibir a palavra a ser adivinhada.
    </li>
    <li>
      <code>for i in palavra_secreta:</code>: Percorre cada letra da palavra secreta utilizando um laço <code>for</code>.
      <ul>
        <li>
          <code>if i in letra_descoberta:</code>: Verifica se a letra atual está presente nas letras corretamente adivinhadas (<code>letra_descoberta</code>).
          <ul>
            <li><code>palavra_formada += i</code>: Adiciona a letra à variável <code>palavra_formada</code> se estiver corretamente adivinhada.</li>
          </ul>
        </li>
        <li>
          <code>else:</code>: Executa caso a letra atual não esteja nas letras corretamente adivinhadas.
          <ul>
            <li><code>palavra_formada += '*'</code>: Adiciona o caractere '*' à variável <code>palavra_formada</code> para representar uma letra não adivinhada.</li>
          </ul>
        </li>
      </ul>
    </li>
    <li>
      <code>print('Palavra formada: ', palavra_formada)</code>: Exibe a palavra formada até o momento, substituindo as letras não adivinhadas pelo caractere '*'.
    </li>
    <li>
      <code>if palavra_secreta == palavra_formada:</code>: Verifica se a palavra secreta foi completamente adivinhada.
      <ul>
        <li><code>print(f'Parabéns! A palavra secreta era: {palavra_secreta}')</code>: Exibe uma mensagem de parabéns, informando a palavra secreta correta.</li>
        <li><code>print(f'Tentativas: {contador_tentativas}x')</code>: Exibe o número de tentativas utilizadas para adivinhar a palavra secreta.</li>
        <li>
          <code>contador_tentativas = 0</code>: Reseta o contador de tentativas para 0.
        </li>
        <li>
          <code>palavra_secreta = input('Escreva uma palavra para ser adivinhada pelo outro jogador: ')</code>: Solicita ao usuário que digite uma nova palavra para ser adivinhada pelo próximo jogador e armazena na variável <code>palavra_secreta</code>.
        </li>
        <li>
          <code>os.system('cls')</code>: Executa o comando para limpar a tela do console (apenas em sistemas operacionais Windows).
        </li>
        <li>
          <code>letra_descoberta = ''</code>: Limpa a variável <code>letra_descoberta</code> que armazena as letras corretamente adivinhadas.
        </li>
        <li>
          <code>palavra_descoberta = ''</code>: Limpa a variável <code>palavra_descoberta</code> (que não é utilizada no código).
        </li>
      </ul>
    </li>
  </ol>

  <h2>Saída</h2>
  <p>
    Ao finalizar a execução do jogo, o jogador pode reiniciar digitando uma nova palavra secreta ou encerrar o programa manualmente.
  </p>

</body>
</html>
