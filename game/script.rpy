# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Estudante")
define p = Character("Professor")
define s = Character("Salmista")


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
    p "Que bênção incrível não?"
    p "Estudamos o capítulo 01 do livro de Salmos, e vimos que é composto por 6 versículos."
    e "Professor, você poderia detalhar esse capítulo melhor para nossa assimilação?" 
    p "Claro que sim!"
    jump explicacao_aula_01

label explicacao_aula_01:
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
    jump final_jogo

 
label final_triste:
    e "Que pena."
    jump final_jogo


label salmo01():
    s "1. Abençoado é o homem que não anda no conselho do ímpio, nem fica no caminho dos pecadores, nem se assenta na cadeira dos escarnecedores."
    s "2. Mas o seu prazer está na lei do SENHOR, e na Sua lei medita dia e noite."
    s "3. E ele será como árvore plantada junto a rios de água, que geram seu fruto em sua estação; sua folha também não murchará; e tudo aquilo que ele faça, prosperará."
    s "4. Os ímpios não são assim; mas são como a palha que o vento lança para longe."
    s "5. Portanto, os ímpios não ficarão de pé no juízo, nem pecadores na congragação dos justos."
    s "6. Porque o SENHOR conhece o caminho dos justos, mas o caminho dos ímpios perecerá."
    return
    # This ends the game.

label final_jogo:
    return
