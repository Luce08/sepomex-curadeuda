## INSTALACIÓN

## Crear Maquina vitual 
python3 -m venv env
## Activar entorno virtual
source env\scripts\activate

## Instalar librerias 
pip install -r requirements.txt
## variables de ambiente para la conexion a base de datos y  Jwt

 set SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://root:123@192.132.1.13:3390/sepomex
 set JWT_SECRET_KEY=super-secret //change

## Comando para iniciar
 python main.py o flask run posicionado en el main.py


## Contenedor db
docker run --name sepomex \
-e MYSQL_ROOT_PASSWORD=admin123 \
-e MYSQL_DATABASE=sepomex \
-e MYSQL_USER=root \
-e MYSQL_PASSWORD=admin123 \
-p 3390:3306 \
-d \
mysql/mysql-server:5.5

## correr script

1.-docker cp  sepomex.sql sepomex:/sepomex.sql

2.-docker exec -it "sepomex" "bash"

## dentro del contenedor ejecutar 
1.-mysql -u root -padmin123
2.-use sepomex;
3.-source sepomex.sql
