# Zona de afectacion del Rio Coahuayana

Muestra la zona de afectación debido a un desbordamiento del Rio

Programa para calcular la zona de influencia y pendientes.

P.E. Ingeniero Topógrafo Geomático, Facultad de Ingeniería Civil, Universidad de Colima, Campus Co-quimatlán, Coquimatlán, Colima, 28400, Oswaldo Missael Garcia Orozco, ogarcia@ucol.mx. 
  
Resumen

Se determinará la zona de afectación a cierta dis-tancia tanto como cosechas principalmente de plá-tanos que se encuentran en lugar como comunida-des cercanas debido al Rio Coahuayana en la parte que comprende desde el puente divisorio entre Colima y Michoacán hasta su desembocadura en el Océano Pacifico. De igual manera se obtendrá la pendiente de dicho lugar para conocer el relieve del terreno y como es que actúa el Rio. La zona de in-fluencia y las pendientes se obtendrán mediante el uso del lenguaje de programación Python, auxiliado del software ArcMap (ArcPy), que es la aplicación central en ArcGIS. Se planea que se obtenga la zona de influencia a 500 metros alrededor el Rio Coahuayana.

Palabras clave: Análisis, Rio Coahuayana, plataneras, afectación, programación, Python.

Abstract

The zone of affectation at a certain distance will be determined, as well as crops mainly from bananas that are in place as well as nearby communities due to the Coahuayana River in the part that includes from the dividing bridge between Colima and Mi-choacán to its mouth in the Pacific Ocean. In the same way, the slope of said place will be obtained to know the relief of the terrain and how the river acts. The area of influence and the slopes will be ob-tained through the use of the Python programming language, aided by the ArcMap software, which It is the core application in ArcGIS. It is planned to obtain the area of influence 500 meters around the Coa-huayana River.

Keywords: Analysis, Coahuayana River, banana plantations, affectation, programming, Python.

Introducción

El rio Coahuayana conduce un caudal conside-rable la mayor parte del año y su cuenca ocupa una superficie de 665.722 km² en el estado. El Rio Naranjo o Coahuayana nace en las inmedia-ciones del Cerro del Tigre en el municipio de Mazamitla, Jalisco, a una elevación aproximada de 2530 metros sobre el nivel mar. Lo alimentan aguas de numerosos ríos y arroyos, y recibe sucesivamente los nombres de Cofradía, San Lorenzo, Tamazula, Tuxpan, Naranjo y Coahua-yana

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/1.jpg)
Figura 1.- (Tramo desde Estapilla hasta su desem-bocadura en el Océano Pacifico del Rio Coahuaya-na)


Inicia su recorrido con dirección suroeste en un tramo de 25 km y en las inmediaciones del cerro de Tamazula de Gordiano, Jalisco, cambia su curso hacia el oeste durante 8 km, para variarlo finalmente hacia el sur – suroeste. Desde su nacimiento hasta su desembocadura en Boca de Apiza, al norte de la Bahía de San Telmo, recorre una distancia aproximada de 152 km. 
Es el límite entre Jalisco y Colima desde el pun-to de unión del arroyo de El Muerto, al sur de la estación de Tonilita, hasta el paso del Naranjo. De este lugar hasta Apiza, sirve de límite con el estado de Michoacán. Tiene como subcuencas intermediarias al Rio Coahuayana y a las lagu-nas de Alcuzahue y Amela.
Son varias las fuentes contaminantes de esta cuenca; sobresale el municipio de Tecomán, debido a que es un centro muy poblado y que cuenta demás con algunas industrias procesa-doras de aceites cítricos en menor grado figu-ran las localidades de Cerro de Ortega, Alzada, Cuauhtémoc y Alcaraces, con descargas muni-cipales, y Quesería, en donde hay instalado un ingenio.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/2.jpg)
Tabla 1.- (Superficie y porcentaje de las cuencas hidrológicas que integran la Subregión Hidrológi-ca)


