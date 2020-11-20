# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Estudante", color="#30300a")
define p = Character("Professor", color="#0A0A0D")
define s = Character("Salmista",  color="#00AC00")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Você é novo aqui."

    e "Estamos numa aula de salmos, cujo objetivo é memorizar a maior quantidade de salmos possíves."

    e "E entendermos o significado de Meditar na voz do SENHOR."

menu:
    "Quer iniciar a aula?"
    
    "Sim, com certeza!":
        jump iniciar_aula

    "Não, passo.":
        jump final_triste 

label iniciar_aula:
    p "Então vamos começar! Inicialmente com o básico:"
    p "Os Salmos são canções e poemas de louvor a Deus"
    p "A partir do surgimento da imprensa, a bíblia foi dividida em capítulos e versículos."
    p "Vamos para nossa primeira aula e também o primeiro salmo de estudo!"
    jump aula_01

label aula_01:
    p "Para começar nada melhor que o Salmo capítulo 01"
    call salmo01()
    p "Estudamos o capítulo 01 do livro de Salmos, e vimos que é composto por 6 versículos."
    menu:
       "Professor, você poderia detalhar esse capítulo melhor para nossa assimilação?": 
          jump explicacao_aula_01
       "Professor, vamos para próxima aula?":
          jump aula_02
label explicacao_aula_01:
    p "Esse salmo é uma bênção incrível, não?"
    p "No versículo 1 é revelado que tipo de homem é Abençoado ou Bem-aventurado pelo Senhor."
    p "Ele precisa saír do conselho dos homens maus, ou seja, dos ímpios."
    p "É necessário que ele não ande nos caminhos dos pecadores, ou seja, aqueles que buscam a fazer coisas erradas o tempo todo."
    p "E também que não se assente a cadeira ou dentro da roda dos escarnecedores, ou seja aquels que falam mal dos outros pelas costas."
    p "Segundo o verso 2, vemos que esse homem é abençoado por Deus, não apenas por desviar do mau, mas por ter prazer, se deleitar na lei do SENHOR e meditar, refletir dia e noite nessa lei."
    p "As bênçãos que vemos no verso 3 são diversas, e dentre elas: fertilidade, e prosperidade."
    p "No verso 4 é mostrado como são os maus para Deus. E o verso 5 finaliza o pensamento mostrando que esses no dia do juízo não estarão de pé entre os justos."
    p "Porque o Deus Altíssimo conhece o caminho dos justos e ímpios, e ambos terão recompensa. Sendo que os maus, a recompensa é a perdição e destruição."
    jump pergunta_explicacao_aula_01

label pergunta_explicacao_aula_01:
    menu:
       "Você entendeu todas as verdades explicadas nesse capítulo?"
       "Sim, entendi tudo! Podemos prosseguir":
           jump aula_02
       "Sim. Entendi, mas quero ver o salmo novamente":
           call salmo01()
           jump pergunta_explicacao_aula_01
       "Não. Por favor repita a explicacao novamente.":
           jump explicacao_aula_01

label aula_02:
    p "Vamos agora ver outro salmo"
    p "Salmo 02"
    call salmo02()
    jump pergunta_explicacao_aula_02

label pergunta_explicacao_aula_02:
    menu:
        p "Você quer que eu repita novamente? Ou quer ver a explicação?"
        "Repita novamente":
              call salmo02()
              jump pergunta_explicacao_aula_02
        "Pode ir para explicação":
              jump explicacao_aula02
        "Não, pode ir para próxima aula":
              jump aula03
        "Não, quero sair":
              jump sair 

label explicacao_aula02:
    p "Aqui temos um salmo de 12 versos."
    e "UAU! Doze versos é muito!"
    p "Você acha? Há salmos de mais de 150 versos."
    e "Professor como eu posso memorizar esses salmos?"
    menu:
       p "Posso te explicar uma estratégia simples agora. Você quer ouvir?"
       "Sim, por favor!":
           call estrategia_01
           jump continuar_explicacao_aula02
       "Não, quero ouvir a explicação apenas.":
           "Então vamos continuar a explicação"
           jump continuar_explicacao_aula02

label continuar_explicacao_aula02:

label aula_03:
 
label sair:
    p "Até a próxima!"
    jump final_jogo

label final_triste:
    p "Que pena."
    jump final_jogo


label estrategia_01:
    p "Uma das estratégias para memorizar é a repetição."
    p "Funciona assim: "
    p "1. repita 10 vezes em voz alta o verso atual, antes de passar para o próximo"
    p "2. quando chegar na 10a vez, volte e tente falar os versos anteriores do último para o primeiro"
    p "3. em cada verso, fale a referência no inicio e no fim, a referência é livro capitulo versículo, ex: Salmo 1:8, fale : Salmo um verso oito."
    p "Pondo em prática, um exemplo:"
    p "Inicie com o Salmo 2:1 e leia 10 vezes, dizendo a referência no início, antes de ler o texto, e no final, após ler o texto."
    p "Passe para o Salmo 2:2 e leia 10 vezes"
    p "Após a décima vez do Salmo 2:2, fale o Salmo 2:1"
    p "Passe para o Salmo 2:3, leia 10 vezes"
    p "Após a décima vez do Salmo 2:3, fale o Salmo 2:2 e depois o Salmo 2:1"
    p "E assim por diante..."
    p "Essa é a primeira estratégia, chamada de estratégia de repetição"
    p "Não pare por aí: relembre o salmo quer vc memorizou quando for dormir, tente recitar para alguém ou para um amigo ou amiga"
    p "Estudos mostram que após você falar 100 vezes um texto, ele efetivamente ficará em sua memória."
    return

