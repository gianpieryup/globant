# Globant Desafio

## Section 1: API
Aclaracion me dan a entender que proveen archivos csv de descarga pero no tiene hipervinculo  `Link to the file` , cree mis archivos csv de prueba

DDL.sql :  La metadata de las 3 tablas en SQL SERVER, cargarla en una BD Globant GLOBANT

Archivo python de carga un csv(hired_employees en este ejemplo) a la BD Globant con conexion windows authentication 
```shell
python main.py
```

Para los otros hay que cambiar el nombre del arhivo csv y definir la metadata

**TODO**
1. Multiples verificaciones de los datos: Tipo de Datos, Cantidad de columnas, etc
2. Generalizar el formato de carga, pasando por consola el nombre del archivo csv y la metadata de columnas



## Section 2: SQL
Databriks: dejo un archivo dbc donde hago las querys que piden
1. Cargar los archivos csv en la parte de datos
2. Crear un cluster
3. Correr la notebook

Les dejo aqui tambien el codigo de estas dos querys de Databriks
```sql
select d.department,
  j.job,
  sum(case when quarter(datetime) = 1 then 1 else 0 end) Q1,
  sum(case when quarter(datetime) = 2 then 1 else 0 end) Q2,
  sum(case when quarter(datetime) = 3 then 1 else 0 end) Q3,
  sum(case when quarter(datetime) = 4 then 1 else 0 end) Q4
from hired_employees h 
join departments d on h.department_id = d.id
join jobs j on h.job_id = j.id
where YEAR(datetime) = '2021'
group by d.department,
  j.job
order by 1 asc, 2 asc
```



```sql
with mean_employees as (
  select department_id, count(id) as hired
  from hired_employees
  where YEAR(datetime) = '2021'
  group by department_id
)
select department_id as id , d.department, count(*) as hired
from hired_employees h
join departments d on h.department_id = d.id
group by department_id, d.department
having count(*) > (select  avg(hired) from mean_employees)
order by 1 asc
```