![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/3.jpg)
Grafica 1.- (Precipitación anual en Michoacán en los últimos 70 años)


1.1. 	Tipos de Ríos

Los tipos de ríos son varios y según su período de actividad se pueden clasificar en: ríos peren-nes, ríos estacionales, ríos transitarios y ríos alóctonos.

•	Ríos perennes.
Estos ríos están formados por cursos de agua localizados en regiones de lluvias abundantes con escasas fluctuaciones a lo largo del año. Sin embargo, incluso en las áreas donde llueve muy poco pueden existir ríos con caudal per-manente si existe una alimentación freática (es decir, de aguas subterráneas) suficiente. La mayoría de los ríos pueden experimentar cam-bios estacionales y diarios en su caudal, debido a las fluctuaciones de las características de la cobertura vegetal, de las precipitaciones y de otras variaciones del tiempo atmosférico como la nubosidad, insolación, evaporación, etc.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/4.jpg)
Figura 2.- (Ejemplo de rio perennes)


•	Ríos estacionales
Estos ríos y ramblas son de zonas con clima tipo mediterráneo, en donde hay estaciones muy diferenciadas, con inviernos húmedos y veranos secos o viceversa. Suelen darse más en zonas de montaña que en las zonas de llanu-ra.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/5.jpg)
Figura 3.- (Ejemplo de ríos estacionales)


•	Ríos Transitorios
Son los ríos de zonas con clima desértico o seco, de caudal que a veces, en los cuales se puede estar sin precipitaciones durante años. Esto es debido a la poca frecuencia de las tor-mentas en zonas de clima de desierto. Pero cuando existen descargas de tormenta, que muchas veces son torrenciales, los ríos surgen rápidamente y a gran velocidad. Reciben el nombre de wadis o uadis, a los cauces casi siempre secos de las zonas desérticas, que pueden llegar a tener crecidas violentas y muy breves.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/6.jpg)
Figura 4.- (Ejemplo de rio transitorio)


•	Ríos Alóctonos
Son ríos, generalmente de zonas áridas, cuyas aguas proceden de otras regiones más lluvio-sas. El Nilo en Egipto siempre se ha tomado como ejemplo de este tipo de ríos. También el Okavango, otro río africano que termina en un amplio delta interior en una cuenca endorreica de clima relativamente seco.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/7.jpg)
Figura 5.- (Ejemplo de Ríos Alóctonos)


1.2. 	Programas y datos que utilizar

Se utilizará programa Python dentro del softwa-re ArcMap o también llamada como ArcPy, donde de la misma manera se utilizará las libre-rías adscritas por default a ArcPy como Buf-fer_analysis, la cual nos permitirá crear las zo-nas de influencias a partir de un determinado polígono, en este caso nuestro polígono será el Rio y la zona de influencia a partir del Rio será de 500 metros.
Para realizar las pendientes sobre el Rio, se utilizará lo mismo Python desde ArcMap, crean-do un TIN sobre nuestra carta edafológica E13B64 a partir de las curvas de nivel pertene-cientes al conjunto de datos vectoriales de la carta.
Para la elaboración de este proyecto haremos uso de los SIG (Sistemas de Información Geo-gráfica), así como también cartas topograficas-producidas por el INEGI escala 1:10 000 y 1:20 000 de la comunidad Cerro de Ortega y de las empresas plataneras para la obtención del daño provocado por el Rio Coahuayana en un cierto lapso (1999-2006), el cual es el principal factor de riesgo de estas empresas plataneras que llegan a exportar sus productos mundialmente.
Para este proyecto también es de suma impor-tancia saber información acerca de los pláta-nos, como es su producción, cuantos vástagos de plátanos existen por metro cuadrado, cuan-tos plátanos puede generar un vástago.

1.3. 	ArcPy

