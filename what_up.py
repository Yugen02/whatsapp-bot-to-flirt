import pywhatkit
from datetime import datetime
import time
import pandas as pd
import numpy as np
from tqdm import tqdm

## STEP 1
## put the phone number
phone_number = '########'

## STEP 2
## add all the firt that you want to send, in this case are in spanish version
df = pd.DataFrame({'piropos':
        ['Si me dedicas una sonrisa pasas de ser linda a perfecta',
        '¿Qué pasó en el cielo que se están cayendo los ángeles?',
        '¡Te voy a poner una multa!. ¿Por qué? Por exceso de belleza',
        'Como se habrán querido tus padres... por haberte hecho tan bonita',
        'Por qué el cielo está nublado? Porque todo el azul está en tus ojos',
        '¿ Tienes alguna herida, guapa ? Tiene que ser duro caerse del cielo',
        'Tus ojos son verdes los míos café, los míos te quieren los tuyos no sé',
        'Cuando el día se nubla, no extraño al sol, porque lo tengo en tu sonrisa',
        'Pasa una mujer y dice adiós... -a DIOS lo vi cuando me miraron tus ojos !!',
        'En otras partes del mundo se están quejando, porque el sol está acá nada mas'
        'Aprovecha que estoy en rebaja guapa y te dejo dos besos por el precio de uno',
        'Tu bellezsa me enciega porque viene desde su corazón y se refleja en tus ojos',
       ' Eres de esa clase de personas, por las cuales a las estrellas se les piden deseos',
      '  Si alguna vez te han dicho que eres bella te mintieron, no eres bella eres hermosa',
        'Celeste es el cielo, amarilla la nata y negros son los ojos de la chica que me mata',
        'Si yo fuera Colón navegaría día y noche para llegar a lo más profundo de tu corazón',
        'Cinco calles he cruzado, seis con el callejón, sólo me falta una para llegar a tu corazón',
        'Si fueras mi novia me volvería ateo ¿ Por que? Porque no tendría nada más que pedirle a Dios',
        'A una hermosa niña acompañada de la madre: ¡Que linda flor, lástima que venga con la maceta!',
        'Por suerte para mi, Dios no se dió cuenta del ángel que se le escapó para cruzarse en mi camino',
        'Cuando Dios creó el mundo lo encontró perfecto, pero luego te formó a ti y el mundo quedó DIVINO',
        'Con una mirada como la tuya, no te hace falta una pistola, ni un cañón. Y con ese encanto y dulzura, rindes a tus pies cualquier varón',
        'Eres tú de esas mujeres maravillosas que conquistan sin faldas cortas, sin grandes escotes. Solo con una sonrisa, tu mirada y tu forma de ser',
        'Cada vez que te veo me dejas sin palabras, sin respiración y sin aliento. Cada vez que me hablas, me enloquece y me fascina el sonido de tu voz. Y si además me sonríes, entonces no se explicarte, todo lo que por ti yo siento',
        'Te invito a ser feliz yo pago',
       ' Cuando caminas no pisas el suelo, lo acaricias',
        'Nos veríamos lindo en un pastel de boda juntos',
        'Tantas formas de vida y yo solo vivo en sus ojos',
        '¿A qué numero llamo si quiero marcarte de por vida?',
        'Me gustas tanto que no se por donde empezar a decírtelo',
        'Todos se quedan con tu físico, pero yo prefiero tu corazón',
        'Hola si te gustan los idiomas cuando quieras te enseño mi lengua',
        'Dime por donde paseas para besar el suelo que pisas, preciosidad!',
        'Eres tan bonita que Dios bajaría a la tierra tan solo para verte pasar',
        '¡Eres como una cámara Sony! Cada vez que la miro no puedo evitar sonreir',
        'En una isla desierta me gustaría estar y sólo de tus besos poderme alimentar',
        'Si fueras lluvia de invierno, yo cerraría el paraguas para sentirte en mi cuerpo',
        'Me gustas tanto, tanto, que hasta me gusta estar preso, en las redes de tu encanto',
        'Si te pellizco seguro que te enojas pero si me pellizcas tu, seguro que me despierto',
        'No son palabras de oro ni tampoco de rubí, son palabras de cariño que compongo para usted',
        'Quisiera ser hormiguita para subir por tu balcón y decirte al oído: guapa, bonita, bombón',
        'En mi vida falta vida, en mi vida falta luz, en mi vida falta alguien y ese alguien eres tú',
        'Señorita, si supiera nadar, me tiraría en la piscina de tus ojos desde el trampolín de sus pestañas',
        'Eres tan hermosa que te regalaría un millón de besos y si no te gustasen te los aceptaría de regreso',
        'Dios se pasó al crearte a ti',
        'Al amor y a ti los conocí al mismo tiempo',
        'Si la belleza fuese tiempo, tú serías 24 horas',
        'Si algún día te pierdes, búscate en mis pensamientos!',
        'Si amarte fuera pecado, tendría el infierno asegurado',
        'Eres lo único que le falta a mi vida para ser perfecto',
        'Eres la única estrella que falta en el cielo de mi vida!',
        'Ahora que te conozco, no tengo nada mas que pedirle a la vida!',
       ' Si no puedo estar contigo por lo menos déjame estar en tus sueños',
        'Viendo sonrisas así de bonitas es fácil tener un buen día, guapa!',
        'Dios debe estar distraído, porque los ángeles se le están escapando',
        'El día que te conocí a los ojos te mire, amigos nos hicimos y de ti me enamoré',
        'Si la vida son dos días, quiero pasar uno conociéndote y el otro despidiéndome',
        'Sólo tengo un propósito para este Año, que tu vida y la mía escojan el mismo destino',
        'Dicen que Robar es Malo .. yo nunca lo haría pero un BesiTo Tuyo con mucho gusto lo robaría!',
        'Los pájaros piden comida, los presos su libertad. Yo te pido Amor mío que nunca me dejes de AMAR',
       ' Esta noche he soñado que al despertar esta mañana te estaría abrazando a ti en vez de mi almohada',
        'Cómo ¡quisiera ser caramelo! y sé que es una idea loca, pero es la forma más dulce que tengo para alcanzar un besito de sus labios',
        'A la mayoría de la gente le gusta ver la Copa del Mundo porque sucede solo una vez cada 4 años; yo prefiero conocerte a ti, porque la posibilidad de conocer a alguien como tú ocurre solo una vez en la vida',
        'Si cocinas como estás caminado, te juro de la casa hoy no salgo .',
        'Puede que no seas perfecta, pero tus defectos son encantadores.',
        'Tengo que cumplir arresto domiciliario. Puedo cumplirlo en tu casa?',
        'Si quieres encontrar a tu príncipe azul, tendrás que besar a este sapo',
       ' Si tuviera un dolar por cada beso, que me das, sería un rico enamorado',
        'Quisiera tener un barco pirata, para navegar por el mar rojo de tus labios y así llegar al tesoro de tu corazón',
        'El sol sale por la ventana, y a tu ventana va a parar, fíjate si eres hermosa, que hasta el sol te viene a despertar',
        'Bendita sea la yerba que se trago la borrega de donde sacaron la lana para hacerle la sotana al cura que te bautizó',
        'Sé que no soy ni el más bonito ni el más deseado pero si sé que puedo pasar el resto de tu vida a tu lado porque te amo',
        'Yo soy tuyo y tú eres mía; de ellos puedes tener la certeza. Tú estás encerrada en mi corazón; la llave se ha perdido y deberás quedar dentro eternamente',
        'Piropos lindos para seducir y conquistar a una mujer que te gusta',
        '¡Dime cómo te llamas y te pido para los Reyes!',
        'No quiero dinero ni riqueza, a mi me basta con tu belleza',
        'Si cierro los ojos y vuelvo a abrirlos, vas a estar todavía?',
        '¿Por casualidad, tu nombre es Gillette? ¡Porque eres lo mejor para el hombre!',
        'Aprovecha hoy que estoy en el mercado, los guapos como yo duramos dos días libres',
       ' No te prometo un castillo, ni tampoco dinero, sólo mi corazón y mi cariño sincero',
        '¿Cómo quiere la gente que yo sea feliz si la mujer que yo quiero está lejos de mi?',
     '   Guapo no soy, riquezas no tengo pero te ofrezco mi corazón que es lo mejor que tengo!',
        'Si el cielo se queda sin estrellas, no me importa pues me he quedado con la más bella',
        'Dos terrones de azúcar en tus labios me encontré, maravillosa sensación que jamás olvidaré!',
        'Si viviéramos en el cielo te regalaría el sol, pero como no llego a eso, te regalo mi corazón',
        'Como enamorar a una mujer',
        'Caminando por la calle, caminando te encontré, y al verte tan seria y guapa, de ti me enamoré',
       ' Que bonitos ojos tienes tan redondos como el sol, se parecen a los ceros que me pone el profesor',
        'Labios de fresa, ojos de chocolate y piel de miel,con esos ingredientes tu madre hizo el mejor pastel',
        'Al mirar tú hardware, me pregunto cómo harás, para que esa configuración, soporte un almacenamiento tan alto de megas de belleza',
        'Nena si yo fuera el tiempo, me detendría a mirarte',
        'Si besarse es contagiarse de gérmenes... ¿Qué te parece si comenzamos la epidemia?',
        'La lima nació verde, el tiempo lo maduró, mi corazón nació libre, y el tuyo lo conquistó',
        '¿Sabes cuando apareció el agujero en la capa de ozono? Cuando tus ojos miraron al cielo',
        'No me tires con piedritas que me vas a lastimar, tirame con besitos que me vas a enamorar',
        'Algunas veces pregunto, ¿dónde está la perfección? y cuando te miro encuentro la solución',
       ' Qué bonito es el amor, qué bonito es el cielo pero más bonito es aun que te digan TE QUIERO',
        'Muchos te dirán, negrita por tí yo me muero, y yo que no te digo nada, soy el que más te quiero',
        'Las naranjas nacieron verdes y cambiaron de color. Mi corazón nació libre y el tuyo lo conquistó',
        'Mirando a una mujer vestida de negro ¿Quien habrá muerto en cielo que los ángeles están de luto?',
        'En el cielo hay una estrella que nunca deja de brillar y en la tierra hay una chica que me hace suspirar',
        'Sólo tienes que verte al espejo para levantar tu ánimo, con esa cara se alegran hasta los días lluviosos!',
        'La sonrisa de tus labios quita brillo al mundo entero, pero ¿qué me importa el mundo, si yo tengo mi lucero?',
        'Dicen que lo negro es luto, yo digo no es verdad, por que negro son tus ojos y son mi FELICIDAD...te quiero ANGÉLICA',
        'Si la palabra “amor” estuviera escrita en cada grano de arena del desierto del Sahara, no alcanzaría para expresar todo el amor que siento por ti',]}
)


print(df)

shuffled = df.sample(frac=1).reset_index()

for i in tqdm(shuffled['piropos']):
    ## You can add the time that you want to send the text in seconds
    sec = time.time() + 60
    date = datetime.fromtimestamp(sec)
    pywhatkit.sendwhatmsg('####-####',
                            i,
                            date.hour,
                            date.minute
                            )

    time.sleep(150)
    # print(i)