label salmo01():
    s "01. Abençoado é o homem que não anda no conselho do ímpio, nem fica no caminho dos pecadores, nem se assenta na cadeira dos escarnecedores."
    s "02. Mas o seu prazer está na lei do SENHOR, e na Sua lei medita dia e noite."
    s "03. E ele será como árvore plantada junto a rios de água, que geram seu fruto em sua estação; sua folha também não murchará; e tudo aquilo que ele faça, prosperará."
    s "04. Os ímpios não são assim; mas são como a palha que o vento lança para longe."
    s "05. Portanto, os ímpios não ficarão de pé no juízo, nem pecadores na congragação dos justos."
    s "06. Porque o SENHOR conhece o caminho dos justos, mas o caminho dos ímpios perecerá."
    return
    # This ends the game.

label salmo02():
    s "01. Por que os pagãos se irritam e os ímpios imaginam coisas vãs?"
    s "02. Os reis da terra se posicionam, e os governantes tomam conselho juntos contra o Senhor e seu Ungido dizendo:"
    s "03. Rompamos as suas ataduras em partes, e lancemos longe de nós suas cordas"
    s "04. Aquele que se assenta nos céus se rirá; o SENHOR os terá em escárnio"
    s "05. Então lhes falará na sua ira, e os aborrecerá no seu desgosto pesaroso;"
    s "06. {i}Contudo, pus meu rei sobre meu santo monte de Sião{/i}"
    s "07. Eu declararei o decreto: O Senhor me disse: {i}Tu és meu filho; neste dia eu te gerei{/i}."
    s "08. {i}Pede-me, e eu te darei os pagãos por tua herança, e as partes extremas da terra por tua possessão{/i}."
    s "09. {i}Tu os quebrarás com uma vara de ferro; tu os arrebentarás em pedaços como a um vaso de oleiro{/i}."
    s "10. Agora, portanto, ó vós reis, sede sábios; sede instruídos, vós juízes da terra."
    s "11. Servi ao Senhor com temor, e regozijai-vos com tremor."
    s "12. Beijai ao Filho, para que ele não se ire, e pereçais no caminho, porque em breve sua ira se inflamará. Abençoados são todos aqueles que põem sua confiança nele."
    return

label salmo03():
    s "01. SENHOR, como aumentaram aqueles que me perturbam! Muitos são aqueles que se levantam contra mim."
    s "02. Há muitos que dizem da minha alma: Não há salvação para ele em Deus. Selá."
    s "03. Mas tu, Ó SENHOR, és um escudo para mim, a minha glória, e o exaltador da minha cabeça."
    s "04. Clamei ao SENHOR com a minha voz, e ele me ouviu do seu santo monte. Selá."
    s "05. Eu me deitei e dormi; acordei, porque o SENHOR me sustentou."
    s "06. Não terei medo de dez milhares de pessoas que se puseram contra mim ao meu redor."
    s "07. Levanta-te, ó SENHOR; salva-me, ó meu Deus; porque atingiste a todos os meus inimigos sobre o osso malar; quebraste os dentes dos ímpios."
    s "08. A salvação pertence ao SENHOR; tua bênção está sobre teu povo. Selá."
    return

label salmo103():
    s "01. "
    s "02. "
    s "03. "
    s "04. "
    s "05. "
    s "06. "
    s "07. "
    s "08. "
    s "09. "
    s "10. "
    s "11. "
    s "12. "
    s "13. "
    s "14. "
    s "15. "
    s "16. "
    s "17. "
    s "18. "
    s "19. "
    s "20. "
    s "21. "
    s "22. "

label salmo117():
    s "01. Louvai ao SENHOR todas as nações, celebrai a Ele, todos os povos."
    s "02. Porque sua bondade prevaleceu sobre nós, e a fidelidade do SENHOR dura para sepre. Aleluia!"
    return

label salmo150():
    s "01. Aleluia! Louvai a Deus em seu santuário, louvai-o no firmamento do seu poder."
    s "02. Louvai-o por suas proezas, louvai-o conforme a imensidão de sua grandeza."
    s "03. Louvai-o com som de trombeta, louvai-o com lira e harpa."
    s "04. Louvai-o com tamborim e flauta, louvai-o com instrumentos de corda e de sopro."
    s "05. Louvai-o com címbalos bem sonoros; louvai-o com címbalos de sons de alegria."
    s "06. Tudo quanto tem fôlego, louve ao SENHOR! Aleluia!"
    return 
label final_jogo:
    return