ArcPy es un paquete de sitio que se basa en el exitoso módulo arcgisscripting y lo sucede. Su objetivo es crear la piedra angular para una ma-nera útil y productiva de realizar análisis de da-tos geográficos, conversión de datos, adminis-tración de datos y automatización de mapas con Python.
Este paquete proporciona una rica experiencia Python nativa, que ofrece finalización de código (escriba una palabra clave y un punto para ob-tener una lista emergente de propiedades y métodos admitidos por esa palabra clave; se-leccione uno para insertarlo), así como docu-mentación de referencia para cada función, módulo y clase.
La ventaja adicional de utilizar ArcPy dentro de Python es que Python es un lenguaje de pro-gramación del propósito general. Es un lenguaje interpretado con asignación dinámica de tipos, adecuado para el trabajo interactivo y la crea-ción rápida de prototipos en programas únicos conocidos como secuencias de comandos, además de ofrecer potencia suficiente como permitir la escritura de aplicaciones grandes. Las aplicaciones ArcGIS escritas con ArcPy se benefician del desarrollo de módulos adiciona-les en numerosos nichos de Python por parte de profesionales del SIG y programadores de muchas disciplinas diferentes.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/8.jpg)
Figura 7.- (Juntando ambos softwares, nace ArcPy)


1.4. 	Zona de influencia o zonas de riesgo en los Ríos en ArcPy.

Una entidad importante de la herramienta Zona de influencia es el parámetro Método que de-termina cómo se construyen las zonas de in-fluencia. Hay dos métodos básicos para cons-truir zonas de influencia: euclidiano y geodési-co.
•	Las de zonas de influencia euclidianas miden la distancia en un plano Carte-siano bidimensional, donde la línea rec-ta o las distancias euclidianas se calcu-lan entre dos puntos en una superficie plana (el plano Cartesiano). Las zonas de influencia euclidianas son el tipo más común de zona de influencia y fun-cionan bien cuando se analizan distan-cias alrededor de las entidades de un sistema de coordenadas proyecta-das, que se concentran en un área rela-tivamente pequeña (como una zona UTM).
•	Las zonas de influencia geodésicas son las que representan la forma real de la Tierra (un elipsoideo, más correctamen-te, un geoide). Las distancias se calcu-lan entre dos puntos de una superficie curva (el geoide) en vez de entre dos puntos de una superficie plana (el plano Cartesiano). Siempre debe considerar la opción de crear zonas de influencia geodésicas cuando
Las entidades de entrada están dispersas (cu-bren varias zonas UTM, regiones grandes o incluso todo el globo).
La referencia espacial (proyección de mapa) de las entidades de entrada distorsiona las distan-cias para mantener otras propiedades como el área.
Las zonas de influencia geodésicas pueden parecer inusuales sobre un mapa plano, pero, cuando se visualizan sobre un globo, tendrán el aspecto correcto (puede utilizar las aplicaciones de ArcGlobe o ArcGIS Explorer para ver datos geográficos en un globo tridimensional). 

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/9.jpg)
Figura 6.- (Tipos de zona de influencias en Python)



2. 	Desarrollo

Por medio de la fotogrametría nosotros podre-mos calcular zona de afectación ha hecho el Rio entre 1999-2006 y cual es principal punto de afectación debido a este cauce.
Se busca que el programa obtenga las zonas de influencia debido al Rio Coahuayana en el pueblo llamado Boca de Apiza, Tecomán, Coli-ma, debido a que en esta comunidad el Rio pasa muy cerca de ella ocasionando grandes inundaciones cuando se presentan precipitacio-nes extremas, así mismo cuidando la agricultura de la localidad se espera establecer zona de influencia en los diferentes cultivos que existen en el lugar para que tomen cartas en el asunto.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/10.jpg)
Figura 7.- (Rio Coahuayana y a un costado la comu-nidad de Boca de Apiza, Tecomán, Colima)


![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/11.jpg)
Figura 8.- (Rio Coahuayana y a un lado diferentes cultivos de plátanos, chile verde, etc.)


