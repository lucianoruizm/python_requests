Curso y ejemplos de Python consumiendo una API con la librería requests (instalación: pip install requests)
Se ven los principales metodos de HTTP
 GET 
 POST 
 PUT
 DELETE

01- Request de datos de la API https://jikan.moe/ que muestra en consola un top de animes mediante la url correspondiente

02- Request de datos de la API https://api.rawg.io/ que muestra en consola los generos de videojuegos y la cantidad existente registrada de cada uno, mediante la url correspondiente, con la API KEY que es solicitada para la autenticación.

Notas:
Un archivo .env es el que contiene la API_KEY, que esta oculto con .gitignore.
Para utilizar .env que contiene la API_KEY Se instaló la librería python-dotenv (instalación: pip install python-dotenv).