Para llevarse a cabo el programa se requiere tener una carpeta en disco C: donde contenga un archivo .SHP de la carta topográfica la cual se quiera considerar.
Posteriormente el usuario deberá indicar al pro-grama a cuantos metros querrá su zona de in-fluencia. 
Para puntos de influencia será el siguiente có-digo.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/12.jpg)


Para conocer las pendientes del lugar será el siguiente código.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/13.jpg)


3. 	Manejo de datos

A continuación, se mostrarán las características donde fue probado el programa.

3.1. 	Tipos de datos manejados

El tipo de datos que se manejan en el programa son datos geoespaciales porque el mismo usuario proporciona al programa datos en for-mato .SHP y guardar en una carpeta en disco C:\\ para que el programa al correrlo automáti-camente al detectar el archivo .SHP dentro de la carpeta, genere en ArcMap la zona de influencia y de la misma manera en el caso de las pen-dientes donde en la misma carpeta en disco C:\\ ocuparemos descargar el conjunto de datos vectoriales de la misma carta topográfica para que el programa pueda correr y generar la trian-gulación (TIN) del lugar.

3.2. 	Sistema Operativo

El programa está probado para trabajar en el Sistema Operativo Windows.

3.3. 	Equipo de prueba

El equipo con el que fue probado el programa presenta las siguientes características:

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/14.jpg)
Figura 9.- (Especificaciones del dispositivo)


![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/15.jpg)
Figura 10.- (Especificaciones de Windows)


4. 	Resultados

Lo que se logro obtener con el código fue un programa en el cual se le agrega un archivo shapefile (.SHP) de la zona a estudiar. Con lo anterior se genera un archivo de ArcMap (.MXD) en otra carpeta donde se da por resultado la zona de influencia dependiendo de la distancia que se le haya indicado en el programa y asi-mismo otro archivo ArcMap (.MXD) donde muestra las pendientes del mismo lugar.
A continuación, se presenta las zonas de in-fluencia y las pendientes en el lugar.

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/16.jpg)


![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/17.jpg)
Figura11.- (Zona de influencia del rio a 500 metros)

![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/18.jpg)


![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/19.jpg)
Figura 12.- (Pendientes de la zona de influencia)


5. 	Conclusiones.

El lenguaje de programación Python puede ser utilizado para trabajar con Sistemas de Informa-ción Geográfica porque es de gran utilidad y facilita el trabajo. Un ejemplo es el caso de este artículo, al estudiar el Rio estamos previniendo a la gente a evacuar rápidamente en una posible crecida del Rio y así como también a prevenir agricultores en que partes pegadas al rio no realizar sembradíos ya que se los llevara le agua. Las expectativas trazadas para este pro-grama se cumplieron, ya que se realice lo espe-rado y que no solamente se puede realizar el programa con el Rio Coahuayana, sino que puede ser aplicado para cualquier rio donde se tenga una carta edafológica o aplicado a otra situación donde esté en riesgo muchas perso-nas.

6.- Bibliografías

•	Anonimo. (2016). Zona de influencia. 06/12/2019, de ArcMap Sitio web: http://desktop.arcgis.com/es/arcmap/10.3/tools/analysis-toolbox/buffer.htm

•	Anonimo. (2017). Pendiente de superfi-cie. 06/12/2019, de ESRI Sitio web: https://pro.arcgis.com/es/pro-app/tool-reference/3d-analyst/surface-slope.htm

•	Anonimo. (2016). Tipos de Rios. 06/12/2019, de Divina Conciencia. Sitio web: http://www.laanunciataikerketa.com/trabajos/divinaconciencia/tipos_rios_actividad.pdf


![PalabrasdelTextoAlternativo](https://github.com/ogarcia1704/Zona-de-afectacion-del-Rio-Coahuayana/blob/master/Imagenes/ZONA%20DE%20RIESGO%20DEL%20RIO%20COAHUAYANA%20(3).jpg)

